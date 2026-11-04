"""R11 / G12: the code reader sandbox. Attacks run against a temp root; the real apps are only read."""

import os
import tempfile
from pathlib import Path
from unittest import mock

import frappe

from lending_assistant.assistant import codereader, guard
from lending_assistant.tests.base import GuardTestCase


def unwrap(envelope):
	return guard.unwrap(envelope)


class TestRealApps(GuardTestCase):
	def test_valid_read(self):
		result = codereader.read("lending/lending/hooks.py", 1, 20)
		self.assertTrue(result.startswith('<data source="code">'))
		parsed = unwrap(result)
		self.assertEqual(parsed["source"], "code")
		self.assertEqual(parsed["path"], "lending/lending/hooks.py")
		self.assertEqual(len(parsed["lines"]), 20)
		self.assertEqual(parsed["lines"][0].split(":")[0], "1")
		self.assertEqual((parsed["start_line"], parsed["end_line"]), (1, 20))
		self.assertFalse(parsed["truncated"])

	def test_read_is_capped_at_200_lines(self):
		parsed = unwrap(codereader.read("frappe/frappe/__init__.py", 1, 500))
		self.assertLessEqual(len(parsed["lines"]), 200)
		self.assertTrue(parsed["truncated"])
		self.assertLessEqual(parsed["end_line"] - parsed["start_line"] + 1, 200)
		self.assertLessEqual(len(codereader.read("frappe/frappe/__init__.py", 1, 500)), guard.MAX_CHARS)
		# no end_line also means at most 200
		self.assertLessEqual(len(unwrap(codereader.read("frappe/frappe/__init__.py"))["lines"]), 200)

	def test_search_is_capped_at_30(self):
		parsed = unwrap(codereader.search("process_loan_interest_accrual"))
		self.assertLessEqual(len(parsed["matches"]), 30)
		self.assertTrue(parsed["matches"])
		self.assertRegex(parsed["matches"][0], r"^\w+/.+:\d+: ")
		many = unwrap(codereader.search("import", app="frappe"))
		self.assertEqual(len(many["matches"]), 30)
		self.assertTrue(many["truncated"])
		self.assertEqual(many["count_returned"], 30)

	def test_search_scopes(self):
		only = unwrap(codereader.search("process_loan_interest_accrual", app="lending", path_glob="*/loan_repayment/*.py"))
		for match in only["matches"]:
			self.assertTrue(match.startswith("lending/"))
			self.assertIn("loan_repayment", match)
		with self.assertRaises(codereader.CodeReaderRefused):
			codereader.search("x", app="lending_assistant")
		with self.assertRaises(codereader.CodeReaderRefused):
			codereader.search("x", app="..")

	def test_bad_search_queries(self):
		for query in ("", "   ", "x" * 201, None, 5, "a\0b"):
			with self.assertRaises(frappe.ValidationError, msg=repr(query)):
				codereader.search(query)
		for glob in ("../*", "/etc/*", "x" * 101, 5):
			with self.assertRaises(frappe.ValidationError, msg=repr(glob)):
				codereader.search("x", path_glob=glob)

	def test_switch_off_refuses_everything(self):
		self.configure(code_reader=0)
		with self.assertRaises(codereader.CodeReaderRefused) as one:
			codereader.read("lending/lending/hooks.py", 1, 5)
		with self.assertRaises(codereader.CodeReaderRefused) as two:
			codereader.search("hooks")
		self.assertEqual(str(one.exception), codereader.OFF)
		self.assertEqual(str(two.exception), codereader.OFF)

	def test_real_attacks_on_the_real_bench(self):
		for path in (
			"../../sites/lending_site/site_config.json",
			"lending/../../sites/lending_site/site_config.json",
			"sites/lending_site/site_config.json",
			"sites/common_site_config.json",
			"/etc/passwd",
			"/home/wadud/.bashrc",
			"~/.bashrc",
			"frappe/.git/config",
			"frappe/.gitignore",
			"lending/.env",
			"lending/lending/__pycache__/hooks.cpython-314.pyc",
			"lending_assistant/lending_assistant/hooks.py",  # an app that is not allowlisted
			"lending/lending/hooks.py\0.txt",
			"lending/lending/hooks.py\\..\\x",
			"lending//..//..//x.py",
			"lending",
			"",
			None,
			5,
			["lending/lending/hooks.py"],
		):
			with self.assertRaises(codereader.CodeReaderRefused, msg=repr(path)) as ctx:
				codereader.read(path, 1, 5)
			self.assertEqual(str(ctx.exception), codereader.REFUSED)


class TestSandboxInTempRoot(GuardTestCase):
	"""Symlinks, size, binary files, hidden files: made in a temp 'apps' folder registered as the root here only."""

	def setUp(self):
		super().setUp()
		self.tmp = tempfile.TemporaryDirectory()
		self.addCleanup(self.tmp.cleanup)
		base = Path(self.tmp.name).resolve()
		self.apps, self.outside = base / "apps", base / "outside"
		app = self.apps / "fakeapp"
		for folder in (app / "pkg", app / ".git", app / "node_modules", app / "__pycache__", app / "sites", self.outside, self.apps / "other"):
			folder.mkdir(parents=True)
		(app / "ok.py").write_text("line one\nneedle x.*y\nxzzy needle2\n")
		(app / "pkg" / "mod.py").write_text("needle in pkg\n")
		(app / "plain.txt").write_text("needle in txt\n")
		(app / "big.py").write_text("needle\n" * 200000)  # about 1.4 MB
		(app / "bin.py").write_bytes(b"needle\0binary")
		(app / ".env").write_text("SECRET=needle")
		(app / ".hidden.py").write_text("needle hidden")
		(app / ".git" / "config").write_text("needle gitconfig")
		(app / ".git" / "hooks.py").write_text("needle GITSECRET")
		(app / "node_modules" / "x.js").write_text("needle node")
		(app / "__pycache__" / "x.py").write_text("needle cache")
		(app / "sites" / "site_config.json").write_text('{"db_password": "needle"}')
		(app / "tool.exe").write_text("needle exe")
		(self.apps / "other" / "ok.py").write_text("needle other app")
		(self.outside / "secret.py").write_text("SECRET_OUTSIDE needle\n")
		os.symlink(self.outside / "secret.py", app / "link_out.py")
		os.symlink(self.outside, app / "link_dir")
		os.symlink(app / ".git" / "hooks.py", app / "link_git.py")
		os.symlink(app / "ok.py", app / "link_in.py")  # a symlink that stays inside is fine
		patches = [
			mock.patch.object(codereader, "_apps_dir", return_value=str(self.apps)),
			mock.patch.object(codereader, "_allowed_apps", return_value=["fakeapp"]),
		]
		for patch in patches:
			patch.start()
			self.addCleanup(patch.stop)

	def assertRefusedWithoutContent(self, path):
		with self.assertRaises(codereader.CodeReaderRefused, msg=path) as ctx:
			codereader.read(path, 1, 50)
		self.assertEqual(str(ctx.exception), codereader.REFUSED)
		for secret in ("SECRET", "needle", "GITSECRET"):
			self.assertNotIn(secret, str(ctx.exception))

	def test_valid_file_works(self):
		parsed = unwrap(codereader.read("fakeapp/ok.py", 1, 10))
		self.assertEqual(parsed["lines"], ["1: line one", "2: needle x.*y", "3: xzzy needle2"])
		self.assertEqual(unwrap(codereader.read("fakeapp/plain.txt"))["lines"], ["1: needle in txt"])

	def test_attacks_are_refused_with_no_content(self):
		for path in (
			"fakeapp/link_out.py",  # symlink to a file outside the root
			"fakeapp/link_dir/secret.py",  # symlink to a folder outside the root
			"fakeapp/link_git.py",  # symlink inside the root that points into .git
			"fakeapp/.env",
			"fakeapp/.hidden.py",
			"fakeapp/.git/config",
			"fakeapp/.git/hooks.py",
			"fakeapp/node_modules/x.js",
			"fakeapp/__pycache__/x.py",
			"fakeapp/sites/site_config.json",
			"fakeapp/big.py",  # over 1 MB
			"fakeapp/bin.py",  # NUL byte
			"fakeapp/tool.exe",  # extension not on the list
			"fakeapp/pkg",  # a folder
			"fakeapp/pkg/../ok.py",
			"fakeapp/missing.py",
			"other/ok.py",  # app not allowlisted
			"fakeapp",
			"/" + str(self.outside / "secret.py"),
			str(self.outside / "secret.py"),
		):
			self.assertRefusedWithoutContent(path)

	def test_a_missing_file_and_a_forbidden_file_look_the_same(self):
		messages = set()
		for path in ("fakeapp/missing.py", "fakeapp/.env", "fakeapp/link_out.py", "fakeapp/big.py", "fakeapp/bin.py"):
			with self.assertRaises(codereader.CodeReaderRefused) as ctx:
				codereader.read(path)
			messages.add(str(ctx.exception))
		self.assertEqual(messages, {codereader.REFUSED})

	def test_internal_symlink_is_allowed_and_shows_the_real_path(self):
		self.assertEqual(unwrap(codereader.read("fakeapp/link_in.py"))["path"], "fakeapp/ok.py")

	def test_search_never_returns_refused_content(self):
		parsed = unwrap(codereader.search("needle"))
		joined = "\n".join(parsed["matches"])
		for forbidden in ("SECRET", "GITSECRET", "gitconfig", "hidden", "node", "cache", "binary", "exe", "other app", "db_password"):
			self.assertNotIn(forbidden, joined)
		found = {m.split(":")[0] for m in parsed["matches"]}
		self.assertEqual(found, {"fakeapp/ok.py", "fakeapp/pkg/mod.py", "fakeapp/plain.txt"})

	def test_search_is_literal(self):
		matches = unwrap(codereader.search("x.*y"))["matches"]
		self.assertEqual(matches, ["fakeapp/ok.py:2: needle x.*y"])
		self.assertEqual(unwrap(codereader.search("^line"))["matches"], [])
