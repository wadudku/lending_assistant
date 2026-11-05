"""M4a guardrail carry-overs: R20 (`after_delete` is trapped), R21 (the `BaseException` note), #39 (owner and
modified_by are never readable). The tool tests are in test_registry.py, test_tools_*.py and test_tools_personas.py.

Administrator only creates fixtures (DECISIONS #41); the action inside the context runs as `ast-senior`.
"""

import uuid

import frappe

from lending_assistant.assistant import guard
from lending_assistant.tests.base import GuardTestCase

TRAP = "lending_assistant.assistant.guard.block_if_read_only"


class TestAfterDeleteTrap(GuardTestCase):
	def test_after_delete_is_in_the_live_hooks(self):
		self.assertIn(TRAP, frappe.get_hooks("doc_events")["*"]["after_delete"])

	def test_a_delete_that_skips_on_trash_is_stopped_at_after_delete_and_rolled_back(self):
		frappe.set_user("Administrator")  # fixture only
		tag = "AST-TEST-DEL-" + uuid.uuid4().hex[:8]
		cat = frappe.get_doc(
			{"doctype": "Loan Category", "loan_category_code": tag, "loan_category_name": tag}
		).insert()
		self.as_user("senior")
		with guard.read_only_tool_context("AST-TEST-after-delete") as ctx:
			with self.assertRaises(frappe.PermissionError):
				# ignore_on_trash skips on_trash and on_change, so after_delete is the first trapped event
				frappe.delete_doc("Loan Category", cat.name, ignore_on_trash=True, force=True)
		self.assertGreaterEqual(ctx.trap_hits, 1)
		self.assertTrue(ctx.violation)
		self.assertTrue(frappe.db.exists("Loan Category", cat.name))  # the DELETE was rolled back


class TestR21Note(GuardTestCase):
	def test_the_docstring_says_where_a_baseexception_really_skips_steps(self):
		doc = guard.read_only_tool_context.__wrapped__.__doc__
		self.assertIn("step 1 runs inside a", " ".join(doc.lower().split()))
		self.assertIn("skips nothing", " ".join(doc.split()))
		self.assertIn("step 2 or step 3", " ".join(doc.split()))
		self.assertNotIn("raised by steps 1-3", " ".join(doc.split()))
