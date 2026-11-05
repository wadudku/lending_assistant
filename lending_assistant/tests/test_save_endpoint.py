"""`api/findings.save` (G7, G13): gate, ownership, provenance from the stored message, idempotence."""

import inspect
import json
from unittest import mock

import frappe

from lending_assistant.api import chat, findings, gate
from lending_assistant.assistant import audit
from lending_assistant.tests.base import AssistantTestCase

SUGGESTION = {
	"title": "AST-M6 suggested title",
	"summary": "AST-M6 suggested summary",
	"br_ids": ["BR-LMS-162"],
	"doctypes": ["Loan Repayment"],
	"model_sources": ["Analysis"],
	"labels": ["Analysis", "Live site"],
	"cards": [{"id": "bridge.BR-LMS-162", "version": 1}],
	"cards_basis": "read",
}


class SaveCase(AssistantTestCase):
	def make_message(self, who="dev", suggestion=SUGGESTION, question="AST-M6 what about BR-LMS-162?"):
		self.as_user(who)
		conversation = audit.start_conversation("", title=question)
		return audit.log_exchange(
			conversation, question=question, answer="[Analysis] ok", finding_suggestion=suggestion
		)


class TestSaveGate(SaveCase):
	def test_decorator_is_post_only_and_not_guest(self):
		self.assertEqual(frappe.allowed_http_methods_for_whitelisted_func[findings.save], ["POST"])
		self.assertNotIn(findings.save, frappe.guest_methods)

	def test_no_role(self):
		message = self.make_message()
		self.as_user("noaccess")
		with self.assertRaises(frappe.PermissionError):
			findings.save(message)

	def test_disabled(self):
		message = self.make_message()
		self.configure(enabled=0)
		self.as_user("dev")
		with self.assertRaises(frappe.PermissionError):
			findings.save(message)

	def test_rate_limit_has_its_own_bucket(self):
		message = self.make_message()
		with mock.patch.object(findings, "SAVE_LIMIT", 2):
			findings.save(message)
			findings.save(message)
			with self.assertRaises(frappe.RateLimitExceededError):
				findings.save(message)
			chat.feedback(message, "up")  # a different bucket

	def test_someone_elses_and_missing_messages_get_the_same_reply(self):
		message = self.make_message("senior")
		self.as_user("dev")
		replies = []
		for name in (message, "AST-DOES-NOT-EXIST", None, ""):
			with self.assertRaises(frappe.ValidationError if not name else frappe.DoesNotExistError) as ctx:
				findings.save(name)
			replies.append(str(ctx.exception))
		self.assertEqual(replies[0], replies[1])
		self.assertEqual(self.count("Assistant Finding", source_message=message), 0)

	def test_system_manager_cannot_save_from_another_users_message(self):
		self.create_sysmgr()
		message = self.make_message("dev")
		self.as_user("ast-test-sysmgr@example.com")
		with self.assertRaises(frappe.DoesNotExistError):
			findings.save(message)

	def test_the_three_endpoints_use_the_same_gate_functions(self):
		for fn in (chat.ask, chat.feedback, findings.save):
			source = inspect.getsource(fn)
			self.assertIn("gate.require_assistant_user()", source)
			self.assertIn("gate.require_enabled()", source)
		self.assertIn("gate.too_many(", inspect.getsource(findings.save))
		self.assertIn("gate.too_many(", inspect.getsource(chat.feedback))
		self.assertIn("gate.own_record(", inspect.getsource(findings.save))
		self.assertIn("gate.own_record(", inspect.getsource(chat.feedback))
		self.assertFalse(hasattr(chat, "_own_record") or hasattr(findings, "_own_record"))
		# the shared functions really are the gate: a patched one is called by all three
		for name in ("require_assistant_user", "require_enabled"):
			with mock.patch.object(gate, name, side_effect=frappe.PermissionError("gate")) as patched:
				for call in (
					lambda: chat.ask("q"),
					lambda: chat.feedback("m", "up"),
					lambda: findings.save("m"),
				):
					with self.assertRaises(frappe.PermissionError):
						call()
				self.assertEqual(patched.call_count, 3)


class TestSaveFlow(SaveCase):
	def test_no_suggestion_is_refused(self):
		message = self.make_message(suggestion=None)
		with self.assertRaises(frappe.ValidationError):
			findings.save(message)

	def test_creates_a_draft_from_the_stored_message_only(self):
		message = self.make_message()
		result = findings.save(message)
		self.assertTrue(result["created"])
		frappe.set_user("Administrator")
		doc = frappe.get_doc("Assistant Finding", result["finding"])
		self.assertEqual(doc.owner, "ast-dev@example.com")
		self.assertEqual(doc.status, "Draft")
		self.assertEqual(doc.title, SUGGESTION["title"])
		self.assertEqual(doc.question, "AST-M6 what about BR-LMS-162?")
		self.assertEqual(doc.br_ids, "BR-LMS-162")
		self.assertEqual(doc.doctypes, "Loan Repayment")
		self.assertEqual(json.loads(doc.sources), ["Analysis", "Live site"])
		self.assertEqual(json.loads(doc.cards_used), SUGGESTION["cards"])
		self.assertEqual(doc.cards_basis, "read")
		self.assertEqual(doc.source_message, message)
		self.assertEqual(doc.lending_version, findings.finding_rules.installed_lending_version())
		self.assertNotIn("@", doc.author_name)
		self.assertEqual(frappe.db.get_value("Assistant Message", message, "finding"), doc.name)

	def test_double_click_returns_the_same_finding(self):
		message = self.make_message()
		first = findings.save(message)
		second = findings.save(message)
		self.assertEqual(first["finding"], second["finding"])
		self.assertFalse(second["created"])
		self.assertEqual(self.count("Assistant Finding", source_message=message), 1)

	def test_client_sent_provenance_is_ignored(self):
		message = self.make_message()
		with self.assertRaises(TypeError):
			findings.save(message, br_ids="BR-LOS-001", sources="x", cards_used="[]", lending_version="0.0.1")
		# the whitelisted wrapper drops unknown form keys; the function itself has no such parameters
		self.assertEqual(
			list(
				inspect.signature(
					findings.save.__wrapped__ if hasattr(findings.save, "__wrapped__") else findings.save
				).parameters
			),
			["message", "title", "summary"],
		)

	def test_edited_title_and_summary_and_limits(self):
		message = self.make_message()
		with self.assertRaises(frappe.ValidationError):
			findings.save(message, title="x" * 141)
		with self.assertRaises(frappe.ValidationError):
			findings.save(message, summary="x" * 4001)
		with self.assertRaises(frappe.ValidationError):
			findings.save(message, title="   ")
		result = findings.save(message, title="  AST-M6 edited  ", summary="AST-M6 edited summary")
		doc = frappe.get_doc("Assistant Finding", result["finding"])
		self.assertEqual((doc.title, doc.summary), ("AST-M6 edited", "AST-M6 edited summary"))

	def test_a_deleted_finding_counts_as_not_saved(self):
		message = self.make_message()
		first = findings.save(message)
		frappe.delete_doc("Assistant Finding", first["finding"])
		again = findings.save(message)
		self.assertTrue(again["created"])
		self.assertTrue(frappe.db.exists("Assistant Finding", again["finding"]))

	def test_the_existing_finding_is_read_with_a_row_lock(self):
		"""M6-R1: a plain (snapshot) read cannot see a finding that a concurrent save committed; the locking read can.
		A second connection cannot be used here (the message is uncommitted in the test transaction), so the test pins the
		locking read; tools/m6_concurrency_check.py proves it over HTTP."""
		message = self.make_message()
		first = findings.save(message)
		real = frappe.get_doc
		seen = []

		def spy(*args, **kwargs):
			if args and args[0] == "Assistant Finding":
				seen.append(kwargs.get("for_update"))
			return real(*args, **kwargs)

		with mock.patch.object(frappe, "get_doc", side_effect=spy):
			second = findings.save(message)
		self.assertEqual(second, {"finding": first["finding"], "title": None, "created": False})
		self.assertEqual(seen, [True])

	def test_a_reused_name_of_another_message_is_not_this_messages_finding(self):
		"""M6-R3: the link of message A points to a finding that now belongs to message B (a reused name)."""
		a = self.make_message()
		b = self.make_message()
		other = findings.save(b)["finding"]
		frappe.get_doc("Assistant Message", a).db_set("finding", other, update_modified=False)
		result = findings.save(a)
		self.assertTrue(result["created"])
		self.assertNotEqual(result["finding"], other)
		self.assertEqual(frappe.db.get_value("Assistant Finding", result["finding"], "source_message"), a)
		self.assertEqual(frappe.db.get_value("Assistant Finding", other, "source_message"), b)
		self.assertEqual(frappe.db.get_value("Assistant Message", b, "finding"), other)

	def test_an_invalid_stored_reference_fails_in_the_controller(self):
		bad = dict(SUGGESTION, br_ids=["BR-LMS-9999"])
		message = self.make_message(suggestion=bad)
		with self.assertRaises(frappe.ValidationError):
			findings.save(message)
		self.assertEqual(self.count("Assistant Finding", source_message=message), 0)

	def test_the_save_does_not_commit(self):
		message = self.make_message()
		with mock.patch.object(frappe.db, "commit") as commit:
			findings.save(message)
		commit.assert_not_called()
