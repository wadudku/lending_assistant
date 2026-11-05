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
		self.assertIn("skips only step 5 (the violation log) and the final raise", " ".join(doc.split()))
		self.assertIn("step 2 or step 3", " ".join(doc.split()))
		self.assertNotIn("raised by steps 1-3", " ".join(doc.split()))


class TestOwnerAndModifiedByAreNeverReadable(GuardTestCase):
	"""#39: who created or last changed a record is never shown, for any doctype, parent or child."""

	def allowlisted(self):
		return [row.allowed_doctype for row in frappe.get_doc("Assistant Settings").doctype_allowlist]

	def test_readable_fields_drops_both_for_every_allowlisted_doctype_and_its_children(self):
		doctypes = self.allowlisted()
		self.assertGreater(len(doctypes), 5)
		checked_children = 0
		for who in ("senior", "dev", "limited"):
			self.as_user(who)
			for doctype in doctypes:
				with self.subTest(who=who, doctype=doctype):
					fields = guard.readable_fields(doctype)
					self.assertNotIn("owner", fields)
					self.assertNotIn("modified_by", fields)
					for df in frappe.get_meta(doctype).get_table_fields():
						child = guard.readable_fields(df.options, parenttype=doctype)
						checked_children += 1
						self.assertNotIn("owner", child)
						self.assertNotIn("modified_by", child)
		self.assertGreater(checked_children, 5)

	def test_a_record_and_its_child_rows_carry_neither(self):
		visible, _hidden = self.loan_names()
		for who in ("senior", "dev", "limited"):
			self.as_user(who)
			with self.subTest(who=who):
				data = guard.unwrap(guard.read_doc("Loan", visible))
				self.assertNotIn("owner", data["data"])
				self.assertNotIn("modified_by", data["data"])
				self.assertIn("loan_product", data["data"])
				for rows in data["children"].values():
					for row in rows:
						self.assertNotIn("owner", row)
						self.assertNotIn("modified_by", row)

	def test_asking_for_them_as_a_field_filter_or_order_is_refused(self):
		self.as_user("senior")
		for column in ("owner", "modified_by"):
			with self.subTest(column=column):
				with self.assertRaises(frappe.ValidationError):
					guard.list_records("Loan", fields=["name", column])
				with self.assertRaises(frappe.ValidationError):
					guard.list_records("Loan", filters={column: "Administrator"})
				with self.assertRaises(frappe.ValidationError):
					guard.list_records("Loan", order_by=f"{column} asc")
