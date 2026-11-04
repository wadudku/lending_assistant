#!/usr/bin/env python3
"""Guardrail scanner (WORKER.md guardrail table, PLAN §2, DECISIONS #35).

Scans `lending_assistant/` (not `tests/`) and exits 1 on any banned pattern that is not on a line marked
`# AST-ALLOWED: <reason>` inside a file that is allowed to use that kind of API. Run it with the bench Python:

    python scripts/guard_scan.py [--root DIR]      # DIR holds the `lending_assistant/` package; default: this repo

The scan is syntactic (Python `ast`, plus line patterns for JavaScript). It is a net for mistakes and for a
careless model-written patch, not a proof: the savepoint rollback and the Reviewer's greps are separate layers.
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
	"file-access": ("assistant/codereader.py",),
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
TXN = {"commit", "rollback", "savepoint", "release_savepoint", "begin"}
TXN_ATTRS = {"_disable_transaction_control", "transaction_writes"}
FILE_CALLS = {"open", "read_text", "read_bytes", "write_text", "write_bytes", "walk", "listdir", "scandir", "glob", "rglob", "iterdir", "copyfile", "rmtree"}  # fmt: skip
EXEC_NAMES = {"eval", "exec", "compile", "__import__"}
EXEC_DOTTED = {"os.system", "os.popen", "frappe.call", "frappe.get_attr", "frappe.get_method", "frappe.enqueue", "frappe.utils.safe_exec.safe_eval"}  # fmt: skip
JS_HTML = re.compile(r"\binnerHTML\b|\bouterHTML\b|insertAdjacentHTML|document\.write|\.html\(|\$\(\s*[`'\"]\s*<")
WHITELIST_OK = {("api/chat.py", "ask"), ("api/chat.py", "feedback"), ("api/findings.py", "save")}


def dotted(node) -> str:
	"""`a.b.c` for Name / Attribute chains; `?` for anything else in the chain."""
	parts = []
	while isinstance(node, ast.Attribute):
		parts.append(node.attr)
		node = node.value
	parts.append(node.id if isinstance(node, ast.Name) else "?")
	return ".".join(reversed(parts))


class Scanner(ast.NodeVisitor):
	def __init__(self, rel: str, lines: list[str]):
		self.rel = rel
		self.lines = lines
		self.hits: list[tuple[int, str, str]] = []  # (line, rule, message)
		self.skip: set[int] = set()  # decorator nodes that are an allowed whitelist

	def hit(self, node, rule: str, message: str):
		self.hits.append((node.lineno, rule, message))

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

	def visit_Attribute(self, node):
		name = dotted(node)
		if node.attr in ("ignore_permissions", "ignore_user_permissions"):
			self.hit(node, "ignore-permissions", f"{name}")
		elif node.attr in TXN_ATTRS:
			self.hit(node, "txn-control", f"{name}")
		elif node.attr == "whitelist" and id(node) not in self.skip:
			self.hit(node, "whitelist", "@frappe.whitelist outside api/chat.py (ask, feedback) and api/findings.py (save)")
		self.generic_visit(node)

	def visit_Name(self, node):
		if node.id == "whitelist" and id(node) not in self.skip:
			self.hit(node, "whitelist", "whitelist outside the allowed endpoints")

	def visit_Assign(self, node):
		for target in node.targets:
			name = dotted(target) if isinstance(target, ast.Attribute) else ""
			if name.startswith(("frappe.session", "frappe.local.session", "frappe.local.user")):
				self.hit(node, "user-switch", f"assignment to {name}")
		self.generic_visit(node)

	def visit_keyword(self, node):
		if node.arg in ("ignore_permissions", "ignore_user_permissions", "ignore_validate", "ignore_links"):
			self.hits.append((node.value.lineno, "ignore-permissions", f"{node.arg}=..."))
		elif node.arg == "allow_guest":
			self.hits.append((node.value.lineno, "guest", "allow_guest"))
		self.generic_visit(node)

	def visit_Call(self, node):
		func = node.func
		name = dotted(func)
		last = name.split(".")[-1]
		in_db = ".db." in f".{name}." or name.startswith("db.")
		in_cache = ".cache." in f".{name}." or name.startswith("cache.")

		if isinstance(func, ast.Name):
			if last in EXEC_NAMES:
				self.hit(node, "generic-exec", f"{last}()")
			elif last == "open":
				self.hit(node, "file-access", "open()")
		elif name in EXEC_DOTTED or name.startswith("subprocess."):
			self.hit(node, "generic-exec", f"{name}()")
		elif name == "frappe.set_user":
			self.hit(node, "user-switch", "frappe.set_user()")
		elif in_db and last in DB_READS:
			self.hit(node, "get-list" if last == "get_list" else "db-read", f"{name}()")
		elif last == "get_all":
			self.hit(node, "db-read", f"{name}()")
		elif last == "get_list" and name.startswith("frappe."):
			self.hit(node, "get-list", f"{name}() outside guard.py")
		elif name.startswith("frappe.") and last in GET_DOCS:
			self.hit(node, "get-doc", f"{name}()")
		elif in_db and last in TXN:
			self.hit(node, "txn-control", f"{name}()")
		elif in_cache:
			pass
		elif last in FILE_CALLS:
			self.hit(node, "file-access", f"{name}()")
		elif last in WRITES and isinstance(func, ast.Attribute):
			if last == "update" and not in_db:
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
	hits = [h for h in scanner.hits]
	return check_markers(rel, lines, hits)


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
