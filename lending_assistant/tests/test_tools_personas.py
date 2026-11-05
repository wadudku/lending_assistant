"""M4a (#46): every tool, run through `dispatch` as each persona: ast-senior, ast-dev, ast-limited, ast-noaccess.

ast-limited has the User Permission `Loan Product = PL-EMI` and sees 16 of the site's 73 Loans (ENVIRONMENT.md §8);
ast-noaccess has no read permission on any lending doctype. Fixtures are found as Administrator; every call is made as
the persona. The never-send and Password fields, `owner` and `modified_by` must be absent from every output.
"""

import frappe

from lending_assistant.assistant import guard
from lending_assistant.tests.base import ToolTestCase

READERS = ("senior", "dev", "limited")
FORBIDDEN_FIELDS = {"owner", "modified_by"}
LIMITED_VISIBLE_LOANS = 16
MISSING = "AST-TEST-NO-SUCH-LOAN"


def all_field_names(value):
	"""Every dict key in a nested result (field names in `data`, `children` and `fields`)."""
	if isinstance(value, dict):
		for key, item in value.items():
			yield key
			yield from all_field_names(item)
		if "fieldname" in value:
			yield value["fieldname"]
	elif isinstance(value, list):
		for item in value:
			yield from all_field_names(item)


class TestToolsPerPersona(ToolTestCase):
	def setUp(self):
		super().setUp()
		self.visible, self.hidden = self.loan_names()
		frappe.set_user("Administrator")  # fixtures only
		self.all_loan_count = len(frappe.get_all("Loan", pluck="name", limit=0))
		self.pl_emi_count = len(
			frappe.get_all("Loan", filters={"loan_product": "PL-EMI"}, pluck="name", limit=0)
		)
		self.never_send = {
			(r.ref_doctype, r.fieldname) for r in frappe.get_doc("Assistant Settings").never_send_fields
		}
		self.password_fields = {
			(dt, df.fieldname)
			for dt in (r.allowed_doctype for r in frappe.get_doc("Assistant Settings").doctype_allowlist)
			for df in frappe.get_meta(dt).fields
			if df.fieldtype == "Password"
		}
		self.customer = frappe.get_all("Customer", pluck="name", limit=1)[0]

	def as_persona(self, who):
		self.as_user(who)

	# --- the fixtures the matrix relies on

	def test_the_boundary_the_tests_rely_on_is_really_there(self):
		self.assertEqual(self.pl_emi_count, LIMITED_VISIBLE_LOANS)
		self.assertGreater(self.all_loan_count, self.pl_emi_count)
		self.assertIn(("Customer", "mobile_no"), self.never_send)
		self.assertIn(("Loan Disbursement", "bank_account"), self.never_send)

	# --- get_screen_help

	def test_get_screen_help_per_persona(self):
		for who in READERS:
			with self.subTest(who=who):
				self.as_persona(who)
				data = self.data(self.call("get_screen_help", doctype="Loan", search=None))
				self.assertEqual(data["doctype"], "Loan")
				self.assertTrue(data["fields"])
				for field in data["fields"]:
					self.assertEqual(
						set(field), {"fieldname", "label", "fieldtype", "options", "reqd", "description"}
					)
				names = {f["fieldname"] for f in data["fields"]}
				self.assertFalse(names & FORBIDDEN_FIELDS)
				self.assertFalse({n for n in names if n.startswith("_")})
				self.assertEqual(data["source"], "live_site")
		self.as_persona("noaccess")
		self.assertIn("permission", self.error(self.call("get_screen_help", doctype="Loan", search=None)))

	def test_get_screen_help_never_lists_never_send_or_password_fields_on_any_allowlisted_doctype(self):
		doctypes = [r.allowed_doctype for r in frappe.get_doc("Assistant Settings").doctype_allowlist]
		for who in (*READERS, "noaccess"):
			self.as_persona(who)
			for doctype in doctypes:
				result = self.call("get_screen_help", doctype=doctype, search=None)
				if result.is_error:
					self.assertIn("permission", self.error(result))
					self.assertEqual(frappe.has_permission(doctype, "read"), False, f"{doctype} as {who}")
					continue
				for field in guard.unwrap(result.content)["fields"]:
					with self.subTest(who=who, doctype=doctype, field=field["fieldname"]):
						self.assertNotIn((doctype, field["fieldname"]), self.never_send)
						self.assertNotIn((doctype, field["fieldname"]), self.password_fields)
						self.assertNotIn(field["fieldname"], FORBIDDEN_FIELDS)

	def test_get_screen_help_hides_a_field_above_the_users_permlevel(self):
		self.as_persona("limited")
		names = {
			f["fieldname"]
			for f in self.data(self.call("get_screen_help", doctype="Loan", search="loan_product"))["fields"]
		}
		self.assertIn("loan_product", names)
		frappe.set_user("Administrator")
		self.set_permlevel("Loan", "loan_product", 9)
		self.as_persona("limited")
		names = {
			f["fieldname"]
			for f in self.data(self.call("get_screen_help", doctype="Loan", search="loan_product"))["fields"]
		}
		self.assertNotIn("loan_product", names)

	def test_check_my_access_per_persona_matches_has_permission_and_names_the_roles(self):
		actions = ["read", "create", "write", "submit", "cancel", "delete"]
		for who in (*READERS, "noaccess"):
			self.as_persona(who)
			for doctype in ("Loan", "Loan Repayment", "Loan Application"):
				data = self.data(self.call("check_my_access", doctype=doctype, actions=actions, docname=None))
				my_roles = set(frappe.get_roles())
				for action in actions:
					with self.subTest(who=who, doctype=doctype, action=action):
						entry = data["actions"][action]
						self.assertEqual(entry["allowed"], bool(frappe.has_permission(doctype, action)))
						self.assertEqual(
							set(entry["you_have_a_role"]), my_roles & set(entry["roles_that_can"])
						)
						self.assertTrue(
							entry["roles_that_can"] or entry["owner_only_roles"],
							"someone must hold the action",
						)
		# ast-noaccess is told nothing is allowed, and which roles would do it
		self.as_persona("noaccess")
		data = self.data(self.call("check_my_access", doctype="Loan", actions=["read"], docname=None))
		self.assertFalse(data["actions"]["read"]["allowed"])
		self.assertEqual(data["actions"]["read"]["you_have_a_role"], [])
		self.assertTrue(data["actions"]["read"]["roles_that_can"])

	def test_check_my_access_on_a_record_boundary_for_limited(self):
		self.as_persona("limited")
		ok = self.data(self.call("check_my_access", doctype="Loan", actions=["read"], docname=self.visible))
		self.assertTrue(ok["actions"]["read"]["allowed"])
		hidden = self.call("check_my_access", doctype="Loan", actions=["read"], docname=self.hidden)
		missing = self.call("check_my_access", doctype="Loan", actions=["read"], docname=MISSING)
		self.assertEqual(self.error(hidden), guard.NOT_FOUND)
		self.assertEqual(hidden, missing)  # byte-identical: the same ToolResult
		self.as_persona("senior")
		self.assertTrue(
			self.data(self.call("check_my_access", doctype="Loan", actions=["read"], docname=self.hidden))[
				"actions"
			]["read"]["allowed"]
		)
		self.as_persona("noaccess")
		self.assertEqual(
			self.call("check_my_access", doctype="Loan", actions=["read"], docname=self.visible), missing
		)

	# --- find_records

	def test_find_records_limited_sees_16_loans_and_never_one_outside_pl_emi(self):
		self.as_persona("limited")
		for limit in (None, 20, 50, 10**9):
			with self.subTest(limit=limit):
				data = self.data(
					self.call(
						"find_records",
						doctype="Loan",
						filters=[],
						fields=["name", "loan_product"],
						order_by=None,
						limit=limit,
					)
				)
				self.assertEqual(data["count_returned"], LIMITED_VISIBLE_LOANS)
				self.assertEqual({r["loan_product"] for r in data["rows"]}, {"PL-EMI"})
				self.assertFalse(data["may_be_partial"])
				self.assertEqual(data["limit_clamped"], bool(limit and limit > 20))

	def test_find_records_filters_cannot_reach_other_products_for_limited(self):
		self.as_persona("limited")

		def other(op, value, values):
			return [{"field": "loan_product", "operator": op, "value": value, "values": values}]

		for label, filters in (
			("!=", other("!=", "PL-EMI", None)),
			("in", other("in", None, ["PL-EMI", "PL-OTHER", "x"])),
			("not in", other("not in", None, ["PL-EMI"])),
			("like", other("like", "%", None)),
			("is set", other("is", "set", None)),
			("two bounds", [*other(">", "", None), *other("<", "zzzz", None)]),
		):
			with self.subTest(filters=label):
				data = self.data(
					self.call(
						"find_records",
						doctype="Loan",
						filters=filters,
						fields=["name", "loan_product"],
						order_by=None,
						limit=20,
					)
				)
				self.assertLessEqual(data["count_returned"], LIMITED_VISIBLE_LOANS)
				self.assertTrue({r["loan_product"] for r in data["rows"]} <= {"PL-EMI"})
		data = self.data(
			self.call(
				"find_records",
				doctype="Loan",
				filters=other("!=", "PL-EMI", None),
				fields=["name"],
				order_by=None,
				limit=20,
			)
		)
		self.assertEqual(data["rows"], [])

	def test_find_records_seniors_see_a_full_page_and_may_be_partial(self):
		for who in ("senior", "dev"):
			with self.subTest(who=who):
				self.as_persona(who)
				data = self.data(
					self.call(
						"find_records",
						doctype="Loan",
						filters=[],
						fields=["name", "loan_product"],
						order_by=None,
						limit=None,
					)
				)
				self.assertEqual(data["count_returned"], 20)
				self.assertTrue(data["may_be_partial"])
				self.assertNotIn("total", data)
				self.assertGreater(len({r["loan_product"] for r in data["rows"]} | {"PL-EMI"}), 0)

	def test_find_records_noaccess_is_refused(self):
		self.as_persona("noaccess")
		self.assertTrue(
			self.call(
				"find_records", doctype="Loan", filters=[], fields=["name"], order_by=None, limit=None
			).is_error
		)

	def test_find_records_refuses_unreadable_never_send_and_identity_fields(self):
		self.as_persona("senior")
		for doctype, field in (
			("Customer", "mobile_no"),
			("Customer", "email_id"),
			("Loan Disbursement", "bank_account"),
			("Loan", "owner"),
			("Loan", "modified_by"),
			("Loan", "_comments"),
		):
			with self.subTest(field=field):
				as_field = self.call(
					"find_records",
					doctype=doctype,
					filters=[],
					fields=["name", field],
					order_by=None,
					limit=None,
				)
				as_filter = self.call(
					"find_records",
					doctype=doctype,
					filters=[{"field": field, "operator": "like", "value": "%", "values": None}],
					fields=["name"],
					order_by=None,
					limit=None,
				)
				as_order = self.call(
					"find_records",
					doctype=doctype,
					filters=[],
					fields=["name"],
					order_by=f"{field} asc",
					limit=None,
				)
				for result in (as_field, as_filter, as_order):
					self.assertTrue(result.is_error, f"{doctype}.{field}")
					self.assertNotIn(field, result.content.replace("not available", ""))

	def test_find_records_output_never_holds_owner_or_modified_by_even_when_asked_for_everything_else(self):
		self.as_persona("dev")
		fields = [
			f["fieldname"]
			for f in self.data(self.call("get_screen_help", doctype="Loan", search=None))["fields"]
		][:30]
		data = self.data(
			self.call("find_records", doctype="Loan", filters=[], fields=fields, order_by=None, limit=3)
		)
		self.assertFalse(set(all_field_names(data)) & FORBIDDEN_FIELDS)
		self.assertLessEqual(
			len(
				self.call(
					"find_records", doctype="Loan", filters=[], fields=fields, order_by=None, limit=20
				).content
			),
			guard.MAX_CHARS,
		)

	# --- get_record

	def test_get_record_per_persona(self):
		for who in READERS:
			with self.subTest(who=who):
				self.as_persona(who)
				data = self.data(self.call("get_record", doctype="Loan", name=self.visible))
				self.assertEqual(data["name"], self.visible)
				self.assertFalse(set(all_field_names(data)) & FORBIDDEN_FIELDS)
				self.assertTrue(data["children"] is not None)
		self.as_persona("noaccess")
		self.assertEqual(
			self.error(self.call("get_record", doctype="Loan", name=self.visible)), guard.NOT_FOUND
		)

	def test_get_record_the_hidden_loan_and_a_missing_one_give_the_identical_reply(self):
		self.as_persona("limited")
		hidden = self.call("get_record", doctype="Loan", name=self.hidden)
		missing = self.call("get_record", doctype="Loan", name=MISSING)
		self.assertEqual(self.error(hidden), guard.NOT_FOUND)
		self.assertEqual(hidden, missing)
		for name in ("", "../x", "%", "x" * 141, "' or 1=1 --"):
			with self.subTest(name=name[:20]):
				self.assertEqual(self.call("get_record", doctype="Loan", name=name), missing)
		self.as_persona("senior")
		self.assertFalse(
			self.call("get_record", doctype="Loan", name=self.hidden).is_error
		)  # the senior can read it
		self.as_persona("noaccess")
		self.assertEqual(self.call("get_record", doctype="Loan", name=self.hidden), missing)

	def test_get_record_has_no_never_send_or_password_fields(self):
		for who in ("senior", "dev"):
			self.as_persona(who)
			data = self.data(self.call("get_record", doctype="Customer", name=self.customer))
			for forbidden in ("mobile_no", "email_id", "owner", "modified_by"):
				self.assertNotIn(forbidden, data["data"], f"{who}: {forbidden}")
			disbursement = frappe.get_all("Loan Disbursement", pluck="name", limit=1)
			if disbursement:
				got = self.data(self.call("get_record", doctype="Loan Disbursement", name=disbursement[0]))
				self.assertNotIn("bank_account", got["data"])
				self.assertNotIn("owner", got["data"])

	def test_get_record_a_permlevel_field_is_absent_for_a_user_without_that_level(self):
		frappe.set_user("Administrator")
		self.set_permlevel("Loan", "loan_product", 9)
		self.as_persona("limited")
		data = self.data(self.call("get_record", doctype="Loan", name=self.visible))
		self.assertNotIn("loan_product", data["data"])
		self.assertIn("name", data["data"])

	# --- code and knowledge tools: no per-user data, the same for everybody

	def test_code_tools_work_the_same_for_every_persona_and_label_their_output_code(self):
		for who in (*READERS, "noaccess"):
			with self.subTest(who=who):
				self.as_persona(who)
				found = self.call("search_code", query="def get_due_details", app="lending", path_glob=None)
				self.assertEqual(found.source, "code")
				self.assertTrue(self.data(found)["matches"])
				read = self.call("read_code", path="lending/lending/hooks.py", start_line=1, end_line=5)
				self.assertEqual(read.source, "code")
				self.assertEqual(len(self.data(read)["lines"]), 5)

	def test_knowledge_tools_work_the_same_for_every_persona(self):
		for who in (*READERS, "noaccess"):
			with self.subTest(who=who):
				self.as_persona(who)
				self.assertEqual(
					self.call("search_knowledge", query="repayment", type=None).source, "analysis"
				)
				self.assertEqual(
					self.call(
						"lookup_knowledge",
						doctype="Loan Repayment",
						action=None,
						br_id=None,
						brd_section=None,
						term=None,
						journey=None,
						dev_item=None,
					).source,
					"analysis",
				)
				self.assertEqual(self.call("get_card", card_id="no-such-card").source, "analysis")

	def test_every_registered_tool_was_exercised_for_every_persona(self):
		"""A tool added to the registry without a persona test fails here."""
		from lending_assistant.assistant.tools import registry

		exercised = {
			"get_screen_help",
			"check_my_access",
			"find_records",
			"get_record",
			"search_code",
			"read_code",
			"search_knowledge",
			"lookup_knowledge",
			"get_card",
			"get_loan_dues",  # per persona in test_tools_dues.py
		}
		self.assertEqual(set(registry.TOOLS), exercised)
