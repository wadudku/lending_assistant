"""M4a scanner: the import allowlist (#45, #138, #142). Every import in the scanned app code must match a row for that
file; network and database-driver modules are a hit everywhere; `import x as y` needs its own row; and
`from os import remove`-style imports of file-changing names are hits (closes the #142 gap).

Each case is written into its own tree and judged by scripts/guard_scan.py on its own.
"""

import ast
import importlib.util
import shutil
import sys

from lending_assistant.tests.base import AssistantTestCase
from lending_assistant.tests.test_guard_scan import SCRIPT, run, tree

NETWORK = [
	"import socket",
	"import requests",
	"from urllib import request",
	"import urllib.request",
	"from urllib.request import urlopen",
	"import http.client",
	"from http import client",
	"import sqlite3",
	"import pymysql",
	"import MySQLdb",
	"import httpx",
	"import smtplib",
	"import ssl",
	"from socket import socket",
]
FILE_CHANGING = [
	"from os import remove",
	"from os import path",
	"from os import unlink, rename",
	"from shutil import move",
	"from shutil import rmtree",
	"from pathlib import Path",
]
# files in which every one of these must be a hit (a tool file, the orchestrator-to-be, a scoped kb file)
FILES = ["assistant/tools/live.py", "assistant/orchestrator.py", "kb/store.py", "assistant/access.py"]


def load_scanner():
	spec = importlib.util.spec_from_file_location("guard_scan_imports_test", SCRIPT)
	module = importlib.util.module_from_spec(spec)
	sys.modules[spec.name] = module
	spec.loader.exec_module(module)
	return module


class TestImportAllowlist(AssistantTestCase):
	def scan(self, rel, source):
		root = tree({rel: source})
		self.addCleanup(shutil.rmtree, root, True)
		return run("--root", root)

	def assertHit(self, rel, source, rule, msg=""):
		result = self.scan(rel, source)
		self.assertEqual(result.returncode, 1, f"{msg}: not flagged\n{result.stdout}")
		self.assertIn(f"[{rule}]", result.stdout, f"{msg}\n{result.stdout}")

	def assertClean(self, rel, source, msg=""):
		result = self.scan(rel, source)
		self.assertEqual(result.returncode, 0, f"{msg}\n{result.stdout}")

	def test_network_and_database_modules_are_a_hit_in_every_file(self):
		for rel in [*FILES, "kb/ingest.py", "assistant/guard.py", "api/chat.py", "install.py"]:
			for line in NETWORK:
				with self.subTest(rel=rel, line=line):
					self.assertHit(rel, f"{line}\n", "network-import", f"{line} in {rel}")

	def test_no_marker_excuses_a_network_import(self):
		for rel in ("assistant/guard.py", "assistant/audit.py", "kb/store.py"):
			with self.subTest(rel=rel):
				self.assertHit(rel, "import socket  # AST-ALLOWED: needed\n", "network-import")

	def test_network_import_is_a_hit_even_inside_a_function(self):
		self.assertHit(
			"assistant/tools/live.py",
			"def f():\n    import requests\n    return requests.get('x')\n",
			"network-import",
		)

	def test_anthropic_is_a_hit_everywhere_today_the_orchestrator_row_comes_in_m4b(self):
		for rel in (
			"assistant/tools/live.py",
			"assistant/orchestrator.py",
			"api/chat.py",
			"assistant/guard.py",
		):
			for line in ("import anthropic", "from anthropic import Anthropic"):
				with self.subTest(rel=rel, line=line):
					self.assertHit(rel, f"{line}\n", "import", f"{line} in {rel}")

	def test_file_changing_names_imported_from_a_stdlib_module_are_hits(self):
		for rel in FILES:
			for line in FILE_CHANGING:
				with self.subTest(rel=rel, line=line):
					self.assertHit(rel, f"{line}\n", "import", f"{line} in {rel}")

	def test_a_marker_does_not_excuse_an_import(self):
		self.assertHit("kb/store.py", "from os import remove  # AST-ALLOWED: cleanup\n", "import")

	def test_an_import_outside_its_files_row_is_a_hit(self):
		for rel, line in [
			("assistant/tools/live.py", "import os"),
			("assistant/tools/live.py", "import json"),
			("assistant/tools/code.py", "import re"),
			("kb/store.py", "import tempfile"),
			("kb/lookup.py", "import json"),
			("kb/retrieve.py", "import math"),
			("assistant/access.py", "import time"),
			("api/chat.py", "import json"),
			("assistant/guard.py", "import time"),
			("assistant/tools/live.py", "from typing import Any"),
			("assistant/tools/live.py", "import copy"),
			("assistant/tools/live.py", "from functools import lru_cache"),
			("assistant/tools/live.py", "import subprocess"),
		]:
			with self.subTest(rel=rel, line=line):
				self.assertHit(
					rel, f"{line}\n", "import" if "subprocess" not in line else "generic-exec", line
				)

	def test_a_listed_import_in_its_own_file_is_clean(self):
		for rel, line in [
			("kb/store.py", "import os"),
			("kb/retrieve.py", "import unicodedata"),
			("assistant/guard.py", "from collections import Counter"),
			("assistant/guard.py", "from datetime import date, datetime, time, timedelta"),
			("assistant/codereader.py", "import fnmatch"),
			("assistant/tools/knowledge.py", "import json"),
		]:
			with self.subTest(rel=rel, line=line):
				self.assertClean(rel, f"{line}\n", line)

	def test_a_name_that_is_not_listed_is_a_hit_even_when_the_module_is_allowed(self):
		self.assertHit("assistant/guard.py", "from collections import OrderedDict\n", "import")
		self.assertHit("assistant/guard.py", "from datetime import tzinfo\n", "import")
		self.assertHit("kb/store.py", "from os import path\n", "import")

	def test_an_alias_of_a_non_frappe_module_is_a_hit_unless_that_exact_alias_is_listed(self):
		for rel, line in [
			("kb/store.py", "import os as o"),
			("kb/store.py", "import json as j"),
			("kb/store.py", "from os import sep as s"),
			("assistant/guard.py", "from collections import Counter as C"),
			("assistant/tools/live.py", "import re as regex"),
		]:
			with self.subTest(rel=rel, line=line):
				self.assertHit(rel, f"{line}\n", "alias", line)

	def test_an_alias_row_allows_only_that_alias(self):
		scanner = load_scanner()
		try:
			rows = [*scanner.IMPORT_ALLOWLIST, ("import", "os", "as o", ("kb/store.py",))]
			scanner.IMPORT_ALLOWLIST[:] = rows
			ok = scanner.scan_python("kb/store.py", "import os as o\n", set())
			other = scanner.scan_python("kb/store.py", "import os as p\n", set())
		finally:
			sys.modules.pop("guard_scan_imports_test", None)
		self.assertEqual(ok, [])
		self.assertTrue(other and other[0][1] == "alias", other)

	def test_a_bare_call_of_a_file_changing_name_is_a_hit_even_if_a_row_is_added(self):
		scanner = load_scanner()
		try:
			scanner.IMPORT_ALLOWLIST.append(("from", "os", "remove", ("assistant/tools/live.py",)))
			scanner.IMPORT_ALLOWLIST.append(("from", "shutil", "move", ("assistant/tools/live.py",)))
			hits = scanner.scan_python(
				"assistant/tools/live.py",
				"from os import remove\nfrom shutil import move\n\ndef f(p):\n    remove(p)\n    move(p, p)\n",
				set(),
			)
		finally:
			sys.modules.pop("guard_scan_imports_test", None)
		self.assertEqual({rule for _line, rule, _msg in hits}, {"file-access"}, hits)
		self.assertEqual(len(hits), 2)

	def test_relative_and_app_imports_are_unchanged(self):
		self.assertClean(
			"assistant/tools/live.py",
			"from lending_assistant.assistant import guard\n\ndef f():\n    return guard.MAX_ROWS\n".replace(
				"guard.MAX_ROWS", "guard.read_doc"
			),
		)

	def test_the_real_app_passes_and_the_rows_equal_the_imports_ast_finds(self):
		scanner = load_scanner()
		try:
			result = scanner.scan(SCRIPT.parent.parent, strict=True)
		finally:
			sys.modules.pop("guard_scan_imports_test", None)
		self.assertEqual(result.problems, [])
		self.assertEqual(result.unused_entries, [])
		package = SCRIPT.parent.parent / "lending_assistant"
		found = set()
		for path in package.rglob("*.py"):
			rel = path.relative_to(package).as_posix()
			if "tests" in rel.split("/"):
				continue
			for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
				if isinstance(node, ast.Import):
					for item in node.names:
						if not item.name.startswith(("frappe", "lending_assistant")):
							found.add(("import", item.name, None, rel))
				elif isinstance(node, ast.ImportFrom) and not node.level:
					if not (node.module or "").startswith(("frappe", "lending_assistant")):
						for item in node.names:
							found.add(("from", node.module, item.name, rel))
		rows = {
			(kind, module, name, entry_files[0])
			for kind, module, name, entry_files in scanner.IMPORT_ALLOWLIST
			if not module.startswith("frappe")
		}
		self.assertEqual(rows, found, "the table and the app's imports must match exactly")
