"""The drift check of PLAN §5.7, run against the ingested cards (M3b). Meta and filesystem reads only.

    bench --site lending_site execute lending_assistant.kb.validate.run

For every approved card it checks that each doctype exists, each `fields` entry (`Doctype.Label`) is a field label or
fieldname of that doctype, each `options` entry (`Doctype.Label=Option`) is one of that Select field's options, each
`menus` path under `Lending` is in the Lending sidebar (the file `lending/workspace_sidebar/lending.json`), and each
`code_refs` path exists inside the installed lending, erpnext or frappe checkout. It does NOT check names written in
card bodies: the build repo's `drift` does that before ingest (DECISIONS #138 Q3). Nothing is written or queried.
"""

import json
import os
import re

import frappe

from lending_assistant.kb import store

APPS_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
APP_ROOTS = {name: os.path.join(APPS_DIR, name) for name in ("lending", "erpnext", "frappe")}
LINE_SUFFIX = re.compile(r":\d+(?:-\d+)?$")  # lending/.../loan.py:471 or :875-901
SIDEBAR = os.path.join(APP_ROOTS["lending"], "lending", "workspace_sidebar", "lending.json")


def _read_text(path: str) -> str:
	with open(path, encoding="utf-8") as handle:  # AST-ALLOWED: reads the Lending sidebar file for the menu check
		return handle.read()


def _meta_of(doctype: str):
	"""The fields of a doctype as plain dicts, or None when the doctype does not exist."""
	try:
		meta = frappe.get_meta(doctype)  # AST-ALLOWED: read-only drift check of a doctype named in an approved card
	except frappe.DoesNotExistError:
		return None
	return [{"label": f.label, "fieldname": f.fieldname, "options": f.options} for f in meta.fields]


def _norm(text) -> str:
	return " ".join(str(text or "").split()).lower()


def sidebar_pairs(items: list[dict]) -> set[tuple[str, str]]:
	"""(section, label) for every link in the sidebar, plus ("", label) for top-level links."""
	pairs, section = set(), ""
	for item in items:
		if item.get("type") == "Section Break":
			section = _norm(item.get("label"))
		else:
			pairs.add((section, _norm(item.get("label"))))
			pairs.add(("", _norm(item.get("label"))))
	return pairs


def _find_field(fields: list[dict], label: str):
	for field in fields:
		if _norm(field["label"]) == _norm(label) or field["fieldname"] == label:
			return field
	return None


def check_cards(cards: list[dict], meta_of, sidebar: set, app_roots: dict) -> tuple[list[str], list[str]]:
	"""(findings, notes). `meta_of(doctype)` gives the field dicts or None; `sidebar` is sidebar_pairs(...)."""
	findings, notes = [], []
	for card in cards:
		cid = card.get("id")
		for doctype in card.get("doctypes") or []:
			if meta_of(doctype) is None:
				findings.append(f"{cid}: doctype {doctype!r} does not exist")
		for ref in card.get("fields") or []:
			doctype, _, label = ref.partition(".")
			fields = meta_of(doctype)
			if fields is None:
				findings.append(f"{cid}: field {ref!r}: no such doctype {doctype!r}")
			elif _find_field(fields, label) is None:
				findings.append(f"{cid}: field {ref!r}: {doctype} has no field labelled {label!r}")
		for ref in card.get("options") or []:
			left, _, option = ref.partition("=")
			doctype, _, label = left.partition(".")
			fields = meta_of(doctype)
			field = _find_field(fields, label) if fields is not None else None
			if fields is None:
				findings.append(f"{cid}: option {ref!r}: no such doctype {doctype!r}")
			elif field is None:
				findings.append(f"{cid}: option {ref!r}: {doctype} has no field labelled {label!r}")
			elif _norm(option) not in [_norm(o) for o in (field["options"] or "").split("\n")]:
				findings.append(f"{cid}: option {ref!r}: {label!r} has no option {option!r}")
		for path in card.get("menus") or []:
			parts = [part.strip() for part in path.split(">")]
			if parts[0] != "Lending":
				notes.append(f"{cid}: menu {path!r} is outside the Lending sidebar; not checked")
			elif len(parts) == 3 and (_norm(parts[1]), _norm(parts[2])) not in sidebar:
				findings.append(f"{cid}: menu {path!r} is not in the Lending sidebar")
			elif len(parts) == 2 and ("", _norm(parts[1])) not in sidebar:
				findings.append(f"{cid}: menu {path!r} is not in the Lending sidebar")
			elif len(parts) not in (2, 3):
				findings.append(f"{cid}: menu {path!r} is not 'Lending > Group > Item'")
		for ref in card.get("code_refs") or []:
			path = LINE_SUFFIX.sub("", ref)
			parts = path.split("/")
			root = app_roots.get(parts[0])
			if root is None or ".." in parts:
				findings.append(f"{cid}: code ref {ref!r} is not inside the lending, erpnext or frappe checkout")
				continue
			full = os.path.realpath(os.path.join(root, *parts))
			if not full.startswith(os.path.realpath(root) + os.sep) or not os.path.exists(full):
				findings.append(f"{cid}: code ref {ref!r} does not exist in the installed app")
	return findings, notes


def run():
	"""Check every ingested card. Prints the findings; returns {"findings": [...], "notes": [...], "checked": n}."""
	st = store.load()
	cards = [card for card in (st.card(cid) for cid in sorted(st.cards)) if card is not None]
	cache: dict = {}

	def meta_of(doctype):
		if doctype not in cache:
			cache[doctype] = _meta_of(doctype)
		return cache[doctype]

	sidebar = sidebar_pairs(json.loads(_read_text(SIDEBAR))["items"])
	findings, notes = check_cards(cards, meta_of, sidebar, APP_ROOTS)
	if len(cards) != len(st.cards):
		findings.append(f"{len(st.cards) - len(cards)} indexed card(s) could not be read")
	for line in findings:
		print("FINDING", line)
	print(f"validate: {len(findings)} finding(s), {len(notes)} note(s), {len(cards)} cards checked")
	return {"findings": findings, "notes": sorted(set(notes)), "checked": len(cards)}
