"""M6 `finding_rules`: references, stale reasons, installed lending version."""

from unittest import mock

from lending_assistant.assistant import finding_rules, prompts
from lending_assistant.kb import store, validate
from lending_assistant.tests.base import AssistantTestCase


class TestFindingRules(AssistantTestCase):
	def test_canonical_br_ids(self):
		self.assertEqual(finding_rules.canonical_br_id("br-lms-162"), "BR-LMS-162")
		self.assertEqual(finding_rules.canonical_br_id("BR-LMS-170c"), "BR-LMS-170c")
		self.assertEqual(finding_rules.canonical_br_id("BR-LMS-170r"), "BR-LMS-170r")
		self.assertIsNone(finding_rules.canonical_br_id("162"))
		self.assertIsNone(finding_rules.canonical_br_id("BR-LMS-999"))
		self.assertIsNone(finding_rules.canonical_br_id("<script>"))

	def test_check_br_ids_names_every_unknown_one(self):
		self.assertEqual(
			finding_rules.check_br_ids("BR-LMS-162\nbr-lms-162\n\nBR-LMS-170c"), ["BR-LMS-162", "BR-LMS-170c"]
		)
		with self.assertRaises(Exception) as ctx:
			finding_rules.check_br_ids(["BR-LMS-162", "BR-LMS-999", "X-1"])
		self.assertIn("BR-LMS-999", str(ctx.exception))
		self.assertIn("X-1", str(ctx.exception))

	def test_check_doctypes(self):
		self.assertEqual(
			finding_rules.check_doctypes(["Loan", "Loan Repayment", "Loan"]), ["Loan", "Loan Repayment"]
		)
		with self.assertRaises(Exception) as ctx:
			finding_rules.check_doctypes("Loan\nNo Such Doctype")
		self.assertIn("No Such Doctype", str(ctx.exception))

	def test_too_many_references(self):
		with self.assertRaises(Exception):
			finding_rules.check_doctypes([f"D{i}" for i in range(11)])

	def test_installed_lending_version_is_read_from_the_checkout(self):
		self.assertRegex(validate.installed_lending_version(), r"^\d+\.\d+\.\d+")

	def test_stale_reasons(self):
		card = next(iter(store.load().cards))
		version = store.load().cards[card]["version"]
		installed = validate.installed_lending_version()
		good = '[{"id": "%s", "version": %s}]' % (card, version)
		self.assertEqual(finding_rules.stale_reasons(good, installed), [])
		changed = '[{"id": "%s", "version": %s}]' % (card, version + 1)
		self.assertIn(f"card changed: {card}", finding_rules.stale_reasons(changed, installed)[0])
		removed = '[{"id": "bridge.BR-XXX-001", "version": 1}]'
		self.assertEqual(finding_rules.stale_reasons(removed, installed), ["card removed: bridge.BR-XXX-001"])
		self.assertEqual(len(finding_rules.stale_reasons(good, "1.0.0")), 1)
		self.assertEqual(finding_rules.stale_reasons("not json", installed), ["cards unknown"])
		with mock.patch.object(finding_rules, "installed_lending_version", return_value="9.9.9"):
			self.assertIn("lending version", finding_rules.stale_reasons(good, installed)[0])

	def test_bridge_verdicts(self):
		verdicts = finding_rules.bridge_verdicts(["BR-LMS-162", "BR-LMS-999"])
		self.assertIn(verdicts["BR-LMS-162"], ("covered", "partial", "gap", "gap_cbs", "not_analysed"))
		self.assertIsNone(verdicts["BR-LMS-999"])
