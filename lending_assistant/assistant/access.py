"""Permission checks for the advisor's "can I...?" notices (PLAN G5).

Both functions answer for the session user only. The doctype must be on the Settings allowlist (R5), and
nothing here takes a user, role or company from its arguments (R9). `route_doctype` / `route_docname` from the
widget are hints at most: they never decide who the user is or what they may do (DECISIONS #37).
"""

import frappe
import frappe.permissions  # not loaded by `bench execute` or a worker until something imports it (M2b-R4)

from lending_assistant.assistant import guard

ACTIONS = ("read", "create", "write", "submit", "cancel", "delete")


def check_my_access(doctype, actions, docname=None) -> dict:
	"""For each action, can the session user do it? With `docname`, on that record (G4 applies).

	Without `docname` this is a meta-only answer and works even when Live data is off. With `docname` the
	record is loaded through the guard, so a missing and an unreadable record give the same error.
	"""
	guard.require_doctype(doctype)
	if isinstance(actions, str):
		actions = [actions]
	if not isinstance(actions, list | tuple) or not actions or any(a not in ACTIONS for a in actions):
		raise frappe.ValidationError(f"Actions must be some of: {', '.join(ACTIONS)}.")

	doc = guard.load_readable(doctype, docname) if docname is not None else None
	access = {
		action: bool(frappe.permissions.has_permission(doctype, action, doc=doc, print_logs=False))
		for action in dict.fromkeys(actions)
	}
	result = {"source": guard.SOURCE_LIVE, "doctype": doctype, "access": access}
	if docname is not None:
		result["docname"] = docname
	return result


def roles_that_can(doctype, action) -> dict:
	"""Roles that hold `action` at permlevel 0, from the doctype meta (Custom DocPerm is already applied).

	`owner_only_roles` hold it only on their own records (the `if_owner` flag). No database query.
	"""
	guard.require_doctype(doctype)
	if action not in ACTIONS:
		raise frappe.ValidationError(f"Action must be one of: {', '.join(ACTIONS)}.")

	roles, owner_only = set(), set()
	for perm in frappe.get_meta(doctype).permissions:
		if (perm.permlevel or 0) == 0 and perm.get(action):
			(owner_only if perm.get("if_owner") else roles).add(perm.role)
	return {
		"source": guard.SOURCE_LIVE,
		"doctype": doctype,
		"action": action,
		"roles": sorted(roles),
		"owner_only_roles": sorted(owner_only - roles),
	}
