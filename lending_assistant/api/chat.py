"""Chat endpoints (G7). The only whitelisted methods in the app: `ask` and `feedback` (`findings.save` comes in M6).

Both are POST-only, never `allow_guest`, require the role Assistant User, and read Assistant Settings
only through `assistant.settings`. `ask` hands the question to `orchestrator.run` (M4b); with no API key set it answers
"The advisor has no API key yet." (status error, no network). The audit row is written on every path.
"""

import time

import frappe
from frappe import _

from lending_assistant.assistant import audit, orchestrator, ratelimit
from lending_assistant.assistant.settings import get_settings

ASSISTANT_USER = "Assistant User"
NOT_FOUND = "I can't find a record with that ID that you have access to."  # G4 wording
HISTORY_TURNS = 4  # earlier exchanges of the same conversation that the model sees (as plain text)

MAX_QUESTION = 4000
MAX_ROUTE = 500
MAX_COMMENT = 1000
DEPTHS = ("Business", "Technical", "Both")
FEEDBACK_VALUES = ("up", "down")
DEFAULT_LIMIT = 30
DEFAULT_WINDOW = 3600
IP_LIMIT = (
	120  # ask, per client IP per IP_WINDOW. Module constants on purpose (DECISIONS #36); tests patch them
)
IP_WINDOW = 3600
FEEDBACK_LIMIT = 60  # feedback, per user per window (own bucket, DECISIONS #28)


@frappe.whitelist(methods=["POST"])
def ask(question=None, conversation=None, route=None, depth="Both", deep=0):
	"""Gate order (G7, DECISIONS #27): login (Frappe) -> role -> enabled -> per-user limit -> IP limit
	-> validation -> ownership. Arguments default to None so a missing one is a validation error, not a 500."""
	started = time.monotonic()

	_require_assistant_user()
	settings = _require_enabled()
	_check_user_rate_limit(settings)
	_check_ip_rate_limit()

	question, route, depth, deep = _validate(question, route, depth, deep)

	history = []
	if conversation:
		conversation = _own_record(audit.CONVERSATION, conversation)
		history = _history(conversation)
	else:
		conversation = audit.start_conversation(
			route, title=question
		)  # title is a derived label, see audit.make_title

	route_doctype, route_docname = _split_route(route)
	outcome = orchestrator.run(
		question,
		route_doctype=route_doctype,
		route_docname=route_docname,
		depth=depth,
		deep=deep,
		history=history,
	)
	message = audit.log_exchange(
		conversation,
		question=question,
		answer=outcome["answer"],
		route=route,
		route_doctype=route_doctype,
		route_docname=route_docname,
		depth=depth,
		deep=deep,
		status=outcome["status"],
		model=outcome["model"],
		roles=frappe.get_roles(),
		tokens_in=outcome["tokens_in"],
		tokens_out=outcome["tokens_out"],
		latency_ms=int((time.monotonic() - started) * 1000),
		tool_calls=outcome["tool_calls"],
		records_read=outcome["records_read"],
		code_files_read=outcome["code_files_read"],
		cards_used=outcome["cards_used"],
		web_sources=outcome["web_sources"],
	)
	return {
		"conversation": conversation,
		"message": message,
		"answer": outcome["answer"],
		"status": outcome["status"],
	}


@frappe.whitelist(methods=["POST"])
def feedback(message=None, value=None, comment=None):
	"""Same gate as `ask` (DECISIONS #28): role -> enabled -> per-user limit (own bucket) -> validation -> ownership."""
	_require_assistant_user()
	settings = _require_enabled()
	window = int(settings.rate_limit_window_seconds or 0) or DEFAULT_WINDOW
	_too_many(ratelimit.exceeded(ratelimit.FEEDBACK_PREFIX, frappe.session.user, FEEDBACK_LIMIT, window))

	if not message or not isinstance(message, str):
		frappe.throw(_("Please say which message the feedback is for."))
	if value not in FEEDBACK_VALUES:
		frappe.throw(_("Feedback must be 'up' or 'down'."))
	if comment is not None and not isinstance(comment, str):
		frappe.throw(_("The comment must be text."))
	comment = comment or ""  # stored exactly as received (DECISIONS #24); only the length is checked
	if len(comment) > MAX_COMMENT:
		frappe.throw(_("The comment is too long (maximum {0} characters).").format(MAX_COMMENT))

	message = _own_record(audit.MESSAGE, message)
	audit.set_feedback(message, value, comment)
	return {"message": message, "feedback": value}


# --- helpers -------------------------------------------------------------------------------------


def _require_assistant_user():
	if ASSISTANT_USER not in frappe.get_roles():
		frappe.throw(
			_("You need the {0} role to use the assistant.").format(ASSISTANT_USER), frappe.PermissionError
		)


def _require_enabled():
	settings = get_settings()
	if not settings.enabled:
		frappe.throw(_("The assistant is turned off."), frappe.PermissionError)
	return settings


def _too_many(over: bool) -> None:
	if over:
		frappe.throw(
			_("You have asked too many questions for now. Please try again later."),
			frappe.RateLimitExceededError,
		)


def _check_user_rate_limit(settings) -> None:
	"""Per-user counter (DECISIONS #11). Atomic, see ratelimit.py."""
	limit = int(settings.rate_limit_per_user or 0) or DEFAULT_LIMIT
	window = int(settings.rate_limit_window_seconds or 0) or DEFAULT_WINDOW
	_too_many(ratelimit.exceeded(ratelimit.USER_PREFIX, frappe.session.user, limit, window))


def _check_ip_rate_limit() -> None:
	"""IP layer (DECISIONS #27). Runs after the role check, so users without the role can't use up the quota."""
	try:
		ip = frappe.local.request_ip or "unknown"
	except AttributeError:  # no request (a test or a background call)
		ip = "unknown"
	_too_many(ratelimit.exceeded(ratelimit.IP_PREFIX, ip, IP_LIMIT, IP_WINDOW))


def _validate(question, route, depth, deep):
	if not isinstance(question, str) or not question.strip():
		frappe.throw(_("Please type a question."))
	# The question is stored exactly as received (DECISIONS #24, #36d); the stripped copy is for the length check only.
	if len(question.strip()) > MAX_QUESTION or len(question) > MAX_QUESTION * 2:
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
		rows = frappe.get_list(  # AST-ALLOWED: own-conversation ownership check, runs as the session user
			doctype,
			filters={"name": name, "user": frappe.session.user},
			pluck="name",
			limit=1,
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


def _history(conversation: str) -> list:
	"""The last HISTORY_TURNS finished exchanges (status ok or limited) of the session user's own conversation, oldest
	first, as `{question, answer, tool_calls}`. The caller has checked ownership. Replayed as plain text only (M4b)."""
	rows = frappe.get_list(  # AST-ALLOWED: own audit log, runs as the session user
		audit.MESSAGE,
		filters={
			"conversation": conversation,
			"user": frappe.session.user,
			"status": ["in", ["ok", "limited"]],
		},
		fields=["question", "answer", "tool_calls"],
		order_by="creation desc",
		limit=HISTORY_TURNS,
	)
	return [
		{
			"question": r.question or "",
			"answer": r.answer or "",
			"tool_calls": audit.parse_list(r.tool_calls),
		}
		for r in reversed(rows)
	]
