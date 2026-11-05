"""M6 scanner rules: findings.py is importable from api/findings.py only, tools/findings.py cannot write, one more
whitelisted method is a hit, and the real tree is clean."""

import shutil
import subprocess
import sys
from pathlib import Path

import frappe

from lending_assistant.tests.base import AssistantTestCase
from lending_assistant.tests.test_guard_scan import SCRIPT, run, tree

OTHERS = [
	"assistant/tools/live.py",
	"assistant/tools/findings.py",
	"assistant/tools/registry.py",
	"assistant/orchestrator.py",
	"assistant/audit.py",
	"assistant/prompts.py",
	"api/chat.py",
	"api/gate.py",
	"kb/store.py",
]
FORMS = [
	"from lending_assistant.assistant import findings",
	"from lending_assistant.assistant import findings as f",
	"from lending_assistant.assistant.findings import create_from_message",
	"import lending_assistant.assistant.findings",
	"import lending_assistant.assistant.findings as f",
	"def g():\n    from lending_assistant.assistant import findings\n    return findings",
	"if True:\n    from lending_assistant.assistant.findings import create_from_message",
]


class TestScanM6(AssistantTestCase):
	def scan(self, rel, source):
		root = tree({rel: source})
		self.addCleanup(shutil.rmtree, root, True)
		return run("--root", root)

	def test_findings_py_is_a_hit_when_imported_anywhere_but_api_findings(self):
		for rel in OTHERS:
			for form in FORMS:
				with self.subTest(rel=rel, form=form):
					result = self.scan(rel, form + "\n")
					self.assertEqual(result.returncode, 1, result.stdout)
					self.assertIn("[findings-import]", result.stdout)

	def test_a_relative_import_is_caught_too(self):
		result = self.scan("assistant/tools/live.py", "from .. import findings\n")
		self.assertEqual(result.returncode, 1, result.stdout)

	def test_a_marker_does_not_excuse_it(self):
		result = self.scan(
			"assistant/orchestrator.py",
			"from lending_assistant.assistant import findings  # AST-ALLOWED: needed\n",
		)
		self.assertEqual(result.returncode, 1, result.stdout)

	def test_the_tool_module_of_the_same_name_is_a_different_module(self):
		code = "from lending_assistant.assistant.tools import findings\n\n\ndef f():\n    return findings\n"
		result = self.scan("assistant/tools/registry.py", code)
		self.assertNotIn("[findings-import]", result.stdout)

	def test_api_findings_may_import_it(self):
		code = (
			"from lending_assistant.assistant import findings\n\n\ndef f():\n"
			"    return findings.create_from_message('a', None, None, '1')\n"
		)
		result = self.scan("api/findings.py", code)
		self.assertNotIn("[findings-import]", result.stdout)

	def test_a_write_in_tools_findings_is_a_hit(self):
		bodies = [
			"doc.insert()",
			"doc.save()",
			"doc.delete()",
			"frappe.get_doc('X').insert(ignore_permissions=True)",
			"frappe.get_all('X')",
			"frappe.db.sql('select 1')",
			"frappe.db.set_value('X', 'y', 'z', 1)",
			"frappe.get_doc('X', 'y')",
		]
		for body in bodies:
			for marker in ("", "  # AST-ALLOWED: because"):
				with self.subTest(body=body, marker=marker):
					code = f"import frappe\n\n\ndef f(doc):\n    {body}{marker}\n"
					result = self.scan("assistant/tools/findings.py", code)
					self.assertEqual(result.returncode, 1, result.stdout)

	def test_a_fourth_whitelisted_method_is_a_hit(self):
		extra = '\n\n@frappe.whitelist(methods=["POST"])\ndef extra():\n    return 1\n'
		for rel, name in (("api/chat.py", "ask"), ("api/findings.py", "save"), ("api/gate.py", "x")):
			with self.subTest(rel=rel):
				code = (
					f'import frappe\n\n\n@frappe.whitelist(methods=["POST"])\ndef {name}():\n    return 1\n'
					+ extra
				)
				result = self.scan(rel, code)
				self.assertEqual(result.returncode, 1, result.stdout)
				self.assertIn("[whitelist]", result.stdout)

	def test_the_real_tree_is_clean(self):
		result = subprocess.run(
			[sys.executable, str(SCRIPT), "--check-allowlist"], capture_output=True, text=True, timeout=120
		)
		self.assertEqual(result.returncode, 0, result.stdout)
