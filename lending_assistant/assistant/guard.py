"""The safety core every tool goes through (PLAN §2 G1-G4, G6, G9; DECISIONS #35, #38).

What is here:

* `read_only_tool_context()`: blocks writes (layer 2, the `doc_events` trap), turns `frappe.db.commit()` into a
  no-op (layer 3), counts write statements (layer 4) and always rolls back to a savepoint (layer 5). It also
  drops any commit / rollback callback (`frappe.db.after_commit.add(...)`, `enqueue_after_commit=True`)
  registered while it was open, because the rollback does not undo those (DECISIONS #40).
* `read_doc()` / `list_records()`: the only ways a tool reads business records. They check the doctype
  allowlist and the Live data switch, read as the session user, filter fields (permlevel, never-send, Password),
  cap the size, and return one `<data>` envelope.
* `as_data()`: wraps a result in that envelope and neutralises marker text inside every string value (G6).

Identity is `frappe.session.user` and nothing else. No function here accepts a user, role or company.
"""

import json
import re
import uuid
from collections import Counter
from contextlib import contextmanager
from datetime import date, datetime, time, timedelta
from decimal import Decimal

import frappe
import frappe.permissions  # not loaded by `bench execute` or a worker until something imports it (M2b-R4)
from frappe.model import get_permitted_fields

from lending_assistant.assistant import settings

SOURCE_LIVE = "live_site"
SOURCES = (SOURCE_LIVE, "code", "analysis")  # "analysis": the approved knowledge cards (M3b)

NOT_FOUND = "I can't find a record with that ID that you have access to."  # G4, one wording for both cases
READ_ONLY_MESSAGE = "The assistant can only read."
LIVE_DATA_OFF = "Live data is turned off in Assistant Settings."
NOT_ALLOWED_DOCTYPE = "That doctype is not available to the assistant."

MAX_CHARS = 8000  # G9: ~8k characters per tool result (the whole envelope)
MAX_ROWS = 20  # G9
MAX_FIELDS = 30
MAX_NAME_LENGTH = 140
SHORTEN_TO = 300  # first step when a result is too big: cut long strings to this many characters

OPERATORS = ("=", "!=", "<", ">", "<=", ">=", "like", "in", "not in", "between", "is")
MAX_FILTERS = 10
ORDER_BY = re.compile(r"^(\w+) (asc|desc)$", re.IGNORECASE)
FIELDNAME = re.compile(r"^\w+$")
_MARKER = re.compile(r"<(\s*/?\s*data)\b", re.IGNORECASE)
_CHILD_LINK_FIELDS = ("parent", "parenttype", "parentfield")
_WHO_FIELDS = (
	"owner",
	"modified_by",
)  # who created / last changed a record: never shown, for any doctype (#39)


class AssistantGuardError(Exception):
	"""The guard's own integrity broke (for example the savepoint is gone). Never swallowed."""


class AssistantRefused(frappe.PermissionError):
	"""A request the guard refuses: doctype not allowlisted, switch off, forbidden path."""


class RecordNotAvailable(frappe.DoesNotExistError):
	"""G4: raised for a missing record and for a record the user may not read, identically."""


# --- G1: the read-only context ------------------------------------------------------------------------------


class ReadOnlyContext:
	"""What `read_only_tool_context()` hands back. Filled in when the block ends."""

	def __init__(self, tool: str):
		self.tool = tool
		self.savepoint = "ast_" + uuid.uuid4().hex[:16]
		self.baseline_writes = 0
		self.trap_base = 0
		self.db_writes = 0  # write statements the tool made (counted before the rollback)
		self.trap_hits = 0  # writes the doc_events trap refused
		self.callbacks_dropped = 0  # commit / rollback callbacks registered inside the context and removed
		self.callbacks_restored = 0  # earlier callbacks the tool consumed inside the context and we put back
		self.identity_changes: list[
			str
		] = []  # what changed under the tool: user, session, connection, site, flags,
		# callback queues that could not be checked or restored (M2b-R19), the guard flag (I4)
		self.savepoint_gone = (
			False  # a raw COMMIT or DDL removed the savepoint: something was committed (M2b-R14)
		)
		self.nested: list["ReadOnlyContext"] = []

	@property
	def violation(self) -> bool:
		return bool(
			self.db_writes
			or self.trap_hits
			or self.callbacks_dropped
			or self.callbacks_restored
			or self.identity_changes
			or self.savepoint_gone
			or any(c.violation for c in self.nested)
		)

	def summary(self) -> dict:
		kids = [c.summary() for c in self.nested]
		return {
			"tool": self.tool,
			"db_writes": self.db_writes + sum(k["db_writes"] for k in kids),
			"trap_hits": self.trap_hits + sum(k["trap_hits"] for k in kids),
			"callbacks_dropped": self.callbacks_dropped + sum(k["callbacks_dropped"] for k in kids),
			"callbacks_restored": self.callbacks_restored + sum(k["callbacks_restored"] for k in kids),
			"identity_changes": len(self.identity_changes) + sum(k["identity_changes"] for k in kids),
			"savepoint_gone": int(self.savepoint_gone) + sum(k["savepoint_gone"] for k in kids),
		}


# The only two reads / writes of `frappe.flags` in this app (scanner rule G), and only for the guard's own keys.
_GUARD_FLAGS = ("ast_read_only", "ast_trap_hits", "ast_guard_stack")  # the guard changes these itself
_RISKY_FLAG_PREFIXES = (
	"ignore_",
	"in_",
	"mute_",
	"ast_",
)  # a change to one of these inside a tool is a violation
_ABSENT = object()  # "this attribute / key does not exist" (a cold connection has no cursor yet)


def _ast_flag(name: str):
	if not name.startswith("ast_"):
		raise AssistantGuardError("The guard reads only its own ast_* flags.")
	return frappe.flags.get(name)  # AST-ALLOWED: the one place guard.py reads frappe.flags


def _set_ast_flag(name: str, value):
	if not name.startswith("ast_"):
		raise AssistantGuardError("The guard writes only its own ast_* flags.")
	frappe.flags[name] = value  # AST-ALLOWED: the one place guard.py writes frappe.flags


def block_if_read_only(doc=None, method=None, *args, **kwargs):
	"""`doc_events["*"]` hook (G1 layer 2). Does nothing unless a tool context is open."""
	if _ast_flag("ast_read_only"):
		_set_ast_flag("ast_trap_hits", (_ast_flag("ast_trap_hits") or 0) + 1)
		raise frappe.PermissionError(READ_ONLY_MESSAGE)


def _capture_identity() -> dict:
	"""Who and what the context starts with, as the REAL objects in `frappe.local` (not the `frappe.db` / `frappe.session`
	proxies, which follow a swap). Compared and put back on exit (M2b-R8, R13).

	A connection that is not open yet (`_conn` is None, no `_cursor`) is captured as such; the context re-captures
	after its savepoint has opened it.
	"""
	snap = {}
	try:
		snap["db"] = (
			frappe.local.db  # AST-ALLOWED: run-time identity layer: the connection object itself, not the proxy
		)
		snap["session"] = frappe.local.session  # AST-ALLOWED: run-time identity layer
		snap["flags"] = frappe.local.flags  # AST-ALLOWED: run-time identity layer
		snap["site"] = frappe.local.site  # AST-ALLOWED: run-time identity layer
	except AttributeError as exc:
		raise AssistantGuardError("There is no database connection or session to guard.") from exc
	snap["user"], snap["sid"] = snap["session"].user, snap["session"].sid
	snap["conn"] = snap[  # AST-ALLOWED: run-time identity layer: None while the connection is not open yet
		"db"
	]._conn
	try:
		snap["cursor"] = snap[  # AST-ALLOWED: run-time identity layer: only exists once a query has run
			"db"
		]._cursor
	except AttributeError:
		snap["cursor"] = _ABSENT
	snap["flag_values"] = dict(snap["flags"])
	return snap


def _discard_connection(snap: dict) -> None:
	"""Undo and close whatever connection the tool swapped in (call before the original is put back).

	Raw driver calls, so the swapped-in connection's own callbacks do not run. After this the guard holds no reference
	to it. Code that keeps its own reference to a rogue connection is a known limit (DECISIONS #46, #47).
	"""
	try:
		rogue = frappe.local.db  # AST-ALLOWED: run-time identity layer: the connection the tool put there
	except AttributeError:
		return  # nothing there any more
	if rogue is snap["db"]:  # the original object with a new socket  # AST-ALLOWED: run-time identity layer
		stray = rogue._conn  # AST-ALLOWED: run-time identity layer: the socket the tool swapped in
		if stray is snap["conn"] or stray is None:  # AST-ALLOWED: run-time identity layer
			return
		try:
			stray.rollback()  # AST-ALLOWED: run-time identity layer: undo what the swapped-in socket did not commit
		except Exception:
			pass
		try:
			stray.close()  # AST-ALLOWED: run-time identity layer: close the swapped-in socket
		except Exception:
			pass
		return
	try:
		if rogue._conn is not None:  # AST-ALLOWED: run-time identity layer
			rogue._conn.rollback()  # AST-ALLOWED: run-time identity layer: undo what the swapped-in connection did not commit
	except Exception:
		pass
	try:
		rogue.close()  # closes the driver connection and drops the object's references to it  # AST-ALLOWED: run-time identity layer
	except Exception:
		pass


def _restore_identity(snap: dict) -> list[str]:
	"""Compare with the entry snapshot and put back what was changed. Returns what had changed.

	Every item is restored on its own: one that cannot be restored (for example `del frappe.local.db`) is reported and
	the rest still run. A write that the tool COMMITTED on a new connection cannot be undone from here; the scanner
	(connect, init, login_as, set_user are never excused) prevents it. "Switch and back" inside one call leaves no trace
	in the end state: a known limit (covered by the scanner's identity bans and the M4 line-by-line review).
	"""
	changed = []
	db = snap["db"]

	try:
		try:
			swapped = frappe.local.db is not db  # AST-ALLOWED: run-time identity layer
		except AttributeError:
			swapped = True  # `del frappe.local.db`
		if swapped:
			changed.append("database connection")
			_discard_connection(snap)
			frappe.local.db = db  # AST-ALLOWED: run-time identity layer: put the original connection back
		elif db._conn is not snap["conn"]:  # AST-ALLOWED: run-time identity layer
			changed.append("database connection (same object, new socket)")
			_discard_connection(snap)
			db._conn = snap["conn"]  # AST-ALLOWED: run-time identity layer
			if snap["cursor"] is not _ABSENT:
				db._cursor = snap["cursor"]  # AST-ALLOWED: run-time identity layer
	except Exception:
		changed.append("database connection could not be restored")

	try:
		try:
			swapped = frappe.local.flags is not snap["flags"]  # AST-ALLOWED: run-time identity layer
		except AttributeError:
			swapped = True
		if swapped:
			changed.append("flags")
			frappe.local.flags = snap["flags"]  # AST-ALLOWED: run-time identity layer
	except Exception:
		changed.append("flags could not be restored")

	try:
		try:
			wrong_site = frappe.local.site != snap["site"]  # AST-ALLOWED: run-time identity layer
		except AttributeError:
			wrong_site = True
		if wrong_site:
			changed.append("site")
			frappe.local.site = snap["site"]  # AST-ALLOWED: run-time identity layer
	except Exception:
		changed.append("site could not be restored")

	try:
		try:
			who_changed = frappe.local.session is not snap["session"]  # AST-ALLOWED: run-time identity layer
		except AttributeError:
			who_changed = True
		if who_changed:
			frappe.local.session = snap["session"]  # AST-ALLOWED: run-time identity layer
		if (
			frappe.session.user != snap["user"]
			or frappe.session.sid != snap["sid"]  # AST-ALLOWED: run-time identity layer
		):
			who_changed = True
			frappe.session.user = snap["user"]  # AST-ALLOWED: run-time identity layer: not set_user
			frappe.session.sid = snap["sid"]  # AST-ALLOWED: run-time identity layer
		if who_changed:
			changed.append("session user")
			# what set_user() resets: permission caches built for the other user must not stay behind
			(  # AST-ALLOWED: run-time identity layer
				frappe.local.user_perms,  # AST-ALLOWED: run-time identity layer
				frappe.local.role_permissions,  # AST-ALLOWED: run-time identity layer
				frappe.local.cache,  # AST-ALLOWED: run-time identity layer
			) = (
				None,
				{},
				{},
			)
	except Exception:
		changed.append("session could not be restored")

	try:
		changed += _restore_flag_values(snap)
	except Exception:
		changed.append("flags could not be restored")
	return changed


def _restore_flag_values(snap: dict) -> list[str]:
	"""Put the contents of `frappe.local.flags` back (M2b-R16). A security-relevant key (`ignore_*`, `in_*`, `mute_*`,
	`ast_*` that is not the guard's own) that differs is reported; any other key is restored silently."""
	flags, before, changed = snap["flags"], snap["flag_values"], []
	for key in set(flags) | set(before):
		if key in _GUARD_FLAGS:
			continue
		now, was = flags.get(key, _ABSENT), before.get(key, _ABSENT)
		if now is was or now == was:
			continue
		if was is _ABSENT:
			flags.pop(key, None)  # AST-ALLOWED: run-time identity layer: remove a flag the tool added
		else:
			flags[key] = was
		if str(key).startswith(_RISKY_FLAG_PREFIXES):
			changed.append(f"flag {key}")
	return changed


def _snapshot_callbacks() -> list:
	"""(manager, its queue object, the queue's contents) for the four commit / rollback callback managers (M2b-R9)."""
	managers = [
		frappe.db.before_commit,  # AST-ALLOWED: G1 callback layer
		frappe.db.after_commit,  # AST-ALLOWED: G1 callback layer
		frappe.db.before_rollback,  # AST-ALLOWED: G1 callback layer
		frappe.db.after_rollback,  # AST-ALLOWED: G1 callback layer
	]
	return [
		(manager, manager._functions, list(manager._functions))  # AST-ALLOWED: G1 callback layer
		for manager in managers
	]


def _restore_callbacks(ctx: ReadOnlyContext, snapshots: list) -> list[str]:
	"""Put every queue back to exactly its contents on entry (M2b-R3, R9). Returns what could not be checked or restored.

	The savepoint rollback only undoes SQL. A callback queued here would run at the next real commit, after the
	guard is gone (that includes `frappe.enqueue(..., enqueue_after_commit=True)` and deferred realtime events).
	Compared by identity of the function, so a context that consumed earlier callbacks and then added as many
	new ones does not hide the swap. A replaced queue object is replaced back.

	Each queue is handled on its own (M2b-R19): a queue whose contents cannot be read (the tool replaced it with
	something that is not a list) is reported, and the original queue object is still put back.
	"""
	problems = []
	for manager, queue, before in snapshots:
		try:
			now = Counter(id(fn) for fn in list(manager._functions))  # AST-ALLOWED: G1 callback layer
			kept = Counter(id(fn) for fn in before)
			ctx.callbacks_dropped += sum((now - kept).values())  # added inside: never run
			ctx.callbacks_restored += sum((kept - now).values())  # earlier ones the tool consumed: put back
		except Exception:
			problems.append("callbacks could not be checked")
		try:
			manager._functions = (  # AST-ALLOWED: G1 callback layer: the original queue object, even if it was replaced
				queue
			)
			queue.clear()
			queue.extend(before)
		except Exception:
			problems.append("callbacks could not be restored")
	return problems


@contextmanager
def read_only_tool_context(tool: str = ""):
	"""Run a tool so that nothing it does can reach the database (G1 layers 2-5, plus the identity check).

	On exit (success, exception, nested), in this order. Each step is in its own `try`, so an `Exception` raised by
	one step does not skip the steps after it:
	1. put back the identity and connection the tool started with;
	2. put back the four commit / rollback callback queues;
	3. read the write and trap counters, and check that the guard flag `ast_read_only` is still True;
	4. roll back to the savepoint (a failure means the savepoint is gone), then put the guard flag, the
	   transaction-control counter and the write counter back exactly as found;
	5. outermost context only: log one violation row if anything was counted (after step 4, so the trap does not
	   block the log; a failing log is swallowed).
	Then it raises AssistantGuardError if the identity, connection, callback queues or guard flag had to be put back
	or could not be, or if the savepoint was gone.

	Not covered: a `BaseException` that is not an `Exception` (KeyboardInterrupt, SystemExit). Step 1 runs inside a
	`try ... finally` whose `finally` holds steps 2-4, so a `BaseException` raised in step 1 skips nothing. One raised
	in step 2 or step 3 is not caught by their `except Exception`: it skips the rest of the block (the savepoint
	rollback, the violation log and the AssistantGuardError), and only the `finally` of step 4 runs (flag, transaction
	control and write counter reset; the savepoint stays open until the request's own rollback). A COMMIT that
	already happened on another connection, and a reference the tool kept to a swapped-in connection, are known
	limits (DECISIONS #46, #47).
	"""
	ctx = ReadOnlyContext(tool)
	identity = _capture_identity()
	db = identity["db"]  # the real connection object, whatever `frappe.db` points to later
	previous_flag = _ast_flag("ast_read_only")
	previous_control = db._disable_transaction_control  # AST-ALLOWED: G1 layer 3: transaction control
	stack = _ast_flag("ast_guard_stack")
	if stack is None:
		stack = []
		_set_ast_flag("ast_guard_stack", stack)

	_set_ast_flag("ast_read_only", True)
	db._disable_transaction_control = (  # AST-ALLOWED: G1 layer 3: transaction control
		previous_control + 1
	)  # frappe.db.commit() is now a no-op
	ctx.baseline_writes = db.transaction_writes  # AST-ALLOWED: G1 layer 4: write counter
	ctx.trap_base = _ast_flag("ast_trap_hits") or 0
	callback_snapshots = (
		_snapshot_callbacks()
	)  # a local, not on ctx: the context object holds plain values only
	try:
		db.savepoint(ctx.savepoint)  # the first query: it opens a connection that was not open yet
	except Exception:
		_set_ast_flag("ast_read_only", previous_flag)
		db._disable_transaction_control = (  # AST-ALLOWED: G1 layer 3: restore transaction control
			previous_control
		)
		raise
	if identity["conn"] is None:  # cold start: the connection the savepoint just opened is the one to guard
		identity = _capture_identity()
	stack.append(ctx)

	try:
		yield ctx
	finally:
		stack.pop()
		try:
			try:
				ctx.identity_changes = _restore_identity(identity)
			except Exception:
				ctx.identity_changes = ["identity could not be restored"]
		finally:
			try:
				try:
					ctx.identity_changes += _restore_callbacks(ctx, callback_snapshots)
				except Exception:
					ctx.identity_changes.append(
						"callbacks could not be restored"
					)  # M2b-R19: the steps below still run
				try:
					# Read the counters BEFORE the rollback: ROLLBACK resets transaction_writes to 0 (database.py:470).
					ctx.db_writes = max(
						0,
						db.transaction_writes  # AST-ALLOWED: G1 layer 4: read the write counter before the rollback
						- ctx.baseline_writes,
					)
				except Exception:
					ctx.db_writes = 1  # the counter could not be read: assume a write, so it is logged
				try:
					ctx.trap_hits = max(0, (_ast_flag("ast_trap_hits") or 0) - ctx.trap_base)
					if _ast_flag("ast_read_only") is not True:
						ctx.identity_changes.append("guard flag changed inside the context")  # I4
				except Exception:
					ctx.identity_changes.append("guard flag could not be read")
				try:
					db.rollback(  # AST-ALLOWED: guard layer 5, the savepoint rollback
						save_point=ctx.savepoint
					)
				except Exception:
					ctx.savepoint_gone = True
				else:
					try:
						db.release_savepoint(ctx.savepoint)
					except Exception:
						pass
			finally:
				_set_ast_flag("ast_read_only", previous_flag)
				db._disable_transaction_control = (  # AST-ALLOWED: G1: restore transaction control
					previous_control
				)
				db.transaction_writes = (  # AST-ALLOWED: G1 layer 4: restore the write counter
					ctx.baseline_writes
				)

		if stack:
			stack[-1].nested.append(ctx)
		elif ctx.violation:
			_log_violation(ctx)  # outermost only, after the flag is restored (the trap would block the log)
		if ctx.identity_changes:
			raise AssistantGuardError(
				"identity or connection changed inside the tool context: " + ", ".join(ctx.identity_changes)
			)
		if ctx.savepoint_gone:
			raise AssistantGuardError(
				"The read-only savepoint no longer exists: something committed inside the tool context."
			)


@contextmanager
def identity_watch(tool: str = ""):
	"""The dispatcher's own identity check (#48), around everything it runs for one tool call.

	On entry it records who and what the request is: `frappe.local.db` (the object, not the proxy), the session, the
	user and sid, the flags and the site. On exit it compares, puts back whatever differs, logs it (counts only) and
	raises AssistantGuardError. It yields nothing: the recorded objects stay inside this module (plain data surface).
	The read-only context does the same check around the tool itself; this one also covers the code between the context
	and the return, and it still works if the context is replaced by something that does not check.
	"""
	identity = _capture_identity()
	try:
		yield
	finally:
		try:
			changed = _restore_identity(identity)
		except Exception:
			changed = ["identity could not be restored"]
		if changed:
			ctx = ReadOnlyContext(tool)
			ctx.identity_changes = changed
			_log_violation(ctx)
			raise AssistantGuardError(
				"identity or connection changed during the tool call: " + ", ".join(changed)
			)


def _log_violation(ctx: ReadOnlyContext):
	"""Counts and the tool name only: never record data."""
	summary = ctx.summary()
	try:
		frappe.log_error(  # AST-ALLOWED: the violation log; counts only, never record data
			title="AST write blocked",
			message=(
				f"user={frappe.session.user} tool={summary['tool'] or '(unnamed)'} "
				f"db_writes_rolled_back={summary['db_writes']} trap_refusals={summary['trap_hits']} "
				f"callbacks_dropped={summary['callbacks_dropped']} callbacks_restored={summary['callbacks_restored']} "
				f"identity_changes={summary['identity_changes']} savepoint_gone={summary['savepoint_gone']}"
			),
		)
	except Exception:
		pass  # logging must never hide the tool's own result or error


# --- G6: data envelope ----------------------------------------------------------------------------------------


def neutralise(text: str) -> str:
	"""Defuse any `<data` / `</data` marker text, whatever the case or spacing."""
	return _MARKER.sub(r"&lt;\1", text)


def _clean(value):
	"""JSON-safe copy of `value`: every string neutralised, dates and decimals as text, numbers untouched."""
	if isinstance(value, str):
		return neutralise(value)
	if value is None or isinstance(value, bool | int | float):
		return value
	if isinstance(value, dict):
		return {str(k): _clean(v) for k, v in value.items()}
	if isinstance(value, list | tuple | set):
		return [_clean(v) for v in value]
	if isinstance(value, datetime | date | time | timedelta | Decimal):
		return str(value)
	return neutralise(str(value))


def _envelope(cleaned, source: str) -> str:
	"""The one place an envelope string is built, so the size `fit` measures is the size that is returned."""
	if isinstance(cleaned, dict):
		cleaned["source"] = source
	return f'<data source="{source}">{json.dumps(cleaned, ensure_ascii=False)}</data>'


def as_data(payload, source: str = SOURCE_LIVE) -> str:
	"""One envelope around the whole result: `<data source="live_site">{json}</data>` (DECISIONS #38.3)."""
	if source not in SOURCES:
		raise frappe.ValidationError("Unknown data source.")
	if isinstance(payload, str):
		payload = {"text": payload}
	return _envelope(_clean(payload), source)


def unwrap(envelope: str) -> dict:
	"""Parse an envelope back into a dict (tests, and internal callers)."""
	match = re.fullmatch(r'<data source="(live_site|code|analysis)">(.*)</data>', envelope, re.DOTALL)
	if not match:
		raise AssistantGuardError("Not a data envelope.")
	return json.loads(match.group(2))


# --- G9: keep results small ------------------------------------------------------------------------------------


def _shorten(obj, limit: int):
	"""Cut long strings in place; return True if anything was cut."""
	cut = False
	items = obj.items() if isinstance(obj, dict) else enumerate(obj) if isinstance(obj, list) else ()
	for key, value in list(items):
		if isinstance(value, str) and len(value) > limit:
			obj[key] = value[:limit] + "…"
			cut = True
		elif isinstance(value, dict | list):
			cut = _shorten(value, limit) or cut
	return cut


def fit(result: dict, row_lists, field_dicts, source: str = SOURCE_LIVE):
	"""Make the envelope fit MAX_CHARS and keep it valid JSON: shorten strings, drop trailing rows, drop fields.

	`result` must already be cleaned (strings neutralised). Sets `truncated` when anything is removed. The cap
	applies to the final envelope string, markers and `source` included.
	"""

	def size():
		return len(_envelope(result, source))  # the real string, with "source" and the markers (M2b-R5)

	if size() <= MAX_CHARS:
		return
	result["truncated"] = True
	if _shorten(result, SHORTEN_TO) and size() <= MAX_CHARS:
		return
	while size() > MAX_CHARS:
		longest = max((rows for rows in row_lists() if rows), key=len, default=None)
		if longest is None:
			break
		longest.pop()
	while size() > MAX_CHARS:
		fields = next((d for d in reversed(list(field_dicts())) if len(d) > 1), None)
		if fields is None:
			break
		fields.pop(next(reversed(fields)))


# --- G2-G4: allowlist, switches, fields ---------------------------------------------------------------------


def require_live_data():
	if not settings.get_settings().live_data:
		raise AssistantRefused(LIVE_DATA_OFF)


def require_doctype(doctype) -> str:
	"""R5: only the Settings allowlist."""
	if not isinstance(doctype, str) or doctype not in {
		row.allowed_doctype for row in settings.get_settings().doctype_allowlist
	}:
		raise AssistantRefused(NOT_ALLOWED_DOCTYPE)
	return doctype


def _never_send(doctype: str) -> set[str]:
	return {
		row.fieldname
		for row in settings.get_settings().never_send_fields
		if row.ref_doctype == doctype and row.fieldname
	}


def readable_fields(doctype: str, parenttype: str | None = None) -> list[str]:
	"""Field names the session user may see: permlevel (G3), minus never-send, minus Password fields (#33), minus
	`owner` and `modified_by` for every doctype, parent and child (#39)."""
	meta = frappe.get_meta(  # AST-ALLOWED: field filtering needs the meta; it never leaves this module
		doctype
	)
	permitted = get_permitted_fields(
		doctype, parenttype=parenttype, user=frappe.session.user, ignore_virtual=True
	)
	blocked = _never_send(doctype) | {df.fieldname for df in meta.fields if df.fieldtype == "Password"}
	valid = set(meta.get_valid_columns())
	skip = (*_CHILD_LINK_FIELDS, *_WHO_FIELDS) if parenttype else _WHO_FIELDS
	fields = []
	for fieldname in permitted:
		if (
			fieldname in valid
			and fieldname not in blocked
			and fieldname not in skip
			and not fieldname.startswith("_")  # _comments, _assign, _liked_by...: other people's text
			and fieldname not in fields
		):
			fields.append(fieldname)
	return fields


def _message_log_size() -> int:
	return len(
		frappe.local.message_log  # AST-ALLOWED: G4 message-log snapshot; always a list once frappe.init has run
	)


def _load_readable(doctype, name):
	"""The checked loader: get_doc, then has_permission("read"). Missing and unreadable look the same (G4)."""
	require_live_data()
	require_doctype(doctype)
	if not isinstance(name, str) or not name or len(name) > MAX_NAME_LENGTH:
		raise RecordNotAvailable(NOT_FOUND)

	log_size = _message_log_size()
	doc = None
	try:
		# Gate first with one permission-aware name query (user permissions, owner and share rules run in SQL).
		# A missing and a hidden record both end here with the same single query, so they cost the same time.
		try:
			visible = frappe.get_list(  # AST-ALLOWED: the checked lister: name gate, runs as the session user
				doctype, filters={"name": name}, pluck="name", limit=1
			)
		except frappe.PermissionError:
			visible = []
		if visible:
			doc = frappe.get_doc(doctype, name)  # AST-ALLOWED: the checked reader; has_permission follows
	except frappe.DoesNotExistError:
		pass
	finally:
		# get_doc's own "not found" message must not reach an HTTP response, or it would tell a missing
		# record from a hidden one.
		del frappe.local.message_log[log_size:]  # AST-ALLOWED: G4: drop get_doc's own not-found message

	allowed = bool(doc) and frappe.permissions.has_permission(doctype, "read", doc=doc, print_logs=False)
	if not allowed:
		raise RecordNotAvailable(NOT_FOUND)
	return doc


def check_actions(doctype, actions, name=None) -> dict:
	"""{action: bool} for the session user. With `name`, on that record, loaded through the checked reader (G4).

	Returns plain data, never the Document, so `access.py` does not need a raw object.
	"""
	doc = _load_readable(doctype, name) if name is not None else None
	return {
		action: bool(frappe.permissions.has_permission(doctype, action, doc=doc, print_logs=False))
		for action in dict.fromkeys(actions)
	}


def read_doc(doctype, name) -> str:
	"""One record plus its child rows, as a `<data>` envelope. The only way a tool reads a single record."""
	doc = _load_readable(doctype, name)
	meta = frappe.get_meta(  # AST-ALLOWED: child-table and permlevel info; it never leaves this module
		doctype
	)
	user = frappe.session.user

	data = {fieldname: doc.get(fieldname) for fieldname in readable_fields(doctype)}
	data.setdefault("name", doc.name)

	children = {}
	permlevels = set(meta.get_permlevel_access("read", user=user))
	for df in meta.get_table_fields():
		if (df.permlevel or 0) not in permlevels:
			continue
		child_fields = readable_fields(df.options, parenttype=doctype)
		children[df.fieldname] = [
			{fieldname: row.get(fieldname) for fieldname in child_fields}
			for row in doc.get(df.fieldname) or []
		]

	result = _clean(
		{"doctype": doctype, "name": doc.name, "truncated": False, "data": data, "children": children}
	)
	fit(
		result,
		row_lists=lambda: result["children"].values(),
		field_dicts=lambda: [result["data"]],
	)
	return as_data(result, SOURCE_LIVE)


# --- list_records ---------------------------------------------------------------------------------------------


def _check_filters(filters, allowed: set[str]) -> list:
	"""Filters as a dict (`{field: value}` or `{field: [operator, value]}`, one condition per field) or as a list of
	`[field, operator, value]` conditions (the same field may appear more than once, for example two date bounds).
	Returns the list form, which `frappe.get_list` takes as it is. At most MAX_FILTERS conditions."""
	if filters is None:
		return []
	if isinstance(filters, dict):
		conditions = []
		for field, spec in filters.items():
			if isinstance(spec, list | tuple):
				if len(spec) != 2:
					raise frappe.ValidationError("A filter operator is not allowed.")
				conditions.append([field, spec[0], spec[1]])
			else:
				conditions.append([field, "=", spec])
	elif isinstance(filters, list | tuple):
		conditions = [list(item) if isinstance(item, list | tuple) else item for item in filters]
	else:
		raise frappe.ValidationError(
			"Filters must be a dict of field: value or a list of [field, operator, value]."
		)
	if len(conditions) > MAX_FILTERS:
		raise frappe.ValidationError(f"At most {MAX_FILTERS} filters.")
	clean = []
	for condition in conditions:
		if not isinstance(condition, list) or len(condition) != 3:
			raise frappe.ValidationError("A filter must be [field, operator, value].")
		field, op, value = condition
		if not isinstance(field, str) or field not in allowed:
			raise frappe.ValidationError("A filter uses a field that is not available.")
		if op not in OPERATORS:
			raise frappe.ValidationError("A filter operator is not allowed.")
		clean.append([field, op, _check_filter_value(op, value)])
	return clean


def _scalar(value):
	if isinstance(value, bool):
		return int(value)
	if isinstance(value, int | float) or (isinstance(value, str) and len(value) <= 200):
		return value
	raise frappe.ValidationError("A filter value is not valid.")


def _check_filter_value(op: str, value):
	if op in ("=", "!=", "<", ">", "<=", ">="):
		return _scalar(value)
	if op == "like":
		if not isinstance(value, str) or len(value) > 100:
			raise frappe.ValidationError("A like filter needs a short text.")
		return value
	if op in ("in", "not in"):
		if not isinstance(value, list | tuple) or not 0 < len(value) <= 50:
			raise frappe.ValidationError("An in filter needs a list of 1 to 50 values.")
		return [_scalar(v) for v in value]
	if op == "between":
		if not isinstance(value, list | tuple) or len(value) != 2:
			raise frappe.ValidationError("A between filter needs two values.")
		return [_scalar(v) for v in value]
	if op == "is":
		if value not in ("set", "not set"):
			raise frappe.ValidationError('An is filter needs "set" or "not set".')
		return value
	raise frappe.ValidationError("A filter operator is not allowed.")


def list_records(doctype, filters=None, fields=None, order_by=None, limit=MAX_ROWS) -> str:
	"""A list of records, as a `<data>` envelope. The only way a tool lists records.

	Explicit arguments only: a `user=` or `company=` keyword raises TypeError. Counts come from the rows
	returned; there is no total anywhere (G4).
	"""
	require_live_data()
	require_doctype(doctype)
	allowed = set(readable_fields(doctype))

	if fields is None:
		fields = ["name"]
	if not isinstance(fields, list | tuple) or not 0 < len(fields) <= MAX_FIELDS:
		raise frappe.ValidationError(f"Fields must be a list of 1 to {MAX_FIELDS} field names.")
	for fieldname in fields:
		if not isinstance(fieldname, str) or fieldname not in allowed:
			raise frappe.ValidationError("A requested field is not available.")
	fields = list(dict.fromkeys(fields))

	clean_filters = _check_filters(filters, allowed)

	if order_by is None:
		order_by = "modified desc" if "modified" in allowed else "name asc"
	match = ORDER_BY.match(order_by) if isinstance(order_by, str) else None
	if not match or match.group(1) not in allowed or not FIELDNAME.match(match.group(1)):
		raise frappe.ValidationError("order_by must be '<field> asc|desc' on an available field.")
	order_by = f"{match.group(1)} {match.group(2).lower()}"

	if isinstance(limit, bool) or not isinstance(limit, int) or limit < 1:
		raise frappe.ValidationError("Limit must be a whole number of 1 or more.")
	limit_clamped = limit > MAX_ROWS
	limit = min(limit, MAX_ROWS)

	rows = (
		frappe.get_list(  # AST-ALLOWED: the checked lister: runs as the session user, filters validated above
			doctype,
			filters=clean_filters,
			fields=fields,
			order_by=order_by,
			limit=limit,
		)
	)
	rows = [{fieldname: row.get(fieldname) for fieldname in fields} for row in rows]

	result = _clean(
		{
			"doctype": doctype,
			"count_returned": len(rows),
			"limit": limit,
			"limit_clamped": limit_clamped,
			"may_be_partial": len(rows) >= limit,
			"truncated": False,
			"rows": rows,
		}
	)
	fit(result, row_lists=lambda: [result["rows"]], field_dicts=lambda: result["rows"])
	result["count_returned"] = len(result["rows"])  # after truncation: only rows actually returned
	return as_data(result, SOURCE_LIVE)
