"""Pure rules for team findings (G11, G13; PLAN §10.8), shared by the Assistant Finding controller, the findings tools
and `api/findings.save`. They read the ingested knowledge base and doctype meta; they write nothing.
"""

import json
import re

import frappe

from lending_assistant.kb import lookup as kb_lookup
from lending_assistant.kb import store, validate

MAX_REFS = 10
BR_FORM = re.compile(r"^BR-([A-Za-z]+)-(\d{1,3})([A-Za-z]?)$", re.IGNORECASE)


def lines(text) -> list[str]:
	"""Non-blank, stripped, de-duplicated lines of a one-per-line field (order kept)."""
	found = (" ".join(str(line).split()) for line in str(text or "").replace("\r", "").split("\n"))
	return list(dict.fromkeys(line for line in found if line))


def canonical_br_id(value) -> str | None:
	"""`BR-LMS-162` for a full BR id the knowledge base knows (also 170r / 170c, which are card ids only), else None.
	A bare number is not accepted: a finding must name the requirement unambiguously (D1)."""
	match = BR_FORM.match(str(value or "").strip())
	if not match:
		return None
	text = f"BR-{match.group(1).upper()}-{match.group(2)}{match.group(3).lower()}"
	keys = kb_lookup.normalise_br_id(text)
	return keys[0] if len(keys) == 1 else None


def _as_list(values) -> list[str]:
	if isinstance(values, str):
		return lines(values)
	return lines("\n".join(str(v) for v in (values or [])))


def check_br_ids(values) -> list[str]:
	"""Canonical BR ids; throws naming every unknown one."""
	found = _as_list(values)
	if len(found) > MAX_REFS:
		frappe.throw(f"At most {MAX_REFS} BR ids are allowed.")
	good, bad = [], []
	for item in found:
		key = canonical_br_id(item)
		(good if key else bad).append(key or item)
	if bad:
		frappe.throw("Unknown BR id(s): " + ", ".join(bad[:10]) + ".")
	return list(dict.fromkeys(good))


def check_doctypes(values) -> list[str]:
	"""Doctype names that exist on the site; throws naming every unknown one."""
	found = _as_list(values)
	if len(found) > MAX_REFS:
		frappe.throw(f"At most {MAX_REFS} doctypes are allowed.")
	bad = [d for d in found if not validate.doctype_exists(d)]
	if bad:
		frappe.throw("Unknown doctype(s): " + ", ".join(bad[:10]) + ".")
	return found


def installed_lending_version() -> str:
	return validate.installed_lending_version()


def parse_json_list(text) -> list | None:
	"""A stored JSON list column as a list, or None when it is not one."""
	if isinstance(text, list):
		return text
	try:
		value = json.loads(text) if text else []
	except ValueError:
		return None
	return value if isinstance(value, list) else None


def stale_reasons(cards_used, lending_version) -> list[str]:
	"""Why a finding should be checked again; empty = fresh. A card that is missing from the approved knowledge base, a card
	with another version, or another installed lending version (PLAN §10.8)."""
	reasons = []
	cards = parse_json_list(cards_used)
	if cards is None:
		reasons.append("cards unknown")
		cards = []
	known = store.load().cards
	for card in cards:
		if not isinstance(card, dict) or not card.get("id"):
			continue
		entry = known.get(card["id"])
		if entry is None:
			reasons.append(f"card removed: {card['id']}")
		elif entry.get("version") != card.get("version"):
			reasons.append(f"card changed: {card['id']} v{card.get('version')} -> v{entry.get('version')}")
	installed = installed_lending_version()
	if installed and (lending_version or "") != installed:
		reasons.append(f"lending version {lending_version or '?'} -> {installed}")
	return reasons


def bridge_verdicts(br_ids) -> dict:
	"""{BR id: verdict of its approved bridge card, or None when there is none}."""
	cards = store.load().cards
	return {br: (cards.get(f"bridge.{br}") or {}).get("verdict") for br in _as_list(br_ids)}
