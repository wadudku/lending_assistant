"""M4a code tools: `search_code` and `read_code` through `registry.dispatch`, over the G12 sandbox in codereader.
They have no per-user data; test_tools_personas.py runs them for every persona."""

import os

import frappe

from lending_assistant.assistant import codereader
from lending_assistant.tests.base import ToolTestCase

READ = "lending/lending/hooks.py"


class TestSearchCode(ToolTestCase):
	def setUp(self):
		super().setUp()
		self.as_user("senior")

	def search(self, query, app=None, path_glob=None):
		return self.call("search_code", query=query, app=app, path_glob=path_glob)

	def test_it_finds_a_known_string_in_lending_with_at_most_30_file_line_matches(self):
		data = self.data(self.search("def get_due_details", app="lending"))
		self.assertTrue(data["matches"])
		self.assertLessEqual(len(data["matches"]), 30)
		self.assertRegex(data["matches"][0], r"^lending/.+\.py:\d+: ")
		self.assertEqual(data["source"], "code")

	def test_a_common_string_is_capped_at_30_matches(self):
		data = self.data(self.search("def ", app="lending"))
		self.assertEqual(len(data["matches"]), 30)
		self.assertTrue(data["truncated"])

	def test_path_glob_narrows_the_search(self):
		data = self.data(self.search("def ", app="lending", path_glob="*loan_repayment.py"))
		self.assertTrue(data["matches"])
		self.assertTrue(all("loan_repayment.py" in m for m in data["matches"]))

	def test_bad_app_glob_and_query_are_refused_with_one_reply(self):
		self.assertEqual(self.error(self.search("hooks", app="frappe_not_allowed")), codereader.REFUSED)
		self.assertEqual(self.error(self.search("hooks", app="../..")), codereader.REFUSED)
		for glob in ("../x", "/etc/*", "x" * 101):
			with self.subTest(glob=glob):
				self.assertTrue(self.search("hooks", path_glob=glob).is_error)
		self.assertTrue(self.search("   ").is_error)
		self.assertIn("too long", self.error(self.search("x" * 201)))

	def test_the_deny_list_hides_secrets_from_the_results(self):
		for query in ("db_password", "encryption_key"):
			with self.subTest(query=query):
				data = self.data(self.search(query))
				paths = [m.split(":")[0] for m in data["matches"]]
				self.assertFalse([p for p in paths if "site_config" in p or "/sites/" in p or "/.git/" in p or p.startswith("sites/")], paths)


class TestReadCode(ToolTestCase):
	def setUp(self):
		super().setUp()
		self.as_user("senior")

	def read(self, path=READ, start_line=None, end_line=None):
		return self.call("read_code", path=path, start_line=start_line, end_line=end_line)

	def test_it_reads_a_known_range(self):
		data = self.data(self.read(start_line=1, end_line=5))
		self.assertEqual(len(data["lines"]), 5)
		self.assertTrue(data["lines"][0].startswith("1: "))
		self.assertEqual(data["path"], READ)

	def test_more_than_200_lines_is_cut_with_a_marker(self):
		data = self.data(self.read(start_line=1, end_line=1000))
		self.assertLessEqual(len(data["lines"]), 200)  # fewer when the 8000-character cap comes first
		self.assertGreater(len(data["lines"]), 100)
		self.assertTrue(data["truncated"])
		self.assertLessEqual(len(self.data(self.read())["lines"]), 200)  # null end_line also gives at most 200

	def test_refusals_give_one_reply_that_does_not_say_whether_the_file_exists(self):
		bench = frappe.utils.get_bench_path()
		self.assertTrue(os.path.isfile(os.path.join(bench, "sites", "common_site_config.json")), "the fixture file exists")
		replies = set()
		for path in (
			"lending/../frappe/frappe/hooks.py",
			"../sites/lending_site/site_config.json",
			"sites/common_site_config.json",
			"lending/.git/config",
			"lending/lending/.env",
			"lending/lending/no_such_file.py",
			"lending/lending/__pycache__/x.pyc",
			"/etc/passwd",
			"lending/lending/hooks.py\x00.txt",
			"",
			"nonexistent_app/x.py",
		):
			with self.subTest(path=path):
				result = self.read(path)
				replies.add(self.error(result))
		self.assertEqual(replies, {codereader.REFUSED})

	def test_a_symlink_that_leaves_the_app_is_refused(self):
		root = os.path.join(frappe.utils.get_bench_path(), "apps", "lending_assistant")
		link = os.path.join(root, "ast_test_link.py")
		target = os.path.join(frappe.utils.get_bench_path(), "sites", "common_site_config.json")
		os.symlink(target, link)
		self.addCleanup(os.remove, link)
		self.assertEqual(self.error(self.read("lending_assistant/ast_test_link.py")), codereader.REFUSED)

	def test_line_numbers_are_checked(self):
		for start, end in ((0, None), (-1, None), (10, 5)):
			with self.subTest(start=start, end=end):
				self.assertTrue(self.read(start_line=start, end_line=end).is_error)
		self.assertTrue(self.call("read_code", path=READ, start_line="1", end_line=None).is_error)
		self.assertTrue(self.call("read_code", path=READ, start_line=True, end_line=None).is_error)

	def test_both_tools_label_their_output_code(self):
		self.assertEqual(self.read(start_line=1, end_line=2).source, "code")
		self.assertEqual(self.call("search_code", query="hooks", app=None, path_glob=None).source, "code")
