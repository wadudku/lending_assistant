"""M4b key-leak tests (#48): a fake key is planted in Assistant Settings and the full `chat.ask` runs on every path with
a scripted client. The key string must appear nowhere: not in the reply, not in the audit rows, not in the Error Log, not
in anything sent to the model, not in the app's log files. `get_api_key` outside the orchestrator is a scan hit
(tests/test_scan_m4b.py)."""

import json
import os
from unittest import mock

import anthropic
import frappe
from frappe.utils import now_datetime

from lending_assistant.api import chat
from lending_assistant.assistant import guard, orchestrator, settings
from lending_assistant.assistant.tools import registry
from lending_assistant.tests import claude_fakes as cf
from lending_assistant.tests.base import ToolTestCase

REAL_API_KEY = orchestrator._api_key  # captured before the base class patches it out
KEY = cf.FAKE_KEY
LABELLED = "[Analysis] fine."


class AuthError(anthropic.AuthenticationError):
	def __init__(self):
		Exception.__init__(self, f"invalid x-api-key {KEY}")


class LeakCase(ToolTestCase):
	def setUp(self):
		super().setUp()
		frappe.set_user("Administrator")
		self.owner_key = REAL_API_KEY()  # the key the owner may have entered: put back afterwards, never lost
		doc = frappe.get_doc("Assistant Settings")
		doc.api_key = KEY
		doc.save(ignore_permissions=True)
		self.configure(live_data=1, code_reader=1, web_search=0)
		self.started = now_datetime()
		patcher = mock.patch.object(orchestrator, "_api_key", side_effect=REAL_API_KEY)
		patcher.start()
		self.addCleanup(patcher.stop)
		self.addCleanup(self.clear_key)

	def clear_key(self):
		frappe.set_user("Administrator")
		doc = frappe.get_doc("Assistant Settings")
		doc.api_key = self.owner_key or ""
		doc.save(ignore_permissions=True)

	def run_path(self, script, dispatch=None):
		client = cf.FakeClient(script)
		patches = [mock.patch.object(orchestrator, "_make_client", return_value=client)]
		if dispatch:
			patches.append(mock.patch.object(orchestrator.registry, "dispatch", side_effect=dispatch))
		for p in patches:
			p.start()
		try:
			self.as_user("senior")
			result = chat.ask("Tell me about the loan and the key.")
		finally:
			for p in patches:
				p.stop()
		return result, client

	def everywhere(self):
		"""All text that could carry the key, apart from the reply itself."""
		frappe.set_user("Administrator")
		blobs = []
		for doctype in ("Assistant Message", "Assistant Conversation"):
			for name in frappe.get_all(doctype, pluck="name", limit_page_length=0):
				blobs.append(json.dumps(frappe.get_doc(doctype, name).as_dict(), default=str))
		for row in frappe.get_all(
			"Error Log", filters={"creation": [">=", self.started]}, fields=["method", "error"]
		):
			blobs.append(json.dumps(row, default=str))
		for folder in (os.path.join(frappe.utils.get_bench_path(), "logs"), frappe.get_site_path("logs")):
			if os.path.isdir(folder):
				for name in os.listdir(folder):
					path = os.path.join(folder, name)
					if os.path.isfile(path) and os.path.getsize(path) < 20_000_000:
						with open(path, errors="ignore") as handle:
							blobs.append(handle.read())
		blobs.append(json.dumps(frappe.local.message_log, default=str))
		return blobs

	def assertNoLeak(self, result, client):
		self.assertNotIn(KEY, json.dumps(result, default=str))
		for call in client.calls:
			self.assertNotIn(KEY, json.dumps({k: v for k, v in call.items()}, default=str))
		for blob in self.everywhere():
			self.assertNotIn(KEY, blob)


class TestKeyNeverLeaks(LeakCase):
	def test_the_key_is_really_planted_and_get_settings_does_not_carry_it(self):
		self.assertEqual(settings.get_api_key(), KEY)
		self.assertNotIn(KEY, json.dumps(settings.get_settings(), default=str))
		self.assertNotIn("api_key", settings.get_settings())

	def test_ok(self):
		result, client = self.run_path([cf.response("end_turn", cf.text(LABELLED))])
		self.assertEqual(result["status"], "ok")
		self.assertNoLeak(result, client)

	def test_the_model_echoing_the_key_is_redacted_in_the_reply_and_the_row(self):
		result, client = self.run_path([cf.response("end_turn", cf.text(f"[Analysis] the key is {KEY}"))])
		self.assertIn("[redacted]", result["answer"])
		self.assertNoLeak(result, client)

	def test_tool_refusal_with_the_real_dispatcher(self):
		script = [
			cf.response("tool_use", cf.tool_use("t1", "get_record", {"doctype": "Assistant Settings", "name": "Assistant Settings"})),
			cf.response("end_turn", cf.text(LABELLED)),
		]  # fmt: skip
		result, client = self.run_path(script)
		sent = client.calls[1]["messages"][-1]["content"][0]
		self.assertTrue(sent["is_error"])
		self.assertNoLeak(result, client)

	def test_dispatch_raise_with_the_key_in_its_message(self):
		def boom(name, args=None):
			raise guard.AssistantGuardError(f"state changed {KEY}")

		script = [cf.response("tool_use", cf.tool_use("t1", "get_card", {"card_id": "x"}))]
		result, client = self.run_path(script, dispatch=boom)
		self.assertEqual(result["status"], "error")
		self.assertNoLeak(result, client)

	def test_api_error_with_the_key_in_the_exception_text(self):
		result, client = self.run_path([AuthError()])
		self.assertEqual(result["status"], "error")
		self.assertNoLeak(result, client)

	def test_any_other_exception_with_the_key(self):
		result, client = self.run_path([ValueError(f"oops {KEY}")])
		self.assertEqual(result["status"], "error")
		self.assertNoLeak(result, client)

	def test_max_tokens(self):
		result, client = self.run_path([cf.response("max_tokens", cf.text("partial"))])
		self.assertEqual(result["status"], "limited")
		self.assertNoLeak(result, client)

	def test_refusal(self):
		result, client = self.run_path(
			[cf.response("refusal", details=cf.Obj(category="cyber", explanation=KEY))]
		)
		self.assertEqual(result["status"], "error")
		self.assertNoLeak(result, client)

	def test_a_tool_result_that_contains_the_key_is_not_sent_by_us_unprompted(self):
		"""Nothing in the app reads the key into a tool: get_card on a real card never carries it."""
		script = [
			cf.response(
				"tool_use", cf.tool_use("t1", "get_screen_help", {"doctype": "Loan", "search": None})
			),
			cf.response("end_turn", cf.text(LABELLED)),
		]
		result, client = self.run_path(script)
		self.assertNoLeak(result, client)

	def test_the_dispatcher_result_type_is_what_the_orchestrator_expects(self):
		self.assertIn("is_error", registry.ToolResult._fields)
