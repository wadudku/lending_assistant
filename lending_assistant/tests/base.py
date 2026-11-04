"""Shared test fixtures for lending_assistant.

`frappe.set_user` is allowed in tests/ only (WORKER guardrail table). Everything the tests write is rolled
back at the end of the class by IntegrationTestCase, so nothing here may call frappe.db.commit(). Redis state
(the per-user rate-limit counters, role caches) is not rolled back, so it is cleaned explicitly.
"""

import frappe
from frappe.tests import IntegrationTestCase

from lending_assistant.api import chat

PERSONAS = {
	"senior": "ast-senior@example.com",
	"dev": "ast-dev@example.com",
	"limited": "ast-limited@example.com",
	"noaccess": "ast-noaccess@example.com",
}
SYSMGR = "ast-test-sysmgr@example.com"  # created per test class: System Manager + Assistant User

SETTINGS_FIELDS = (
	"enabled",
	"live_data",
	"code_reader",
	"web_search",
	"default_model",
	"deep_model",
	"max_tokens",
	"rate_limit_per_user",
	"rate_limit_window_seconds",
	"retention_days",
)


class AssistantTestCase(IntegrationTestCase):
	@classmethod
	def setUpClass(cls):
		super().setUpClass()
		for email in PERSONAS.values():
			if not frappe.db.exists("User", email):
				raise AssertionError(f"Persona {email} is missing: run tools/m0_setup_personas.py (M0/M1).")

	def setUp(self):
		super().setUp()
		frappe.set_user("Administrator")
		self._original = {f: frappe.get_doc("Assistant Settings").get(f) for f in SETTINGS_FIELDS}
		self.configure(enabled=1)
		self.clear_rate_limits()

	def tearDown(self):
		frappe.set_user("Administrator")
		self.configure(**self._original)
		self.clear_rate_limits()
		super().tearDown()

	# --- helpers

	def configure(self, **values):
		"""Change Assistant Settings (as Administrator, in the test transaction)."""
		user = frappe.session.user
		frappe.set_user("Administrator")
		try:
			settings = frappe.get_doc("Assistant Settings")
			settings.update(values)
			settings.save(ignore_permissions=True)
		finally:
			frappe.set_user(user)

	def clear_rate_limits(self):
		for email in [*PERSONAS.values(), SYSMGR]:
			for window in (3600, 60, 10):
				frappe.cache.delete(chat._rate_key(email, window))

	def as_user(self, who):
		frappe.set_user(PERSONAS.get(who, who))

	def create_sysmgr(self):
		"""A user who is System Manager AND Assistant User: can read every log row (DECISIONS #21)."""
		if not frappe.db.exists("User", SYSMGR):
			frappe.get_doc(
				{
					"doctype": "User",
					"email": SYSMGR,
					"first_name": "AST SysMgr",
					"send_welcome_email": 0,
					"roles": [{"role": "System Manager"}, {"role": "Assistant User"}],
				}
			).insert(ignore_permissions=True)
		frappe.clear_cache(user=SYSMGR)

	def count(self, doctype, **filters):
		"""Row count as Administrator, for before/after comparisons (never assume an empty site)."""
		return len(frappe.get_all(doctype, filters=filters, pluck="name", limit_page_length=0))
