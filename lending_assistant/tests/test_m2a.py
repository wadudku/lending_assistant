"""M2a: verbatim audit, atomic counters, gate order, feedback gate, missing arguments, settings seeds."""

from unittest.mock import patch

import frappe

from lending_assistant import install
from lending_assistant.api import chat
from lending_assistant.assistant import audit, ratelimit
from lending_assistant.tests.base import TEST_IP, AssistantTestCase

XSS_QUESTION = '<img src=x onerror="alert(1)"><b>x</b>'
XSS_ROUTE = "Form/Loan/<script>alert(1)</script>"
XSS_ANSWER = '<p onclick="steal()">answer</p><script>1</script>'
XSS_COMMENT = '<svg onload="alert(1)">bad</svg>'


class TestVerbatimAudit(AssistantTestCase):
	def test_audit_verbatim(self):
		"""Every logged text field is stored byte-for-byte (DECISIONS #24, #28, #36)."""
		self.as_user("dev")
		padded = "  " + XSS_QUESTION + "\n  "  # stored exactly as received: no strip
		result = chat.ask(padded, route=XSS_ROUTE)

		# the answer and the JSON fields come from log_exchange (the orchestrator, M4)
		conversation = result["conversation"]
		json_fields = dict(
			roles=["Assistant User", "<b>role</b>"],
			tool_calls=[{"name": "t", "args": {"q": XSS_QUESTION}}],
			records_read=[{"doctype": "Loan", "name": XSS_ROUTE}],
			code_files_read=["<script>x</script>.py"],
			cards_used=[{"id": "<i>c</i>", "version": 1}],
			web_sources=["https://example.com/?a=<b>"],
		)
		message = audit.log_exchange(
			conversation, question=padded, answer=XSS_ANSWER, route=XSS_ROUTE, **json_fields
		)
		chat.feedback(message, "down", XSS_COMMENT)

		frappe.set_user("Administrator")
		stored = frappe.get_doc("Assistant Message", message)
		self.assertEqual(stored.question, padded)
		self.assertEqual(stored.answer, XSS_ANSWER)
		self.assertEqual(stored.route, XSS_ROUTE)
		self.assertEqual(stored.feedback_comment, XSS_COMMENT)
		for field, value in json_fields.items():
			expected = value if field != "roles" else sorted(value)
			self.assertEqual(frappe.parse_json(stored.get(field)), expected, field)

		first = frappe.get_doc("Assistant Message", result["message"])
		self.assertEqual(first.question, padded)
		self.assertEqual(first.route, XSS_ROUTE)
		self.assertEqual(frappe.get_doc("Assistant Conversation", conversation).first_route, XSS_ROUTE)

	def test_title_is_a_derived_label(self):
		"""The title is NOT verbatim: first 100 characters, tags removed, whitespace collapsed (#36a)."""
		self.assertEqual(audit.make_title(XSS_QUESTION), "x")
		self.assertEqual(audit.make_title("  What  is\n DPD? "), "What is DPD?")
		self.assertEqual(len(audit.make_title("a" * 500)), 100)
		self.assertEqual(audit.make_title("<img src=x onerror=1>"), "(no text)")
		self.assertEqual(audit.make_title(None), "(no text)")

		self.as_user("dev")
		result = chat.ask('<img src=x onerror="document.title=1">hello')
		frappe.set_user("Administrator")
		title = frappe.get_doc("Assistant Conversation", result["conversation"]).title
		self.assertEqual(title, "hello")
		self.assertNotIn("<", title)

	def test_code_fields_are_not_display_fields(self):
		"""The verbatim fields must not be list/filter/title/search fields (#36b)."""
		verbatim = {
			"Assistant Message": [
				"question",
				"answer",
				"route",
				"feedback_comment",
				"roles",
				"tool_calls",
				"records_read",
				"code_files_read",
				"cards_used",
				"web_sources",
			],
			"Assistant Conversation": ["first_route"],
		}
		for doctype, fields in verbatim.items():
			meta = frappe.get_meta(doctype)
			searchable = {meta.title_field, *(meta.search_fields or "").replace(" ", "").split(",")}
			for name in fields:
				df = meta.get_field(name)
				self.assertEqual(df.fieldtype, "Code", f"{doctype}.{name}")
				self.assertFalse(df.in_list_view or df.in_standard_filter, f"{doctype}.{name}")
				self.assertNotIn(name, searchable, f"{doctype}.{name}")


class TestCounters(AssistantTestCase):
	def test_rate_counter_has_ttl(self):
		key = ratelimit.key_for(ratelimit.USER_PREFIX, "ast-ttl-check", 60)
		frappe.cache.delete(key)
		self.addCleanup(frappe.cache.delete, key)

		self.assertEqual(ratelimit.hit(key, 60), 1)  # first call
		self.assertGreater(frappe.cache.ttl(key), 0)

		frappe.cache.delete(key)  # the key expires mid-window
		self.assertEqual(ratelimit.hit(key, 60), 1)
		self.assertGreater(frappe.cache.ttl(key), 0)

		# a key that somehow has no expiry (the M1 race) is healed by the next call
		frappe.cache.persist(key)
		self.assertEqual(frappe.cache.ttl(key), -1)
		self.assertEqual(ratelimit.hit(key, 60), 2)
		self.assertGreater(frappe.cache.ttl(key), 0)

	def test_ask_counters_always_have_ttl(self):
		self.configure(rate_limit_per_user=5, rate_limit_window_seconds=3600)
		frappe.local.request_ip = TEST_IP
		self.addCleanup(setattr, frappe.local, "request_ip", None)
		self.as_user("dev")
		chat.ask("one")
		chat.feedback(chat.ask("two")["message"], "up")
		for prefix, ident in (
			(ratelimit.USER_PREFIX, "ast-dev@example.com"),
			(ratelimit.FEEDBACK_PREFIX, "ast-dev@example.com"),
			(ratelimit.IP_PREFIX, TEST_IP),
		):
			self.assertGreater(frappe.cache.ttl(ratelimit.key_for(prefix, ident, 3600)), 0, prefix)

	def test_ip_limit_after_role(self):
		"""Users without the role don't use up the IP quota (M1-R1, DECISIONS #27)."""
		frappe.local.request_ip = TEST_IP
		self.addCleanup(setattr, frappe.local, "request_ip", None)
		with patch.object(chat, "IP_LIMIT", 2):
			self.as_user("noaccess")
			for _ in range(10):
				with self.assertRaises(frappe.PermissionError):
					chat.ask("burst")
			self.assertFalse(
				frappe.cache.get(ratelimit.key_for(ratelimit.IP_PREFIX, TEST_IP, chat.IP_WINDOW))
			)

			self.as_user("dev")
			chat.ask("first")
			chat.ask("second")
			before = self.count("Assistant Message")
			with self.assertRaises(frappe.RateLimitExceededError):
				chat.ask("third")
			self.assertEqual(self.count("Assistant Message"), before, "an IP-limited call writes nothing")

	def test_ip_limit_after_enabled_and_user_limit(self):
		"""Gate order: role -> enabled -> per-user -> IP. A disabled assistant doesn't touch the IP counter."""
		frappe.local.request_ip = TEST_IP
		self.addCleanup(setattr, frappe.local, "request_ip", None)
		self.configure(enabled=0)
		self.as_user("dev")
		with self.assertRaises(frappe.PermissionError):
			chat.ask("off")
		self.assertFalse(frappe.cache.get(ratelimit.key_for(ratelimit.IP_PREFIX, TEST_IP, chat.IP_WINDOW)))


class TestFeedbackGate(AssistantTestCase):
	def make_message(self):
		self.as_user("dev")
		return chat.ask("to rate")["message"]

	def test_feedback_gate(self):
		message = self.make_message()

		# no role
		self.as_user("noaccess")
		with self.assertRaises(frappe.PermissionError):
			chat.feedback(message, "up")

		# disabled
		self.configure(enabled=0)
		self.as_user("dev")
		with self.assertRaises(frappe.PermissionError) as ctx:
			chat.feedback(message, "up")
		self.assertIn("turned off", str(ctx.exception))
		frappe.set_user("Administrator")
		self.assertFalse(frappe.get_doc("Assistant Message", message).feedback)
		self.configure(enabled=1)

		# own bucket: the ask limit and the feedback limit are separate
		self.configure(rate_limit_per_user=2)  # make_message used one ask
		self.as_user("dev")
		with patch.object(chat, "FEEDBACK_LIMIT", 2):
			self.assertEqual(chat.feedback(message, "up")["feedback"], "up")
			self.assertEqual(chat.feedback(message, "down", "why")["feedback"], "down")
			with self.assertRaises(frappe.RateLimitExceededError):
				chat.feedback(message, "up")
		chat.ask("still allowed: asks have their own bucket")

		frappe.set_user("Administrator")
		self.assertEqual(frappe.get_doc("Assistant Message", message).feedback, "down")

	def test_feedback_ownership_still_checked(self):
		message = self.make_message()
		self.as_user("senior")
		with self.assertRaises(frappe.DoesNotExistError):
			chat.feedback(message, "up")


class TestMissingArguments(AssistantTestCase):
	def test_missing_args(self):
		before = self.count("Assistant Message")
		self.as_user("dev")
		with self.assertRaises(frappe.ValidationError) as ctx:
			chat.ask()
		self.assertIn("Please type a question", str(ctx.exception))
		for kwargs in ({}, {"message": "x"}, {"value": "up"}, {"message": None, "value": None}):
			with self.assertRaises(frappe.ValidationError, msg=str(kwargs)):
				chat.feedback(**kwargs)
		with self.assertRaises(frappe.ValidationError):
			chat.feedback("x", "up", comment=["not text"])
		frappe.set_user("Administrator")
		self.assertEqual(self.count("Assistant Message"), before)


class TestSettingsSeeds(AssistantTestCase):
	def test_settings_effort_and_tokens(self):
		settings = frappe.get_doc("Assistant Settings")
		settings.default_effort = ""
		settings.deep_effort = ""
		settings.save(ignore_permissions=True)
		result = install.seed_defaults()
		self.assertEqual(result["set_effort"], ["default_effort", "deep_effort"])
		settings = frappe.get_doc("Assistant Settings")
		self.assertEqual((settings.default_effort, settings.deep_effort), ("medium", "medium"))

		# an owner's choice is kept
		settings.default_effort = "max"
		settings.save(ignore_permissions=True)
		install.seed_defaults()
		self.assertEqual(frappe.get_doc("Assistant Settings").default_effort, "max")

		# max_tokens: only an untouched 4096 is raised
		settings = frappe.get_doc("Assistant Settings")
		settings.max_tokens = 4096
		settings.save(ignore_permissions=True)
		self.assertTrue(install.raise_max_tokens_default())
		self.assertEqual(frappe.get_doc("Assistant Settings").max_tokens, 16000)

		for owner_value in (8000, 16000, 4097, 32000):
			settings = frappe.get_doc("Assistant Settings")
			settings.max_tokens = owner_value
			settings.save(ignore_permissions=True)
			self.assertFalse(install.raise_max_tokens_default())
			self.assertEqual(frappe.get_doc("Assistant Settings").max_tokens, owner_value)

		meta = frappe.get_meta("Assistant Settings")
		self.assertEqual(
			meta.get_field("default_effort").options.split("\n"), ["low", "medium", "high", "xhigh", "max"]
		)
		self.assertEqual(
			meta.get_field("deep_effort").options.split("\n"), ["low", "medium", "high", "xhigh", "max"]
		)

	def test_never_send_seed(self):
		self.assertEqual(len(install.DEFAULT_NEVER_SEND), 15)
		settings = frappe.get_doc("Assistant Settings")
		settings.set("never_send_fields", [])
		settings.save(ignore_permissions=True)

		result = install.seed_defaults()
		self.assertEqual(len(result["added_never_send"]) + len(result["skipped_never_send"]), 15)
		self.assertEqual(
			result["skipped_never_send"], [], "every field in #33 exists on 16.5.1 / erpnext 16.35"
		)
		rows = [(r.ref_doctype, r.fieldname) for r in frappe.get_doc("Assistant Settings").never_send_fields]
		self.assertEqual(rows, install.DEFAULT_NEVER_SEND)

		# a second run changes nothing
		modified = frappe.get_doc("Assistant Settings").modified
		again = install.seed_defaults()
		self.assertEqual((again["added_never_send"], again["skipped_never_send"]), ([], []))
		self.assertEqual(frappe.get_doc("Assistant Settings").modified, modified)

		# an owner edit is kept (one row removed, one added: no re-seed)
		settings = frappe.get_doc("Assistant Settings")
		settings.set("never_send_fields", settings.never_send_fields[:3])
		settings.append("never_send_fields", {"ref_doctype": "Loan", "fieldname": "loan_amount"})
		settings.save(ignore_permissions=True)
		install.seed_defaults()
		rows = [(r.ref_doctype, r.fieldname) for r in frappe.get_doc("Assistant Settings").never_send_fields]
		self.assertEqual(rows, [*install.DEFAULT_NEVER_SEND[:3], ("Loan", "loan_amount")])

	def test_never_send_skips_missing(self):
		settings = frappe.get_doc("Assistant Settings")
		settings.set("never_send_fields", [])
		settings.save(ignore_permissions=True)

		def fake_field_exists(doctype, fieldname):
			return (doctype, fieldname) not in {("Customer", "gender"), ("Sales Team", "contact_no")}

		with patch.object(install, "_field_exists", side_effect=fake_field_exists):
			result = install.seed_defaults()
		self.assertEqual(result["skipped_never_send"], ["Customer.gender", "Sales Team.contact_no"])
		self.assertEqual(len(result["added_never_send"]), 13)
