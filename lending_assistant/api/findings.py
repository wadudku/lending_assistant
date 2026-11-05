"""The findings endpoint (G7, G13). The third and last whitelisted method in the app: `save`.

POST only, never `allow_guest`, same gate as `feedback` (role -> enabled -> per-user limit in its own bucket ->
validation -> ownership). A finding exists only after a user's click; its provenance comes from the stored message.
"""

import frappe
from frappe import _

from lending_assistant.api import gate
from lending_assistant.assistant import audit, finding_rules, findings, ratelimit

SAVE_LIMIT = 20  # per user per window (own bucket)
DEFAULT_WINDOW = 3600
MAX_TITLE = 140
MAX_SUMMARY = 4000


@frappe.whitelist(methods=["POST"])
def save(message=None, title=None, summary=None):
	gate.require_assistant_user()
	settings = gate.require_enabled()
	window = int(settings.rate_limit_window_seconds or 0) or DEFAULT_WINDOW
	gate.too_many(ratelimit.exceeded(ratelimit.FINDING_PREFIX, frappe.session.user, SAVE_LIMIT, window))

	if not message or not isinstance(message, str):
		frappe.throw(_("Please say which answer to save."))
	title = _text(title, MAX_TITLE, _("The title"))
	summary = _text(summary, MAX_SUMMARY, _("The summary"))

	message = gate.own_record(audit.MESSAGE, message)
	return findings.create_from_message(message, title, summary, finding_rules.installed_lending_version())


def _text(value, limit: int, what):
	"""None (use the stored text) or the stripped text, 1..limit characters."""
	if value is None:
		return None
	if not isinstance(value, str) or not value.strip():
		frappe.throw(_("{0} must be text.").format(what))
	value = value.strip()
	if len(value) > limit:
		frappe.throw(_("{0} is too long (maximum {1} characters).").format(what, limit))
	return value
