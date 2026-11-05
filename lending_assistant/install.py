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

# DECISIONS #33 (approved by the owner): personal contact, identity and banking fields that never go to the
# model. The guard drops Password fields on top of this list (M2b). 15 fields.
DEFAULT_NEVER_SEND = [
	("Customer", "mobile_no"),
	("Customer", "email_id"),
	("Customer", "tax_id"),
	("Customer", "primary_address"),
	("Customer", "image"),
	("Customer", "gender"),
	("Sales Team", "contact_no"),
	("Loan Application", "applicant_email_address"),
	("Loan Application", "applicant_phone_number"),
	("Loan Application", "address_line_1"),
	("Loan Application", "address_line_2"),
	("Loan Co-Applicants", "applicant_email"),
	("Loan Co-Applicants", "applicant_mobile"),
	("Loan Disbursement", "bank_account"),
	("Loan Repayment", "bank_account"),
]
DEFAULT_EFFORT = "medium"  # DECISIONS #145 (was high in #31): default model (Sonnet 5.5)
OLD_DEFAULT_EFFORT = "high"  # the value #31 seeded; only this is changed by the #145 patch
DEEP_EFFORT = "medium"  # DECISIONS #31: Deep analysis model (Opus 5.5)
OLD_MAX_TOKENS = 4096
NEW_MAX_TOKENS = 16000  # DECISIONS #32


def _doctype_exists(name: str) -> bool:
	return bool(frappe.db.exists("DocType", name))  # AST-ALLOWED: install seed, meta check


def _field_exists(doctype: str, fieldname: str) -> bool:
	return _doctype_exists(
		doctype
	) and frappe.get_meta(  # AST-ALLOWED: install seed, meta check (has_field returns a bool)
		doctype
	).has_field(fieldname)


def after_install():
	seed_defaults()


def seed_defaults() -> dict:
	"""Fill empty allowlists in Assistant Settings. Returns what it added and what it skipped."""
	settings = frappe.get_doc("Assistant Settings")  # AST-ALLOWED: install seed
	result = {
		"added_doctypes": [],
		"skipped_missing_doctypes": [],
		"added_code_apps": [],
		"added_never_send": [],
		"skipped_never_send": [],
		"set_effort": [],
	}

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

	if not settings.never_send_fields:
		for doctype, fieldname in DEFAULT_NEVER_SEND:
			if _field_exists(doctype, fieldname):
				settings.append("never_send_fields", {"ref_doctype": doctype, "fieldname": fieldname})
				result["added_never_send"].append(f"{doctype}.{fieldname}")
			else:
				result["skipped_never_send"].append(f"{doctype}.{fieldname}")

	for fieldname, value in (("default_effort", DEFAULT_EFFORT), ("deep_effort", DEEP_EFFORT)):
		if not settings.get(fieldname):
			settings.set(fieldname, value)
			result["set_effort"].append(fieldname)

	if any(result[k] for k in ("added_doctypes", "added_code_apps", "added_never_send", "set_effort")):
		settings.save(ignore_permissions=True)  # AST-ALLOWED: install seed
	return result


def raise_max_tokens_default() -> bool:
	"""DECISIONS #32: 4096 -> 16000, but only while the stored value is still exactly 4096 (an owner edit stays)."""
	settings = frappe.get_doc("Assistant Settings")  # AST-ALLOWED: install seed
	if settings.max_tokens != OLD_MAX_TOKENS:
		return False
	settings.max_tokens = NEW_MAX_TOKENS
	settings.save(ignore_permissions=True)  # AST-ALLOWED: install seed
	return True


def lower_default_effort() -> bool:
	"""DECISIONS #145: default_effort high -> medium, but only while the stored value is still the seeded `high` (an owner
	edit, including a later choice of `high` after the patch has run once, is not touched by any other value)."""
	settings = frappe.get_doc("Assistant Settings")  # AST-ALLOWED: install seed
	if settings.default_effort != OLD_DEFAULT_EFFORT:
		return False
	settings.default_effort = DEFAULT_EFFORT
	settings.save(ignore_permissions=True)  # AST-ALLOWED: install seed
	return True
