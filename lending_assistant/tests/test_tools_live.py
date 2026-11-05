"""M4a live-site tools: argument handling and the details that are not about a persona (those are in
test_tools_personas.py). All calls go through `registry.dispatch`."""

import frappe

from lending_assistant.assistant import guard
from lending_assistant.tests.base import ToolTestCase

FILTER = {"field": "loan_product", "operator": "=", "value": "PL-EMI", "values": None}


def find(testcase, **overrides):
	args = {"doctype": "Loan", "filters": [], "fields": ["name", "loan_product"], "order_by": None, "limit": None}
	args.update(overrides)
	return testcase.call("find_records", **args)


class TestGetScreenHelp(ToolTestCase):
	def setUp(self):
		super().setUp()
		self.as_user("senior")

	def test_a_large_doctype_is_cut_with_a_marker_and_a_count_and_stays_under_the_cap(self):
		result = self.call("get_screen_help", doctype="Loan", search=None)
		data = self.data(result)
		self.assertLessEqual(len(result.content), guard.MAX_CHARS)
		self.assertTrue(data["truncated"])
		self.assertGreater(data["fields_omitted"], 0)
		self.assertEqual(data["fields_omitted"], data["fields_total"] - len(data["fields"]))
		self.assertIn("search", data["note"])

	def test_search_reaches_the_fields_that_the_cut_left_out_and_is_not_truncated(self):
		full = self.data(self.call("get_screen_help", doctype="Loan", search=None))
		shown = {f["fieldname"] for f in full["fields"]}
		everything = self.data(self.call("get_screen_help", doctype="Loan", search="a"))  # nearly every field matches "a"
		self.assertGreater(everything["fields_total"], len(shown))
		hidden_name = "penalty_income_account"  # one of the last fields
		self.assertNotIn(hidden_name, shown)
		found = self.data(self.call("get_screen_help", doctype="Loan", search="PENALTY INCOME"))  # case-insensitive, label
		self.assertIn(hidden_name, {f["fieldname"] for f in found["fields"]})
		self.assertFalse(found["truncated"])
		self.assertEqual(found["fields_omitted"], 0)
		self.assertNotIn("note", found)
		by_name = self.data(self.call("get_screen_help", doctype="Loan", search="repayment_periods"))
		self.assertEqual([f["fieldname"] for f in by_name["fields"]], ["repayment_periods"])
		self.assertEqual(self.data(self.call("get_screen_help", doctype="Loan", search="zzzz-no-field"))["fields"], [])

	def test_the_fields_carry_label_type_options_and_description_and_the_doctype_has_a_controller_path(self):
		data = self.data(self.call("get_screen_help", doctype="Loan Repayment", search="posting"))
		field = data["fields"][0]
		self.assertEqual(field["fieldname"], "posting_date")
		self.assertEqual(field["fieldtype"], "Datetime")
		self.assertEqual(data["module"], "Loan Management")
		self.assertEqual(data["controller_path"], "lending/lending/loan_management/doctype/loan_repayment/loan_repayment.py")

	def test_the_controller_path_is_null_when_the_code_reader_is_off(self):
		self.configure(code_reader=0)
		self.assertIsNone(self.data(self.call("get_screen_help", doctype="Loan", search="posting"))["controller_path"])

	def test_linked_doctypes_say_whether_they_are_on_the_allowlist(self):
		data = self.data(self.call("get_screen_help", doctype="Loan", search="a"))
		links = {row["doctype"]: row for row in data["linked_doctypes"]}
		self.assertTrue(links["Loan Product"]["on_allowlist"])
		self.assertFalse(links["Company"]["on_allowlist"])

	def test_layout_and_hidden_fields_are_skipped(self):
		types = {f["fieldtype"] for f in self.data(self.call("get_screen_help", doctype="Loan Repayment", search=None))["fields"]}
		self.assertFalse(types & {"Section Break", "Column Break", "Tab Break", "HTML", "Button"})

	def test_a_doctype_that_is_not_on_the_allowlist_is_refused(self):
		for doctype in ("User", "DocType", "Error Log", "", "loan"):
			with self.subTest(doctype=doctype):
				self.assertEqual(self.error(self.call("get_screen_help", doctype=doctype, search=None)), guard.NOT_ALLOWED_DOCTYPE)

	def test_a_long_search_is_refused(self):
		self.assertIn("too long", self.error(self.call("get_screen_help", doctype="Loan", search="x" * 101)))


class TestCheckMyAccess(ToolTestCase):
	def setUp(self):
		super().setUp()
		self.as_user("senior")

	def test_actions_must_be_one_to_six_different_ones(self):
		self.assertIn("1 to 6", self.error(self.call("check_my_access", doctype="Loan", actions=[], docname=None)))
		self.assertIn("1 to 6", self.error(self.call("check_my_access", doctype="Loan", actions=["read", "read"], docname=None)))

	def test_a_doctype_off_the_allowlist_is_refused(self):
		self.assertEqual(self.error(self.call("check_my_access", doctype="User", actions=["read"], docname=None)), guard.NOT_ALLOWED_DOCTYPE)

	def test_roles_come_from_docperm_and_custom_docperm(self):
		frappe.set_user("Administrator")
		self.addCleanup(frappe.clear_cache, doctype="Loan Category")
		before = self.data_as("senior", "Loan Category")
		self.assertTrue(before["actions"]["read"]["roles_that_can"])
		if not frappe.db.exists("Role", "AST-TEST-Role"):
			frappe.get_doc({"doctype": "Role", "role_name": "AST-TEST-Role"}).insert(ignore_permissions=True)
		frappe.get_doc(
			{
				"doctype": "Custom DocPerm",
				"parent": "Loan Category",
				"parenttype": "DocType",
				"parentfield": "permissions",
				"role": "AST-TEST-Role",
				"permlevel": 0,
				"read": 1,
				"delete": 1,
			}
		).insert(ignore_permissions=True)
		frappe.clear_cache(doctype="Loan Category")
		after = self.data_as("senior", "Loan Category")
		self.assertIn("AST-TEST-Role", after["actions"]["read"]["roles_that_can"])
		self.assertIn("AST-TEST-Role", after["actions"]["delete"]["roles_that_can"])

	def data_as(self, who, doctype):
		self.as_user(who)
		return self.data(self.call("check_my_access", doctype=doctype, actions=["read", "delete"], docname=None))


class TestFindRecords(ToolTestCase):
	def setUp(self):
		super().setUp()
		self.as_user("senior")

	def test_limit_zero_negative_and_huge(self):
		for bad in (0, -1):
			with self.subTest(limit=bad):
				self.assertIn("whole number", self.error(find(self, limit=bad)))
		data = self.data(find(self, limit=10**9))
		self.assertTrue(data["limit_clamped"])
		self.assertEqual(data["limit"], 20)
		self.assertEqual(self.data(find(self, limit=3))["count_returned"], 3)
		self.assertFalse(self.data(find(self, limit=3))["limit_clamped"])

	def test_the_same_field_may_be_used_twice_for_a_range(self):
		data = self.data(
			find(
				self,
				filters=[
					{"field": "docstatus", "operator": ">=", "value": 0, "values": None},
					{"field": "docstatus", "operator": "<=", "value": 1, "values": None},
				],
				fields=["name", "docstatus"],
			)
		)
		self.assertTrue(data["rows"])
		self.assertTrue(all(0 <= r["docstatus"] <= 1 for r in data["rows"]))

	def test_in_not_in_between_is_and_like(self):
		self.assertTrue(self.data(find(self, filters=[{"field": "loan_product", "operator": "in", "value": None, "values": ["PL-EMI", "x"]}]))["rows"])
		rows = self.data(find(self, filters=[{"field": "loan_product", "operator": "not in", "value": None, "values": ["PL-EMI"]}]))["rows"]
		self.assertTrue(all(r["loan_product"] != "PL-EMI" for r in rows))
		self.assertTrue(self.data(find(self, filters=[{"field": "docstatus", "operator": "between", "value": None, "values": [0, 1]}]))["rows"])
		self.assertTrue(self.data(find(self, filters=[{"field": "loan_product", "operator": "is", "value": "set", "values": None}]))["rows"])
		self.assertTrue(self.data(find(self, filters=[{"field": "name", "operator": "like", "value": "ACC-LOAN%", "values": None}]))["rows"])

	def test_bad_filters_are_refused(self):
		def one(**overrides):
			return find(self, filters=[{**FILTER, **overrides}])

		self.assertIn("not available", self.error(one(field="no_such_field")))
		self.assertIn("not available", self.error(one(field="name; drop table tabLoan")))
		self.assertIn("takes", self.error(one(operator="in")))  # in without values
		self.assertIn("takes", self.error(one(operator="=", values=["a"])))  # = with values
		self.assertIn("takes", self.error(one(operator="=", value=None)))
		self.assertIn("too many", self.error(one(operator="in", value=None, values=[str(i) for i in range(51)])))
		self.assertIn("two values", self.error(one(operator="between", value=None, values=["a"])))
		self.assertIn("short text", self.error(one(operator="like", value="x" * 101)))
		self.assertIn("set", self.error(one(operator="is", value="maybe")))
		self.assertIn("allowed values", self.error(one(operator="; drop")))

	def test_order_by(self):
		self.assertTrue(self.data(find(self, order_by="name desc"))["rows"])
		for bad in ("name; drop table tabLoan", "name", "1 asc", "(select 1) asc", "name asc, status", ""):
			with self.subTest(order_by=bad):
				self.assertIn("order_by", self.error(find(self, order_by=bad)))

	def test_fields_must_be_one_to_thirty_readable_names(self):
		self.assertIn("1 to 30", self.error(find(self, fields=[])))
		self.assertIn("not available", self.error(find(self, fields=["name", "*"])))
		self.assertIn("not available", self.error(find(self, fields=["count(name)"])))

	def test_a_doctype_off_the_allowlist_is_refused(self):
		self.assertEqual(self.error(find(self, doctype="User")), guard.NOT_ALLOWED_DOCTYPE)

	def test_the_result_never_holds_a_total_count(self):
		data = self.data(find(self, limit=2))
		self.assertEqual(data["count_returned"], 2)
		self.assertFalse({"total", "count", "total_count"} & set(data))


class TestGetRecord(ToolTestCase):
	def test_child_rows_are_present_and_are_filtered(self):
		self.as_user("senior")
		name = frappe.get_all("Loan Product", pluck="name", limit=1)[0]
		data = self.data(self.call("get_record", doctype="Loan Product", name=name))
		self.assertIn("children", data)
		for rows in data["children"].values():
			for row in rows:
				self.assertFalse({"owner", "modified_by", "parent", "parenttype", "parentfield"} & set(row))

	def test_a_doctype_off_the_allowlist_is_refused(self):
		self.as_user("senior")
		self.assertEqual(self.error(self.call("get_record", doctype="User", name="Administrator")), guard.NOT_ALLOWED_DOCTYPE)
