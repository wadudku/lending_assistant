"""Permission checks for the advisor's "can I...?" notices (PLAN G5).

Both functions answer for the session user only. The doctype must be on the Settings allowlist (R5), and
nothing here takes a user, role or company from its arguments (R9). `route_doctype` / `route_docname` from the
widget are hints at most: they never decide who the user is or what they may do (DECISIONS #37).
"""

import frappe

from lending_assistant.assistant import codereader, guard, settings

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

	access = guard.check_actions(doctype, actions, docname)
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
	for perm in frappe.get_meta(doctype).permissions:  # AST-ALLOWED: permission rows from the meta; only role names leave this module
		if (perm.permlevel or 0) == 0 and perm.get(action):
			(owner_only if perm.get("if_owner") else roles).add(perm.role)
	return {
		"source": guard.SOURCE_LIVE,
		"doctype": doctype,
		"action": action,
		"roles": sorted(roles),
		"owner_only_roles": sorted(owner_only - roles),
	}


LAYOUT_FIELDTYPES = frozenset(
	{"Section Break", "Column Break", "Tab Break", "HTML", "Button", "Heading", "Fold", "Image", "Table Break"}
)
LINK_FIELDTYPES = ("Link", "Table", "Table MultiSelect")
DESCRIPTION_CHARS = 160
SEARCH_CHARS = 100


def describe_doctype(doctype, search=None) -> dict:
	"""Screen help for one doctype, as plain data: the fields the session user may read, the module, the controller
	path (when the code reader is on) and the doctypes the fields link to (G3, G8).

	Only fields `guard.readable_fields` returns: so no never-send, Password, `owner`, `modified_by` or `_` fields, and
	nothing above the user's permlevel. Layout and hidden fields are skipped. `search` is a case-insensitive substring of
	the label or fieldname. A user who cannot read the doctype at all gets a refusal. Works with Live data off: it is
	meta, not business data.
	"""
	guard.require_doctype(doctype)
	if search is not None and (not isinstance(search, str) or len(search) > SEARCH_CHARS):
		raise frappe.ValidationError(f"search must be text of at most {SEARCH_CHARS} characters.")
	if not guard.check_actions(doctype, ["read"])["read"]:
		raise guard.AssistantRefused("You don't have permission to read that doctype.")

	meta = frappe.get_meta(doctype)  # AST-ALLOWED: field labels and types for screen help; only plain text leaves this function
	readable = set(guard.readable_fields(doctype))
	allowed = {row.allowed_doctype for row in settings.get_settings().doctype_allowlist}
	needle = search.strip().lower() if search else ""
	fields, linked = [], {}
	for df in meta.fields:
		if df.fieldname not in readable or df.fieldtype in LAYOUT_FIELDTYPES or df.hidden:
			continue
		if needle and needle not in (df.label or "").lower() and needle not in df.fieldname.lower():
			continue
		fields.append(
			{
				"fieldname": df.fieldname,
				"label": df.label,
				"fieldtype": df.fieldtype,
				"options": df.options,
				"reqd": int(bool(df.reqd)),
				"description": (df.description or "")[:DESCRIPTION_CHARS],
			}
		)
		if df.fieldtype in LINK_FIELDTYPES and df.options:
			linked[df.options] = {"doctype": df.options, "via_field": df.fieldname, "on_allowlist": df.options in allowed}
	return {
		"doctype": doctype,
		"module": meta.module,
		"controller_path": codereader.controller_path(meta.module, doctype),
		"fields": fields,
		"fields_total": len(fields),
		"linked_doctypes": list(linked.values()),
	}
