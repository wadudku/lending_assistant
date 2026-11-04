"""Chat endpoints (G7). The only whitelisted methods in the app: `ask` and `feedback` (`findings.save` comes in M6).

Both are POST-only, never `allow_guest`, require the role Assistant User, and read Assistant Settings
only through `assistant.settings`. In M1 `ask` returns a stub reply: no Claude call, no tools.
"""

import time

import frappe
from frappe import _
from frappe.rate_limiter import rate_limit

from lending_assistant.assistant import audit
from lending_assistant.assistant.settings import get_settings

ASSISTANT_USER = "Assistant User"
STUB_ANSWER = "Stub reply: the advisor isn't connected yet."
NOT_FOUND = "I can't find a record with that ID that you have access to."  # G4 wording
STUB_MODEL = "stub"

MAX_QUESTION = 4000
MAX_ROUTE = 500
MAX_COMMENT = 1000
DEPTHS = ("Business", "Technical", "Both")
FEEDBACK_VALUES = ("up", "down")
DEFAULT_LIMIT = 30
DEFAULT_WINDOW = 3600


@frappe.whitelist(methods=["POST"])
@rate_limit(limit=120, seconds=3600, methods=["POST"])  # outer, IP-based layer (DECISIONS #11)
def ask(question, conversation=None, route=None, depth="Both", deep=0):
	started = time.monotonic()

	_require_assistant_user()

	settings = get_settings()
	if not settings.enabled:
		frappe.throw(_("The assistant is turned off."), frappe.PermissionError)

	_check_user_rate_limit(settings)

	question, route, depth, deep = _validate(question, route, depth, deep)

	if conversation:
		conversation = _own_record(audit.CONVERSATION, conversation)
	else:
		conversation = audit.start_conversation(route, title=question)

	route_doctype, route_docname = _split_route(route)
	message = audit.log_exchange(
		conversation,
		question=question,
		answer=STUB_ANSWER,
		route=route,
		route_doctype=route_doctype,
		route_docname=route_docname,
		depth=depth,
		deep=deep,
		status="ok",
		model=STUB_MODEL,
		roles=frappe.get_roles(),
		latency_ms=int((time.monotonic() - started) * 1000),
	)
	return {"conversation": conversation, "message": message, "answer": STUB_ANSWER}


@frappe.whitelist(methods=["POST"])
def feedback(message, value, comment=None):
	_require_assistant_user()

	if value not in FEEDBACK_VALUES:
		frappe.throw(_("Feedback must be 'up' or 'down'."))
	comment = (comment or "").strip()
	if len(comment) > MAX_COMMENT:
		frappe.throw(_("The comment is too long (maximum {0} characters).").format(MAX_COMMENT))

	message = _own_record(audit.MESSAGE, message)
	audit.set_feedback(message, value, comment)
	return {"message": message, "feedback": value}


# --- helpers -------------------------------------------------------------------------------------


def _require_assistant_user():
	if ASSISTANT_USER not in frappe.get_roles():
		frappe.throw(_("You need the {0} role to use the assistant.").format(ASSISTANT_USER), frappe.PermissionError)


def _rate_key(user: str, window: int) -> str:
	return frappe.cache.make_key(f"ast:rl:{user}:{window}")


def _check_user_rate_limit(settings) -> None:
	"""Per-user counter (DECISIONS #11). The stock `rate_limit` keys on IP, never on the user."""
	limit = int(settings.rate_limit_per_user or 0) or DEFAULT_LIMIT
	window = int(settings.rate_limit_window_seconds or 0) or DEFAULT_WINDOW
	key = _rate_key(frappe.session.user, window)

	if not frappe.cache.get(key):
		frappe.cache.setex(key, window, 0)
	if frappe.cache.incrby(key, 1) > limit:
		frappe.throw(
			_("You have asked too many questions for now. Please try again later."),
			frappe.RateLimitExceededError,
		)


def _validate(question, route, depth, deep):
	if not isinstance(question, str) or not question.strip():
		frappe.throw(_("Please type a question."))
	question = question.strip()
	if len(question) > MAX_QUESTION:
		frappe.throw(_("The question is too long (maximum {0} characters).").format(MAX_QUESTION))

	route = route if route is not None else ""
	if not isinstance(route, str) or len(route) > MAX_ROUTE:
		frappe.throw(_("The route is too long (maximum {0} characters).").format(MAX_ROUTE))

	if depth not in DEPTHS:
		frappe.throw(_("Depth must be one of: {0}.").format(", ".join(DEPTHS)))

	if isinstance(deep, bool):
		deep = int(deep)
	if deep in ("0", "1"):
		deep = int(deep)
	if deep not in (0, 1):
		frappe.throw(_("Deep must be 0 or 1."))

	return question, route, depth, deep


def _own_record(doctype: str, name) -> str:
	"""Return `name` if the session user owns it; otherwise the same G4 reply as for a missing record.

	`frappe.get_list` applies the doctype permissions as the session user. The extra `user` filter keeps
	a System Manager (who can read every row) from continuing or rating somebody else's conversation.
	"""
	rows = []
	if isinstance(name, str) and name:
		rows = frappe.get_list(
			doctype,
			filters={"name": name, "user": frappe.session.user},
			pluck="name",
			limit_page_length=1,
		)
	if not rows:
		frappe.throw(_(NOT_FOUND), frappe.DoesNotExistError)
	return rows[0]


def _split_route(route: str):
	"""Desk routes look like 'Form/Loan/LOAN-0001' or 'List/Loan/List'; return (doctype, docname)."""
	parts = [p for p in (route or "").strip("/").split("/") if p]
	if len(parts) >= 3 and parts[0].lower() == "form":
		return parts[1], "/".join(parts[2:])
	if len(parts) >= 2 and parts[0].lower() in ("list", "report", "query-report"):
		return parts[1], ""
	return "", ""
