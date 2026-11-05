"""The four live-site tools (PLAN §4, M4a): `get_screen_help`, `check_my_access`, `find_records`, `get_record`.

Every function reads through `guard` or `access` and nothing else: no `get_meta`, no `get_list`, no `get_doc` here.
The session user is the only identity: no argument names a user, role or company. Each returns one
`<data source="live_site">` envelope within the G9 size cap. The registry (registry.py) validates the arguments,
checks the switches, runs the function inside the read-only context and checks the result. No `@frappe.whitelist`.

Schemas are strict-compatible (#141 R3): `additionalProperties: false`, every property in `required` (optional ones are
nullable), and no length or range keywords. Python checks the limits, in the registry and in the guard.
"""

import frappe

from lending_assistant.assistant import access, guard

MAX_FIND_LIMIT = guard.MAX_ROWS
OPERATORS = ("=", "!=", "<", ">", "<=", ">=", "like", "in", "not in", "between", "is")
LIST_OPERATORS = ("in", "not in", "between")


def _string_or_null(description: str) -> dict:
	return {"type": ["string", "null"], "description": description}


GET_SCREEN_HELP_SCHEMA = {
	"name": "get_screen_help",
	"description": (
		"Describe one doctype's screen: the fields the current user may see (label, type, options, description), the "
		"module, the controller file path, and the doctypes it links to. Without 'search' a large doctype is cut and "
		"says how many fields were left out; pass 'search' (a part of a label or fieldname) to reach them."
	),
	"strict": True,
	"input_schema": {
		"type": "object",
		"properties": {
			"doctype": {"type": "string", "description": "The doctype name, for example Loan Repayment."},
			"search": _string_or_null(
				"Only fields whose label or fieldname contains this text (case-insensitive), or null."
			),
		},
		"required": ["doctype", "search"],
		"additionalProperties": False,
	},
}
CHECK_MY_ACCESS_SCHEMA = {
	"name": "check_my_access",
	"description": (
		"Can the current user do these actions on a doctype (or on one record)? Also names the roles that hold each "
		"action, so you can say who to ask. Actions: read, create, write, submit, cancel, delete."
	),
	"strict": True,
	"input_schema": {
		"type": "object",
		"properties": {
			"doctype": {"type": "string", "description": "The doctype name, for example Loan."},
			"actions": {
				"type": "array",
				"items": {"type": "string", "enum": list(access.ACTIONS)},
				"description": "One to six different actions.",
			},
			"docname": _string_or_null(
				"A record ID to check the actions on that record, or null for the doctype."
			),
		},
		"required": ["doctype", "actions", "docname"],
		"additionalProperties": False,
	},
}
_FILTER = {
	"type": "object",
	"properties": {
		"field": {"type": "string", "description": "A fieldname you can read."},
		"operator": {"type": "string", "enum": list(OPERATORS)},
		"value": {
			"type": ["string", "number", "null"],
			"description": "The value for =, !=, <, >, <=, >=, like (at most 100 characters), and for is: 'set' or 'not set'. Null for in, not in and between.",
		},
		"values": {
			"type": ["array", "null"],
			"items": {"type": ["string", "number"]},
			"description": "For in and not in: 1 to 50 values. For between: exactly two. Null for every other operator.",
		},
	},
	"required": ["field", "operator", "value", "values"],
	"additionalProperties": False,
}
FIND_RECORDS_SCHEMA = {
	"name": "find_records",
	"description": (
		"List up to 20 records of a doctype that the current user can see, with the fields you ask for. Example: "
		"find Loans of one product disbursed after a date: doctype 'Loan', filters [{field:'loan_product', operator:'=', "
		"value:'PL-EMI', values:null}, {field:'disbursement_date', operator:'>', value:'2026-01-01', values:null}], "
		"fields ['name','status'], order_by 'name asc', limit 10. The same field may appear in two filters. There is no "
		"total count: the rows returned are all you can count."
	),
	"strict": True,
	"input_schema": {
		"type": "object",
		"properties": {
			"doctype": {"type": "string", "description": "The doctype name."},
			"filters": {
				"type": "array",
				"items": _FILTER,
				"description": "At most 10 conditions; an empty list means no filter.",
			},
			"fields": {
				"type": "array",
				"items": {"type": "string"},
				"description": "1 to 30 fieldnames you can read.",
			},
			"order_by": _string_or_null("'<fieldname> asc' or '<fieldname> desc', or null."),
			"limit": {
				"type": ["integer", "null"],
				"description": "Rows wanted, 1 to 20; null means 20. More than 20 is cut to 20.",
			},
		},
		"required": ["doctype", "filters", "fields", "order_by", "limit"],
		"additionalProperties": False,
	},
}
GET_RECORD_SCHEMA = {
	"name": "get_record",
	"description": (
		"Read one record the current user can see, with its child tables. A record that does not exist and one the user "
		"may not read give the same answer."
	),
	"strict": True,
	"input_schema": {
		"type": "object",
		"properties": {
			"doctype": {"type": "string", "description": "The doctype name."},
			"name": {"type": "string", "description": "The record ID."},
		},
		"required": ["doctype", "name"],
		"additionalProperties": False,
	},
}
SCHEMAS = (GET_SCREEN_HELP_SCHEMA, CHECK_MY_ACCESS_SCHEMA, FIND_RECORDS_SCHEMA, GET_RECORD_SCHEMA)


OMITTED_NOTE = "Some fields were left out. Call again with 'search' to reach them."


def get_screen_help(doctype, search=None) -> str:
	described = access.describe_doctype(doctype, search)
	cleaned = guard.unwrap(  # unwrap(as_data(...)) = the same dict with every string neutralised
		guard.as_data({**described, "truncated": False, "fields_omitted": 0, "note": OMITTED_NOTE})
	)
	total = len(cleaned["fields"])
	guard.fit(cleaned, row_lists=lambda: [cleaned["fields"]], field_dicts=lambda: [])
	while True:  # the omitted count can add a digit or two: re-check against the real envelope until it fits
		cleaned["fields_omitted"] = total - len(cleaned["fields"])
		if len(guard.as_data(cleaned)) <= guard.MAX_CHARS or not cleaned["fields"]:
			break
		cleaned["fields"].pop()
	if cleaned["fields_omitted"]:
		cleaned["truncated"] = True
	else:
		cleaned.pop("note", None)
	return guard.as_data(cleaned)


def check_my_access(doctype, actions, docname=None) -> str:
	if (
		not isinstance(actions, list | tuple)
		or not 1 <= len(actions) <= len(access.ACTIONS)
		or len(set(actions)) != len(actions)
	):
		raise frappe.ValidationError("Give 1 to 6 different actions.")
	answer = access.check_my_access(doctype, list(actions), docname)
	mine = set(frappe.get_roles())
	per_action = {}
	for action in actions:
		roles = access.roles_that_can(doctype, action)
		per_action[action] = {
			"allowed": bool(answer["access"][action]),
			"roles_that_can": roles["roles"],
			"owner_only_roles": roles["owner_only_roles"],
			"you_have_a_role": sorted(mine & set(roles["roles"])),
		}
	result = {"doctype": doctype, "actions": per_action}
	if docname is not None:
		result["docname"] = docname
	return guard.as_data(result)


def _condition(item: dict) -> list:
	"""One strict-schema filter object -> the `[field, operator, value]` form the guard validates."""
	operator = item["operator"]
	if operator in LIST_OPERATORS:
		if item["value"] is not None or item["values"] is None:
			raise frappe.ValidationError(
				f"The {operator} operator takes 'values' (a list) and a null 'value'."
			)
		return [item["field"], operator, list(item["values"])]
	if item["values"] is not None or item["value"] is None:
		raise frappe.ValidationError(f"The {operator} operator takes 'value' and a null 'values'.")
	return [item["field"], operator, item["value"]]


def find_records(doctype, filters, fields, order_by=None, limit=None) -> str:
	if not isinstance(filters, list | tuple):
		raise frappe.ValidationError("filters must be a list.")
	conditions = [_condition(item) for item in filters]
	return guard.list_records(
		doctype,
		filters=conditions,
		fields=fields,
		order_by=order_by,
		limit=MAX_FIND_LIMIT if limit is None else limit,
	)


def get_record(doctype, name) -> str:
	return guard.read_doc(doctype, name)
