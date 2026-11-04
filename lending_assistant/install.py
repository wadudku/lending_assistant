"""Install-time seeding (DECISIONS #19).

`seed_defaults()` is called from `after_install` (fresh sites) and from a `post_model_sync` patch
(sites where the app is already installed). It only fills empty tables and never overwrites edits.
It touches Assistant Settings only.
"""

import frappe

# PLAN §4 default allowlist, with Loan Classification instead of Loan Classification Range (DECISIONS #13).
DEFAULT_DOCTYPES = [
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
DEFAULT_CODE_APPS = ["lending", "erpnext", "frappe"]


def _doctype_exists(name: str) -> bool:
	return bool(frappe.db.exists("DocType", name))


def after_install():
	seed_defaults()


def seed_defaults() -> dict:
	"""Fill empty allowlists in Assistant Settings. Returns what it added and what it skipped."""
	settings = frappe.get_doc("Assistant Settings")  # AST-ALLOWED: install seed
	result = {"added_doctypes": [], "skipped_missing_doctypes": [], "added_code_apps": []}

	if not settings.doctype_allowlist:
		for name in DEFAULT_DOCTYPES:
			if _doctype_exists(name):
				settings.append("doctype_allowlist", {"allowed_doctype": name})
				result["added_doctypes"].append(name)
			else:
				result["skipped_missing_doctypes"].append(name)

	if not settings.code_app_allowlist:
		for app in DEFAULT_CODE_APPS:
			settings.append("code_app_allowlist", {"app_name": app})
			result["added_code_apps"].append(app)

	if result["added_doctypes"] or result["added_code_apps"]:
		settings.save(ignore_permissions=True)  # AST-ALLOWED: install seed
	return result
