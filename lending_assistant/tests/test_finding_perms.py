"""G13 permission matrix for Assistant Finding, through the doctype permissions, `frappe.client` and the form save path."""

import json


import frappe
import frappe.desk.form.save

from lending_assistant.tests.base import FINDING, AssistantTestCase, make_finding


class TestFindingPerms(AssistantTestCase):
	def setUp(self):
		super().setUp()
		self.create_sysmgr()
		self.own = make_finding("dev", title="AST-M6 dev own")
		self.other = make_finding("senior", title="AST-M6 senior own")

	def new_doc_json(self):
		return json.dumps(
			{
				"doctype": FINDING,
				"title": "AST-M6 made by hand",
				"summary": "x",
				"status": "Draft",
				"br_ids": "BR-LMS-162",
				"doctypes": "",
				"question": "q",
				"lending_version": "16.5.1",
			}
		)

	def test_nobody_can_create_through_the_api(self):
		for who in ("dev", "senior", "limited", "noaccess", "ast-test-sysmgr@example.com"):
			with self.subTest(who=who):
				self.as_user(who)
				with self.assertRaises((frappe.PermissionError, frappe.ValidationError)):
					frappe.client.insert(self.new_doc_json())
				with self.assertRaises((frappe.PermissionError, frappe.ValidationError)):
					frappe.get_doc(json.loads(self.new_doc_json())).insert()

	def test_dev_reads_all_edits_and_deletes_only_own(self):
		self.as_user("dev")
		rows = frappe.get_list(FINDING, pluck="name")
		self.assertIn(self.own.name, rows)
		self.assertIn(self.other.name, rows)
		frappe.client.set_value(FINDING, self.own.name, "title", "AST-M6 edited")
		self.assertEqual(frappe.db.get_value(FINDING, self.own.name, "title"), "AST-M6 edited")
		with self.assertRaises(frappe.PermissionError):
			frappe.client.set_value(FINDING, self.other.name, "title", "AST-M6 hijack")
		with self.assertRaises(frappe.PermissionError):
			frappe.client.delete(FINDING, self.other.name)
		frappe.client.delete(FINDING, self.own.name)
		self.assertFalse(frappe.db.exists(FINDING, self.own.name))

	def test_dev_cannot_set_confirmed_not_even_on_their_own(self):
		self.as_user("dev")
		with self.assertRaises(frappe.PermissionError):
			frappe.client.set_value(FINDING, self.own.name, "status", "Confirmed")
		self.assertEqual(frappe.db.get_value(FINDING, self.own.name, "status"), "Draft")

	def test_senior_confirms_and_edits_and_deletes_any(self):
		self.as_user("senior")
		frappe.client.set_value(FINDING, self.own.name, "status", "Confirmed")
		row = frappe.db.get_value(FINDING, self.own.name, ["status", "confirmed_by"], as_dict=True)
		self.assertEqual((row.status, row.confirmed_by), ("Confirmed", "ast-senior@example.com"))
		frappe.client.set_value(FINDING, self.own.name, "title", "AST-M6 reviewed")
		self.assertEqual(frappe.db.get_value(FINDING, self.own.name, "status"), "Confirmed")
		frappe.client.delete(FINDING, self.own.name)
		self.assertFalse(frappe.db.exists(FINDING, self.own.name))

	def test_noaccess_is_refused_everywhere(self):
		self.as_user("noaccess")
		with self.assertRaises(frappe.PermissionError):
			frappe.get_list(FINDING)
		with self.assertRaises(frappe.PermissionError):
			frappe.get_doc(FINDING, self.own.name).check_permission("read")
		with self.assertRaises(frappe.PermissionError):
			frappe.client.set_value(FINDING, self.own.name, "title", "x")
		with self.assertRaises(frappe.PermissionError):
			frappe.client.delete(FINDING, self.own.name)

	def test_system_manager_reads_but_cannot_write(self):
		self.as_user("ast-test-sysmgr@example.com")
		self.assertTrue(frappe.has_permission(FINDING, "read", doc=self.own))
		self.assertFalse(frappe.has_permission(FINDING, "write", doc=self.own))
		self.assertFalse(frappe.has_permission(FINDING, "delete", doc=self.own))
		self.assertFalse(frappe.has_permission(FINDING, "create"))
		with self.assertRaises(frappe.PermissionError):
			frappe.client.set_value(FINDING, self.own.name, "title", "x")

	def test_the_form_save_path_enforces_the_same_rules(self):
		self.as_user("dev")
		doc = frappe.get_doc(FINDING, self.own.name)
		doc.status = "Confirmed"
		with self.assertRaises(frappe.PermissionError):
			frappe.desk.form.save.savedocs(frappe.as_json(doc.as_dict()), "Save")
