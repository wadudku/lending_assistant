import frappe

from lending_assistant.api import chat
from lending_assistant.tests.base import AssistantTestCase

NOT_FOUND = "I can't find a record with that ID that you have access to."
FAKE = "AST-DOES-NOT-EXIST"


def error_text(exc):
	return str(exc.exception)


class TestAsk(AssistantTestCase):
	def counts(self):
		return self.count("Assistant Message"), self.count("Assistant Conversation")

	# --- who may call, and when

	def test_ask_requires_role(self):
		before = self.counts()
		self.as_user("noaccess")
		with self.assertRaises(frappe.PermissionError):
			chat.ask("What is DPD?")
		frappe.set_user("Administrator")
		self.assertEqual(self.counts(), before)

	def test_ask_disabled(self):
		self.configure(enabled=0)
		before = self.counts()
		self.as_user("dev")
		with self.assertRaises(frappe.PermissionError) as ctx:
			chat.ask("What is DPD?")
		self.assertIn("turned off", error_text(ctx))
		frappe.set_user("Administrator")
		self.assertEqual(self.counts(), before)

	# --- the stub reply and the log row (G10)

	def test_ask_stub_and_log(self):
		self.as_user("dev")
		dev_before = len(frappe.get_list("Assistant Message", pluck="name", limit_page_length=0))

		result = chat.ask("What is DPD?", route="Form/Loan/AST-LOAN-1", depth="Technical", deep=1)
		self.assertEqual(set(result), {"conversation", "message", "answer", "status", "labels"})
		self.assertEqual(result["answer"], "The advisor has no API key yet.")
		self.assertEqual(result["status"], "error")

		self.assertEqual(
			len(frappe.get_list("Assistant Message", pluck="name", limit_page_length=0)), dev_before + 1
		)

		frappe.set_user("Administrator")
		message = frappe.get_doc("Assistant Message", result["message"])
		self.assertEqual(message.user, "ast-dev@example.com")
		self.assertEqual(message.owner, "ast-dev@example.com")
		self.assertEqual(message.conversation, result["conversation"])
		self.assertEqual(message.question, "What is DPD?")
		self.assertEqual(message.answer, result["answer"])
		self.assertEqual(message.route, "Form/Loan/AST-LOAN-1")
		self.assertEqual((message.route_doctype, message.route_docname), ("Loan", "AST-LOAN-1"))
		self.assertEqual(
			(message.depth, message.deep, message.status, message.model), ("Technical", 1, "error", "stub")
		)
		self.assertIn("Assistant User", frappe.parse_json(message.roles))
		self.assertGreaterEqual(message.latency_ms, 0)

		conversation = frappe.get_doc("Assistant Conversation", result["conversation"])
		self.assertEqual(conversation.user, "ast-dev@example.com")
		self.assertEqual(conversation.message_count, 1)
		self.assertEqual(conversation.title, "What is DPD?")
		self.assertEqual(conversation.first_route, "Form/Loan/AST-LOAN-1")

		# a second question in the same conversation adds a row, not a conversation
		self.as_user("dev")
		again = chat.ask("And NPA?", conversation=result["conversation"])
		self.assertEqual(again["conversation"], result["conversation"])
		self.assertNotEqual(again["message"], result["message"])
		frappe.set_user("Administrator")
		self.assertEqual(frappe.get_doc("Assistant Conversation", result["conversation"]).message_count, 2)

	def test_ask_validation(self):
		bad_calls = [
			dict(question=""),
			dict(question="   "),
			dict(question=None),
			dict(),  # no argument at all: a validation error, not a TypeError (M1-R2)
			dict(question="x" * 4001),
			dict(question="ok", depth="Fast"),
			dict(question="ok", route="r" * 501),
			dict(question="ok", deep=2),
		]
		before = self.counts()
		self.as_user("dev")
		for kwargs in bad_calls:
			with self.assertRaises(
				frappe.ValidationError, msg=str({k: str(v)[:20] for k, v in kwargs.items()})
			):
				chat.ask(**kwargs)
		frappe.set_user("Administrator")
		self.assertEqual(self.counts(), before, "rejected calls must not write")

		# the limits themselves are accepted
		self.as_user("dev")
		chat.ask("x" * 4000, route="r" * 500, depth="Business", deep="0")
		chat.ask("ok", depth="Both", deep=True)

	# --- per-user rate limit (DECISIONS #11)

	def test_rate_limit_per_user(self):
		self.configure(rate_limit_per_user=2, rate_limit_window_seconds=3600)
		self.as_user("dev")
		chat.ask("one")
		chat.ask("two")
		before = self.counts()
		with self.assertRaises(frappe.RateLimitExceededError):
			chat.ask("three")
		with self.assertRaises(frappe.RateLimitExceededError):
			chat.ask("four")

		# a different user is not affected: the limit is per user, not shared
		self.as_user("senior")
		self.assertEqual(chat.ask("senior one")["answer"], "The advisor has no API key yet.")
		frappe.set_user("Administrator")
		self.assertEqual(self.counts(), (before[0] + 1, before[1] + 1), "rate-limited calls write nothing")

	# --- ownership (G4, DECISIONS #21)

	def test_conversation_ownership(self):
		self.as_user("dev")
		mine = chat.ask("dev question")
		self.as_user("senior")
		with self.assertRaises(frappe.DoesNotExistError) as other:
			chat.ask("hijack", conversation=mine["conversation"])
		with self.assertRaises(frappe.DoesNotExistError) as fake:
			chat.ask("hijack", conversation=FAKE)
		self.assertEqual(error_text(other), error_text(fake))
		self.assertIn(NOT_FOUND, error_text(other))
		# the owner can still continue it
		self.as_user("dev")
		self.assertEqual(
			chat.ask("again", conversation=mine["conversation"])["conversation"], mine["conversation"]
		)
		frappe.set_user("Administrator")
		self.assertEqual(frappe.get_doc("Assistant Conversation", mine["conversation"]).message_count, 2)

	def test_sysmgr_cannot_use_others_conversation(self):
		"""A System Manager who is also an Assistant User reads every row but must not append to or rate
		somebody else's conversation (DECISIONS #21)."""
		self.create_sysmgr()
		self.as_user("dev")
		mine = chat.ask("dev question")
		frappe.set_user("Administrator")
		count_before = frappe.get_doc("Assistant Conversation", mine["conversation"]).message_count

		frappe.set_user("ast-test-sysmgr@example.com")
		# proof that the extra `user` filter is what protects it: plain permissions DO let this user read the row
		visible = frappe.get_list(
			"Assistant Conversation", filters={"name": mine["conversation"]}, pluck="name"
		)
		self.assertEqual(visible, [mine["conversation"]])

		with self.assertRaises(frappe.DoesNotExistError) as other:
			chat.ask("hijack", conversation=mine["conversation"])
		with self.assertRaises(frappe.DoesNotExistError) as fake:
			chat.ask("hijack", conversation=FAKE)
		self.assertEqual(error_text(other), error_text(fake))
		with self.assertRaises(frappe.DoesNotExistError) as rate_other:
			chat.feedback(mine["message"], "down", "not mine")
		with self.assertRaises(frappe.DoesNotExistError) as rate_fake:
			chat.feedback(FAKE, "down", "not mine")
		self.assertEqual(error_text(rate_other), error_text(rate_fake))
		self.assertIn(NOT_FOUND, error_text(rate_other))

		frappe.set_user("Administrator")
		self.assertEqual(
			frappe.get_doc("Assistant Conversation", mine["conversation"]).message_count, count_before
		)
		self.assertFalse(frappe.get_doc("Assistant Message", mine["message"]).feedback)

		# but their own conversations work
		frappe.set_user("ast-test-sysmgr@example.com")
		own = chat.ask("sysmgr question")
		self.assertEqual(chat.feedback(own["message"], "up")["feedback"], "up")

	def test_feedback_own_only(self):
		self.as_user("dev")
		mine = chat.ask("dev question")
		self.assertEqual(chat.feedback(mine["message"], "up", "helpful")["feedback"], "up")
		frappe.set_user("Administrator")
		message = frappe.get_doc("Assistant Message", mine["message"])
		self.assertEqual((message.feedback, message.feedback_comment), ("up", "helpful"))

		self.as_user("senior")
		with self.assertRaises(frappe.DoesNotExistError) as other:
			chat.feedback(mine["message"], "down", "not mine")
		with self.assertRaises(frappe.DoesNotExistError) as fake:
			chat.feedback(FAKE, "down")
		self.assertEqual(error_text(other), error_text(fake))
		self.assertIn(NOT_FOUND, error_text(other))

		self.as_user("dev")
		with self.assertRaises(frappe.ValidationError):
			chat.feedback(mine["message"], "meh")
		self.as_user("noaccess")
		with self.assertRaises(frappe.PermissionError):
			chat.feedback(mine["message"], "up")
		frappe.set_user("Administrator")
		message.reload()
		self.assertEqual((message.feedback, message.feedback_comment), ("up", "helpful"))

	def test_logs_visible_to_owner_only(self):
		self.as_user("dev")
		dev = chat.ask("dev question")
		self.as_user("senior")
		senior = chat.ask("senior question")

		def visible(doctype):
			return set(frappe.get_list(doctype, pluck="name", limit_page_length=0))

		self.as_user("dev")
		self.assertIn(dev["message"], visible("Assistant Message"))
		self.assertNotIn(senior["message"], visible("Assistant Message"))
		self.assertIn(dev["conversation"], visible("Assistant Conversation"))
		self.assertNotIn(senior["conversation"], visible("Assistant Conversation"))

		self.as_user("senior")
		self.assertIn(senior["message"], visible("Assistant Message"))
		self.assertNotIn(dev["message"], visible("Assistant Message"))
		self.assertNotIn(dev["conversation"], visible("Assistant Conversation"))

		# users who are not System Manager cannot write or delete the log by hand
		for who in ("dev", "senior"):
			self.as_user(who)
			self.assertFalse(frappe.has_permission("Assistant Message", "write"), who)
			self.assertFalse(frappe.has_permission("Assistant Message", "delete"), who)
			self.assertFalse(frappe.has_permission("Assistant Conversation", "create"), who)

		# System Manager (Administrator here) reads all
		frappe.set_user("Administrator")
		self.assertIn(dev["message"], visible("Assistant Message"))
		self.assertIn(senior["message"], visible("Assistant Message"))
