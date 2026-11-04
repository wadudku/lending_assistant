"""G5 groundwork: access.check_my_access and access.roles_that_can."""

import frappe

from lending_assistant.assistant import access, guard
from lending_assistant.tests.base import GuardTestCase


class TestAccess(GuardTestCase):
	def test_submit_repayment_limited_vs_senior(self):
		self.as_user("limited")
		limited = access.check_my_access("Loan Repayment", ["submit", "read", "create"])
		self.assertFalse(limited["access"]["submit"])
		self.assertFalse(limited["access"]["create"])
		self.assertTrue(limited["access"]["read"])
		self.assertEqual(limited["source"], "live_site")
		self.as_user("senior")
		self.assertTrue(access.check_my_access("Loan Repayment", ["submit"])["access"]["submit"])
		self.assertTrue(access.check_my_access("Loan Repayment", "cancel")["access"]["cancel"])

	def test_roles_that_can_names_the_real_roles(self):
		result = access.roles_that_can("Loan Repayment", "submit")
		self.assertIn("Loan Manager", result["roles"])
		self.assertNotIn("Loan Reporter", result["roles"])
		self.assertIn("Loan Reporter", access.roles_that_can("Loan Repayment", "read")["roles"])
		self.assertEqual(result, access.roles_that_can("Loan Repayment", "submit"))

	def test_roles_that_can_does_no_database_query(self):
		access.roles_that_can("Loan Repayment", "write")  # warm the meta cache and the cached Settings
		calls = []
		original = frappe.db.sql

		def counting(*args, **kwargs):
			calls.append(args[:1])
			return original(*args, **kwargs)

		frappe.db.sql = counting
		try:
			access.roles_that_can("Loan Repayment", "write")
		finally:
			frappe.db.sql = original
		self.assertEqual(calls, [])

	def test_with_docname_g4_applies(self):
		visible, hidden = self.loan_names()
		self.as_user("limited")
		result = access.check_my_access("Loan", ["read", "write", "submit"], docname=visible)
		self.assertEqual(result["access"], {"read": True, "write": False, "submit": False})
		errors = []
		for name in (hidden, "AST-DOES-NOT-EXIST"):
			with self.assertRaises(guard.RecordNotAvailable) as ctx:
				access.check_my_access("Loan", ["read"], docname=name)
			errors.append(str(ctx.exception))
		self.assertEqual(errors[0], errors[1])
		self.as_user("senior")
		self.assertTrue(access.check_my_access("Loan", ["read", "submit"], docname=hidden)["access"]["read"])

	def test_bad_arguments(self):
		for actions in ([], ["fly"], ["read", "drop"], None, 5, [None]):
			with self.assertRaises(frappe.ValidationError, msg=repr(actions)):
				access.check_my_access("Loan", actions)
		with self.assertRaises(frappe.ValidationError):
			access.roles_that_can("Loan", "fly")
