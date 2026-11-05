"""M3b scanner entries: file access and get_meta are allowed only in the named kb files and functions (DECISIONS #138 Q1).

Each case is written into its own tree and judged by scripts/guard_scan.py on its own.
"""

import shutil

from lending_assistant.tests.base import AssistantTestCase
from lending_assistant.tests.test_guard_scan import run, tree

OPEN = "def {fn}(path):\n    with open(path, 'rb') as handle:  # AST-ALLOWED: reads an ingested knowledge file\n        return handle.read()\n"
OPEN_UNMARKED = "def {fn}(path):\n    with open(path, 'rb') as handle:\n        return handle.read()\n"
META = "import frappe\n\ndef {fn}(doctype):\n    return frappe.get_meta(doctype)  # AST-ALLOWED: read-only drift check\n"

# (path, function) where a marked open() is accepted
OPEN_OK = [
	("kb/store.py", "_read_text"),
	("kb/ingest.py", "_read_bytes"),
	("kb/ingest.py", "_write_bytes"),
	("kb/ingest.py", "_list_dir"),
	("kb/ingest.py", "_make_dirs"),
	("kb/ingest.py", "_remove_file"),
	("kb/validate.py", "_read_text"),
]
# marked open(): refused, either because the file has no allowance or because the function is not the scoped one
OPEN_REFUSED = [
	("kb/lookup.py", "_read_text"),
	("kb/search.py", "_read_text"),
	("kb/retrieve.py", "_read_text"),
	("assistant/tools/knowledge.py", "_read_text"),
	("assistant/tools/__init__.py", "_read_text"),
	("kb/store.py", "load"),
	("kb/store.py", "get_card"),
	("kb/ingest.py", "run"),
	("kb/validate.py", "run"),
	("assistant/tools/knowledge.py", "get_card"),
]


class TestKbScanner(AssistantTestCase):
	def make_tree(self, files):
		root = tree(files)
		self.addCleanup(shutil.rmtree, root, True)
		return root

	def test_a_marked_open_is_accepted_only_in_the_scoped_helpers(self):
		for path, fn in OPEN_OK:
			with self.subTest(path=path, fn=fn):
				result = run("--root", self.make_tree({path: OPEN.format(fn=fn)}))
				self.assertEqual(result.returncode, 0, result.stdout)

	def test_open_elsewhere_is_still_a_hit(self):
		for path, fn in OPEN_REFUSED:
			with self.subTest(path=path, fn=fn):
				result = run("--root", self.make_tree({path: OPEN.format(fn=fn)}))
				self.assertEqual(result.returncode, 1, result.stdout)
				self.assertIn("[file-access]", result.stdout)

	def test_an_unmarked_open_is_a_hit_even_in_the_scoped_helper(self):
		for path, fn in OPEN_OK:
			with self.subTest(path=path, fn=fn):
				result = run("--root", self.make_tree({path: OPEN_UNMARKED.format(fn=fn)}))
				self.assertEqual(result.returncode, 1, result.stdout)
				self.assertIn("[file-access]", result.stdout)

	def test_other_file_calls_in_lookup_and_knowledge_are_hits(self):
		for path in ("kb/lookup.py", "assistant/tools/knowledge.py"):
			for call in ("os.listdir(p)", "os.walk(p)", "Path(p).read_text()", "Path(p).write_bytes(b'')"):
				with self.subTest(path=path, call=call):
					code = f"import os\nfrom pathlib import Path\n\ndef f(p):\n    return {call}\n"
					result = run("--root", self.make_tree({path: code}))
					self.assertEqual(result.returncode, 1, result.stdout)
					self.assertIn("[file-access]", result.stdout)

	def test_file_changing_calls_are_hits_outside_the_scoped_helpers(self):
		calls = [
			"os.remove(p)",
			"os.unlink(p)",
			"os.rename(p, p)",
			"os.replace(p, p)",
			"os.makedirs(p)",
			"os.mkdir(p)",
			"os.rmdir(p)",
			"os.removedirs(p)",
			"shutil.copy(p, p)",
			"shutil.copy2(p, p)",
			"shutil.copytree(p, p)",
			"shutil.move(p, p)",
			"os.chmod(p, 0)",
			"os.symlink(p, p)",
			"os.link(p, p)",
			"os.truncate(p, 0)",
			"Path(p).unlink()",
			"Path(p).rename(p)",
			"Path(p).replace(p)",
			"Path(p).mkdir()",
			"Path(p).chmod(0)",
			"Path(p).symlink_to(p) or Path(p).unlink()",
			"pathlib.Path(p).replace(p)",
			"p.replace(q)",
		]
		for path in ("kb/lookup.py", "assistant/tools/knowledge.py", "kb/ingest.py"):
			for call in calls:
				with self.subTest(path=path, call=call):
					code = (
						"import os\nimport shutil\nimport pathlib\nfrom pathlib import Path\n\ndef f(p, q):\n    return "
						+ call
						+ "\n"
					)
					result = run("--root", self.make_tree({path: code}))
					self.assertEqual(result.returncode, 1, result.stdout)
					self.assertIn("[file-access]", result.stdout)

	def test_a_marked_makedirs_and_remove_are_accepted_only_in_their_helpers(self):
		for fn, call in (
			("_make_dirs", "os.makedirs(p)"),
			("_remove_file", "os.remove(p)"),
			("_write_bytes", "os.replace(p, p)"),
		):
			code = f"import os\n\ndef {fn}(p):\n    {call}  # AST-ALLOWED: checked inside the folder\n"
			self.assertEqual(run("--root", self.make_tree({"kb/ingest.py": code})).returncode, 0, fn)
			other = code.replace(fn, "_other")
			result = run("--root", self.make_tree({"kb/ingest.py": other}))
			self.assertEqual(result.returncode, 1, fn)
			result = run("--root", self.make_tree({"kb/lookup.py": code}))
			self.assertEqual(result.returncode, 1, fn)

	def test_str_dict_and_list_methods_with_the_same_names_are_not_file_calls(self):
		code = "def f(text, items, table):\n    items.remove(1)\n    table.copy()\n    return text.replace('a', 'b')\n"
		for path in ("kb/lookup.py", "kb/ingest.py"):
			result = run("--root", self.make_tree({path: code}))
			self.assertEqual(result.returncode, 0, result.stdout)

	def test_get_meta_is_accepted_only_in_validate_meta_of(self):
		result = run("--root", self.make_tree({"kb/validate.py": META.format(fn="_meta_of")}))
		self.assertEqual(result.returncode, 0, result.stdout)

	def test_get_meta_elsewhere_is_a_hit(self):
		cases = [
			("kb/store.py", "load"),
			("kb/store.py", "_meta_of"),
			("kb/ingest.py", "_meta_of"),
			("kb/lookup.py", "_meta_of"),
			("kb/search.py", "_meta_of"),
			("kb/retrieve.py", "_meta_of"),
			("assistant/tools/knowledge.py", "_meta_of"),
			("kb/validate.py", "run"),
		]
		for path, fn in cases:
			with self.subTest(path=path, fn=fn):
				result = run("--root", self.make_tree({path: META.format(fn=fn)}))
				self.assertEqual(result.returncode, 1, result.stdout)
				self.assertIn("[not-allowed]", result.stdout)

	def test_get_meta_without_a_marker_is_a_hit_in_validate(self):
		code = "import frappe\n\ndef _meta_of(doctype):\n    return frappe.get_meta(doctype)\n"
		result = run("--root", self.make_tree({"kb/validate.py": code}))
		self.assertEqual(result.returncode, 1, result.stdout)

	def test_frappe_db_reads_stay_banned_in_every_kb_file(self):
		for path in (
			"kb/store.py",
			"kb/ingest.py",
			"kb/validate.py",
			"kb/lookup.py",
			"kb/search.py",
			"kb/retrieve.py",
			"assistant/tools/knowledge.py",
		):
			with self.subTest(path=path):
				code = "import frappe\n\ndef _read_text():\n    return frappe.db.exists('DocType', 'Loan')  # AST-ALLOWED: because\n"
				result = run("--root", self.make_tree({path: code}))
				self.assertEqual(result.returncode, 1, result.stdout)

	def test_the_real_app_passes_with_the_dead_entry_check(self):
		result = run("--check-allowlist")
		self.assertEqual(result.returncode, 0, result.stdout)
		self.assertIn("clean", result.stdout)
