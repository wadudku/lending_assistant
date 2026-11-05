"""The three knowledge tools (PLAN §4, M3b): `lookup_knowledge`, `get_card`, `search_knowledge`.

They read only the approved knowledge cards that ship with the app (`kb/knowledge/`). They make no database call, take
no record from the site and write nothing. Each runs inside `guard.read_only_tool_context`, returns one
`<data source="analysis">` envelope (G6, G11), and stays within the G9 size cap. There is no registry, no orchestrator
and no `@frappe.whitelist` here: wiring is M4.

The knowledge base is not permission-controlled data (it is the app's own files), so the role check stays in the chat
endpoint (G7). A card id is only ever a dict key in the store (G12): an unknown, draft or malformed id gets the same
answer.
"""

import json

import frappe

from lending_assistant.assistant import guard
from lending_assistant.kb import lookup as kb_lookup
from lending_assistant.kb import search as kb_search
from lending_assistant.kb import store

SOURCE = "analysis"
NOT_FOUND = "I can't find a card with that ID."
NO_MATCH = "No card matches those keys."
MAX_ARG = 200
HEAD_RESERVE = 1800  # characters kept free for the front matter when a long body is cut at a paragraph
CARD_FIELDS = (
	"id", "type", "title", "summary", "version", "status", "verdict", "analysis_status", "br_ids", "brd_section",
	"doctypes", "dev_items", "journeys", "actions", "terms", "fields", "options", "menus", "related", "lending_version",
	"code_refs", "images", "sources",
)  # fmt: skip


def _string_or_null(description: str) -> dict:
	return {"type": ["string", "null"], "description": description}


LOOKUP_KNOWLEDGE_SCHEMA = {
	"name": "lookup_knowledge",
	"description": (
		"Find knowledge cards by exact key: a doctype, an action on a doctype, a BR id, a BRD section, a glossary or "
		"lifecycle term, a journey or a development item. Returns ranked summaries, never card bodies; use get_card "
		"to read one. Pass null for keys you do not have."
	),
	"strict": True,
	"input_schema": {
		"type": "object",
		"properties": {
			"doctype": _string_or_null("A Frappe Lending doctype name, for example Loan Repayment."),
			"action": _string_or_null("What the user does, for example create, submit, waive, or Loan Repayment:create."),
			"br_id": _string_or_null("A BRD requirement id: BR-LMS-123, 123, 170r."),
			"brd_section": _string_or_null("A BRD section number, for example 7.7 or 7.7.1."),
			"term": _string_or_null("A glossary, lifecycle or decision term, for example write-off or SMA."),
			"journey": _string_or_null("A journey, J1 to J11."),
			"dev_item": _string_or_null("A development item, D1 to D20."),
		},
		"required": ["doctype", "action", "br_id", "brd_section", "term", "journey", "dev_item"],
		"additionalProperties": False,
	},
}
GET_CARD_SCHEMA = {
	"name": "get_card",
	"description": "Read one approved knowledge card (front matter and body) by its id, for example bridge.BR-LMS-162.",
	"strict": True,
	"input_schema": {
		"type": "object",
		"properties": {"card_id": {"type": "string", "description": "A card id from lookup_knowledge or search_knowledge (at most 200 characters)."}},
		"required": ["card_id"],
		"additionalProperties": False,
	},
}
SEARCH_KNOWLEDGE_SCHEMA = {
	"name": "search_knowledge",
	"description": "Keyword search over the approved knowledge cards. Returns the top 5 summaries. Use it when lookup_knowledge finds nothing.",
	"strict": True,
	"input_schema": {
		"type": "object",
		"properties": {
			"query": {"type": "string", "description": "Words describing what to find (at most 500 characters)."},
			"type": {
				"type": ["string", "null"],
				"enum": [*store.TYPES, None],
				"description": "Only cards of this type, or null for all.",
			},
		},
		"required": ["query", "type"],
		"additionalProperties": False,
	},
}
SCHEMAS = (LOOKUP_KNOWLEDGE_SCHEMA, GET_CARD_SCHEMA, SEARCH_KNOWLEDGE_SCHEMA)


def _text_arg(value, name: str):
	if value is None:
		return None
	if not isinstance(value, str) or len(value) > MAX_ARG:
		frappe.throw(f"{name} must be text of at most {MAX_ARG} characters.")
	return value


def _envelope(result: dict) -> str:
	guard.fit(result, row_lists=lambda: [result.get("results", [])], field_dicts=lambda: [], source=SOURCE)
	return guard.as_data(result, source=SOURCE)


def _summaries(rows: list[dict]) -> dict:
	if not rows:
		return {"results": [], "count": 0, "message": NO_MATCH}
	return {"results": rows, "count": len(rows)}


def lookup_knowledge(doctype=None, action=None, br_id=None, brd_section=None, term=None, journey=None, dev_item=None) -> str:
	with guard.read_only_tool_context("lookup_knowledge"):
		rows = kb_lookup.lookup(
			doctype=_text_arg(doctype, "doctype"),
			action=_text_arg(action, "action"),
			br_id=_text_arg(br_id, "br_id"),
			brd_section=_text_arg(brd_section, "brd_section"),
			term=_text_arg(term, "term"),
			journey=_text_arg(journey, "journey"),
			dev_item=_text_arg(dev_item, "dev_item"),
		)
		return _envelope(_summaries(rows))


def search_knowledge(query, type=None) -> str:
	with guard.read_only_tool_context("search_knowledge"):
		if not isinstance(query, str) or len(query) > 500:
			frappe.throw("query must be text of at most 500 characters.")
		if type is not None and type not in store.TYPES:
			frappe.throw("type must be one of the card types or null.")
		return _envelope(_summaries(kb_search.search(query, type=type)))


def get_card(card_id) -> str:
	with guard.read_only_tool_context("get_card"):
		card = store.get_card(card_id)
		if card is None:
			return guard.as_data({"message": NOT_FOUND}, source=SOURCE)  # unknown, draft and malformed ids alike (G4)
		result = {key: card[key] for key in CARD_FIELDS if key in card}
		budget = guard.MAX_CHARS - HEAD_RESERVE - len(json.dumps(result, ensure_ascii=False))
		paragraphs, used = [], 0
		for paragraph in card["body"].split("\n\n"):
			used += len(json.dumps(paragraph, ensure_ascii=False)) + 2
			if used > budget and paragraphs:
				result["truncated"] = True
				break
			paragraphs.append(paragraph)
		result["body"] = "\n\n".join(paragraphs)
		return _envelope(result)
