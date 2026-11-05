"""The gate steps shared by every whitelisted endpoint (G7, DECISIONS #27, #28; M6 D9). Moved out of `api/chat.py` with no
change in behaviour, so `ask`, `feedback` and `findings.save` call the same functions. Nothing here is whitelisted.
"""

import frappe
from frappe import _

from lending_assistant.assistant.settings import get_settings

ASSISTANT_USER = "Assistant User"
NOT_FOUND = "I can't find a record with that ID that you have access to."  # G4 wording


def require_assistant_user():
	if ASSISTANT_USER not in frappe.get_roles():
		frappe.throw(
			_("You need the {0} role to use the assistant.").format(ASSISTANT_USER), frappe.PermissionError
		)


def require_enabled():
	settings = get_settings()
	if not settings.enabled:
		frappe.throw(_("The assistant is turned off."), frappe.PermissionError)
	return settings


def too_many(over: bool) -> None:
	if over:
		frappe.throw(
			_("You have asked too many questions for now. Please try again later."),
			frappe.RateLimitExceededError,
		)


def own_record(doctype: str, name) -> str:
	"""Return `name` if the session user owns it; otherwise the same G4 reply as for a missing record.

	`frappe.get_list` applies the doctype permissions as the session user. The extra `user` filter keeps
	a System Manager (who can read every row) from continuing, rating or saving from somebody else's conversation.
	"""
	rows = []
	if isinstance(name, str) and name:
		rows = frappe.get_list(  # AST-ALLOWED: own-record ownership check, runs as the session user
			doctype,
			filters={"name": name, "user": frappe.session.user},
			pluck="name",
			limit=1,
		)
	if not rows:
		frappe.throw(_(NOT_FOUND), frappe.DoesNotExistError)
	return rows[0]
