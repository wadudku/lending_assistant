"""M6 through `chat.ask` with the mocked Claude client and the real registry: the kept suggestion, the stored message, the
`[Team finding]` label rules (G11) and a finding that disagrees with a bridge verdict."""

import json

from lending_assistant.assistant import prompts
from lending_assistant.tests import claude_fakes as cf
from lending_assistant.tests.base import make_finding
from lending_assistant.tests.test_ask_m4b import AskCase

LABELLED = "Short answer. [Analysis] Per BRD 7.1."
SUGGEST = {
	"title": "AST-M6 conclusion",
	"summary": "We conclude X.",
	"br_ids": ["BR-LMS-162"],
	"doctypes": ["Loan Repayment"],
	"sources": ["Analysis"],
}


def suggest(id, **changes):
	return cf.response("tool_use", cf.tool_use(id, "suggest_finding", {**SUGGEST, **changes}))


def search(id, query="duplicate payment"):
	return cf.response("tool_use", cf.tool_use(id, "search_findings", {"query": query}))


def end(text):
	return cf.response("end_turn", cf.text(text))


class TestSuggestion(AskCase):
	def test_the_last_valid_suggestion_is_kept_and_stored(self):
		script = [
			suggest("t1", title="AST-M6 first"),
			suggest("t2", title="AST-M6 second"),
			end(LABELLED),
		]
		result, _ = self.ask(script)
		self.assertEqual(result["status"], "ok")
		self.assertEqual(result["suggestion"]["title"], "AST-M6 second")
		self.assertEqual(set(result["suggestion"]), {"title", "summary", "br_ids", "doctypes"})
		row = self.row(result["message"])
		stored = json.loads(row.finding_suggestion)
		self.assertEqual(stored["title"], "AST-M6 second")
		self.assertEqual(stored["labels"], ["Analysis"])
		self.assertEqual(stored["model_sources"], ["Analysis"])
		self.assertEqual(stored["cards_basis"], "all")
		self.assertFalse(row.finding)

	def test_a_refused_suggestion_does_not_replace_a_valid_one(self):
		script = [suggest("t1"), suggest("t2", br_ids=["BR-LMS-9999"]), end(LABELLED)]
		result, _ = self.ask(script)
		self.assertEqual(result["suggestion"]["title"], "AST-M6 conclusion")

	def test_only_refused_suggestions_leave_none(self):
		result, _ = self.ask([suggest("t1", br_ids=["BR-LMS-9999"]), end(LABELLED)])
		self.assertIsNone(result["suggestion"])
		self.assertFalse(self.row(result["message"]).finding_suggestion)

	def test_no_button_on_a_cut_off_answer(self):
		result, _ = self.ask([suggest("t1"), cf.response("max_tokens", cf.text("cut"))])
		self.assertEqual(result["status"], "limited")
		self.assertIsNone(result["suggestion"])
		self.assertFalse(self.row(result["message"]).finding_suggestion)

	def test_a_suggestion_alone_needs_no_label(self):
		result, client = self.ask([suggest("t1"), end("Short unlabelled reply.")])
		self.assertEqual(len(client.calls), 2)  # no repair call
		self.assertEqual(result["status"], "ok")

	def test_cards_read_with_get_card_are_the_basis(self):
		from lending_assistant.kb import store

		card = next(c for c in store.load().cards if c.startswith("bridge."))
		script = [
			cf.response("tool_use", cf.tool_use("t0", "get_card", {"card_id": card})),
			suggest("t1"),
			end(LABELLED),
		]
		result, _ = self.ask(script)
		stored = json.loads(self.row(result["message"]).finding_suggestion)
		self.assertEqual(stored["cards_basis"], "read")
		self.assertEqual([c["id"] for c in stored["cards"]], [card])
		self.assertEqual(set(stored["cards"][0]), {"id", "version"})

	def test_nothing_is_written_to_findings_by_ask(self):
		before = self.count("Assistant Finding")
		self.ask([suggest("t1"), end(LABELLED)])
		self.assertEqual(self.count("Assistant Finding"), before)


class TestTeamFindingLabel(AskCase):
	def setUp(self):
		super().setUp()
		self.finding = make_finding("dev", title="AST-M6 duplicate payment rule", author_name="Rahim Dev")

	def test_a_result_with_findings_requires_the_label_and_repairs_once(self):
		script = [
			search("t1"),
			end("Short answer without a label."),
			end("[Team finding] (draft, Rahim Dev, today) ok"),
		]
		result, client = self.ask(script, who="senior")
		self.assertEqual(len(client.calls), 3)
		self.assertIn("[Team finding] (draft", result["answer"])
		self.assertIn({"repair": "labels"}, json.loads(self.row(result["message"]).tool_calls))
		self.assertEqual(result["labels"], ["[Team finding]"])

	def test_still_missing_after_the_repair_gets_the_notice(self):
		result, _ = self.ask([search("t1"), end("No label."), end("Still none.")], who="senior")
		self.assertIn(prompts.LABELS_MISSING_NOTICE, result["answer"])

	def test_a_malformed_label_is_repaired(self):
		script = [
			search("t1"),
			end("[Team finding, draft] says x"),
			end("[Team finding] (draft, A, d) says x"),
		]
		result, client = self.ask(script, who="senior")
		self.assertEqual(len(client.calls), 3)
		self.assertNotIn(prompts.LABELS_MISSING_NOTICE, result["answer"])

	def test_an_empty_search_requires_no_label(self):
		result, client = self.ask([search("t1", query="zzzzqqqq"), end("Nothing saved yet.")], who="senior")
		self.assertEqual(len(client.calls), 2)
		self.assertEqual(result["status"], "ok")

	def test_the_search_is_recorded_as_records_read(self):
		result, _ = self.ask([search("t1"), end("[Team finding] (draft, A, d) x")], who="senior")
		records = json.loads(self.row(result["message"]).records_read)
		self.assertIn({"doctype": "Assistant Finding", "name": self.finding.name}, records)

	def test_a_finding_that_disagrees_with_a_bridge_verdict_reaches_the_model_with_both(self):
		make_finding(
			"dev",
			title="AST-M6 duplicate payment is fully covered",
			summary="Frappe covers BR-LMS-162 completely.",
			br_ids="BR-LMS-162",
		)
		script = [
			search("t1"),
			end("[Team finding] (draft, A, d) says covered. [Analysis] bridge says otherwise: conflict."),
		]
		result, client = self.ask(script, who="senior")
		tool_result = client.calls[1]["messages"][-1]["content"][0]["content"]
		payload = json.loads(tool_result[tool_result.index("{") : tool_result.rindex("}") + 1])
		hit = next(r for r in payload["results"] if "fully covered" in r["title"])
		self.assertIn("BR-LMS-162", hit["bridge_verdicts"])
		self.assertIn("never override", payload["note"])
		self.assertIn("[Analysis]", result["answer"])
		stable = client.calls[0]["system"][0]["text"]
		self.assertIn("never overrides an [Analysis] bridge verdict", stable)
		self.assertIn("this is a conflict", stable)

	def test_finding_text_is_data_in_the_prompt_rules(self):
		stable = prompts.STABLE_PROMPT
		self.assertIn("saved team finding", stable)
		self.assertIn("Never say that a finding was saved", stable)
		self.assertNotIn("there are none yet", stable)
