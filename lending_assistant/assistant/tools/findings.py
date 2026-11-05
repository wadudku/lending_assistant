"""The two findings tools (PLAN §4, G13; M6): `search_findings` and `suggest_finding`.

`search_findings` reads team findings with `frappe.get_list` as the session user (G2) and ranks them in Python; the author
is the stored `author_name` (never an email, G8). `suggest_finding` writes NOTHING: it validates a suggestion and echoes it,
so the orchestrator can offer a "Save as finding" button. Only `api/findings.save` (a user's click) creates a finding, and
this module cannot import the module that does (scan rule `findings-import`).
"""

import re

import frappe

from lending_assistant.assistant import finding_rules, guard

SEARCH_SOURCE = "team_finding"
SUGGEST_SOURCE = "suggestion"
SOURCE_WORDS = (
	"Analysis",
	"Team finding",
	"Live site",
	"Code",
	"General knowledge",
	"Web",
)  # = prompts.LABEL_WORDS
FETCH = 200
TOP = 5
SUMMARY_MAX = 1500
ENVELOPE_ROOM = 6500  # characters shared by the summaries of one result (D3)
MAX_TITLE = 140
MAX_SUMMARY = 4000
STOP = frozenset(
	"the a an and or of to in on for is are was be what how why did do does we our us it this that with".split()
)
FIELDS = [
	"name",
	"title",
	"summary",
	"status",
	"creation",
	"br_ids",
	"doctypes",
	"cards_used",
	"lending_version",
	"author_name",
]
NOTE = "These are team notes, not verified analysis. They never override a bridge verdict."
NO_AUTHOR = "a team member"

SEARCH_FINDINGS_SCHEMA = {
	"name": "search_findings",
	"description": (
		"Recall what the team concluded before: saved team findings (draft or confirmed). Returns up to 5 findings with "
		"status, author, date, BR ids, doctypes, whether they are stale (check again) and the bridge verdicts of their BR ids. "
		"A finding is a team note, never an analysis result, and never overrides a bridge verdict."
	),
	"strict": True,
	"input_schema": {
		"type": "object",
		"properties": {
			"query": {
				"type": "string",
				"description": "Words describing the topic (at most 500 characters).",
			},
			"br_id": {
				"type": "string",
				"description": "Only findings about this BR id, for example BR-LMS-162.",
			},
			"doctype": {"type": "string", "description": "Only findings about this doctype."},
		},
		"required": ["query"],
		"additionalProperties": False,
	},
}
SUGGEST_FINDING_SCHEMA = {
	"name": "suggest_finding",
	"description": (
		"Offer the user a Save as finding button for a conclusion that is new and useful to the team. Nothing is saved: the "
		"user decides. Use it at most once per answer, only after you reached the conclusion."
	),
	"strict": True,
	"input_schema": {
		"type": "object",
		"properties": {
			"title": {"type": "string", "description": "A short title (at most 140 characters)."},
			"summary": {
				"type": "string",
				"description": "The conclusion in plain words (at most 4000 characters).",
			},
			"br_ids": {
				"type": "array",
				"items": {"type": "string"},
				"description": "BR ids it concerns, e.g. BR-LMS-162.",
			},
			"doctypes": {
				"type": "array",
				"items": {"type": "string"},
				"description": "Doctypes it concerns.",
			},
			"sources": {
				"type": "array",
				"items": {"type": "string", "enum": list(SOURCE_WORDS)},
				"description": "The source labels the conclusion rests on.",
			},
		},
		"required": ["title", "summary", "br_ids", "doctypes", "sources"],
		"additionalProperties": False,
	},
}
SCHEMAS = (SEARCH_FINDINGS_SCHEMA, SUGGEST_FINDING_SCHEMA)


def _words(text: str) -> list[str]:
	found = (w for w in re.findall(r"[a-z0-9]+", (text or "").lower()) if len(w) >= 2 and w not in STOP)
	return list(dict.fromkeys(found))


def _score(row, terms: list[str]) -> int:
	title, summary, brs = (row.title or "").lower(), (row.summary or "").lower(), (row.br_ids or "").lower()
	return sum((3 if t in title else 0) + (1 if t in summary else 0) + (3 if t in brs else 0) for t in terms)


def _filters(br_id, doctype):
	filters = []
	if br_id:
		filters.append(["br_ids", "like", f"%{br_id}%"])
	if doctype:
		filters.append(["doctypes", "like", f"%{doctype}%"])
	return filters


def _result(row, cap: int) -> dict:
	summary = row.summary or ""
	reasons = finding_rules.stale_reasons(row.cards_used, row.lending_version)
	brs = finding_rules.lines(row.br_ids)
	author = " ".join(str(row.author_name or "").split())
	author = author if author and "@" not in author else NO_AUTHOR
	date = str(row.creation)[:10]
	return {
		"name": row.name,
		"title": row.title,
		"summary": summary[:cap],
		"summary_truncated": len(summary) > cap,
		"status": row.status,
		"author": author,
		"date": date,
		"label_detail": f"{(row.status or '').lower()}, {author}, {date}",
		"br_ids": brs,
		"doctypes": finding_rules.lines(row.doctypes),
		"stale": bool(reasons),
		"stale_reasons": reasons,
		"bridge_verdicts": finding_rules.bridge_verdicts(brs),
	}


def search_findings(query, br_id=None, doctype=None) -> str:
	with guard.read_only_tool_context("search_findings"):
		if not isinstance(query, str) or len(query) > 500:
			frappe.throw("query must be text of at most 500 characters.")
		if br_id is not None:
			wanted_br = finding_rules.canonical_br_id(br_id)
			if not wanted_br:
				frappe.throw("br_id must look like BR-LMS-162 and exist in the knowledge base.")
		else:
			wanted_br = None
		if doctype is not None and (not isinstance(doctype, str) or len(doctype) > 140):
			frappe.throw("doctype must be a doctype name.")
		rows = frappe.get_list(  # AST-ALLOWED: team findings, read as the session user (G2)
			"Assistant Finding",
			filters=_filters(wanted_br, doctype),
			fields=FIELDS,
			order_by="creation desc",
			limit_page_length=FETCH,
		)
		terms = _words(query)
		scored = []
		for row in rows:
			if wanted_br and wanted_br not in finding_rules.lines(row.br_ids):
				continue
			if doctype and doctype not in finding_rules.lines(row.doctypes):
				continue
			score = _score(row, terms)
			if score > 0 or wanted_br or doctype:
				scored.append((score, row))
		scored.sort(key=lambda pair: -pair[0])  # stable: newest first among equal scores
		top = [row for _score_, row in scored[:TOP]]
		if not top:
			return guard.as_data(
				{"results": [], "count": 0, "message": "No team findings match."}, source=SEARCH_SOURCE
			)
		cap = min(SUMMARY_MAX, ENVELOPE_ROOM // len(top))
		result = {"results": [_result(row, cap) for row in top], "count": len(top), "note": NOTE}
		cleaned = guard.unwrap(guard.as_data(result, source=SEARCH_SOURCE))
		guard.fit(
			cleaned, row_lists=lambda: [cleaned["results"]], field_dicts=lambda: [], source=SEARCH_SOURCE
		)
		cleaned["count"] = len(cleaned["results"])
		return guard.as_data(cleaned, source=SEARCH_SOURCE)


def suggest_finding(title, summary, br_ids, doctypes, sources) -> str:
	with guard.read_only_tool_context("suggest_finding"):
		title = " ".join(str(title or "").split())
		summary = str(summary or "").strip()
		if not title or len(title) > MAX_TITLE:
			frappe.throw(f"title is required and at most {MAX_TITLE} characters.")
		if not summary or len(summary) > MAX_SUMMARY:
			frappe.throw(f"summary is required and at most {MAX_SUMMARY} characters.")
		suggestion = {
			"title": title,
			"summary": summary,
			"br_ids": finding_rules.check_br_ids(br_ids),
			"doctypes": finding_rules.check_doctypes(doctypes),
			"sources": list(dict.fromkeys(s for s in sources if s in SOURCE_WORDS)),
		}
		return guard.as_data(
			{
				"message": "A Save as finding button will be shown to the user; nothing is saved.",
				"suggestion": suggestion,
			},
			source=SUGGEST_SOURCE,
		)
