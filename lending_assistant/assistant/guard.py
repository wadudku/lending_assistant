"""The safety core every tool goes through (PLAN §2 G1-G4, G6, G9; DECISIONS #35, #38).

What is here:

* `read_only_tool_context()`: blocks writes (layer 2, the `doc_events` trap), turns `frappe.db.commit()` into a
  no-op (layer 3), counts write statements (layer 4) and always rolls back to a savepoint (layer 5).
* `read_doc()` / `list_records()`: the only ways a tool reads business records. They check the doctype
  allowlist and the Live data switch, read as the session user, filter fields (permlevel, never-send, Password),
  cap the size, and return one `<data>` envelope.
* `as_data()`: wraps a result in that envelope and neutralises marker text inside every string value (G6).

Identity is `frappe.session.user` and nothing else. No function here accepts a user, role or company.
"""

import json
import re
import uuid
from contextlib import contextmanager
from datetime import date, datetime, time, timedelta
from decimal import Decimal

import frappe
from frappe.model import get_permitted_fields

from lending_assistant.assistant import settings

SOURCE_LIVE = "live_site"
SOURCES = (SOURCE_LIVE, "code")

NOT_FOUND = "I can't find a record with that ID that you have access to."  # G4, one wording for both cases
READ_ONLY_MESSAGE = "The assistant can only read."
LIVE_DATA_OFF = "Live data is turned off in Assistant Settings."
NOT_ALLOWED_DOCTYPE = "That doctype is not available to the assistant."

MAX_CHARS = 8000  # G9: ~8k characters per tool result (the whole envelope)
MAX_ROWS = 20  # G9
MAX_FIELDS = 30
MAX_NAME_LENGTH = 140
SHORTEN_TO = 300  # first step when a result is too big: cut long strings to this many characters

OPERATORS = ("=", "!=", "<", ">", "<=", ">=", "like", "in", "between", "is")
ORDER_BY = re.compile(r"^(\w+) (asc|desc)$", re.IGNORECASE)
FIELDNAME = re.compile(r"^\w+$")
_MARKER = re.compile(r"<(\s*/?\s*data)\b", re.IGNORECASE)
_CHILD_LINK_FIELDS = ("parent", "parenttype", "parentfield")


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
		self.nested: list["ReadOnlyContext"] = []

	@property
	def violation(self) -> bool:
		return bool(self.db_writes or self.trap_hits or any(c.violation for c in self.nested))

	def summary(self) -> dict:
		return {
			"tool": self.tool,
			"db_writes": self.db_writes + sum(c.summary()["db_writes"] for c in self.nested),
			"trap_hits": self.trap_hits + sum(c.summary()["trap_hits"] for c in self.nested),
		}


def block_if_read_only(doc=None, method=None, *args, **kwargs):
	"""`doc_events["*"]` hook (G1 layer 2). Does nothing unless a tool context is open."""
	if frappe.flags.ast_read_only:
		frappe.flags.ast_trap_hits = (frappe.flags.ast_trap_hits or 0) + 1
		raise frappe.PermissionError(READ_ONLY_MESSAGE)


@contextmanager
def read_only_tool_context(tool: str = ""):
	"""Run a tool so that nothing it does can reach the database (G1 layers 2-5).

	On exit, always (success, exception, nested): roll back to the savepoint, record a violation if write
	statements were counted, and put the flag and the transaction-control counter back exactly as found.
	If the savepoint is gone (a raw COMMIT or DDL ran) it raises AssistantGuardError.
	"""
	db = frappe.db
	ctx = ReadOnlyContext(tool)
	previous_flag = frappe.flags.ast_read_only
	previous_control = db._disable_transaction_control  # AST-ALLOWED: G1 layer 3: transaction control
	stack = frappe.flags.ast_guard_stack
	if stack is None:
		stack = frappe.flags.ast_guard_stack = []

	frappe.flags.ast_read_only = True
	db._disable_transaction_control = previous_control + 1  # frappe.db.commit() is now a no-op  # AST-ALLOWED: G1 layer 3: transaction control
	ctx.baseline_writes = db.transaction_writes  # AST-ALLOWED: G1 layer 4: write counter
	ctx.trap_base = frappe.flags.ast_trap_hits or 0
	try:
		db.savepoint(ctx.savepoint)  # AST-ALLOWED: G1 layer 5: savepoint
	except Exception:
		frappe.flags.ast_read_only = previous_flag
		db._disable_transaction_control = previous_control  # AST-ALLOWED: G1 layer 3: restore transaction control
		raise
	stack.append(ctx)

	try:
		yield ctx
	finally:
		stack.pop()
		# Read the counters BEFORE the rollback: ROLLBACK resets transaction_writes to 0 (database.py:470).
		ctx.db_writes = max(0, db.transaction_writes - ctx.baseline_writes)  # AST-ALLOWED: G1 layer 4: read the write counter before the rollback
		ctx.trap_hits = max(0, (frappe.flags.ast_trap_hits or 0) - ctx.trap_base)
		savepoint_gone = False
		try:
			db.rollback(save_point=ctx.savepoint)  # AST-ALLOWED: guard layer 5, the savepoint rollback
		except Exception:
			savepoint_gone = True
		else:
			try:
				db.release_savepoint(ctx.savepoint)  # AST-ALLOWED: guard layer 5, cleanup
			except Exception:
				pass
		finally:
			frappe.flags.ast_read_only = previous_flag
			db._disable_transaction_control = previous_control  # AST-ALLOWED: G1: restore transaction control
			db.transaction_writes = ctx.baseline_writes  # AST-ALLOWED: G1 layer 4: restore the write counter

		if stack:
			stack[-1].nested.append(ctx)
		elif ctx.violation:
			_log_violation(ctx)  # outermost only, after the flag is restored (the trap would block the log)
		if savepoint_gone:
			raise AssistantGuardError(
				"The read-only savepoint no longer exists: something committed inside the tool context."
			)


def _log_violation(ctx: ReadOnlyContext):
	"""Counts and the tool name only: never record data."""
	summary = ctx.summary()
	try:
		frappe.log_error(
			title="AST write blocked",
			message=(
				f"user={frappe.session.user} tool={summary['tool'] or '(unnamed)'} "
				f"db_writes_rolled_back={summary['db_writes']} trap_refusals={summary['trap_hits']}"
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


def as_data(payload, source: str = SOURCE_LIVE) -> str:
	"""One envelope around the whole result: `<data source="live_site">{json}</data>` (DECISIONS #38.3)."""
	if source not in SOURCES:
		raise frappe.ValidationError("Unknown data source.")
	if isinstance(payload, str):
		payload = {"text": payload}
	cleaned = _clean(payload)
	if isinstance(cleaned, dict):
		cleaned["source"] = source
	return f'<data source="{source}">{json.dumps(cleaned, ensure_ascii=False)}</data>'


def unwrap(envelope: str) -> dict:
	"""Parse an envelope back into a dict (tests, and internal callers)."""
	match = re.fullmatch(r'<data source="(live_site|code)">(.*)</data>', envelope, re.DOTALL)
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


def _fit(result: dict, row_lists, field_dicts, source: str = SOURCE_LIVE):
	"""Make the envelope fit MAX_CHARS and keep it valid JSON: shorten strings, drop trailing rows, drop fields.

	`result` must already be cleaned (strings neutralised). Sets `truncated` when anything is removed.
	"""

	def size():
		return len(f'<data source="{source}">{json.dumps(result, ensure_ascii=False)}</data>')

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
	"""Field names the session user may see: permlevel (G3), minus never-send, minus Password fields (#33)."""
	meta = frappe.get_meta(doctype)
	permitted = get_permitted_fields(
		doctype, parenttype=parenttype, user=frappe.session.user, ignore_virtual=True
	)
	blocked = _never_send(doctype) | {df.fieldname for df in meta.fields if df.fieldtype == "Password"}
	valid = set(meta.get_valid_columns())
	skip = _CHILD_LINK_FIELDS if parenttype else ()
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
	return len(getattr(frappe.local, "message_log", None) or [])


def load_readable(doctype, name):
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
		if getattr(frappe.local, "message_log", None) is not None:
			del frappe.local.message_log[log_size:]

	allowed = bool(doc) and frappe.permissions.has_permission(doctype, "read", doc=doc, print_logs=False)
	if not allowed:
		raise RecordNotAvailable(NOT_FOUND)
	return doc


def read_doc(doctype, name) -> str:
	"""One record plus its child rows, as a `<data>` envelope. The only way a tool reads a single record."""
	doc = load_readable(doctype, name)
	meta = frappe.get_meta(doctype)
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
			{fieldname: row.get(fieldname) for fieldname in child_fields} for row in doc.get(df.fieldname) or []
		]

	result = _clean({"doctype": doctype, "name": doc.name, "truncated": False, "data": data, "children": children})
	_fit(
		result,
		row_lists=lambda: result["children"].values(),
		field_dicts=lambda: [result["data"]],
	)
	return as_data(result, SOURCE_LIVE)


# --- list_records ---------------------------------------------------------------------------------------------


def _check_filters(filters, allowed: set[str]) -> dict:
	if filters is None:
		return {}
	if not isinstance(filters, dict):
		raise frappe.ValidationError("Filters must be a dict of field: value or field: [operator, value].")
	clean = {}
	for field, spec in filters.items():
		if field not in allowed:
			raise frappe.ValidationError("A filter uses a field that is not available.")
		if isinstance(spec, list | tuple):
			if len(spec) != 2 or spec[0] not in OPERATORS:
				raise frappe.ValidationError("A filter operator is not allowed.")
			op, value = spec[0], spec[1]
		else:
			op, value = "=", spec
		clean[field] = [op, _check_filter_value(op, value)]
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
	if op == "in":
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

	rows = frappe.get_list(  # AST-ALLOWED: the checked lister: runs as the session user, filters validated above
		doctype,
		filters=clean_filters,
		fields=fields,
		order_by=order_by,
		limit=limit,
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
	_fit(result, row_lists=lambda: [result["rows"]], field_dicts=lambda: result["rows"])
	result["count_returned"] = len(result["rows"])  # after truncation: only rows actually returned
	return as_data(result, SOURCE_LIVE)
