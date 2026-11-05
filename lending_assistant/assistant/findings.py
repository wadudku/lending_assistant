"""Findings writer (G13; the second of the only two modules allowed to write, the first is audit.py).

It creates one Assistant Finding from a stored Assistant Message and links the message to it. It is reachable ONLY from
`api/findings.save` (a user's click): no tool, no orchestrator and no other module may import it (scan rule
`findings-import`). Everything but the title and summary comes from the stored message, never from the client.
Nothing here commits: the request does.
"""

import json

import frappe

from lending_assistant.assistant import audit

FINDING = "Assistant Finding"
NOT_FOUND = "I can't find a record with that ID that you have access to."  # G4 wording
NO_NAME = "a team member"


def _author_name() -> str:
	"""The saving user's full name, never the email (G8); stored on the finding so tools do not look users up."""
	user = frappe.get_doc("User", frappe.session.user)  # AST-ALLOWED: own name
	name = " ".join(str(user.get("full_name") or "").split())
	return name if name and "@" not in name else NO_NAME


def _is_link_of(name, message_name) -> bool:
	"""True when the finding `name` exists and was saved from this message. A locking read (`for_update=True`) sees the
	latest committed row, not this request's snapshot, so a finding committed by a concurrent save is found (M6-R1). A
	reused name that belongs to another message does not count (M6-R3)."""
	try:
		doc = frappe.get_doc(FINDING, name, for_update=True)  # AST-ALLOWED: exists?
	except frappe.DoesNotExistError:
		return False
	return doc.source_message == message_name


def create_from_message(message_name: str, title, summary, lending_version: str) -> dict:
	"""Create the finding for the caller's own message. Returns `{"finding", "title", "created"}`.

	A second call for a message that already has a finding returns that finding. A message whose finding was deleted counts
	as not saved: the link is cleared and a new finding is made."""
	# Row lock (for_update): a double click is serialised. Ownership was checked by the caller.
	msg = frappe.get_doc(audit.MESSAGE, message_name, for_update=True)  # AST-ALLOWED: own message
	if msg.user != frappe.session.user:
		frappe.throw(NOT_FOUND, frappe.DoesNotExistError)

	if msg.finding:
		if _is_link_of(msg.finding, msg.name):
			return {"finding": msg.finding, "title": None, "created": False}
		msg.db_set("finding", "", update_modified=False)  # AST-ALLOWED: clear dead link

	try:
		suggestion = json.loads(msg.finding_suggestion or "")
	except ValueError:
		suggestion = None
	if not isinstance(suggestion, dict) or not suggestion.get("title") or not suggestion.get("summary"):
		frappe.throw("There is nothing to save for this answer.")

	# The new finding is built only from the stored message (and the edited title and summary).
	doc = frappe.get_doc(  # AST-ALLOWED: new finding
		{
			"doctype": FINDING,
			"title": title or suggestion["title"],
			"summary": summary or suggestion["summary"],
			"status": "Draft",
			"question": msg.question,
			"br_ids": "\n".join(suggestion.get("br_ids") or []),
			"doctypes": "\n".join(suggestion.get("doctypes") or []),
			"sources": json.dumps(suggestion.get("labels") or []),
			"cards_used": json.dumps(suggestion.get("cards") or []),
			"cards_basis": suggestion.get("cards_basis") or "",
			"lending_version": lending_version,
			"author_name": _author_name(),
			"source_message": msg.name,
		}
	)
	# The roles have no create, so this is the only insert; the controller still validates as the user.
	doc.insert(ignore_permissions=True)  # AST-ALLOWED: the only insert
	msg.db_set("finding", doc.name, update_modified=False)  # AST-ALLOWED: link
	return {"finding": doc.name, "title": doc.title, "created": True}
