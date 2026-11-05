"""M4b trace: usage sums and the G10 lists come from plain data, with no key, thinking or request body."""

import json

from lending_assistant.assistant import guard, trace
from lending_assistant.tests import claude_fakes as cf
from lending_assistant.tests.base import AssistantTestCase


class TestTrace(AssistantTestCase):
	def test_usage_adds_all_three_prompt_parts(self):
		totals = trace.UsageTotals()
		totals.add(cf.usage(i=5, o=2, cw=100, cr=200))
		totals.add(cf.usage(i=1, o=1, web=3))
		self.assertEqual((totals.tokens_in, totals.tokens_out), (306, 3))
		self.assertEqual(totals.web_search_requests, 3)

	def test_a_missing_or_odd_usage_counts_the_call_and_nothing_else(self):
		totals = trace.UsageTotals()
		totals.add(None)
		totals.add(cf.Obj(input_tokens="12", output_tokens=True))
		self.assertEqual((totals.calls, totals.tokens_in, totals.tokens_out), (2, 0, 0))

	def test_arguments_are_capped_and_plain(self):
		out = trace.cap_arguments({"a": "x" * 900, "b": [1, "y" * 900], "c": object()})
		self.assertEqual(len(out["a"]), 501)
		self.assertEqual(len(out["b"][1]), 501)
		self.assertIsInstance(out["c"], str)
		json.dumps(out)

	def test_records_files_and_cards_ignore_results_that_are_not_envelopes(self):
		for fn in (trace.records_from, trace.code_files_from, trace.cards_from):
			self.assertEqual(fn("get_record", "not an envelope"), [])
			self.assertEqual(fn("get_record", '{"error": "x"}'), [])

	def test_records_are_read_from_the_result_never_from_the_arguments(self):
		env = guard.as_data({"doctype": "Loan", "name": "REAL"}, "live_site")
		self.assertEqual(trace.records_from("get_record", env), [{"doctype": "Loan", "name": "REAL"}])
		self.assertEqual(trace.records_from("check_my_access", env), [])
