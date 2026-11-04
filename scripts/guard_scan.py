#!/usr/bin/env python3
"""Guardrail scanner (WORKER.md guardrail table, PLAN §2, DECISIONS #35, #40, #41, #43).

Scans `lending_assistant/` (not `tests/`) and exits 1 on any hit that is not excused. Run it with the bench Python:

    python scripts/guard_scan.py [--root DIR] [--check-allowlist]

    DIR holds the `lending_assistant/` package; default: this repo.
    --check-allowlist also fails on dead allowlist entries and on markers that excuse nothing.

HOW IT DECIDES (DECISIONS #43: an allowlist, not a denylist)
  Everything rooted at `frappe` is a hit unless it matches an entry in ALLOWLIST or IMPORT_ALLOWLIST below. A hit is
  excused only by `# AST-ALLOWED: <reason>` on its line, and only in a file that may use that kind of API (ALLOWED
  for the named rules, the `files` of the entry for the allowlist).

  (A) the module can't be bound: the name `frappe` may only be the root of an attribute chain;
  (B) every attribute chain rooted at `frappe` must match an ALLOWLIST entry (`not-allowed` otherwise);
  (C) imports are allowlisted too (`import` otherwise);
  (D) a call to a method named like a DB read, write, commit, identity or side-effect API is a hit whatever the receiver;
  (E) dunders and `__builtins__`; (F) `frappe.conf` / `get_site_config`; (G) writes to `frappe.flags`.

  The named rules below (db-read, write, qb, ...) are the old denylist. They stay because they give a hit a precise
  name and because their per-file marker table is how the existing marked lines are excused.

KNOWN LIMITS (also in build/reports/M2b_r2_report.md): a syntactic scan can't follow values that are computed at run
time (a name built from strings and fetched with a call the scan does not know), anything reached through a module
the app does not own, or code that is not Python/JS under `lending_assistant/`. The run-time layers in
`assistant/guard.py` (write trap, savepoint rollback, identity and connection check, callback snapshot) and the
Reviewer's greps are separate layers. This scan is a net for careless or AI-written code, not a proof against a
determined insider.
"""

import argparse
import ast
import re
import sys
from pathlib import Path
from typing import NamedTuple

PACKAGE = "lending_assistant"
MARKER = re.compile(r"(?:#|//)\s*AST-ALLOWED:(.*)$")

# --- where a marker is accepted ----------------------------------------------------------------------------------------
# Which files may carry a marked line for each named rule. A rule absent here, or with (), has no allowed file at all.
OWN_WRITERS = ("assistant/audit.py", "assistant/findings.py", "install.py", "patches/")
GUARD = "assistant/guard.py"
ALLOWED = {
	"write": OWN_WRITERS,
	"ignore-permissions": OWN_WRITERS,
	"get-doc": (*OWN_WRITERS, GUARD, "assistant/settings.py"),
	"get-list": (GUARD, "api/chat.py"),
	"db-read": ("install.py",),
	"txn-control": (GUARD,),
	"callbacks": (GUARD,),  # frappe.db.before/after_commit/rollback and their _functions
	"alias": (GUARD,),  # frappe.db / qb / local / session bound to a name or passed on
	"user-switch": (GUARD,),  # the run-time identity layer restores user, session and connection (M2b-R8)
	"flags": (GUARD,),  # frappe.flags: only the two helpers in guard.py
	"secrets": ("install.py", "assistant/settings.py"),  # frappe.conf, get_site_config, get_password
	"file-access": ("assistant/codereader.py",),
	"db-other": (),  # any frappe.db.<attr> that is not read, write or one of the transaction lines
	"qb": (),
	"client-api": (),  # frappe.client.* / frappe.desk.*: whole documents, no never-send or Password filter (G3)
	"side-effect": (),  # enqueue, sendmail, realtime
	"dynamic": (),  # getattr / setattr / dunders / globals / vars / attrgetter
	"identity-call": (),  # set_user, connect, init, login_as: no marker is ever accepted
	"generic-exec": (),
	"whitelist": (),
	"guest": (),
	"js-html": (),
	"not-allowed": (),  # (B) a frappe chain that is on no allowlist entry
	"import": (),  # (C) an import that is on no allowlist entry
	"app-api": (),  # (H) one app module reaching another module's private or unlisted names (M2b-R11)
	"controller-import": (),  # (I) a doctype controller class imported outside doctype/ (M2b-R12)
}

# --- (R17) where in guard.py a marker for these rules is accepted -------------------------------------------------------
# A marker excuses a hit only inside one of the named functions (any enclosing function counts, so a nested helper is
# fine). The trusted, marked surface is therefore a handful of functions, not a whole file (DECISIONS #45).
IDENTITY_FUNCS = ("_capture_identity", "_restore_identity", "_discard_connection")
SCOPES = {
	GUARD: {
		"user-switch": IDENTITY_FUNCS,
		"alias": IDENTITY_FUNCS,
		"txn-control": (*IDENTITY_FUNCS, "read_only_tool_context"),
		"callbacks": ("_snapshot_callbacks", "_restore_callbacks"),
		"flags": ("_ast_flag", "_set_ast_flag", "_capture_identity", "_restore_identity", "_restore_flag_values"),
	}
}

# --- (B) the chain allowlist -------------------------------------------------------------------------------------------
# (chain, files, mode, marked). `chain` is a dotted name, `x.*` means `x` and anything below it. `files` are exact
# paths, folder prefixes ending in "/", `**/name/` (any folder called name) or ("*",). `mode` is how the chain is used:
#   read = loaded, not called   call = called   use = read, called or a class base   base = class base only
#   store = assigned or deleted   any = all of them.
# `marked` entries also need `# AST-ALLOWED: <reason>` on the line. Every entry must be used by the app
# (--check-allowlist), so there are no dead entries that widen the hole.
ANYWHERE = ("*",)
ALLOWLIST = [
	# anywhere, unmarked
	("frappe._", ANYWHERE, "call", False),
	("frappe.throw", ANYWHERE, "call", False),
	("frappe.PermissionError", ANYWHERE, "use", False),
	("frappe.ValidationError", ANYWHERE, "use", False),
	("frappe.DoesNotExistError", ANYWHERE, "use", False),
	("frappe.RateLimitExceededError", ANYWHERE, "use", False),
	("frappe.session.user", ANYWHERE, "read", False),
	("frappe.get_roles", ANYWHERE, "call", False),
	("frappe.utils.now_datetime", ANYWHERE, "call", False),
	("frappe.utils.strip_html_tags", ANYWHERE, "call", False),
	# one file or folder, unmarked
	("frappe.utils.get_bench_path", ("assistant/codereader.py",), "call", False),
	("frappe.permissions.has_permission", (GUARD,), "call", False),
	("frappe.model.get_permitted_fields", (GUARD,), "call", False),
	("frappe.model.document.Document", ("**/doctype/",), "base", False),
	("frappe.whitelist", ("api/",), "call", False),
	("frappe.cache.*", ("assistant/ratelimit.py",), "call", False),
	("frappe.local.request_ip", ("api/chat.py",), "read", False),
	# marked lines only. get_meta returns a live Meta (a Document): tool code gets meta facts from guard/access helpers
	("frappe.get_meta", (GUARD, "assistant/access.py", "install.py"), "call", True),
	("frappe.flags.*", (GUARD,), "any", True),
	("frappe.local.message_log", (GUARD,), "any", True),
	("frappe.log_error", (GUARD,), "call", True),
	("frappe.local.site", (GUARD,), "any", True),
	("frappe.session.user", (GUARD,), "store", True),
	("frappe.session.sid", (GUARD,), "any", True),
	("frappe.local.user_perms", (GUARD,), "store", True),
	("frappe.local.role_permissions", (GUARD,), "store", True),
	("frappe.local.cache", (GUARD,), "store", True),
]

# --- (C) the import allowlist ------------------------------------------------------------------------------------------
# (kind, module, name, files). "import" entries are `import module`; "from" entries are `from module import name`.
IMPORT_ALLOWLIST = [
	("import", "frappe", None, ANYWHERE),
	("import", "frappe.permissions", None, (GUARD,)),
	("from", "frappe", "_", ANYWHERE),
	("from", "frappe.utils", "now_datetime", ANYWHERE),
	("from", "frappe.utils", "strip_html_tags", ANYWHERE),
	("from", "frappe.model", "get_permitted_fields", (GUARD,)),
	("from", "frappe.model.document", "Document", ("**/doctype/",)),
]


# --- (H) the app's own modules ---------------------------------------------------------------------------------------
# What any app module may import or call from another app module (M2b-R11). Everything else, and every `_name`, is a
# hit. The first block is the surface tools get; it returns plain data only (tests/test_guard_surface.py).
ASSISTANT = PACKAGE + ".assistant"
APP_API = {
	f"{ASSISTANT}.guard": {
		"read_doc", "list_records", "as_data", "read_only_tool_context", "RecordNotAvailable", "AssistantGuardError",
	},
	f"{ASSISTANT}.access": {"check_my_access", "roles_that_can"},
	f"{ASSISTANT}.codereader": {"read", "search"},
	f"{ASSISTANT}.settings": {"get_settings"},
	f"{ASSISTANT}.audit": set(),
	f"{ASSISTANT}.ratelimit": set(),
	f"{PACKAGE}.install": set(),
}  # fmt: skip
# (module, name, files, reserved): extra names for particular files. `reserved` grants are for code that does not exist
# yet (M4); they are exempt from the dead-entry check and a test shows they work only in their file.
APP_GRANTS = [
	(f"{ASSISTANT}.guard", "require_doctype", ("assistant/access.py",), False),
	(f"{ASSISTANT}.guard", "check_actions", ("assistant/access.py",), False),
	(f"{ASSISTANT}.guard", "SOURCE_LIVE", ("assistant/access.py",), False),
	(f"{ASSISTANT}.guard", "fit", ("assistant/codereader.py",), False),
	(f"{ASSISTANT}.guard", "AssistantRefused", ("assistant/codereader.py",), False),
	(f"{ASSISTANT}.settings", "get_api_key", ("assistant/orchestrator.py",), True),
	(f"{ASSISTANT}.audit", "CONVERSATION", ("api/chat.py",), False),
	(f"{ASSISTANT}.audit", "MESSAGE", ("api/chat.py",), False),
	(f"{ASSISTANT}.audit", "start_conversation", ("api/chat.py",), False),
	(f"{ASSISTANT}.audit", "log_exchange", ("api/chat.py",), False),
	(f"{ASSISTANT}.audit", "set_feedback", ("api/chat.py",), False),
	(f"{ASSISTANT}.ratelimit", "exceeded", ("api/chat.py",), False),
	(f"{ASSISTANT}.ratelimit", "USER_PREFIX", ("api/chat.py",), False),
	(f"{ASSISTANT}.ratelimit", "IP_PREFIX", ("api/chat.py",), False),
	(f"{ASSISTANT}.ratelimit", "FEEDBACK_PREFIX", ("api/chat.py",), False),
	(f"{PACKAGE}.install", "seed_defaults", ("patches/",), False),
	(f"{PACKAGE}.install", "raise_max_tokens_default", ("patches/",), False),
]  # fmt: skip
# A doctype controller: `...doctype.<x>.<x>` (a class that loads rows without any permission check).
CONTROLLER = re.compile(r"(?:^|\.)doctype\.(\w+)\.\1(?:\.|$)")


def grant_key(grant) -> str:
	module, name, files, _reserved = grant
	return f"{module}.{name} in {', '.join(files)}"


def is_app(name: str) -> bool:
	return name == PACKAGE or name.startswith(PACKAGE + ".")


def app_target(full: str):
	"""(module, rest) for the longest APP_API module that `full` starts with, else (None, [])."""
	best = None
	for module in APP_API:
		if (full == module or full.startswith(module + ".")) and (best is None or len(module) > len(best)):
			best = module
	if best is None:
		return None, []
	return best, [part for part in full[len(best) :].split(".") if part]


class Entry(NamedTuple):
	chain: str
	files: tuple
	mode: str
	marked: bool

	@property
	def key(self) -> str:
		return f"{self.chain} [{self.mode}{', marked' if self.marked else ''}] in {', '.join(self.files)}"


ENTRIES = [Entry(*row) for row in ALLOWLIST]
MODES = {
	"read": {"load"}, "call": {"call"}, "use": {"load", "call", "base"}, "base": {"base"}, "store": {"store"},
	"any": {"load", "call", "base", "store"},
}  # fmt: skip


def import_key(entry) -> str:
	kind, module, name, files = entry
	return f"{'import ' + module if kind == 'import' else 'from ' + module + ' import ' + name} in {', '.join(files)}"


def file_ok(rel: str, files) -> bool:
	for spec in files:
		if spec == "*" or rel == spec:
			return True
		if spec.startswith("**/") and spec.endswith("/"):
			if ("/" + rel).find("/" + spec[3:]) != -1:
				return True
		elif spec.endswith("/") and rel.startswith(spec):
			return True
	return False


def chain_matches(pattern: str, full: str) -> bool:
	if pattern.endswith(".*"):
		return full == pattern[:-2] or full.startswith(pattern[:-1])
	return full == pattern


# --- the old denylist: names for hits, and the markers that already excuse today's lines -------------------------------
DB_READS = {
	"get_value", "get_values", "get_single_value", "sql", "sql_list", "sql_ddl", "count", "exists",
	"get_all", "get_list", "multisql", "escape",
}  # fmt: skip
GET_DOCS = {"get_doc", "get_cached_doc", "get_last_doc", "get_single", "new_doc", "get_cached_value"}
WRITES = {
	"insert", "save", "submit", "cancel", "delete", "delete_doc", "rename_doc", "set_value", "db_insert",
	"db_update", "db_set", "truncate", "bulk_insert", "set_single_value", "update", "run_method",
}  # fmt: skip
# The ONLY frappe.db attributes tool code may touch, and only on lines the guard marks (DECISIONS #35, #41, #43).
DB_TXN_ALLOWED = {
	"savepoint", "rollback", "release_savepoint", "_disable_transaction_control", "transaction_writes", "_conn",
	"_cursor", "close",
}  # fmt: skip
DB_CALLBACKS = {"before_commit", "after_commit", "before_rollback", "after_rollback"}
TXN_ATTRS = {"_disable_transaction_control", "transaction_writes", "_conn", "_cursor"}
FILE_CALLS = {"open", "read_text", "read_bytes", "write_text", "write_bytes", "walk", "listdir", "scandir", "glob", "rglob", "iterdir", "copyfile", "rmtree"}  # fmt: skip
EXEC_NAMES = {"eval", "exec", "compile", "__import__"}
DYNAMIC_NAMES = {"getattr", "setattr", "delattr", "globals", "vars"}
EXEC_DOTTED = {
	"os.system", "os.popen", "frappe.call", "frappe.get_attr", "frappe.get_method", "operator.attrgetter",
	"operator.methodcaller", "sys.modules", "sys._getframe", "sys._current_frames", "sys.exc_info",
}  # fmt: skip
DYNAMIC_DOTTED = {"operator.attrgetter", "operator.methodcaller", "sys.modules"}
EXEC_PREFIXES = (
	"subprocess", "importlib", "runpy", "pkgutil", "ctypes", "builtins", "frappe.utils.safe_exec",
	"gc", "inspect", "imp", "code", "codeop", "pdb",
)  # fmt: skip
SIDE_EFFECT_DOTTED = {
	"frappe.sendmail", "frappe.enqueue", "frappe.enqueue_doc", "frappe.publish_realtime", "frappe.publish_progress",
}  # fmt: skip
SIDE_EFFECT_PREFIXES = ("frappe.utils.background_jobs", "frappe.email.queue")
CLIENT_API_PREFIXES = ("frappe.client", "frappe.desk", "frappe.model.db_query")
SECRET_PREFIXES = ("frappe.conf", "os.environ", "os.getenv", "os.putenv")
SECRET_DOTTED = {"frappe.get_site_config"}
# Names that must never be bound to a variable or passed on as a value: the alias would hide later calls.
BARE_ALIAS = {"frappe.db", "frappe.qb", "frappe.local", "frappe.session"}
TRACK_ALIAS = BARE_ALIAS | {"frappe.flags", "frappe.local.session", "frappe.local.flags"}
# `frappe.local.<x>` is what `frappe.<x>` points to for these.
LOCAL_PROXIED = {"db", "qb", "flags", "session", "conf"}
# Writing to any of these changes who the session is (G2) or switches permission checks off.
PROTECTED = (
	"frappe.session", "frappe.local.session", "frappe.local.user",
	"frappe.flags.ignore_permissions", "frappe.local.flags.ignore_permissions",
)  # fmt: skip
MUTATORS = {"update", "setdefault", "pop", "popitem", "clear", "__setitem__", "__delitem__"}

# (D) method names that are banned whatever the receiver is (an alias cannot hide them): name -> rule.
METHOD_RULES = {
	**dict.fromkeys(["sql", "sql_ddl", "multisql", "get_value", "get_values", "get_all", "sql_list", "get_single_value"], "db-read"),
	**dict.fromkeys(["get_doc", "get_cached_doc", "new_doc", "get_last_doc", "get_cached_value", "get_single"], "get-doc"),
	**dict.fromkeys(["delete_doc", "rename_doc", "set_value", "db_set", "insert", "save", "submit", "cancel", "delete", "db_insert", "db_update", "truncate", "bulk_insert", "set_single_value"], "write"),  # fmt: skip
	**dict.fromkeys(["commit", "rollback"], "txn-control"),
	**dict.fromkeys(["connect", "init", "login_as", "set_user"], "user-switch"),
	**dict.fromkeys(["enqueue", "enqueue_doc", "queue_action", "sendmail", "publish_realtime", "publish_progress"], "side-effect"),
	**dict.fromkeys(["get_site_config", "get_password"], "secrets"),
	"get_list": "get-list",
	"run": "qb",  # only when the receiver chain has qb / query in it
}  # fmt: skip
QB_WORDS = {"qb", "query", "query_builder", "Engine", "get_query", "from_"}

# (E) dunders: a way to reach builtins or the module dict without naming them.
DUNDERS = {
	"__builtins__", "__dict__", "__class__", "__globals__", "__subclasses__", "__mro__", "__getattribute__",
	"__import__", "__getattr__", "__setattr__", "__delattr__", "__bases__", "__base__", "__code__", "__closure__",
	"__func__", "__self__", "__reduce__", "__reduce_ex__", "mro",  # `type(x).mro()[1]` reaches the Document class (R12)
	# stack frames and tracebacks hand out another module's globals (`frame.f_globals['frappe']`)
	"f_globals", "f_locals", "f_back", "f_builtins", "gi_frame", "cr_frame", "ag_frame", "tb_frame",
}  # fmt: skip
DUNDER_NAMES = {"__builtins__", "__import__"}

JS_HTML = re.compile(r"\binnerHTML\b|\bouterHTML\b|insertAdjacentHTML|document\.write|\.html\(|\$\(\s*[`'\"]\s*<")
WHITELIST_OK = {("api/chat.py", "ask"), ("api/chat.py", "feedback"), ("api/findings.py", "save")}


def dotted(node) -> str:
	"""`a.b.c` for Name / Attribute chains; `?` for anything else at the root of the chain."""
	parts = []
	while isinstance(node, ast.Attribute):
		parts.append(node.attr)
		node = node.value
	parts.append(node.id if isinstance(node, ast.Name) else "?")
	return ".".join(reversed(parts))


def under(full: str, prefix: str) -> bool:
	return full == prefix or full.startswith(prefix + ".")


def normalise(full: str) -> str:
	"""`frappe.local.db` is what the `frappe.db` proxy points to: judge them as the same thing."""
	parts = full.split(".")
	if parts[:2] == ["frappe", "local"] and len(parts) > 2 and parts[2] in LOCAL_PROXIED:
		return ".".join(["frappe", *parts[2:]])
	return full


def classify(full: str, call: bool):
	"""(rule, message) when the resolved dotted name is on the old denylist, else None."""
	full = normalise(full)
	shown = full + ("()" if call else "")
	parts = full.split(".")
	last = parts[-1]
	if any(under(full, p) for p in CLIENT_API_PREFIXES):
		return "client-api", f"{shown}: returns whole documents; use guard.read_doc / guard.list_records (G3)"
	if under(full, "frappe.qb") or under(full, "frappe.query_builder"):
		return "qb", f"{shown}: the query builder has no permission check"
	if any(under(full, p) for p in SECRET_PREFIXES) or full in SECRET_DOTTED:
		return "secrets", f"{shown}: site secrets (G8, G12)"
	if parts[:2] == ["frappe", "db"]:
		if len(parts) == 2:
			return "alias", "frappe.db bound to a name or passed as a value"
		attr = parts[2]
		if attr in DB_CALLBACKS:
			return "callbacks", f"{shown}: commit/rollback callbacks"
		if attr in DB_TXN_ALLOWED:
			return "txn-control", shown
		if attr in DB_READS:
			return ("get-list" if attr == "get_list" else "db-read"), shown
		if attr in WRITES:
			return "write", shown
		return "db-other", f"{shown}: frappe.db.{attr} is not on the allowlist (DDL, defaults, commit and the rest)"
	if full in ("frappe.get_value", "frappe.get_single_value", "frappe.get_all"):
		return "db-read", shown
	if full == "frappe.get_list":
		return "get-list", f"{shown} outside guard.py"
	if parts[0] == "frappe" and len(parts) == 2 and last in GET_DOCS:
		return "get-doc", shown
	if full in ("frappe.set_user", "frappe.connect", "frappe.init", "frappe.connect_replica"):
		return "user-switch", shown
	if full in SIDE_EFFECT_DOTTED or any(under(full, p) for p in SIDE_EFFECT_PREFIXES):
		return "side-effect", f"{shown}: queues work or sends something the rollback cannot undo"
	if full in DYNAMIC_DOTTED:
		return "dynamic", shown
	if full in EXEC_DOTTED or any(under(full, p) for p in EXEC_PREFIXES):
		return "generic-exec", shown
	if full in BARE_ALIAS:
		return "alias", f"{full} bound to a name or passed as a value"
	if parts[0] == "frappe" and len(parts) == 2 and last in WRITES and last not in ("update", "run_method"):
		return "write", shown
	return None


class Hit(NamedTuple):
	line: int
	rule: str
	message: str
	files: tuple | None = None  # None: use ALLOWED[rule]


class Scanner(ast.NodeVisitor):
	def __init__(self, rel: str, lines: list[str], tree: ast.AST):
		self.rel = rel
		self.lines = lines
		self.hits: list[Hit] = []
		self.skip: set[int] = set()  # decorator nodes that are an allowed whitelist
		self.aliases: dict[str, str] = {}  # local name -> dotted origin (imports and `d = frappe.db`)
		self.used_entries: set[str] = set()
		self.parent: dict[int, ast.AST] = {}
		for outer in ast.walk(tree):
			for child in ast.iter_child_nodes(outer):
				self.parent[id(child)] = outer
		self.collect_imports(tree)

	def hit(self, node, rule: str, message: str, files=None):
		self.hits.append(Hit(node.lineno, rule, message, files))

	def hit_found(self, node, found, call: bool):
		self.hit(node, *found)
		if call and found[0] == "user-switch":
			self.hit(node, "identity-call", f"{found[1]}: an identity or connection switch; no marker is accepted")

	# --- helpers

	def resolve(self, node) -> str:
		"""Dotted name with the root replaced by what it was imported or assigned from."""
		name = dotted(node)
		root, _, rest = name.partition(".")
		origin = self.aliases.get(root)
		if origin and origin != root:
			return origin + ("." + rest if rest else "")
		return name

	def is_chain_base(self, node) -> bool:
		parent = self.parent.get(id(node))
		return isinstance(parent, ast.Attribute) and parent.value is node

	def use_of(self, node) -> str:
		parent = self.parent.get(id(node))
		if isinstance(getattr(node, "ctx", None), ast.Store | ast.Del):
			return "store"
		if isinstance(parent, ast.Call) and parent.func is node:
			return "call"
		if isinstance(parent, ast.Subscript) and parent.value is node and isinstance(parent.ctx, ast.Store | ast.Del):
			return "store"
		if isinstance(parent, ast.ClassDef) and node in parent.bases:
			return "base"
		return "load"

	# --- (C) imports, collected before the walk so the order of statements does not matter

	def import_allowed(self, kind: str, module: str, name: str | None):
		for entry in IMPORT_ALLOWLIST:
			if entry[0] == kind and entry[1] == module and entry[2] == name and file_ok(self.rel, entry[3]):
				self.used_entries.add(import_key(entry))
				return True
		return False

	def collect_imports(self, tree):
		for node in ast.walk(tree):
			if isinstance(node, ast.Import):
				for item in node.names:
					self.judge_import_statement(node, item)
			elif isinstance(node, ast.ImportFrom):
				self.judge_from_import(node)

	def judge_import_statement(self, node, item):
		name = item.name
		if item.asname:
			self.aliases[item.asname] = name
			self.check_binding(node, item.asname)
		if name == "frappe" or name.startswith("frappe."):
			if item.asname:
				self.hit(node, "alias", f"import {name} as {item.asname}: the frappe module may not be bound to another name (A)")
			found = classify(name, False)
			if found:
				self.hit(node, found[0], f"import of {name}: {found[1]}")
			if not self.import_allowed("import", name, None):
				self.hit(node, "import", f"import {name} is not on the import allowlist (C)")
		elif any(under(name, p) for p in EXEC_PREFIXES):
			self.hit(node, "generic-exec", f"import of {name}")
		elif is_app(name):
			self.judge_app_import(node, name)
		self.judge_controller(node, name)

	def judge_from_import(self, node):
		module = self.absolute_module(node)
		for item in node.names:
			bound = item.asname or item.name
			if bound == "frappe":
				self.hit(node, "alias", "a name `frappe` bound by an import")
		is_app_module = is_app(module)
		is_frappe = module == "frappe" or module.startswith("frappe.")
		for item in node.names:
			if item.name == "*":
				self.hit(node, "app-api" if is_app_module else "alias" if is_frappe else "import", f"star import from {module}")
				continue
			full = f"{module}.{item.name}"
			self.aliases[item.asname or item.name] = full
			self.judge_controller(node, full)
			if is_app_module:
				self.judge_app_import(node, full)
				continue
			if is_frappe:
				found = classify(full, False)
				if found:
					self.hit(node, found[0], f"import of {full}: {found[1]}")
				if item.asname and item.asname != item.name:
					self.hit(node, "alias", f"from {module} import {item.name} as {item.asname}: no other names for frappe things (A)")
				if not self.import_allowed("from", module, item.name):
					self.hit(node, "import", f"from {module} import {item.name} is not on the import allowlist (C)")
			elif any(under(full, p) for p in EXEC_PREFIXES) or full in EXEC_DOTTED or full in DYNAMIC_DOTTED:
				self.hit(node, "generic-exec" if full not in DYNAMIC_DOTTED else "dynamic", f"import of {full}")

	def absolute_module(self, node) -> str:
		"""The dotted module of a `from` import, with a relative import resolved against this file."""
		if not node.level:
			return node.module or ""
		package = [PACKAGE, *self.rel.split("/")[:-1]]
		base = package[: len(package) - (node.level - 1)]
		return ".".join([*base, *([node.module] if node.module else [])])

	def own_module(self) -> str:
		parts = self.rel[:-3].split("/") if self.rel.endswith(".py") else self.rel.split("/")
		if parts[-1] == "__init__":
			parts = parts[:-1]
		return ".".join([PACKAGE, *parts])

	# --- (H) the app's own modules, (I) controller classes

	def judge_controller(self, node, full: str):
		if CONTROLLER.search(full) and not file_ok(self.rel, ("**/doctype/",)):
			self.hit(node, "controller-import", f"{full}: a doctype controller loads rows with no permission check (I)")

	def judge_app_import(self, node, full: str):
		"""`import a.b` / `from a import b`: a module may be imported; an unknown module, or a private or unlisted
		name, is a hit on the import line too (uses are judged where they happen)."""
		if full in APP_API or full == self.own_module():
			return
		module, rest = app_target(full)
		if module is None:
			self.hit(node, "app-api", f"{full} is not an app module on the API table (H)")
		elif module != self.own_module():
			self.app_name_check(node, module, rest)

	def app_name_check(self, node, module: str, rest: list):
		name = rest[0]
		if any(part.startswith("_") for part in rest):
			self.hit(node, "app-api", f"{module}.{'.'.join(rest)}: a private name of another app module (H)")
			return
		if name in APP_API[module]:
			return
		for grant in APP_GRANTS:
			if grant[0] == module and grant[1] == name and file_ok(self.rel, grant[2]):
				self.used_entries.add(grant_key(grant))
				return
		self.hit(node, "app-api", f"{module}.{name} is not a public name of {module.rsplit('.', 1)[1]} for {self.rel} (H)")

	def judge_app(self, node, full: str, use: str):
		module, rest = app_target(full)
		if module is None:
			self.hit(node, "app-api", f"{full} is not an app module on the API table (H)")
		elif module == self.own_module():
			return
		elif not rest:
			self.hit(node, "app-api", f"{module} used as a value: it may only be the root of an attribute chain (H)")
		else:
			self.app_name_check(node, module, rest)

	# --- (B) the allowlist

	def judge_chain(self, node):
		"""Judge one maximal chain: `a.b.c` (or a bare imported name) with the way it is used."""
		resolved = self.resolve(node)
		full = normalise(resolved)
		use = self.use_of(node)
		call = use == "call"
		found = classify(resolved, call)
		if found:
			self.hit_found(node, found, call)
		elif full.split(".")[0] == "frappe":
			self.judge_allowlist(node, full, use)
		elif is_app(full):
			self.judge_app(node, full, use)
		if full.split(".")[0] == "frappe" and under(full, "frappe.flags"):
			self.judge_flags(node, use)

	def judge_allowlist(self, node, full: str, use: str):
		matches = [
			e for e in ENTRIES if chain_matches(e.chain, full) and use in MODES[e.mode] and file_ok(self.rel, e.files)
		]
		if not matches:
			self.hit(node, "not-allowed", f"{full} ({use}) is not on the allowlist for {self.rel} (B)")
			return
		plain = [e for e in matches if not e.marked]
		if plain:
			self.used_entries.add(plain[0].key)
			return
		self.used_entries.add(matches[0].key)
		self.hit(node, "not-allowed", f"{full}: allowed here only on a line marked '# AST-ALLOWED: <reason>'", matches[0].files)

	def judge_flags(self, node, use: str):
		"""(G) frappe.flags may only be touched by guard.py's marked helpers: no write, mutator or computed key."""
		parent = self.parent.get(id(node))
		if use == "store":
			self.hit(node, "flags", "write to frappe.flags")
		elif isinstance(parent, ast.Subscript) and parent.value is node and not isinstance(parent.slice, ast.Constant):
			self.hit(node, "flags", "computed key on frappe.flags")
		elif use == "call" and dotted(node).split(".")[-1] in MUTATORS:
			self.hit(node, "flags", f"{dotted(node)}() changes frappe.flags")

	# --- (A) the module cannot be bound

	def check_binding(self, node, name):
		if name == "frappe":
			self.hit(node, "alias", "the name `frappe` is rebound (A)")

	def visit_arg(self, node):
		self.check_binding(node, node.arg)
		self.generic_visit(node)

	def visit_Global(self, node):
		for name in node.names:
			self.check_binding(node, name)

	visit_Nonlocal = visit_Global

	def visit_ExceptHandler(self, node):
		if node.name:
			self.check_binding(node, node.name)
		self.generic_visit(node)

	def visit_ClassDef(self, node):
		self.check_binding(node, node.name)
		self.generic_visit(node)

	def visit_MatchAs(self, node):
		if node.name:
			self.check_binding(node, node.name)
		self.generic_visit(node)

	def visit_MatchStar(self, node):
		if node.name:
			self.check_binding(node, node.name)
		self.generic_visit(node)

	def visit_MatchMapping(self, node):
		if node.rest:
			self.check_binding(node, node.rest)
		self.generic_visit(node)

	def identity_target(self, target, node):
		"""A write to the session identity, the connection or the permission flags, in any assignment shape."""
		if isinstance(target, ast.Tuple | ast.List):
			for item in target.elts:
				self.identity_target(item, node)
			return
		if isinstance(target, ast.Starred):
			self.identity_target(target.value, node)
			return
		key = None
		direct = True
		while isinstance(target, ast.Subscript):
			key = target.slice
			target = target.value
			direct = False
		if not isinstance(target, ast.Attribute | ast.Name):
			return
		full = self.resolve(target)
		parts = full.split(".")
		if full == "frappe.local" or any(under(full, p) for p in PROTECTED):
			self.hit(node, "user-switch", f"write to {full}")
		elif direct and parts[:2] == ["frappe", "local"] and len(parts) == 3:
			self.hit(node, "user-switch", f"write to {full}")
		elif normalise(full) in ("frappe.flags",) and isinstance(key, ast.Constant):
			if isinstance(key.value, str) and key.value.startswith("ignore_"):
				self.hit(node, "user-switch", f"write to {full}[{key.value!r}]")

	def remember_alias(self, target, value):
		"""`d = frappe.db` -> later `d.sql()` is judged as `frappe.db.sql()`."""
		if not isinstance(target, ast.Name) or not isinstance(value, ast.Attribute | ast.Name):
			return
		full = self.resolve(value)
		if normalise(full) in TRACK_ALIAS or classify(full, False):
			self.aliases[target.id] = full

	# --- visitors

	def visit_FunctionDef(self, node):
		self.check_binding(node, node.name)
		for dec in node.decorator_list:
			target = dec.func if isinstance(dec, ast.Call) else dec
			if dotted(target).split(".")[-1] == "whitelist":
				if (self.rel, node.name) in WHITELIST_OK:
					self.skip.add(id(dec))
					self.skip.add(id(target))
		self.generic_visit(node)

	visit_AsyncFunctionDef = visit_FunctionDef

	def visit_Attribute(self, node):
		name = dotted(node)
		if node.attr in ("ignore_permissions", "ignore_user_permissions"):
			self.hit(node, "ignore-permissions", f"{name}")
		elif node.attr in TXN_ATTRS:
			self.hit(node, "txn-control", f"{name}")
		elif node.attr == "_functions":
			self.hit(node, "callbacks", f"{name}: private callback queue")
		elif node.attr == "whitelist" and id(node) not in self.skip:
			self.hit(node, "whitelist", "@frappe.whitelist outside api/chat.py (ask, feedback) and api/findings.py (save)")
		if node.attr in DUNDERS:
			self.hit(node, "dynamic", f"{name}: dunder access (E)")
		if node.attr == "frappe":
			self.hit(node, "alias", f"{name}: the frappe module reached through another object (A)")
		if not self.is_chain_base(node):
			self.judge_chain(node)
		self.generic_visit(node)

	def visit_Name(self, node):
		if node.id == "whitelist" and id(node) not in self.skip:
			self.hit(node, "whitelist", "whitelist outside the allowed endpoints")
		if node.id in DUNDER_NAMES:
			self.hit(node, "dynamic", f"{node.id}: reaches the builtins without naming them (E)")
		if node.id == "frappe":
			if isinstance(node.ctx, ast.Store | ast.Del):
				self.hit(node, "alias", "the name `frappe` is rebound (A)")
			elif not self.is_chain_base(node):
				self.hit(node, "alias", "`frappe` used as a value: it may only be the root of an attribute chain (A)")
		elif node.id in self.aliases and isinstance(node.ctx, ast.Load) and not self.is_chain_base(node):
			self.judge_chain(node)

	def visit_Subscript(self, node):
		key = node.slice
		if isinstance(key, ast.Constant) and isinstance(key.value, str) and key.value in DUNDERS:
			self.hit(node, "dynamic", f"subscript {key.value!r}: dunder access (E)")
		self.generic_visit(node)

	def visit_Assign(self, node):
		for target in node.targets:
			self.identity_target(target, node)
			self.remember_alias(target, node.value)
		self.generic_visit(node)

	def visit_AnnAssign(self, node):
		self.identity_target(node.target, node)
		if node.value is not None:
			self.remember_alias(node.target, node.value)
		self.generic_visit(node)

	def visit_AugAssign(self, node):
		self.identity_target(node.target, node)
		self.generic_visit(node)

	def visit_Delete(self, node):
		for target in node.targets:
			self.identity_target(target, node)
		self.generic_visit(node)

	def visit_keyword(self, node):
		if node.arg in ("ignore_permissions", "ignore_user_permissions", "ignore_validate", "ignore_links"):
			self.hits.append(Hit(node.value.lineno, "ignore-permissions", f"{node.arg}=..."))
		elif node.arg == "allow_guest":
			self.hits.append(Hit(node.value.lineno, "guest", "allow_guest"))
		self.generic_visit(node)

	def visit_Call(self, node):
		func = node.func
		if isinstance(func, ast.Attribute):
			self.judge_method(node, func)
		elif isinstance(func, ast.Name) and func.id not in self.aliases:  # a builtin, not an imported or assigned name
			if func.id in EXEC_NAMES:
				self.hit(node, "generic-exec", f"{func.id}()")
			elif func.id in DYNAMIC_NAMES:
				self.hit(node, "dynamic", f"{func.id}(): dynamic attribute access hides what is being touched")
			elif func.id == "open":
				self.hit(node, "file-access", "open()")
			elif func.id == "type" and len(node.args) == 1 and not node.keywords:
				self.hit(node, "dynamic", "type(x): hands out the class of any object, Document included (R12)")
		self.generic_visit(node)

	def judge_method(self, node, func):
		"""(D) a method name is judged whatever the receiver, so an alias cannot hide it."""
		method = func.attr
		name = self.resolve(func)
		rule = METHOD_RULES.get(method)
		if method == "run" and not any(
			(isinstance(n, ast.Attribute) and n.attr in QB_WORDS) or (isinstance(n, ast.Name) and n.id in QB_WORDS)
			for n in ast.walk(func.value)
		):
			rule = None
		if rule:
			found = (rule, f"{name}(): `.{method}()` is banned whatever the receiver is (D)")
			self.hit_found(node, found, True)
		if method in MUTATORS:
			receiver = self.resolve(func.value)
			if any(under(receiver, p) for p in PROTECTED):
				self.hit(node, "user-switch", f"{name}()")
			if dotted(func.value).split(".")[-1] == "flags":
				self.hit(node, "flags", f"{name}() changes a flags dict")
		if method in FILE_CALLS:
			self.hit(node, "file-access", f"{name}()")


def allowed_here(rel: str, rule: str, files=None) -> bool:
	return file_ok(rel, ALLOWED.get(rule, ()) if files is None else files)


def in_scope(rel: str, rule: str, line: int, functions) -> bool:
	"""R17: for the scoped rules a marker is accepted only inside the named functions of that file."""
	names = SCOPES.get(rel, {}).get(rule)
	if names is None:
		return True
	return any(name in names and start <= line <= end for name, start, end in functions)


def check_markers(rel: str, lines: list[str], hits, used_lines: set[int], functions=()):
	problems = []
	seen = set()
	for hit in sorted(set(hits), key=lambda h: (h.line, h.rule, h.message)):
		if (hit.line, hit.rule, hit.files) in seen:  # one report per line and rule (and excuse)
			continue
		seen.add((hit.line, hit.rule, hit.files))
		text = lines[hit.line - 1] if 0 < hit.line <= len(lines) else ""
		marker = MARKER.search(text)
		if not marker:
			problems.append((hit.line, hit.rule, f"{hit.message}: banned here without '# AST-ALLOWED: <reason>'"))
		elif not marker.group(1).strip():
			problems.append((hit.line, hit.rule, f"{hit.message}: AST-ALLOWED needs a reason"))
		elif not allowed_here(rel, hit.rule, hit.files):
			problems.append((hit.line, hit.rule, f"{hit.message}: AST-ALLOWED is not permitted in {rel} for '{hit.rule}'"))
		elif not in_scope(rel, hit.rule, hit.line, functions):
			where = ", ".join(SCOPES[rel][hit.rule])
			problems.append((hit.line, hit.rule, f"{hit.message}: AST-ALLOWED for '{hit.rule}' is accepted only inside {where} (R17)"))
		else:
			used_lines.add(hit.line)
	return problems


def check_marker_lines(lines: list[str], used_lines: set[int], strict: bool):
	"""A marker needs a reason wherever it is; with `strict`, a marker that excuses nothing is a problem too."""
	problems = []
	for number, text in enumerate(lines, 1):
		marker = MARKER.search(text)
		if not marker:
			continue
		if not marker.group(1).strip():
			problems.append((number, "marker", "AST-ALLOWED needs a reason"))
		elif strict and number not in used_lines:
			problems.append((number, "marker", "AST-ALLOWED excuses nothing on this line: remove it"))
	return problems


def scan_python(rel: str, source: str, used: set[str], strict: bool = False):
	lines = source.splitlines()
	try:
		tree = ast.parse(source)
	except SyntaxError as exc:
		return [(exc.lineno or 1, "syntax", f"cannot parse: {exc.msg}")]
	scanner = Scanner(rel, lines, tree)
	scanner.visit(tree)
	used |= scanner.used_entries
	used_lines: set[int] = set()
	functions = [
		(n.name, n.lineno, n.end_lineno or n.lineno)
		for n in ast.walk(tree)
		if isinstance(n, ast.FunctionDef | ast.AsyncFunctionDef)
	]
	problems = check_markers(rel, lines, scanner.hits, used_lines, functions)
	extra = check_marker_lines(lines, used_lines, strict)
	return problems + [p for p in extra if not any(q[0] == p[0] and "needs a reason" in q[2] for q in problems)]


def scan_js(rel: str, source: str, strict: bool = False):
	lines = source.splitlines()
	hits = [Hit(i, "js-html", "raw HTML sink") for i, line in enumerate(lines, 1) if JS_HTML.search(line)]
	used_lines: set[int] = set()
	problems = check_markers(rel, lines, hits, used_lines)
	extra = check_marker_lines(lines, used_lines, strict)
	return problems + [p for p in extra if not any(q[0] == p[0] and "needs a reason" in q[2] for q in problems)]


class Result(NamedTuple):
	problems: list[str]
	count: int
	unused_entries: list[str]


def all_entry_keys() -> list[str]:
	return (
		[e.key for e in ENTRIES]
		+ [import_key(e) for e in IMPORT_ALLOWLIST]
		+ [grant_key(g) for g in APP_GRANTS if not g[3]]
	)


def scan(root: Path, strict: bool = False) -> Result:
	package = root / PACKAGE
	problems, count, used = [], 0, set()
	for path in sorted(package.rglob("*")):
		rel = path.relative_to(package).as_posix()
		parts = rel.split("/")
		if not path.is_file() or "tests" in parts or "__pycache__" in parts or "node_modules" in parts:
			continue
		if path.suffix == ".py":
			found = scan_python(rel, path.read_text(encoding="utf-8"), used, strict)
		elif path.suffix == ".js" and "public" in parts and "dist" not in parts:
			found = scan_js(rel, path.read_text(encoding="utf-8"), strict)
		else:
			continue
		count += 1
		problems.extend(f"{PACKAGE}/{rel}:{line}: [{rule}] {message}" for line, rule, message in found)
	return Result(problems, count, [key for key in all_entry_keys() if key not in used])


def main(argv=None) -> int:
	parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
	parser.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
	parser.add_argument("--check-allowlist", action="store_true", help="also fail on dead allowlist entries and unused markers")
	args = parser.parse_args(argv)
	root = Path(args.root)
	if not (root / PACKAGE).is_dir():
		print(f"guard_scan: no {PACKAGE}/ folder under {root}", file=sys.stderr)
		return 2
	result = scan(root, strict=args.check_allowlist)
	problems = list(result.problems)
	if args.check_allowlist:
		problems += [f"allowlist: dead entry, used nowhere in the app: {key}" for key in result.unused_entries]
	for line in problems:
		print(line)
	print(f"guard_scan: {'FAILED, ' + str(len(problems)) + ' hit(s)' if problems else 'clean'} ({result.count} files scanned)")
	return 1 if problems else 0


if __name__ == "__main__":
	sys.exit(main())
