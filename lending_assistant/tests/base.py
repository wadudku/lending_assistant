"""Shared test fixtures for lending_assistant.

`frappe.set_user` is allowed in tests/ only (WORKER guardrail table). Everything the tests write is rolled
back at the end of the class by IntegrationTestCase, so nothing here may call frappe.db.commit(). Redis state
(the per-user rate-limit counters, role caches) is not rolled back, so it is cleaned explicitly.
"""

import frappe
from frappe.tests import IntegrationTestCase

from lending_assistant.assistant import ratelimit

PERSONAS = {
	"senior": "ast-senior@example.com",
	"dev": "ast-dev@example.com",
	"limited": "ast-limited@example.com",
	"noaccess": "ast-noaccess@example.com",
}
TEST_IP = "10.9.9.9"
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
		for window in (3600, 60, 10):
			for email in [*PERSONAS.values(), SYSMGR]:
				for prefix in (ratelimit.USER_PREFIX, ratelimit.FEEDBACK_PREFIX):
					frappe.cache.delete(ratelimit.key_for(prefix, email, window))
			# the IP layer counts every accepted call: tests run without a request, so the IP is "unknown"
			for ip in ("unknown", TEST_IP):
				frappe.cache.delete(ratelimit.key_for(ratelimit.IP_PREFIX, ip, window))

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


class GuardTestCase(AssistantTestCase):
	"""For the M2b guard tests: Live data and Code reader on, and the Settings tables put back afterwards.

	Settings is cached in Redis and Redis is not rolled back, so any change to a table has to be undone by
	saving again, not just by the class-level rollback.
	"""

	TABLES = ("doctype_allowlist", "code_app_allowlist", "never_send_fields")

	def setUp(self):
		super().setUp()
		settings = frappe.get_doc("Assistant Settings")
		self._tables = {t: [row.as_dict(no_nulls=True) for row in settings.get(t)] for t in self.TABLES}
		self.configure(live_data=1, code_reader=1)
		self._property_setters = []

	def tearDown(self):
		frappe.set_user("Administrator")
		for name, doctype in self._property_setters:
			frappe.db.delete("Property Setter", {"name": name})
			frappe.clear_cache(doctype=doctype)
		settings = frappe.get_doc("Assistant Settings")
		for table, rows in self._tables.items():
			settings.set(table, [])
			for row in rows:
				settings.append(table, {k: v for k, v in row.items() if k not in ("name", "parent", "parentfield", "parenttype", "idx", "doctype", "creation", "modified", "modified_by", "owner", "docstatus")})
		settings.save(ignore_permissions=True)
		super().tearDown()

	def add_never_send(self, doctype, fieldname):
		settings = frappe.get_doc("Assistant Settings")
		settings.append("never_send_fields", {"ref_doctype": doctype, "fieldname": fieldname})
		settings.save(ignore_permissions=True)

	def allow_doctype(self, doctype):
		settings = frappe.get_doc("Assistant Settings")
		settings.append("doctype_allowlist", {"allowed_doctype": doctype})
		settings.save(ignore_permissions=True)

	def set_permlevel(self, doctype, fieldname, level=1):
		"""Temporary permlevel on one field (a Property Setter made here, removed in tearDown; DECISIONS #10)."""
		frappe.make_property_setter(
			{"doctype": doctype, "fieldname": fieldname, "property": "permlevel", "value": level, "property_type": "Int"},
			validate_fields_for_doctype=False,
		)
		name = frappe.db.get_value("Property Setter", {"doc_type": doctype, "field_name": fieldname, "property": "permlevel"})
		self._property_setters.append((name, doctype))
		frappe.clear_cache(doctype=doctype)

	def loan_names(self):
		"""(visible-to-limited, hidden-from-limited) loan names, found as Administrator."""
		visible = frappe.get_all("Loan", filters={"loan_product": "PL-EMI"}, pluck="name", limit=1)
		hidden = frappe.get_all("Loan", filters={"loan_product": ["!=", "PL-EMI"]}, pluck="name", limit=1)
		if not visible or not hidden:
			raise AssertionError("The site needs a PL-EMI loan and a non-PL-EMI loan for the boundary tests.")
		return visible[0], hidden[0]
