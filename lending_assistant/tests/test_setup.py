import json
from pathlib import Path

import frappe
from frappe.utils.password import set_encrypted_password

from lending_assistant import install
from lending_assistant.api import chat
from lending_assistant.assistant import settings as settings_module
from lending_assistant.tests.base import AssistantTestCase

ROLES = ["Assistant User", "Assistant Reviewer"]

# PLAN §4 with DECISIONS #13 (Loan Classification instead of Loan Classification Range)
EXPECTED_DOCTYPES = [
	"Loan",
	"Loan Product",
	"Loan Application",
	"Loan Disbursement",
	"Loan Repayment",
	"Loan Demand",
	"Loan Interest Accrual",
	"Loan Repayment Schedule",
	"Loan Restructure",
	"Loan Write Off",
	"Loan Security",
	"Loan Security Assignment",
	"Loan Security Shortfall",
	"Loan Freeze Log",
	"Loan NPA Log",
	"Days Past Due Log",
	"Loan Partner",
	"Loan Category",
	"Loan Classification",
	"Customer",
]
APP_DIR = Path(frappe.get_app_path("lending_assistant"))


class TestSetup(AssistantTestCase):
	def test_roles_fixture(self):
		for role in ROLES:
			self.assertEqual(frappe.db.get_value("Role", role, "desk_access"), 1, role)
			self.assertEqual(frappe.db.get_value("Role", role, "disabled"), 0, role)

		fixtures = frappe.get_hooks("fixtures", app_name="lending_assistant")
		self.assertEqual(len(fixtures), 1)
		self.assertEqual(fixtures[0]["dt"], "Role")
		self.assertEqual(fixtures[0]["filters"], [["name", "in", ROLES]])

		exported = json.loads((APP_DIR / "fixtures" / "role.json").read_text())
		self.assertEqual({d["doctype"] for d in exported}, {"Role"})
		self.assertEqual({d["name"] for d in exported}, set(ROLES))
		self.assertTrue(all(d["desk_access"] == 1 for d in exported))

	def test_settings_defaults(self):
		# the switches are off by default (field defaults), whatever the owner has set since
		meta = frappe.get_meta("Assistant Settings")
		for field in ("enabled", "live_data", "code_reader", "web_search"):
			self.assertEqual(str(meta.get_field(field).default), "0", field)
		for field, value in (("max_tokens", "16000"), ("default_effort", "high"), ("deep_effort", "medium"), ("rate_limit_per_user", "30"),
			("rate_limit_window_seconds", "3600"), ("retention_days", "180"),
			("default_model", "claude-sonnet-5-5"), ("deep_model", "claude-opus-5-5")):
			self.assertEqual(str(meta.get_field(field).default), value, field)

		# empty the tables, then seed
		settings = frappe.get_doc("Assistant Settings")
		settings.set("doctype_allowlist", [])
		settings.set("code_app_allowlist", [])
		settings.enabled = 1
		settings.save(ignore_permissions=True)

		result = install.seed_defaults()
		self.assertEqual(result["added_doctypes"], EXPECTED_DOCTYPES)
		self.assertEqual(result["skipped_missing_doctypes"], [])
		self.assertEqual(result["added_code_apps"], ["lending", "erpnext", "frappe"])

		settings = settings_module.get_settings()
		self.assertEqual([r.allowed_doctype for r in settings.doctype_allowlist], EXPECTED_DOCTYPES)
		self.assertEqual([r.app_name for r in settings.code_app_allowlist], ["lending", "erpnext", "frappe"])
		self.assertEqual(settings.enabled, 1, "seeding must not touch the switches")
		for name in EXPECTED_DOCTYPES:
			self.assertTrue(frappe.db.exists("DocType", name), name)

		# idempotent: a second run adds nothing and does not bump `modified`
		modified = frappe.get_doc("Assistant Settings").modified
		again = install.seed_defaults()
		self.assertEqual((again["added_doctypes"], again["added_code_apps"]), ([], []))
		self.assertEqual(frappe.get_doc("Assistant Settings").modified, modified)

		# keeps owner edits: with one row removed (non-empty table), seeding changes nothing
		settings = frappe.get_doc("Assistant Settings")
		settings.set("doctype_allowlist", settings.doctype_allowlist[:5])
		settings.save(ignore_permissions=True)
		install.seed_defaults()
		self.assertEqual(len(settings_module.get_settings().doctype_allowlist), 5)

	def test_seed_skips_missing_doctypes(self):
		settings = frappe.get_doc("Assistant Settings")
		settings.set("doctype_allowlist", [])
		settings.save(ignore_permissions=True)

		real_exists = frappe.db.exists

		def fake_exists(dt, *args, **kwargs):
			if dt == "DocType" and args and args[0] == "Loan Partner":
				return None
			return real_exists(dt, *args, **kwargs)

		from unittest.mock import patch

		with patch.object(frappe.db, "exists", side_effect=fake_exists):
			result = install.seed_defaults()
		self.assertEqual(result["skipped_missing_doctypes"], ["Loan Partner"])
		self.assertEqual(len(result["added_doctypes"]), 19)
		self.assertNotIn("Loan Partner", [r.allowed_doctype for r in frappe.get_doc("Assistant Settings").doctype_allowlist])

	def test_settings_not_readable(self):
		secret = "sk-ast-test-DUMMY-not-a-real-key"  # never a real key; rolled back with the class
		set_encrypted_password("Assistant Settings", "Assistant Settings", secret, "api_key")
		self.assertEqual(settings_module.get_api_key(), secret)

		for who in ("dev", "senior", "limited", "noaccess"):
			self.as_user(who)
			self.assertFalse(frappe.has_permission("Assistant Settings", "read"), who)
			self.assertFalse(frappe.has_permission("Assistant Settings", "write"), who)
			with self.assertRaises(frappe.PermissionError):
				frappe.get_doc("Assistant Settings").check_permission("read")

		self.as_user("dev")
		response = chat.ask("Where is the key?", route="Form/Loan/AST-X")
		self.assertNotIn(secret, json.dumps(response))
		message = frappe.get_doc("Assistant Message", response["message"])
		self.assertNotIn(secret, json.dumps(message.as_dict(), default=str))

		frappe.set_user("Administrator")
		self.assertTrue(frappe.has_permission("Assistant Settings", "read"))

	def test_only_two_whitelisted_methods(self):
		"""G7: only chat.ask and chat.feedback are whitelisted (findings.save comes in M6)."""
		found = []
		for path in APP_DIR.rglob("*.py"):
			if "tests" in path.relative_to(APP_DIR).parts:
				continue
			for line in path.read_text().splitlines():
				if line.strip().startswith("@frappe.whitelist"):
					found.append((path.relative_to(APP_DIR).as_posix(), line.strip()))
		self.assertEqual(
			sorted(found),
			[
				("api/chat.py", '@frappe.whitelist(methods=["POST"])'),
				("api/chat.py", '@frappe.whitelist(methods=["POST"])'),
			],
		)
		for fn in (chat.ask, chat.feedback):
			self.assertEqual(frappe.allowed_http_methods_for_whitelisted_func[fn], ["POST"])
			self.assertNotIn(fn, frappe.guest_methods)
