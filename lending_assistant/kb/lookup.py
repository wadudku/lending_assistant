"""Key lookup over the ingested index (PLAN §5.5, §5.6). Pure Python over plain dicts: no files, no database.

`lookup(...)` takes explicit keys (doctype, action, BR id, BRD section, term, journey, dev item), normalises them,
finds cards through the index's own `by_*` maps and returns ranked SUMMARIES (id, type, title, summary, version,
status). A card body is never returned here.

#103: `dev_item` resolves only to the card `devitem.D<n>` (D1..D20). It never reaches the many cards that merely
list `D<n>` in their front matter, and nothing reads card text, so a "D3" inside a BRD quote or a section 12/13 card
can never become a dev item.
"""

import re

from lending_assistant.kb import store

FAMILIES = ("LMS", "LOS", "INT", "GOV")
MAX_RESULTS = 10
MAX_ARG_CHARS = 200

# Weights of one key on one card (general constants; a card matched by several keys adds them).
W_BR = 60  # a card that lists the BR id
W_BR_NAMED = 120  # the concept / bridge card named for the BR id
W_DEV = 100
W_JOURNEY = 100
W_JOURNEY_HOWTO = 30
W_SECTION = 50
W_SECTION_NAMED = 90
W_SECTION_PARENT = 40
W_ACTION = 80
W_TERM = 70
W_DOCTYPE = 40
W_SCREEN = 30  # extra for the screen card of a doctype
W_MENTION = 20  # the part of a doctype name after "Loan " written alone (refund -> Loan Refund)
W_ROUTE = 35
W_ROUTE_SCREEN = 30

_BR = re.compile(r"^(?:BR[\s_\-]?)?(?:(LMS|LOS|INT|GOV)[\s_\-]?)?(\d{1,3})([a-z])?$", re.I)
_SECTION = re.compile(
	r"^(?:(?:section|sec|clause|chapter|brd|para)\s*)?§?\s*(\d{1,2}(?:\.\d{1,2}){0,3})$", re.I
)
_DEV = re.compile(r"^(?:dev(?:elopment)?[\s_\-]*item[\s_\-]*)?D?[\s_\-]*(\d{1,2})$", re.I)
_JOURNEY = re.compile(r"^(?:J|journey[\s_\-]*J?)[\s_\-]*(\d{1,2})$", re.I)
_SEP = re.compile(r"[\s_\-]+")


def _clean(value) -> str | None:
	if not isinstance(value, str):
		return None
	value = value.strip()
	return value if value and len(value) <= MAX_ARG_CHARS and "\x00" not in value else None


def norm_term(text: str) -> str:
	"""`Write-Off`, `write off`, `write_off` -> `write off`."""
	return _SEP.sub(" ", text.strip().lower())


def vocabulary(st) -> dict:
	cache = st.derived.get("lookup")
	if cache is None:
		terms: dict[str, str] = {}
		for key in st.map("by_term"):
			terms.setdefault(norm_term(key), key)
		doctypes: dict[str, str] = {}
		for key in st.map("by_doctype"):
			doctypes.setdefault(norm_term(key), key)
		screens = {
			entry["doctypes"][0]: cid
			for cid, entry in st.cards.items()
			if entry["type"] == "screen" and entry.get("doctypes")
		}
		cache = st.derived["lookup"] = {"terms": terms, "doctypes": doctypes, "screens": screens}
	return cache


# --- normalisers (also used by retrieve) -----------------------------------------------------------------------------


def normalise_br_id(value, st=None) -> list[str]:
	"""Canonical BR keys: `BR-LMS-123`, `123`, `br-lms-123`, `170r`, `BR-LOS-002a`. A bare number can be in several
	families, so it expands to every family that has it (LMS first)."""
	st = st or store.load()
	text = _clean(value)
	match = _BR.match(text) if text else None
	if not match:
		return []
	family, number, letter = match.group(1), match.group(2).zfill(3), (match.group(3) or "").lower()
	families = [family.upper()] if family else FAMILIES
	keys = [f"BR-{fam}-{number}{letter}" for fam in families]
	return [key for key in keys if br_cards(key, st)]


def br_cards(key: str, st) -> list[str]:
	"""Cards for one canonical BR key. `170r` is not in by_br_id, only in card ids, so look at both."""
	ids = list(st.map("by_br_id").get(key, []))
	for kind in ("concept", "bridge"):
		cid = f"{kind}.{key}"
		if cid in st.cards and cid not in ids:
			ids.append(cid)
	return ids


def normalise_section(value) -> str | None:
	text = _clean(value)
	match = _SECTION.match(text) if text else None
	return match.group(1) if match else None


def normalise_dev_item(value) -> str | None:
	text = _clean(value)
	match = _DEV.match(text) if text else None
	if not match or not 1 <= int(match.group(1)) <= 20:
		return None
	return f"D{int(match.group(1))}"


def normalise_journey(value, st=None) -> str | None:
	st = st or store.load()
	text = _clean(value)
	match = _JOURNEY.match(text) if text else None
	if not match:
		return None
	key = f"J{int(match.group(1))}"
	return key if key in st.map("by_journey") else None


def normalise_term(value, st=None) -> str | None:
	"""The by_term key for a word or phrase (case, hyphen, underscore, a trailing plural s), or None."""
	st = st or store.load()
	text = _clean(value)
	if not text:
		return None
	terms = vocabulary(st)["terms"]
	key = norm_term(text)
	for candidate in (key, key[:-1] if key.endswith("s") else key):
		if candidate in terms:
			return terms[candidate]
	return None


def normalise_doctype(value, st=None) -> str | None:
	"""The by_doctype key for a doctype name (case, snake_case, plural), or None."""
	st = st or store.load()
	text = _clean(value)
	if not text:
		return None
	names = vocabulary(st)["doctypes"]
	key = norm_term(text)
	for candidate in (key, key[:-1] if key.endswith("s") else key):
		if candidate in names:
			return names[candidate]
	return None


# --- scoring -----------------------------------------------------------------------------------------------------------


def score_keys(st, keys: dict) -> dict[str, int]:
	"""id -> score for already-normalised keys:
	br_id [BR-LMS-123], dev_item [D12], journey [J3], section [7.7], term [by_term keys], action [Doctype:action],
	doctype [name], route [name]. Unknown keys add nothing."""
	scores: dict[str, int] = {}

	def add(cid, points):
		if cid in st.cards:
			scores[cid] = scores.get(cid, 0) + points

	for key in keys.get("br_id", []):
		for cid in br_cards(key, st):
			add(
				cid,
				W_BR_NAMED
				if cid.endswith("." + key) and cid.split(".")[0] in ("concept", "bridge")
				else W_BR,
			)
	for key in keys.get("dev_item", []):
		add(f"devitem.{key}", W_DEV)  # only the dev item card (#103)
	for key in keys.get("journey", []):
		add(f"journey.{key}", W_JOURNEY)
		for cid in st.map("by_journey").get(key, []):
			if cid != f"journey.{key}":
				add(cid, W_JOURNEY_HOWTO)
	for key in keys.get("section", []):
		node = key
		while node:
			listed = st.map("by_brd_section").get(node)
			if listed is not None:
				for cid in listed:
					add(
						cid,
						W_SECTION_NAMED
						if cid == f"brd_section.{node}"
						else W_SECTION
						if node == key
						else W_SECTION_PARENT,
					)
				break
			node = node.rpartition(".")[0]
	for key in keys.get("term", []):
		for cid in st.map("by_term").get(key, []):
			add(cid, W_TERM)
	for key in keys.get("action", []):
		for cid in st.map("by_action").get(key, []):
			add(cid, W_ACTION)
	screens = vocabulary(st)["screens"]
	for field, weight, screen_weight in (
		("doctype", W_DOCTYPE, W_SCREEN), ("route", W_ROUTE, W_ROUTE_SCREEN), ("mention", W_MENTION, 0),
	):  # fmt: skip
		for name in keys.get(field, []):
			for cid in st.map("by_doctype").get(name, []):
				add(cid, weight)
			if name in screens and screen_weight:
				add(screens[name], screen_weight)
	return scores


def rank(st, scores: dict[str, int], tilt: dict[str, int] | None = None, tie=None) -> list[str]:
	"""Best first. `tilt` adds points by card type; `tie` (id -> number) breaks equal totals, then the id."""
	tilt = tilt or {}
	tie = tie or {}

	def sort_key(cid):
		return (-(scores[cid] + tilt.get(st.cards[cid]["type"], 0)), -tie.get(cid, 0), cid)

	return sorted(scores, key=sort_key)


def lookup(
	doctype=None, action=None, br_id=None, brd_section=None, term=None, journey=None, dev_item=None, st=None
):
	"""Ranked summaries (at most 10) for the given keys. Any key that is empty or unknown is ignored."""
	st = st or store.load()
	keys: dict[str, list[str]] = {}
	if br_id is not None:
		keys["br_id"] = normalise_br_id(br_id, st)
	if brd_section is not None:
		section = normalise_section(brd_section)
		keys["section"] = [section] if section else []
	if journey is not None:
		found = normalise_journey(journey, st)
		keys["journey"] = [found] if found else []
	if dev_item is not None:
		found = normalise_dev_item(dev_item)
		keys["dev_item"] = [found] if found else []
	if term is not None:
		found = normalise_term(term, st)
		keys["term"] = [found] if found else []
	name = normalise_doctype(doctype, st) if doctype is not None else None
	if doctype is not None:
		keys["doctype"] = [name] if name else []
	if action is not None:
		text = _clean(action)
		actions = []
		if text and ":" in text:
			actions = [text] if text in st.map("by_action") else []
		elif text and name:
			slug = norm_term(text).replace(" ", "_")
			actions = [f"{name}:{slug}"] if f"{name}:{slug}" in st.map("by_action") else []
		elif text:
			slug = norm_term(text).replace(" ", "_")
			actions = [key for key in st.map("by_action") if key.endswith(":" + slug)]
		keys["action"] = actions
	scores = score_keys(st, keys)
	return [st.summary(cid) for cid in rank(st, scores)[:MAX_RESULTS]]
