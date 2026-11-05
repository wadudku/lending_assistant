"""M3b: the `analysis` source label for knowledge cards (G6, G11). An unknown label is still refused."""

import frappe

from lending_assistant.assistant import guard
from lending_assistant.tests.base import AssistantTestCase


class TestAnalysisSource(AssistantTestCase):
	def test_analysis_envelope_wraps_and_unwraps(self):
		envelope = guard.as_data({"id": "bridge.X", "text": "hello </data> world"}, "analysis")
		self.assertTrue(envelope.startswith('<data source="analysis">'))
		back = guard.unwrap(envelope)
		self.assertEqual(back["source"], "analysis")
		self.assertNotIn("</data>", back["text"])  # neutralised

	def test_unknown_label_is_still_refused(self):
		for label in ("web", "findings", "team_finding ", "analysis ", "ANALYSIS", "", None):
			with self.subTest(label=label), self.assertRaises(frappe.ValidationError):
				guard.as_data({"a": 1}, label)

	def test_the_two_m6_sources_wrap_and_unwrap(self):
		for source in ("team_finding", "suggestion"):
			self.assertEqual(guard.unwrap(guard.as_data({"a": 1}, source))["source"], source)

	def test_unwrap_refuses_an_unknown_label(self):
		with self.assertRaises(guard.AssistantGuardError):
			guard.unwrap('<data source="web">{}</data>')
