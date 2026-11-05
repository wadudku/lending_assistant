"""M4b `get_loan_dues` (option B, #148): sums of Loan Demand rows read through the guard, per persona (#46)."""

from decimal import Decimal
from unittest import mock

import frappe

from lending_assistant.assistant import guard
from lending_assistant.assistant.tools import dues, registry
from lending_assistant.tests.base import ToolTestCase

MISSING = "AST-TEST-NO-SUCH-LOAN"


def row(i, dtype="EMI", subtype="Interest", date="2026-01-05 00:00:00", amount=100, paid=0, left=100):
	return {
		"name": f"LM-LD-{i:05d}", "demand_date": date, "demand_type": dtype, "demand_subtype": subtype,
		"demand_amount": amount, "paid_amount": paid, "outstanding_amount": left, "waived_amount": 0,
	}  # fmt: skip


def page_lister(all_rows, per_call=None):
	"""A stand-in for guard.list_records that serves `all_rows` by the keyset filter, 20 at a time."""
	calls = []

	def fake(doctype, filters=None, fields=None, order_by=None, limit=20):
		calls.append(filters)
		last = next((f[2] for f in filters if f[0] == "name"), "")
		due = next(f[2] for f in filters if f[0] == "demand_date")
		bal = next(f for f in filters if f[0] == "outstanding_amount")
		rows = [
			r for r in all_rows
			if r["name"] > last and r["demand_date"] <= due
			and (r["outstanding_amount"] > 0 if bal[1] == ">" else r["outstanding_amount"] <= 0)
		][:limit]  # fmt: skip
		return guard.as_data(
			{
				"rows": [{k: r.get(k) for k in fields} for r in rows],
				"count_returned": len(rows),
				"truncated": False,
			}
		)

	fake.calls = calls
	return fake


class TestLoanDuesLogic(ToolTestCase):
	"""The arithmetic, with the Loan read and the list stubbed; the permission boundaries are in the next class."""

	def run_with(self, rows, as_on="2026-02-01", **kw):
		lister = page_lister(rows)
		loan_env = guard.as_data(
			{
				"doctype": "Loan",
				"name": "L-1",
				"data": {"status": "Disbursed", "loan_product": "PL-EMI"},
				"children": {},
			}
		)
		with (
			mock.patch.object(dues.guard, "read_doc", return_value=loan_env),
			mock.patch.object(dues.guard, "list_records", side_effect=lister),
			mock.patch.object(dues.guard, "readable_fields", return_value=[*row(1), "loan", "docstatus"]),
		):
			result = dues.get_loan_dues("L-1", as_on)
		return guard.unwrap(result), lister

	def test_billed_paid_outstanding_and_overdue_per_demand_type(self):
		rows = [
			row(1, "EMI", "Principal", "2026-01-05 00:00:00", 500, 500, 0),
			row(2, "EMI", "Interest", "2026-01-05 00:00:00", 100, 40, 60),
			row(3, "EMI", "Interest", "2026-02-01 00:00:00", 100, 0, 100),  # due on the date: not overdue
			row(4, "Penalty", "Penalty", "2026-01-20 00:00:00", 10, 0, 10),
			row(5, "EMI", "Interest", "2026-03-01 00:00:00", 100, 0, 100),  # after the date: left out
		]
		data, _ = self.run_with(rows)
		self.assertEqual(data["rows_read"], 4)
		self.assertEqual(data["totals"]["billed"], 710.0)
		self.assertEqual(data["totals"]["paid"], 540.0)
		self.assertEqual(data["totals"]["outstanding"], 170.0)
		self.assertEqual(data["totals"]["overdue"], 70.0)
		self.assertEqual(data["totals"]["due_on_date"], 100.0)
		self.assertEqual(data["oldest_overdue_date"], "2026-01-05")
		interest = next(g for g in data["by_demand"] if g["demand_subtype"] == "Interest")
		self.assertEqual((interest["billed"], interest["overdue"], interest["rows"]), (200.0, 60.0, 2))
		self.assertFalse(data["incomplete"])

	def test_every_result_carries_the_fixed_note(self):
		data, _ = self.run_with([])
		self.assertEqual(data["note"], dues.NOTE)
		self.assertIn("NOT included", data["note"])
		self.assertEqual(data["totals"]["billed"], 0.0)

	def test_paging_goes_past_20_rows_by_name(self):
		rows = [row(i, left=1, amount=1) for i in range(1, 46)]
		data, lister = self.run_with(rows)
		self.assertEqual(data["rows_read"], 45)
		self.assertEqual(data["totals"]["outstanding"], 45.0)
		self.assertEqual(len(lister.calls), 4)  # three pages of open demands, one of settled
		self.assertFalse(data["incomplete"])
		self.assertEqual(
			data["complete_totals"], ["outstanding", "overdue", "due_on_date", "billed", "paid", "waived"]
		)

	def test_the_row_cap_marks_the_result_incomplete(self):
		rows = [
			row(i, left=1, amount=1) for i in range(1, 260)
		]  # all with a balance: more than one phase can read
		data, lister = self.run_with(rows)
		self.assertEqual(data["rows_read"], dues.MAX_PAGES * dues.PAGE)
		self.assertTrue(data["incomplete"])
		self.assertIn("every total is a lower bound", data["incomplete_note"])
		self.assertEqual(data["complete_totals"], [])
		self.assertEqual(
			len(lister.calls), dues.MAX_PAGES + 1
		)  # the capped open phase, then one settled call

	def test_a_loan_with_over_200_demands_keeps_outstanding_and_overdue_complete(self):
		"""R5: 300 settled demands (the oldest names) and 15 open ones (the newest): the old name-order read lost the open ones."""
		settled = [row(i, left=0, amount=10, paid=10, date="2025-01-05 00:00:00") for i in range(1, 301)]
		open_ = [row(i, left=7, amount=10, paid=3, date="2025-06-05 00:00:00") for i in range(301, 316)]
		data, lister = self.run_with([*settled, *open_])
		self.assertEqual(data["totals"]["outstanding"], 105.0)
		self.assertEqual(data["totals"]["overdue"], 105.0)
		self.assertTrue(data["incomplete"])  # the 300 settled rows did not all fit
		self.assertEqual(data["complete_totals"], ["outstanding", "overdue", "due_on_date"])
		self.assertIn("Outstanding and overdue are complete", data["incomplete_note"])
		self.assertEqual(data["rows_read"], 15 + dues.MAX_PAGES * dues.PAGE)
		self.assertLessEqual(data["totals"]["billed"], 3150.0)
		self.assertEqual(len(lister.calls), 1 + dues.MAX_PAGES)

	def test_bad_dates_are_refused_in_python(self):
		for bad in ("2026-13-01", "01-02-2026", "tomorrow", "", 20260101, "2026-1-1  "):
			with self.subTest(bad=bad):
				with self.assertRaises(frappe.ValidationError):
					dues._parse_date(bad)
		self.assertIsNotNone(dues._parse_date(None))

	def test_sums_use_decimal_not_float_drift(self):
		rows = [row(i, amount=Decimal("0.1"), left=Decimal("0.1")) for i in range(1, 4)]
		for r in rows:
			r["demand_amount"] = r["outstanding_amount"] = 0.1
		data, _ = self.run_with(rows)
		self.assertEqual(data["totals"]["billed"], 0.3)


class TestLoanDuesPerPersona(ToolTestCase):
	def setUp(self):
		super().setUp()
		frappe.set_user("Administrator")  # fixtures only
		self.visible = frappe.get_all(
			"Loan Demand", filters={"docstatus": 1, "loan_product": "PL-EMI"}, pluck="loan", limit=1
		)[0]
		self.hidden = frappe.get_all(
			"Loan Demand", filters={"docstatus": 1, "loan_product": ["!=", "PL-EMI"]}, pluck="loan", limit=1
		)[0]
		self.truth = frappe.get_all(
			"Loan Demand",
			filters={"loan": self.visible, "docstatus": 1},
			fields=["demand_amount", "outstanding_amount"],
			limit=0,
		)
		self.configure(live_data=1)

	def test_senior_and_dev_get_totals_equal_to_the_rows(self):
		for who in ("senior", "dev"):
			with self.subTest(who=who):
				self.as_user(who)
				data = self.data(self.call("get_loan_dues", loan=self.visible, as_on_date="2099-12-31"))
				self.assertEqual(data["source"], "live_site")
				self.assertEqual(data["rows_read"], len(self.truth))
				self.assertAlmostEqual(
					data["totals"]["billed"], round(sum(r.demand_amount for r in self.truth), 2), places=2
				)
				self.assertIn("NOT included", data["note"])
				self.assertEqual(data["loan_details"]["loan_product"], "PL-EMI")

	def test_limited_sees_a_pl_emi_loan_and_gets_the_g4_reply_for_a_hidden_one(self):
		self.as_user("limited")
		self.data(self.call("get_loan_dues", loan=self.visible, as_on_date=None))
		hidden = self.call("get_loan_dues", loan=self.hidden, as_on_date=None)
		missing = self.call("get_loan_dues", loan=MISSING, as_on_date=None)
		self.assertEqual(self.error(hidden), guard.NOT_FOUND)
		self.assertEqual(hidden.content, missing.content)

	def test_senior_reads_the_loan_that_limited_cannot(self):
		self.as_user("senior")
		data = self.data(self.call("get_loan_dues", loan=self.hidden, as_on_date=None))
		self.assertNotEqual(data["loan_details"]["loan_product"], "PL-EMI")

	def test_noaccess_is_refused(self):
		self.as_user("noaccess")
		result = self.call("get_loan_dues", loan=self.visible, as_on_date=None)
		self.assertTrue(result.is_error)
		self.assertNotIn(self.visible, result.content)

	def test_live_data_off_is_refused(self):
		self.configure(live_data=0)
		self.as_user("senior")
		self.assertEqual(
			self.error(self.call("get_loan_dues", loan=self.visible, as_on_date=None)), guard.LIVE_DATA_OFF
		)

	def test_bad_arguments_are_refused_before_the_function_runs(self):
		self.as_user("senior")
		for args in (
			{"loan": self.visible, "as_on_date": "x", "user": "a"},
			{"loan": 5, "as_on_date": None},
		):
			with self.subTest(args=args):
				self.assertTrue(registry.dispatch("get_loan_dues", args).is_error)
		self.assertIn(
			"YYYY-MM-DD", self.error(self.call("get_loan_dues", loan=self.visible, as_on_date="nope"))
		)

	def test_no_row_is_written_and_nothing_is_imported_from_lending(self):
		self.as_user("senior")
		before = frappe.db.count("Loan Demand")
		self.data(self.call("get_loan_dues", loan=self.visible, as_on_date=None))
		self.assertEqual(frappe.db.count("Loan Demand"), before)
		source = open(dues.__file__).read()
		self.assertNotIn("import lending", source)
		self.assertNotIn("from lending.", source)

	def test_the_schema_is_strict_compatible(self):
		schema = dues.GET_LOAN_DUES_SCHEMA["input_schema"]
		self.assertTrue(dues.GET_LOAN_DUES_SCHEMA["strict"])
		self.assertFalse(schema["additionalProperties"])
		self.assertEqual(schema["required"], ["loan"])  # as_on_date is optional, not nullable (M4b)
