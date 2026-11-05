"""The retrieval order of PLAN §5.6: lookup first, then BM25 (M3b). This is what the eval measures and what M4's
orchestrator will call. Pure Python over the ingested index; no files, no database.

`retrieve(question, route_doctype, depth)` returns exactly the top 3 cards (when the base has that many), each with the
method that found it ("lookup" or "search"). General rules only: keys are found by pattern and by the index's own
vocabulary (BR ids, sections, journeys, dev items, terms, doctype names, action words); nothing is keyed to a question
or a card.
"""

import re
import unicodedata

from lending_assistant.kb import lookup, search, store

TOP = 3
LOOKUP_MIN = 3  # search runs only when lookup gives fewer cards than this
MAX_QUESTION_CHARS = 1000
SEARCH_TILT_SHARE = 0.8  # an intent tilt is worth this fraction of itself on a BM25 score
STRONG = ("br_id", "section", "journey", "dev_item", "term", "action")  # keys that are more than a doctype

_BR_FULL = re.compile(
	r"(?<![A-Za-z0-9])(?:BR[\s_\-]?)?(LMS|LOS|INT|GOV)[\s_\-]?(\d{1,3})([rca])?(?![A-Za-z0-9])", re.I
)
_BR_BARE = re.compile(
	r"(?<![A-Za-z0-9])(?:BR|requirement|req|rule)[\s_\-#]*(\d{1,3})([rca])?(?![A-Za-z0-9])", re.I
)
_SECTION_WORD = re.compile(
	r"(?:section|sec\.?|clause|chapter|brd|§|para(?:graph)?)\s*(\d{1,2}(?:\.\d{1,2}){0,3})(?!\d)", re.I
)
_SECTION_DOTTED = re.compile(r"(?<![\d.,A-Za-z])(\d{1,2}\.\d{1,2}(?:\.\d{1,2})?)(?![\d%]|,\d|\.\d)")
_JOURNEY = re.compile(r"(?<![A-Za-z0-9])J\s?-?(\d{1,2})(?![A-Za-z0-9])|\bjourney\s*J?\s*-?(\d{1,2})\b", re.I)
_DEV_NAMED = re.compile(r"\bdev(?:elopment)?[\s_\-]*items?\s*D?\s*-?(\d{1,2})\b", re.I)
_DEV_BARE = re.compile(r"(?<![A-Za-z0-9_\-])D\s?-?(\d{1,2})(?![A-Za-z0-9])")  # capital D only
_DEV_NOT = re.compile(
	r"\b(?:dependency|dependencies|risk|risks|brd|section\s*1[23]|nrb\s+must|mitigation|assumption)\b", re.I
)  # #103: "D3" near these words is the BRD's own numbering
_STATE_CUE = re.compile(
	r"\b(?:status|state|stage|flag|label|labelled|labeled|class|classified|loan is|goes to|becomes)\b"
)

# Ordinary English words that are also states or terms: they count as a term only with a cue nearby (or in capitals).
COMMON_TERMS = {
	"active", "application", "booked", "bot", "batch", "bill", "closed", "credit", "demand", "ledger", "partner",
	"settled", "standard", "override", "classification", "sampling", "provision", "entry date",
}  # fmt: skip

# General English action words -> the action slug used in the index (`Doctype:slug`).
ACTION_WORDS = [
	(r"\b(?:create|creating|new|add|record|enter|raise|book|make|open)\b", "create"),
	(r"\b(?:submit|post|posting|finali[sz]e|confirm)\b", "submit"),
	(r"\b(?:cancel|reverse|undo)\b", "cancel"),
	(r"\b(?:view|see|show|find|look(?:ing)? (?:up|at)|check|display|list|history)\b", "view"),
	(r"\b(?:approve|approval|sign[- ]off)\b", "approve"),
	(r"\b(?:waive|waiver)\b", "waive"),
	(r"\b(?:freeze|frozen|block)\b", "freeze"),
	(r"\b(?:settle|settlement)\b", "settle"),
	(r"\b(?:close|closure|clear)\b", "close_loan"),
	(r"\b(?:pay ahead|prepay|prepayment|pay in advance|in advance)\b", "pay_ahead"),
	(r"\b(?:run|process|trigger|execute|generate)\b", "run"),
	(r"\b(?:pledge|collateral)\b", "pledge"),
	(r"\b(?:payoff|pay off)\b", "payoff_figure"),
]

# What the question is asking for -> a tilt (points) on card types. Tilts rank candidates; they never create one.
INTENTS = [
	(r"\bhow (?:do|can|should|would|could) (?:i|we|you|someone|a|an|the)\b|\bhow to\b|\bsteps?\b|\bwhere do i (?:click|go)\b", {"howto": 25}),
	(r"\bwhat (?:is|are|does) (?:a|an|the)?\s*\w+(?: \w+)? (?:mean|stand)|\bwhat (?:is|are) (?:a|an|the)\b|\bstands? for\b|\bdefin(?:e|ition)\b|\bwhat does \S+ mean\b", {"glossary": 20, "lifecycle": 15, "concept": 10}),
	(r"\bcovered\b|\bgap\b|\bverdict\b|\bdoes (?:frappe|lending|the app|the system)\b|\bhow does frappe\b|\bsupport(?:s|ed)?\b|\bmatch(?:es)?\b|\bmissing\b|\bwhy (?:can'?t|cannot|doesn'?t|does not|isn'?t|is not|won'?t)\b", {"bridge": 25}),
	(r"\bwhat does the brd\b|\bwhy does the (?:bank|brd|nrb)\b|\bsummari[sz]e\b|\bwhich requirements\b|\bwhat is in section\b|\bwhat does section\b", {"concept": 15, "brd_section": 25}),
	(r"\bplanned\b|\bwhat are we building\b|\bdev(?:elopment)? items?\b|\bbuild for\b|\bto build\b|\bwe build\b|\bproposed\b|\bfix\b", {"devitem": 25}),
	(r"\bend[- ]to[- ]end\b|\bwhole process\b|\bwalk me through\b|\bstages?\b|\bjourney\b|\bfrom start to finish\b", {"journey": 25}),
	(r"\bwho approves\b|\ballowed to\b|\boptions? for\b|\bdifference between\b|\bversus\b|\bvs\.?\b", {"decision": 20}),
	(r"\bscreen\b|\bform\b|\bpage\b|\bwhat am i looking at\b|\bthis (?:record|document)\b|\bwhat is this\b|\bwhat do (?:its|the) \w+ fields\b", {"screen": 25}),
	(r"\b(?:state|status|stage)\b", {"lifecycle": 15}),
]  # fmt: skip
DEPTH_TILT = {
	"business": {"concept": 10, "glossary": 10, "brd_section": 10, "decision": 10},
	"technical": {"bridge": 10, "screen": 10, "howto": 10},
}


def _normal(text: str) -> str:
	return unicodedata.normalize("NFKC", text)[:MAX_QUESTION_CHARS]


def _sep(text: str) -> str:
	"""Lower-case with every run of space, hyphen or underscore as one space, so `write-off` = `write off`."""
	return " " + lookup.norm_term(text) + " "


def _fold(word: str) -> str:
	return word[:-1] if len(word) > 3 and word.endswith("s") and not word.endswith("ss") else word


def _words(text: str) -> list[str]:
	return [_fold(w) for w in re.findall(r"[a-z0-9]+", text.lower())]


# --- key extraction ----------------------------------------------------------------------------------------------------


def _doctypes(text: str, st) -> tuple[list[str], list[str], str]:
	"""Doctype names written in the question, longest first. Returns (names, weak mentions, text with spans blanked)."""
	spaced = _sep(text)
	found, weak = [], []
	names = sorted(lookup.vocabulary(st)["doctypes"].items(), key=lambda kv: -len(kv[0]))
	for norm, name in names:
		if norm == "loan":
			continue  # in almost every question; only "Loan form / screen / record" below counts
		if " " not in norm and not re.search(
			r"(?<![A-Za-z0-9])" + re.escape(name) + r"(?![A-Za-z0-9])", text
		):
			continue  # a one-word doctype (Customer, Branch, Report) counts only when written with its capital
		pattern = r"(?<![a-z0-9])" + re.escape(norm) + r"(?:s|es)?(?![a-z0-9])"
		hit = re.search(pattern, spaced)
		if hit:
			found.append(name)
			spaced = spaced[: hit.start()] + " " * (hit.end() - hit.start()) + spaced[hit.end() :]
	# "refund" for Loan Refund: the part after "Loan " counts as a weaker mention when it is a whole word of 6+ letters
	for norm, name in names:
		tail = norm[5:] if norm.startswith("loan ") else ""
		if name in found or len(tail) < 6 or (" " in tail and len(tail.split()) > 2):
			continue
		hit = re.search(r"(?<![a-z0-9])" + re.escape(tail) + r"(?:s|es)?(?![a-z0-9])", spaced)
		if hit and not any(name.lower() in other.lower() for other in found if other != name):
			weak.append(name)
			spaced = spaced[: hit.start()] + " " * (hit.end() - hit.start()) + spaced[hit.end() :]
	loose = re.search(r"\bloan\b(?= (?:form|screen|doctype|record|page|document)\b)", spaced)
	if loose and "Loan" in st.map("by_doctype") and "Loan" not in found:
		found.append("Loan")
	return found, weak, spaced


def _terms(original: str, blanked: str, st) -> list[str]:
	"""by_term keys found in the question (longest first, spans consumed). Short terms need capitals; ordinary
	English words need a state cue nearby."""
	found, spaced = [], blanked
	terms = sorted(lookup.vocabulary(st)["terms"].items(), key=lambda kv: -len(kv[0]))
	for norm, key in terms:
		if len(norm) <= 3:
			if not re.search(r"(?<![A-Za-z0-9])" + re.escape(key.upper()) + r"(?![A-Za-z0-9])", original):
				continue
			if norm not in spaced:
				continue
		pattern = r"(?<![a-z0-9])" + re.escape(norm) + r"(?:s|es|d|ed)?(?![a-z0-9])"
		hit = re.search(pattern, spaced)
		if not hit:
			continue
		if norm in COMMON_TERMS:
			window = " ".join(spaced[: hit.start()].split()[-4:] + spaced[hit.end() :].split()[:4])
			if not _STATE_CUE.search(window):
				continue
		found.append(key)
		spaced = spaced[: hit.start()] + " " * (hit.end() - hit.start()) + spaced[hit.end() :]
	return found


_QUOTED = re.compile(
	r"(?<![A-Za-z0-9])'[^']*'(?![A-Za-z0-9])|\"[^\"]*\"|\u201c[^\u201d]*\u201d|\u2018[^\u2019]*\u2019"
)


def _quoted_spans(text: str) -> list[tuple[int, int]]:
	return [(m.start(), m.end()) for m in _QUOTED.finditer(text)]


def _in_spans(spans, start: int) -> bool:
	return any(a <= start < b for a, b in spans)


def brd_context(text: str) -> bool:
	"""#103: a BRD-dependency cue word anywhere in the question. Then a bare "D<n>" is the BRD's own numbering."""
	return bool(_DEV_NOT.search(text))


def names_dev_item(text: str) -> bool:
	"""The question names a dev item outright ("dev item 4", "development item D4"), outside any quotes."""
	spans = _quoted_spans(text)
	return any(not _in_spans(spans, m.start()) for m in _DEV_NAMED.finditer(text))


def extract_keys(question: str, route_doctype=None, st=None) -> dict:
	"""The keys the question names. See the module docstring for the rules; each is general."""
	st = st or store.load()
	original = _normal(question) if isinstance(question, str) else ""
	lower = original.lower()
	keys: dict[str, list[str]] = {
		name: []
		for name in (
			"br_id",
			"section",
			"journey",
			"dev_item",
			"term",
			"action",
			"doctype",
			"route",
			"mention",
		)
	}

	def push(name, value):
		if value and value not in keys[name]:
			keys[name].append(value)

	for match in _BR_FULL.finditer(original):
		for key in lookup.normalise_br_id(
			f"BR-{match.group(1).upper()}-{match.group(2)}{(match.group(3) or '').lower()}", st
		):
			push("br_id", key)
	for match in _BR_BARE.finditer(original):
		for key in lookup.normalise_br_id(f"{match.group(1)}{(match.group(2) or '').lower()}", st):
			push("br_id", key)
	by_section = st.map("by_brd_section")
	for match in _SECTION_WORD.finditer(original):
		push("section", match.group(1))
	for match in _SECTION_DOTTED.finditer(original):
		if match.group(1) in by_section:
			push("section", match.group(1))
	for match in _JOURNEY.finditer(original):
		key = lookup.normalise_journey("J" + (match.group(1) or match.group(2)), st)
		push("journey", key)
	quoted = _quoted_spans(original)
	for match in _DEV_NAMED.finditer(original):
		if not _in_spans(quoted, match.start()):
			push("dev_item", lookup.normalise_dev_item(match.group(1)))
	if not brd_context(original):  # #103: with a BRD cue anywhere, or inside quotes, "D<n>" is not a dev item
		for match in _DEV_BARE.finditer(original):
			if not _in_spans(quoted, match.start()):
				push("dev_item", lookup.normalise_dev_item(match.group(1)))

	named, weak, blanked = _doctypes(original, st)
	for name in named:
		push("doctype", name)
	for name in weak:
		push("mention", name)
	route = lookup.normalise_doctype(route_doctype, st) if route_doctype else None
	if route:
		push("route", route)
	for key in _terms(original, blanked, st):
		push("term", key)

	words = _words(lower)
	joined = " " + " ".join(words) + " "
	slugs = set()
	for pattern, slug in ACTION_WORDS:
		if re.search(pattern, lower):
			slugs.add(slug)
	by_action = st.map("by_action")
	for action_key in by_action:
		slug = action_key.partition(":")[2]
		parts = [_fold(p) for p in slug.split("_")]
		if len(parts) >= 2 and " " + " ".join(parts) + " " in joined:
			push("action", action_key)  # a multi-word action named in the question needs no doctype
		elif len(parts) == 1 and parts[0] in words:
			slugs.add(slug)
	for name in [*keys["doctype"], *keys["route"]]:
		for slug in sorted(slugs):
			if f"{name}:{slug}" in by_action:
				push("action", f"{name}:{slug}")
	return keys


def intent_tilt(question: str, depth=None) -> dict[str, int]:
	lower = _normal(question).lower() if isinstance(question, str) else ""
	tilt: dict[str, int] = {}
	for pattern, bump in INTENTS:
		if re.search(pattern, lower):
			for kind, points in bump.items():
				tilt[kind] = tilt.get(kind, 0) + points
	for kind, points in DEPTH_TILT.get(depth, {}).items():
		tilt[kind] = tilt.get(kind, 0) + points
	return tilt


# --- the order of §5.6 ---------------------------------------------------------------------------------------------------


def retrieve_detail(question, route_doctype=None, depth=None, st=None) -> dict:
	"""`{"top": [{"id","method","score"}...], "lookup": [ids best first], "keys": {...}}`."""
	st = st or store.load()
	if not isinstance(question, str) or not question.strip():
		return {"top": [], "lookup": [], "keys": {}}
	keys = extract_keys(question, route_doctype, st)
	tilt = intent_tilt(question, depth)
	text_scores = search.bm25_scores(_normal(question), st)
	points = lookup.score_keys(st, keys)
	ordered = lookup.rank(st, points, tilt, text_scores)
	normal = _normal(question)
	if brd_context(normal) and not names_dev_item(normal):  # #103: no devitem card, from lookup or search
		ordered = [cid for cid in ordered if st.cards[cid]["type"] != "devitem"]
		text_scores = {cid: sc for cid, sc in text_scores.items() if st.cards[cid]["type"] != "devitem"}
	top = [
		{"id": cid, "method": "lookup", "score": points[cid] + tilt.get(st.cards[cid]["type"], 0)}
		for cid in ordered[:TOP]
	]
	doctype_only = bool(ordered) and not any(keys[name] for name in STRONG)
	if doctype_only:
		top = top[: TOP - 1]
	if len(top) < TOP:
		chosen = {item["id"] for item in top}
		adjusted = {
			cid: score + tilt.get(st.cards[cid]["type"], 0) * SEARCH_TILT_SHARE
			for cid, score in text_scores.items()
			if cid not in chosen
		}
		for cid in sorted(adjusted, key=lambda c: (-round(adjusted[c], 9), len(c), c))[: TOP - len(top)]:
			top.append({"id": cid, "method": "search", "score": round(adjusted[cid], 3)})
	return {"top": top, "lookup": ordered, "keys": keys}


def retrieve(question, route_doctype=None, depth=None, st=None) -> list[dict]:
	"""The top 3 cards for a question: lookup first, BM25 only when lookup gives fewer than 3 (or only doctype keys)."""
	return retrieve_detail(question, route_doctype, depth, st)["top"]
