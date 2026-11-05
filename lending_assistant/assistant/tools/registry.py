"""The tool registry and the dispatcher (PLAN §4, §2 G1-G9, G11; DECISIONS #46, #48, #49, #146).

`TOOLS` is a static dict: tool name -> {function, schema, description, needs_switch, source}. `dispatch(name, args)` is the
only way the orchestrator (M4b) runs a tool. In this order it:

1. checks the name is in `TOOLS`;
2. validates the arguments against the tool's schema in Python (types, unknown keys, enums, lengths, counts);
3. checks the setting switch (`live_data` / `code_reader`);
4. runs the function inside `guard.identity_watch` and `guard.read_only_tool_context(name)`, and holds the context (#49 I1);
5. fails closed if the context counted anything but trap refusals, or if the identity check fired;
6. checks the result is one `<data>` envelope with this tool's source label, within the size cap, or wraps a dict.

Contract for the orchestrator (go brief item 2): `dispatch` RETURNS a `ToolResult`. An expected refusal (unknown tool, bad
arguments, a switch off, no permission, a record that is missing or hidden, a write that the trap refused) comes back as
`ToolResult(is_error=True, content='{"error": "..."}')`, to be sent as a `tool_result` with `is_error: true`. It RAISES
(`guard.AssistantGuardError`, or the unexpected exception) only when the guard itself failed: identity or connection
changed, a database write got past the trap, a callback or savepoint problem, or an internal error. The orchestrator ends
the turn then. Every refusal and failure is logged with the tool name and kind only, never an argument or a value.

The schemas carry no length, count or range keyword (#141 R3, strict mode); the limits are in `LIMITS` and `MAX_*` below.
Identity is `frappe.session.user`: no tool takes a user, role or company.
"""

import json
from typing import NamedTuple

import frappe

from lending_assistant.assistant import codereader, guard, settings
from lending_assistant.assistant.tools import code, dues, findings, knowledge, live

MAX_STRING = 200  # characters of any string argument, unless LIMITS says otherwise
MAX_ARRAY = 50  # items of any array argument, unless LIMITS says otherwise
MAX_MESSAGE = 300  # characters of a validation message passed on to the model
LIMITS = {  # "<tool>.<argument path>": characters (strings) or items (arrays)
	"search_knowledge.query": 500,
	"search_code.query": codereader.MAX_QUERY,
	"search_code.path_glob": 100,
	"search_code.app": 100,
	"read_code.path": 300,
	"check_my_access.actions": 6,
	"find_records.filters": guard.MAX_FILTERS,
	"find_records.filters[].value": 200,
	"find_records.filters[].values": 50,
	"find_records.fields": guard.MAX_FIELDS,
	"find_records.order_by": 100,
	"get_screen_help.search": 100,
	"search_findings.query": 500,
	"search_findings.br_id": 40,
	"search_findings.doctype": 140,
	"suggest_finding.title": 140,
	"suggest_finding.summary": 4000,
	"suggest_finding.br_ids": 10,
	"suggest_finding.br_ids[]": 40,
	"suggest_finding.doctypes": 10,
	"suggest_finding.doctypes[]": 140,
	"suggest_finding.sources": 6,
}
SWITCHES = (None, "live_data", "code_reader")
SOURCES = ("analysis", "live_site", "code", "team_finding", "suggestion")
GUARD_MESSAGE = "The assistant can only read."
PERMISSION_MESSAGE = "You don't have permission for that."


class ToolError(Exception):
	"""An argument or call that the dispatcher refuses. Its text is safe to show the model."""


class ToolResult(NamedTuple):
	content: str  # an envelope `<data source="...">{json}</data>`, or '{"error": "..."}' when is_error
	is_error: bool = False
	source: str | None = None  # the G11 label of a successful result; None for an error


def _entry(function, schema, needs_switch, source) -> dict:
	return {
		"function": function,
		"schema": schema,
		"description": schema["description"],
		"needs_switch": needs_switch,
		"source": source,
	}


TOOLS = {
	"lookup_knowledge": _entry(
		knowledge.lookup_knowledge, knowledge.LOOKUP_KNOWLEDGE_SCHEMA, None, "analysis"
	),
	"get_card": _entry(knowledge.get_card, knowledge.GET_CARD_SCHEMA, None, "analysis"),
	"search_knowledge": _entry(
		knowledge.search_knowledge, knowledge.SEARCH_KNOWLEDGE_SCHEMA, None, "analysis"
	),
	# meta and permission facts, no business data (check_my_access with a docname needs Live data inside the guard)
	"search_findings": _entry(
		findings.search_findings, findings.SEARCH_FINDINGS_SCHEMA, None, "team_finding"
	),
	"suggest_finding": _entry(findings.suggest_finding, findings.SUGGEST_FINDING_SCHEMA, None, "suggestion"),
	"get_screen_help": _entry(live.get_screen_help, live.GET_SCREEN_HELP_SCHEMA, None, "live_site"),
	"check_my_access": _entry(live.check_my_access, live.CHECK_MY_ACCESS_SCHEMA, None, "live_site"),
	"find_records": _entry(live.find_records, live.FIND_RECORDS_SCHEMA, "live_data", "live_site"),
	"get_record": _entry(live.get_record, live.GET_RECORD_SCHEMA, "live_data", "live_site"),
	"get_loan_dues": _entry(dues.get_loan_dues, dues.GET_LOAN_DUES_SCHEMA, "live_data", "live_site"),
	"search_code": _entry(code.search_code, code.SEARCH_CODE_SCHEMA, "code_reader", "code"),
	"read_code": _entry(code.read_code, code.READ_CODE_SCHEMA, "code_reader", "code"),
}


# --- argument validation ---------------------------------------------------------------------------------------


def _is_type(value, name: str) -> bool:
	if name == "string":
		return isinstance(value, str)
	if name == "integer":
		return isinstance(value, int) and not isinstance(value, bool)
	if name == "number":
		return isinstance(value, int | float) and not isinstance(value, bool)
	if name == "boolean":
		return isinstance(value, bool)
	if name == "null":
		return value is None
	if name == "array":
		return isinstance(value, list | tuple)
	if name == "object":
		return isinstance(value, dict)
	return False


def _types(spec: dict) -> list:
	if "anyOf" in spec:
		return [t for branch in spec["anyOf"] for t in _types(branch)]
	kind = spec.get("type")
	return list(kind) if isinstance(kind, list | tuple) else [kind]


def _plain_name(key) -> str:
	text = str(key)[:40]
	return text if text.replace("_", "").isalnum() else "(a name)"


def _check(value, spec: dict, path: str, tool: str):
	"""Return a cleaned copy of `value`, or raise ToolError. Never echoes a value."""
	if (
		"anyOf" in spec
	):  # the first branch that accepts the value wins; each branch checks its own type and enum
		for branch in spec["anyOf"]:
			try:
				return _check(value, branch, path, tool)
			except ToolError:
				continue
		if not any(_is_type(value, t) for t in _types(spec)):
			raise ToolError(
				f"Argument '{path}' has the wrong type: expected {' or '.join(str(t) for t in _types(spec))}."
			)
		raise ToolError(f"Argument '{path}' is not one of the allowed values.")
	types = _types(spec)
	if not any(_is_type(value, t) for t in types):
		raise ToolError(
			f"Argument '{path}' has the wrong type: expected {' or '.join(str(t) for t in types)}."
		)
	if "enum" in spec and value not in spec["enum"]:
		raise ToolError(f"Argument '{path}' is not one of the allowed values.")
	limit_key = f"{tool}.{path}"
	if isinstance(value, str):
		if len(value) > LIMITS.get(limit_key, MAX_STRING):
			raise ToolError(f"Argument '{path}' is too long.")
		return value
	if isinstance(value, list | tuple):
		if len(value) > LIMITS.get(limit_key, MAX_ARRAY):
			raise ToolError(f"Argument '{path}' has too many items.")
		item_spec = spec.get("items") or {}
		return [_check(item, item_spec, f"{path}[]", tool) for item in value]
	if isinstance(value, dict):
		return _check_object(value, spec, path, tool)
	return value


def _check_object(value: dict, spec: dict, path: str, tool: str) -> dict:
	properties = spec.get("properties", {})
	for key in value:
		if key not in properties:
			raise ToolError(f"Unknown argument '{_plain_name(key)}'.")
	clean = {}
	for key, sub in properties.items():
		where = f"{path}.{key}" if path else key
		optional = key not in spec.get("required", list(properties))
		if key not in value:
			if optional or "null" in _types(sub):
				clean[key] = None  # an omitted optional argument is None for the tool, as a null always was
				continue
			raise ToolError(f"Missing argument '{where}'.")
		if (
			optional and value[key] is None
		):  # an explicit null for an optional argument is still accepted (M4a)
			clean[key] = None
			continue
		clean[key] = _check(value[key], sub, where, tool)
	return clean


def validate_args(schema: dict, args, tool: str = "") -> dict:
	"""Check `args` against a tool's `input_schema` and return a cleaned copy. Raises ToolError."""
	if args is None:
		args = {}
	if not isinstance(args, dict):
		raise ToolError("The arguments must be an object.")
	return _check_object(args, schema, "", tool)


# --- dispatch -----------------------------------------------------------------------------------------------------


def _logger():
	"""Frappe's default level is WARNING under the dev server and ERROR otherwise (and under the test runner), which would
	drop refusals. Lower this one logger to WARNING so they are written (M4a-R2); it never goes higher than Frappe's."""
	logger = frappe.logger("lending_assistant_tools")
	if logger.level > 30:  # 30 is logging.WARNING
		logger.setLevel(30)
	return logger


def _log(kind: str, tool: str):
	"""User, tool name and kind only: never an argument or a value (G8, G10).

	Refusals go out at `warning` and internal errors at `error`: Frappe's logger drops `info` (its level is WARNING under
	the dev server and ERROR otherwise), so an `info` line never reached the file (M4a-R2).
	"""
	try:
		level = _logger().error if kind == "internal_error" else _logger().warning
		level(f"user={frappe.session.user} tool={tool or '(unknown)'} {kind}")
	except Exception:
		pass  # logging must never hide the tool's own result or error


def _refuse(kind: str, tool: str, message: str) -> ToolResult:
	_log(kind, tool)
	return ToolResult(json.dumps({"error": guard.neutralise(message)}, ensure_ascii=False), True, None)


def tool_definitions() -> list[dict]:
	"""Copies of the schemas of the tools that are on, for the Claude API `tools` parameter. Changing a copy changes nothing."""
	cfg = settings.get_settings()
	on = {None: True, "live_data": bool(cfg.live_data), "code_reader": bool(cfg.code_reader)}
	return [json.loads(json.dumps(e["schema"])) for e in TOOLS.values() if on[e["needs_switch"]]]


def _switch_message(switch):
	cfg = settings.get_settings()
	if switch == "live_data" and not cfg.live_data:
		return guard.LIVE_DATA_OFF
	if switch == "code_reader" and not cfg.code_reader:
		return codereader.OFF
	return None


def _check_envelope(envelope, tool: str, source: str) -> str:
	if not isinstance(envelope, str):
		envelope = guard.as_data(envelope, source)  # a dict result is wrapped here
	try:
		payload = guard.unwrap(envelope)  # raises AssistantGuardError if it is not one envelope
	except ValueError as exc:  # json.JSONDecodeError: two envelopes joined, or text that is not JSON (M4a-R5)
		raise guard.AssistantGuardError(
			f"Tool {tool} returned a result that is not one data envelope."
		) from exc
	if not envelope.startswith(f'<data source="{source}">') or payload.get("source") != source:
		raise guard.AssistantGuardError(f"Tool {tool} returned a result with the wrong source label.")
	if len(envelope) > guard.MAX_CHARS:
		raise guard.AssistantGuardError(f"Tool {tool} returned more than {guard.MAX_CHARS} characters.")
	return envelope


def dispatch(name, args=None) -> ToolResult:
	"""Run one tool for the session user. See the module docstring for the contract."""
	entry = TOOLS.get(name) if isinstance(name, str) else None
	if entry is None:
		return _refuse("unknown_tool", "", "Unknown tool.")
	try:
		cleaned = validate_args(entry["schema"]["input_schema"], args, name)
	except ToolError as exc:
		return _refuse("bad_arguments", name, str(exc))
	off = _switch_message(entry["needs_switch"])
	if off:
		return _refuse("switch_off", name, off)

	ctx, result, error = None, None, None
	try:
		with guard.identity_watch(
			name
		):  # #48: the request's connection and user are still the same afterwards
			with guard.read_only_tool_context(
				name
			) as ctx:  # #49 I1: held, so a swallowed trap error is still seen
				result = entry["function"](**cleaned)
	except guard.AssistantGuardError:
		raise  # fail closed: already logged by the guard
	except guard.RecordNotAvailable, frappe.DoesNotExistError:
		error = ("not_found", guard.NOT_FOUND)  # G4: one reply for a missing and a hidden record
	except guard.AssistantRefused as exc:  # includes CodeReaderRefused
		error = ("refused", str(exc) or PERMISSION_MESSAGE)
	except frappe.PermissionError:
		error = ("permission", PERMISSION_MESSAGE)
	except frappe.ValidationError as exc:
		error = ("invalid", str(exc)[:MAX_MESSAGE] or "The request is not valid.")
	except Exception:
		_log("internal_error", name)
		raise

	if ctx is not None:
		counts = ctx.summary()
		if any(
			counts[k]
			for k in (
				"db_writes",
				"callbacks_dropped",
				"callbacks_restored",
				"identity_changes",
				"savepoint_gone",
			)
		):
			_log("guard_failure", name)
			raise guard.AssistantGuardError(
				f"Tool {name} wrote or changed state inside the read-only context."
			)
		if counts["trap_hits"]:  # a write was tried and refused by the trap; any result is discarded
			return _refuse("write_refused", name, GUARD_MESSAGE)
	if error:
		return _refuse(error[0], name, error[1])
	envelope = _check_envelope(result, name, entry["source"])
	return ToolResult(envelope, False, entry["source"])
