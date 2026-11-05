"""M3b validate: the drift check on the ingested cards, and an injected error is caught."""

import os

from lending_assistant.kb import store, validate
from lending_assistant.tests.base import AssistantTestCase

FIELDS = [
	{"label": "Status", "fieldname": "status", "options": "Draft\nSanctioned\nDisbursed"},
	{"label": "Reference Number", "fieldname": "reference_number", "options": None},
]


def meta_of(doctype):
	return FIELDS if doctype == "Loan" else None


SIDEBAR = {("loan management", "loan"), ("", "loan")}
ROOTS = {"lending": os.path.join(validate.APPS_DIR, "lending")}


def check(**card):
	return validate.check_cards([{"id": "bridge.X", **card}], meta_of, SIDEBAR, ROOTS)


class TestValidate(AssistantTestCase):
	def test_zero_findings_on_the_ingested_set(self):
		result = validate.run()
		self.assertEqual(result["findings"], [])
		self.assertEqual(result["checked"], 941)

	def test_a_clean_card_has_no_findings(self):
		findings, _ = check(
			doctypes=["Loan"], fields=["Loan.Status", "Loan.reference_number"], options=["Loan.Status=Sanctioned"],
			menus=["Lending > Loan Management > Loan"], code_refs=["lending/hooks.py", "lending/hooks.py:12", "lending/hooks.py:12-20"],
		)
		self.assertEqual(findings, [])

	def test_one_injected_error_of_each_kind_is_reported_once(self):
		cases = {
			"doctypes": (["Loan Nope"], "does not exist"),
			"fields": (["Loan.Wrong Label"], "no field labelled"),
			"options": (["Loan.Status=Nonexistent"], "no option"),
			"menus": (["Lending > Loan Management > Missing"], "not in the Lending sidebar"),
			"code_refs": (["lending/does_not_exist.py"], "does not exist"),
		}
		for key, (value, word) in cases.items():
			with self.subTest(key=key):
				findings, _ = check(**{key: value})
				self.assertEqual(len(findings), 1, findings)
				self.assertIn(word, findings[0])

	def test_a_field_on_a_missing_doctype_and_an_option_on_a_missing_field(self):
		self.assertEqual(len(check(fields=["Nope.Status"])[0]), 1)
		self.assertEqual(len(check(options=["Loan.Nope=Draft"])[0]), 1)

	def test_dotdot_and_foreign_code_refs_are_findings(self):
		for ref in ("lending/../frappe/hooks.py", "../etc/passwd", "/etc/passwd", "other/x.py", "lending/../../x"):
			with self.subTest(ref=ref):
				self.assertEqual(len(check(code_refs=[ref])[0]), 1)

	def test_menus_outside_lending_are_notes_not_findings(self):
		findings, notes = check(menus=["Accounting > General Ledger"])
		self.assertEqual(findings, [])
		self.assertEqual(len(notes), 1)

	def test_the_injected_error_is_caught_end_to_end(self):
		"""Change one real field label in a loaded copy of the cards and run the same check with a real meta."""
		cards = [store.get_card("bridge.BR-LMS-162")]
		cards[0]["fields"] = ["Loan Repayment.Reference Numbr"]
		sidebar = validate.sidebar_pairs([])
		findings, _ = validate.check_cards(cards, validate._meta_of, sidebar, validate.APP_ROOTS)
		self.assertEqual(len(findings), 1)
		self.assertIn("Reference Numbr", findings[0])
