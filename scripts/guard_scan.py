#!/usr/bin/env python3
"""Guardrail scanner (WORKER.md guardrail table, PLAN §2, DECISIONS #35, #40, #41).

Scans `lending_assistant/` (not `tests/`) and exits 1 on any banned pattern that is not on a line marked
`# AST-ALLOWED: <reason>` inside a file that is allowed to use that kind of API. Run it with the bench Python:

    python scripts/guard_scan.py [--root DIR]      # DIR holds the `lending_assistant/` package; default: this repo

The scan is syntactic (Python `ast`, plus line patterns for JavaScript). It resolves `from x import y [as z]`,
`import x as z` and `d = frappe.db` style aliases before it looks at a name, and it DENIES `frappe.db.*` by
default: only the transaction lines the guard marks are on the allowlist. It is a net for mistakes and for a
careless model-written patch, not a proof. What it cannot see is listed in the M2b report ("known limits");
the savepoint rollback, the write trap and the Reviewer's greps are separate layers.
"""

import argparse
import ast
import re
import sys
from pathlib import Path

PACKAGE = "lending_assistant"
MARKER = re.compile(r"(?:#|//)\s*AST-ALLOWED:(.*)$")

# Which files may carry a marked line for each rule. A rule absent here has no allowed file at all.
OWN_WRITERS = ("assistant/audit.py", "assistant/findings.py", "install.py", "patches/")
ALLOWED = {
	"write": OWN_WRITERS,
	"ignore-permissions": OWN_WRITERS,
	"get-doc": (*OWN_WRITERS, "assistant/guard.py", "assistant/settings.py"),
	"get-list": ("assistant/guard.py", "api/chat.py"),
	"db-read": ("install.py",),
	"txn-control": ("assistant/guard.py",),
	"callbacks": ("assistant/guard.py",),  # frappe.db.before/after_commit/rollback and their _functions
	"alias": ("assistant/guard.py",),  # frappe.db / qb / local / session bound to a name or passed on
	"file-access": ("assistant/codereader.py",),
	"db-other": (),  # any frappe.db.<attr> that is not read, write or one of the transaction lines
	"qb": (),
	"client-api": (),  # frappe.client.* / frappe.desk.*: whole documents, no never-send or Password filter (G3)
	"side-effect": (),  # enqueue, sendmail, realtime
	"dynamic": (),  # getattr / setattr / delattr / globals / vars / attrgetter
	"user-switch": (),
	"generic-exec": (),
	"whitelist": (),
	"guest": (),
	"js-html": (),
}

DB_READS = {
	"get_value", "get_values", "get_single_value", "sql", "sql_list", "sql_ddl", "count", "exists",
	"get_all", "get_list", "multisql", "escape",
}  # fmt: skip
GET_DOCS = {"get_doc", "get_cached_doc", "get_last_doc", "get_single", "new_doc", "get_cached_value"}
WRITES = {
	"insert", "save", "submit", "cancel", "delete", "delete_doc", "rename_doc", "set_value", "db_insert",
	"db_update", "db_set", "truncate", "bulk_insert", "set_single_value", "update", "run_method",
}  # fmt: skip
# The ONLY frappe.db attributes tool code may touch, and only on lines the guard marks (DECISIONS #35, #41).
DB_TXN_ALLOWED = {"savepoint", "rollback", "release_savepoint", "_disable_transaction_control", "transaction_writes"}
DB_CALLBACKS = {"before_commit", "after_commit", "before_rollback", "after_rollback"}
TXN_ATTRS = {"_disable_transaction_control", "transaction_writes"}
FILE_CALLS = {"open", "read_text", "read_bytes", "write_text", "write_bytes", "walk", "listdir", "scandir", "glob", "rglob", "iterdir", "copyfile", "rmtree"}  # fmt: skip
EXEC_NAMES = {"eval", "exec", "compile", "__import__"}
DYNAMIC_NAMES = {"getattr", "setattr", "delattr", "globals", "vars"}
EXEC_DOTTED = {
	"os.system", "os.popen", "frappe.call", "frappe.get_attr", "frappe.get_method", "operator.attrgetter",
	"operator.methodcaller", "sys.modules",
}  # fmt: skip
DYNAMIC_DOTTED = {"operator.attrgetter", "operator.methodcaller", "sys.modules"}
EXEC_PREFIXES = ("subprocess", "importlib", "runpy", "pkgutil", "ctypes", "builtins", "frappe.utils.safe_exec")
SIDE_EFFECT_DOTTED = {
	"frappe.sendmail", "frappe.enqueue", "frappe.enqueue_doc", "frappe.publish_realtime", "frappe.publish_progress",
}  # fmt: skip
SIDE_EFFECT_PREFIXES = ("frappe.utils.background_jobs", "frappe.email.queue")
CLIENT_API_PREFIXES = ("frappe.client", "frappe.desk", "frappe.model.db_query")
SIDE_EFFECT_METHODS = {"enqueue", "enqueue_doc", "queue_action", "sendmail", "publish_realtime", "publish_progress"}
# Names that must never be bound to a variable or passed on as a value: the alias would hide later calls.
BARE_ALIAS = {"frappe.db", "frappe.qb", "frappe.local", "frappe.session"}
TRACK_ALIAS = BARE_ALIAS | {"frappe.flags", "frappe.local.session", "frappe.local.flags"}
# Writing to any of these changes who the session is (G2) or switches permission checks off.
PROTECTED = (
	"frappe.session", "frappe.local.session", "frappe.local.user",
	"frappe.flags.ignore_permissions", "frappe.local.flags.ignore_permissions",
)  # fmt: skip
MUTATORS = {"update", "setdefault", "pop", "popitem", "clear", "__setitem__", "__delitem__"}
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


def classify(full: str, call: bool):
	"""(rule, message) when the resolved dotted name is banned, else None."""
	if under(full, "frappe.local.db"):  # frappe.db is a proxy for frappe.local.db
		full = "frappe.db" + full[len("frappe.local.db"):]
	shown = full + ("()" if call else "")
	parts = full.split(".")
	last = parts[-1]
	if any(under(full, p) for p in CLIENT_API_PREFIXES):
		return "client-api", f"{shown}: returns whole documents; use guard.read_doc / guard.list_records (G3)"
	if under(full, "frappe.qb"):
		return "qb", f"{shown}: frappe.qb has no permission check"
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
	if full == "frappe.set_user":
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


class Scanner(ast.NodeVisitor):
	def __init__(self, rel: str, lines: list[str]):
		self.rel = rel
		self.lines = lines
		self.hits: list[tuple[int, str, str]] = []  # (line, rule, message)
		self.skip: set[int] = set()  # decorator nodes that are an allowed whitelist
		self.aliases: dict[str, str] = {}  # local name -> dotted origin (imports and `d = frappe.db`)
		self.handled: set[int] = set()  # Attribute / Name nodes already judged as part of a longer chain

	def hit(self, node, rule: str, message: str):
		self.hits.append((node.lineno, rule, message))

	# --- helpers

	def resolve(self, node) -> str:
		"""Dotted name with the root replaced by what it was imported or assigned from."""
		name = dotted(node)
		root, _, rest = name.partition(".")
		origin = self.aliases.get(root)
		if origin and origin != root:
			return origin + ("." + rest if rest else "")
		return name

	def mark_chain(self, node):
		"""Mark every Attribute / Name in a chain as judged, so the parts are not judged again alone."""
		while isinstance(node, ast.Attribute):
			self.handled.add(id(node))
			node = node.value
		if isinstance(node, ast.Name):
			self.handled.add(id(node))

	def judge_import(self, node, full: str):
		found = classify(full, False)
		if found is None and any(under(full, p) for p in EXEC_PREFIXES):
			found = ("generic-exec", full)
		if found:
			self.hit(node, found[0], f"import of {full}: {found[1]}")

	def identity_target(self, target, node):
		"""A write to the session identity or to the permission flags, in any assignment shape."""
		if isinstance(target, ast.Tuple | ast.List):
			for item in target.elts:
				self.identity_target(item, node)
			return
		if isinstance(target, ast.Starred):
			self.identity_target(target.value, node)
			return
		key = None
		while isinstance(target, ast.Subscript):
			key = target.slice
			target = target.value
		if not isinstance(target, ast.Attribute | ast.Name):
			return
		full = self.resolve(target)
		if full == "frappe.local" or any(under(full, p) for p in PROTECTED):
			self.hit(node, "user-switch", f"write to {full}")
		elif full in ("frappe.flags", "frappe.local.flags") and isinstance(key, ast.Constant):
			if isinstance(key.value, str) and key.value.startswith("ignore_"):
				self.hit(node, "user-switch", f"write to {full}[{key.value!r}]")

	def remember_alias(self, target, value):
		"""`d = frappe.db` -> later `d.sql()` is judged as `frappe.db.sql()`."""
		if not isinstance(target, ast.Name) or not isinstance(value, ast.Attribute | ast.Name):
			return
		full = self.resolve(value)
		if full in TRACK_ALIAS or classify(full, False):
			self.aliases[target.id] = full

	# --- visitors

	def visit_FunctionDef(self, node):
		for dec in node.decorator_list:
			target = dec.func if isinstance(dec, ast.Call) else dec
			if dotted(target).split(".")[-1] == "whitelist":
				if (self.rel, node.name) in WHITELIST_OK:
					self.skip.add(id(dec))
					self.skip.add(id(target))
		self.generic_visit(node)

	visit_AsyncFunctionDef = visit_FunctionDef

	def visit_Import(self, node):
		for item in node.names:
			self.judge_import(node, item.name)
			if item.asname:
				self.aliases[item.asname] = item.name

	def visit_ImportFrom(self, node):
		module = node.module or ""
		if node.level:  # relative import: inside the app, nothing to judge
			return
		for item in node.names:
			if item.name == "*":
				if module == "frappe" or module.startswith("frappe."):
					self.hit(node, "alias", f"star import from {module}")
				continue
			full = f"{module}.{item.name}"
			self.judge_import(node, full)
			self.aliases[item.asname or item.name] = full

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
		if id(node) not in self.handled:
			self.mark_chain(node)
			found = classify(self.resolve(node), False)
			if found:
				self.hit(node, *found)
		self.generic_visit(node)

	def visit_Name(self, node):
		if node.id == "whitelist" and id(node) not in self.skip:
			self.hit(node, "whitelist", "whitelist outside the allowed endpoints")
		elif id(node) not in self.handled and node.id in self.aliases and isinstance(node.ctx, ast.Load):
			found = classify(self.resolve(node), False)
			if found:
				self.hit(node, *found)

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
			self.hits.append((node.value.lineno, "ignore-permissions", f"{node.arg}=..."))
		elif node.arg == "allow_guest":
			self.hits.append((node.value.lineno, "guest", "allow_guest"))
		self.generic_visit(node)

	def visit_Call(self, node):
		func = node.func
		raw = dotted(func)
		name = self.resolve(func)
		last = name.split(".")[-1]
		in_cache = ".cache." in f".{name}." or name.startswith("cache.")
		self.mark_chain(func)
		found = classify(name, True)

		if found:
			self.hit(node, *found)
		elif isinstance(func, ast.Name) and name == raw:  # a builtin, not an imported or assigned name
			if last in EXEC_NAMES:
				self.hit(node, "generic-exec", f"{last}()")
			elif last in DYNAMIC_NAMES:
				self.hit(node, "dynamic", f"{last}(): dynamic attribute access hides what is being touched")
			elif last == "open":
				self.hit(node, "file-access", "open()")
		elif in_cache:
			pass
		elif isinstance(func, ast.Attribute) and last in MUTATORS and any(under(name.rsplit(".", 1)[0], p) for p in PROTECTED):
			self.hit(node, "user-switch", f"{name}()")
		elif last in SIDE_EFFECT_METHODS:
			self.hit(node, "side-effect", f"{name}(): queues work or sends something the rollback cannot undo")
		elif last == "get_all":
			self.hit(node, "db-read", f"{name}()")
		elif last == "get_list" and name.startswith("frappe."):
			self.hit(node, "get-list", f"{name}() outside guard.py")
		elif last in FILE_CALLS:
			self.hit(node, "file-access", f"{name}()")
		elif last in WRITES and isinstance(func, ast.Attribute):
			if last == "update":
				pass  # dict.update / doc.update(values) is not a DB write
			elif last == "run_method" and not name.startswith("frappe."):
				pass
			else:
				self.hit(node, "write", f"{name}()")
		self.generic_visit(node)


def allowed_here(rel: str, rule: str) -> bool:
	return any(rel == a or (a.endswith("/") and rel.startswith(a)) for a in ALLOWED.get(rule, ()))


def check_markers(rel: str, lines: list[str], hits):
	problems = []
	for lineno, rule, message in sorted(set(hits)):
		text = lines[lineno - 1] if 0 < lineno <= len(lines) else ""
		marker = MARKER.search(text)
		if not marker:
			problems.append((lineno, rule, f"{message}: banned here without '# AST-ALLOWED: <reason>'"))
		elif not marker.group(1).strip():
			problems.append((lineno, rule, f"{message}: AST-ALLOWED needs a reason"))
		elif not allowed_here(rel, rule):
			problems.append((lineno, rule, f"{message}: AST-ALLOWED is not permitted in {rel} for '{rule}'"))
	return problems


def scan_python(rel: str, source: str):
	lines = source.splitlines()
	try:
		tree = ast.parse(source)
	except SyntaxError as exc:
		return [(exc.lineno or 1, "syntax", f"cannot parse: {exc.msg}")]
	scanner = Scanner(rel, lines)
	scanner.visit(tree)
	return check_markers(rel, lines, scanner.hits)


def scan_js(rel: str, source: str):
	lines = source.splitlines()
	hits = [(i, "js-html", "raw HTML sink") for i, line in enumerate(lines, 1) if JS_HTML.search(line)]
	return check_markers(rel, lines, hits)


def scan(root: Path) -> tuple[list[str], int]:
	package = root / PACKAGE
	problems, count = [], 0
	for path in sorted(package.rglob("*")):
		rel = path.relative_to(package).as_posix()
		parts = rel.split("/")
		if not path.is_file() or "tests" in parts or "__pycache__" in parts or "node_modules" in parts:
			continue
		if path.suffix == ".py":
			found = scan_python(rel, path.read_text(encoding="utf-8"))
		elif path.suffix == ".js" and "public" in parts and "dist" not in parts:
			found = scan_js(rel, path.read_text(encoding="utf-8"))
		else:
			continue
		count += 1
		problems.extend(f"{PACKAGE}/{rel}:{line}: [{rule}] {message}" for line, rule, message in found)
	return problems, count


def main(argv=None) -> int:
	parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
	parser.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
	args = parser.parse_args(argv)
	root = Path(args.root)
	if not (root / PACKAGE).is_dir():
		print(f"guard_scan: no {PACKAGE}/ folder under {root}", file=sys.stderr)
		return 2
	problems, count = scan(root)
	for line in problems:
		print(line)
	print(f"guard_scan: {'FAILED, ' + str(len(problems)) + ' hit(s)' if problems else 'clean'} ({count} files scanned)")
	return 1 if problems else 0


if __name__ == "__main__":
	sys.exit(main())
