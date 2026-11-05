"""M4b `chat.ask` with the orchestrator: the audit row on every path, the history from the caller's own conversation,
and one run through the real registry as each persona."""

import json
from unittest import mock

import frappe

from lending_assistant.api import chat
from lending_assistant.assistant import guard, orchestrator
from lending_assistant.tests import claude_fakes as cf
from lending_assistant.tests.base import ToolTestCase

LABELLED = "Short answer. [Analysis] Per BRD 7.1."


class AskCase(ToolTestCase):
	def setUp(self):
		super().setUp()
		self.configure(
			live_data=1, code_reader=1, web_search=0, default_effort="medium", deep_effort="medium"
		)
		for patcher in (mock.patch.object(orchestrator, "_api_key", return_value=cf.FAKE_KEY),):
			patcher.start()
			self.addCleanup(patcher.stop)

	def ask(self, script, who="senior", dispatch=None, **kwargs):
		client = cf.FakeClient(script)
		self.addCleanup(lambda: self.assertEqual(client.alternation_problems, []))
		patches = [mock.patch.object(orchestrator, "_make_client", return_value=client)]
		if dispatch:
			patches.append(mock.patch.object(orchestrator.registry, "dispatch", side_effect=dispatch))
		for p in patches:
			p.start()
		try:
			self.as_user(who)
			question = kwargs.pop("question", "What is DPD?")
			return chat.ask(question, **kwargs), client
		finally:
			for p in patches:
				p.stop()

	def row(self, name):
		frappe.set_user("Administrator")
		return frappe.get_doc("Assistant Message", name)


class TestAskWiring(AskCase):
	def test_the_audit_row_carries_the_g10_fields(self):
		script = [
			cf.response("tool_use", cf.tool_use("t1", "get_card", {"card_id": "x"}), u=cf.usage(i=10, o=5, cw=300), model="claude-opus-5-5"),
			cf.response("end_turn", cf.text(LABELLED), u=cf.usage(i=20, o=9, cr=300), model="claude-opus-5-5"),
		]  # fmt: skip
		result, _ = self.ask(
			script,
			dispatch=lambda n, a=None: registry_ok(),
			route="Form/Loan/AST-L-1", depth="Technical", deep=1,
		)  # fmt: skip
		self.assertEqual(set(result), {"conversation", "message", "answer", "status"})
		row = self.row(result["message"])
		self.assertEqual(
			(row.status, row.model, row.depth, row.deep), ("ok", "claude-opus-5-5", "Technical", 1)
		)
		self.assertEqual((row.tokens_in, row.tokens_out), (10 + 300 + 20 + 300, 14))
		self.assertEqual(json.loads(row.tool_calls)[0]["name"], "get_card")
		self.assertEqual(json.loads(row.cards_used), [{"id": "c1", "version": 3, "via": "get_card"}])
		self.assertEqual((row.route_doctype, row.route_docname), ("Loan", "AST-L-1"))
		self.assertEqual(row.answer, LABELLED)
		self.assertGreaterEqual(row.latency_ms, 0)

	def test_every_path_writes_exactly_one_row(self):
		cases = {
			"limited": [cf.response("max_tokens", cf.text("cut"))],
			"refusal": [cf.response("refusal")],
			"api_error": [RuntimeError("x")],
		}
		for name, script in cases.items():
			with self.subTest(path=name):
				before = self.count("Assistant Message")
				result, _ = self.ask(script)
				self.assertEqual(self.count("Assistant Message"), before + 1)
				self.assertEqual(self.row(result["message"]).status, result["status"])

	def test_no_key_still_writes_the_row_and_makes_no_call(self):
		with mock.patch.object(orchestrator, "_api_key", return_value=None):
			before = self.count("Assistant Message")
			self.as_user("dev")
			result = chat.ask("hello")
		self.assertEqual((result["status"], result["answer"]), ("error", "The advisor has no API key yet."))
		self.assertEqual(self.count("Assistant Message"), before + 1)

	def test_the_second_question_sees_the_first_as_plain_text_and_error_rows_are_skipped(self):
		first, _ = self.ask([cf.response("end_turn", cf.text(LABELLED))], question="First question?")
		failed, _ = self.ask(
			[RuntimeError("x")], question="Broken question?", conversation=first["conversation"]
		)
		self.assertEqual(failed["status"], "error")
		_, client = self.ask(
			[cf.response("end_turn", cf.text(LABELLED))],
			question="Second?",
			conversation=first["conversation"],
		)
		messages = client.calls[0]["messages"]
		self.assertEqual(
			messages,
			[
				{"role": "user", "content": "First question?"},
				{"role": "assistant", "content": LABELLED},
				{"role": "user", "content": "Second?"},
			],
		)

	def test_a_replayed_turn_carries_a_note_of_the_tools_it_used(self):
		script = [
			cf.response("tool_use", cf.tool_use("t1", "get_card", {"card_id": "c1"})),
			cf.response("end_turn", cf.text(LABELLED)),
		]
		first, _ = self.ask(script, dispatch=lambda n, a=None: registry_ok(), question="First question?")
		_, client = self.ask(
			[cf.response("end_turn", cf.text(LABELLED))],
			question="Second?",
			conversation=first["conversation"],
		)
		replayed = client.calls[0]["messages"][1]["content"]
		self.assertTrue(replayed.startswith(LABELLED))
		self.assertIn("(Tools used in that answer, results not repeated: get_card(card_id=c1): ok)", replayed)

	def test_history_never_comes_from_somebody_elses_conversation(self):
		first, _ = self.ask([cf.response("end_turn", cf.text(LABELLED))], question="Private?")
		with self.assertRaises(frappe.DoesNotExistError):
			self.ask([cf.response("end_turn", cf.text("x"))], who="dev", conversation=first["conversation"])

	def test_the_gates_still_run_before_the_orchestrator(self):
		with mock.patch.object(orchestrator, "run") as run:
			self.as_user("noaccess")
			with self.assertRaises(frappe.PermissionError):
				chat.ask("hello")
			run.assert_not_called()


def registry_ok():
	from lending_assistant.assistant.tools import registry

	return registry.ToolResult(guard.as_data({"id": "c1", "version": 3}, "analysis"), False, "analysis")


class TestRealRegistryPerPersona(AskCase):
	"""One scripted model that asks for the same two tools, run through the REAL dispatcher as each persona (#46)."""

	def script(self, loan):
		return [
			cf.response(
				"tool_use",
				cf.tool_use("a", "get_record", {"doctype": "Loan", "name": loan}),
				cf.tool_use("b", "get_loan_dues", {"loan": loan, "as_on_date": None}),
			),
			cf.response("end_turn", cf.text("[Live site] done.")),
		]

	def tool_contents(self, client):
		return [b["content"] for b in client.calls[1]["messages"][-1]["content"]]

	def test_limited_gets_the_g4_reply_for_a_hidden_loan_and_the_data_for_a_visible_one(self):
		visible, hidden = self.loan_names()
		frappe.set_user("Administrator")
		_, client = self.ask(self.script(visible), who="limited")
		for content in self.tool_contents(client):
			self.assertTrue(content.startswith('<data source="live_site">'), content[:120])
		_, client = self.ask(self.script(hidden), who="limited")
		for content in self.tool_contents(client):
			self.assertEqual(json.loads(content)["error"], guard.NOT_FOUND)

	def test_senior_reads_both(self):
		_, hidden = self.loan_names()
		_, client = self.ask(self.script(hidden), who="senior")
		for content in self.tool_contents(client):
			self.assertTrue(content.startswith('<data source="live_site">'))

	def test_live_data_off_refuses_both_tools_and_the_turn_goes_on(self):
		visible, _ = self.loan_names()
		self.configure(live_data=0)
		result, client = self.ask(self.script(visible), who="senior")
		self.assertEqual(result["status"], "ok")
		for content in self.tool_contents(client):
			self.assertEqual(json.loads(content)["error"], guard.LIVE_DATA_OFF)
