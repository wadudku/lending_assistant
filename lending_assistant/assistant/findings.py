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
	user = frappe.get_doc(
		"User", frappe.session.user
	)  # AST-ALLOWED: the saving user's own name for the finding
	name = " ".join(str(user.get("full_name") or "").split())
	return name if name and "@" not in name else NO_NAME


def _exists(name) -> bool:
	try:
		frappe.get_doc(FINDING, name)  # AST-ALLOWED: does the linked finding still exist?
	except frappe.DoesNotExistError:
		return False
	return True


def create_from_message(message_name: str, title, summary, lending_version: str) -> dict:
	"""Create the finding for the caller's own message. Returns `{"finding", "title", "created"}`.

	A second call for a message that already has a finding returns that finding. A message whose finding was deleted counts
	as not saved: the link is cleared and a new finding is made."""
	msg = frappe.get_doc(  # AST-ALLOWED: row lock, so a double click is serialised; ownership was checked by the caller
		audit.MESSAGE, message_name, for_update=True
	)
	if msg.user != frappe.session.user:
		frappe.throw(NOT_FOUND, frappe.DoesNotExistError)

	if msg.finding:
		if _exists(msg.finding):
			return {"finding": msg.finding, "title": None, "created": False}
		msg.db_set("finding", "", update_modified=False)  # AST-ALLOWED: clear a link to a deleted finding

	try:
		suggestion = json.loads(msg.finding_suggestion or "")
	except ValueError:
		suggestion = None
	if not isinstance(suggestion, dict) or not suggestion.get("title") or not suggestion.get("summary"):
		frappe.throw("There is nothing to save for this answer.")

	doc = frappe.get_doc(  # AST-ALLOWED: the new finding, built only from the stored message
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
	doc.insert(
		ignore_permissions=True
	)  # AST-ALLOWED: the roles have no create; this is the only insert, validate still runs
	msg.db_set("finding", doc.name, update_modified=False)  # AST-ALLOWED: link the message to its finding
	return {"finding": doc.name, "title": doc.title, "created": True}
