"""Audit log writer (G10). One of the only two modules allowed to write (the other is findings.py, M6).

It writes Assistant Conversation and Assistant Message rows, nothing else. The rows are created while
the session user is the logged-in user, so `owner` is that user and the `if_owner` permission works.
Nothing here commits: the request commits.
"""

import json

import frappe
from frappe.utils import now_datetime

CONVERSATION = "Assistant Conversation"
MESSAGE = "Assistant Message"
TITLE_LENGTH = 100


def _json(value):
	return None if value is None else json.dumps(value, default=str)


def start_conversation(route: str | None = None, title: str | None = None) -> str:
	"""Create a conversation for the session user and return its name."""
	conversation = frappe.new_doc(CONVERSATION)
	conversation.user = frappe.session.user
	conversation.title = (title or "").strip()[:TITLE_LENGTH]
	conversation.first_route = route or ""
	conversation.last_activity = now_datetime()
	conversation.message_count = 0
	conversation.insert(ignore_permissions=True)  # AST-ALLOWED: app's own audit log
	return conversation.name


def log_exchange(
	conversation: str,
	*,
	question: str,
	answer: str,
	route: str | None = None,
	route_doctype: str | None = None,
	route_docname: str | None = None,
	depth: str = "Both",
	deep: int = 0,
	status: str = "ok",
	model: str | None = None,
	roles: list | None = None,
	tokens_in: int = 0,
	tokens_out: int = 0,
	latency_ms: int = 0,
	tool_calls: list | None = None,
	records_read: list | None = None,
	code_files_read: list | None = None,
	cards_used: list | None = None,
	web_sources: list | None = None,
) -> str:
	"""Write one Assistant Message (one exchange) and update its conversation. Returns the message name."""
	message = frappe.new_doc(MESSAGE)
	message.update(
		{
			"conversation": conversation,
			"user": frappe.session.user,
			"route": route or "",
			"route_doctype": route_doctype or "",
			"route_docname": route_docname or "",
			"depth": depth,
			"deep": 1 if deep else 0,
			"question": question,
			"answer": answer,
			"status": status,
			"model": model,
			"roles": _json(sorted(roles)) if roles is not None else None,
			"tokens_in": tokens_in,
			"tokens_out": tokens_out,
			"latency_ms": latency_ms,
			"tool_calls": _json(tool_calls),
			"records_read": _json(records_read),
			"code_files_read": _json(code_files_read),
			"cards_used": _json(cards_used),
			"web_sources": _json(web_sources),
		}
	)
	message.insert(ignore_permissions=True)  # AST-ALLOWED: app's own audit log

	parent = frappe.get_doc(CONVERSATION, conversation)
	parent.message_count = (parent.message_count or 0) + 1
	parent.last_activity = now_datetime()
	parent.save(ignore_permissions=True)  # AST-ALLOWED: app's own audit log
	return message.name


def set_feedback(message: str, value: str, comment: str | None = None) -> None:
	"""Store thumbs up/down (and an optional comment) on a message. The caller checks ownership."""
	doc = frappe.get_doc(MESSAGE, message)
	doc.feedback = value
	doc.feedback_comment = comment or ""
	doc.save(ignore_permissions=True)  # AST-ALLOWED: app's own audit log
