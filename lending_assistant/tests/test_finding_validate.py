"""Controller rules of Assistant Finding: immutable provenance, status, references, and the author delete."""

import frappe

from lending_assistant.tests.base import FINDING, AssistantTestCase, make_finding


class TestFindingValidate(AssistantTestCase):
	def test_each_provenance_field_is_immutable(self):
		doc = make_finding("dev", cards_used='[{"id": "x", "version": 1}]')
		changes = {
			"question": "other?",
			"sources": '["Web"]',
			"cards_used": "[]",
			"cards_basis": "all",
			"lending_version": "1.0.0",
			"author_name": "Someone Else",
			"source_message": "abc",
		}
		self.as_user("dev")
		for field, value in changes.items():
			with self.subTest(field=field):
				doc = frappe.get_doc(FINDING, doc.name)
				doc.set(field, value)
				with self.assertRaises(frappe.ValidationError):
					doc.save()

	def test_whitespace_in_json_is_not_a_change(self):
		doc = make_finding("dev", sources='["Analysis"]')
		self.as_user("dev")
		doc = frappe.get_doc(FINDING, doc.name)
		doc.sources = '[ "Analysis" ]'
		doc.save()

	def test_owner_cannot_change(self):
		doc = make_finding("dev")
		self.as_user("dev")
		doc = frappe.get_doc(FINDING, doc.name)
		doc.owner = "ast-senior@example.com"
		with self.assertRaises((frappe.ValidationError, frappe.PermissionError)):
			doc.save()

	def confirmed(self):
		doc = make_finding("dev")
		self.as_user("senior")
		doc = frappe.get_doc(FINDING, doc.name)
		doc.status = "Confirmed"
		doc.save()
		return doc.name

	def test_author_edit_of_confirmed_goes_back_to_draft(self):
		name = self.confirmed()
		self.as_user("dev")
		doc = frappe.get_doc(FINDING, name)
		doc.summary = "AST-M6 changed by the author"
		doc.save()
		row = frappe.db.get_value(FINDING, name, ["status", "confirmed_by", "confirmed_on"], as_dict=True)
		self.assertEqual(row.status, "Draft")
		self.assertIsNone(row.confirmed_by)
		self.assertIsNone(row.confirmed_on)
		self.assertTrue(
			any("back to Draft" in m for m in frappe.get_message_log()[-1:][0].values() if isinstance(m, str))
		)

	def test_author_save_without_a_content_change_keeps_confirmed(self):
		name = self.confirmed()
		self.as_user("dev")
		frappe.get_doc(FINDING, name).save()
		self.assertEqual(frappe.db.get_value(FINDING, name, "status"), "Confirmed")

	def test_author_may_demote_but_not_set_confirmed(self):
		name = self.confirmed()
		self.as_user("dev")
		doc = frappe.get_doc(FINDING, name)
		doc.status = "Draft"
		doc.save()
		doc.status = "Confirmed"
		with self.assertRaises(frappe.PermissionError):
			doc.save()

	def test_reviewer_edit_keeps_confirmed_and_the_original_confirmer(self):
		name = self.confirmed()
		before = frappe.db.get_value(FINDING, name, ["confirmed_by", "confirmed_on"], as_dict=True)
		self.as_user("senior")
		doc = frappe.get_doc(FINDING, name)
		doc.title = "AST-M6 reviewed title"
		doc.confirmed_by = "Administrator"  # a client-sent value is ignored
		doc.save()
		row = frappe.db.get_value(FINDING, name, ["status", "confirmed_by", "confirmed_on"], as_dict=True)
		self.assertEqual(row.status, "Confirmed")
		self.assertEqual(row.confirmed_by, before.confirmed_by)

	def test_unknown_references_are_refused_with_their_names(self):
		doc = make_finding("dev")
		self.as_user("dev")
		doc = frappe.get_doc(FINDING, doc.name)
		doc.br_ids = "BR-LMS-162\nBR-LMS-9999"
		with self.assertRaises(frappe.ValidationError) as ctx:
			doc.save()
		self.assertIn("BR-LMS-9999", str(ctx.exception))
		doc = frappe.get_doc(FINDING, doc.name)
		doc.br_ids = "BR-LMS-170c"
		doc.doctypes = "Loan\nNot A Doctype"
		with self.assertRaises(frappe.ValidationError) as ctx:
			doc.save()
		self.assertIn("Not A Doctype", str(ctx.exception))
		doc = frappe.get_doc(FINDING, doc.name)
		doc.br_ids = "BR-LMS-170c\nbr-lms-162"
		doc.doctypes = "Loan"
		doc.save()
		self.assertEqual(doc.br_ids, "BR-LMS-170c\nBR-LMS-162")

	def test_lengths(self):
		with self.assertRaises(frappe.ValidationError):
			make_finding("dev", title="x" * 141)
		with self.assertRaises(frappe.ValidationError):
			make_finding("dev", summary="x" * 4001)

	def test_onload_carries_the_stale_reasons(self):
		doc = make_finding(
			"dev", cards_used='[{"id": "bridge.BR-XXX-001", "version": 1}]', lending_version="1.0.0"
		)
		doc = frappe.get_doc(FINDING, doc.name)
		doc.run_method("onload")
		reasons = doc.get_onload("stale_reasons")
		self.assertEqual(len(reasons), 2)

	def test_an_author_can_delete_their_finding_even_when_a_message_names_it(self):
		doc = make_finding("dev", source_message="some-message")
		self.as_user("dev")
		frappe.delete_doc(FINDING, doc.name)
		self.assertFalse(frappe.db.exists(FINDING, doc.name))
