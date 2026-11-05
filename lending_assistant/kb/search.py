"""BM25 over the approved cards' index fields (title, summary, keywords, id), plain Python (M3b, PLAN §5.5, §5.6).

No bodies are read: the index already carries the compiler's `keywords` for every card. One weighted term
frequency per card (BM25F style): title x3, summary x1, the compiler's keywords x1 (they repeat the title and
summary, so the effective weight is title 4, summary 2), card id x2. Okapi BM25 with k1 = 1.2, b = 0.75.
"""

import math
import re

from lending_assistant.kb import store

K1 = 1.2
B = 0.75
TITLE_WEIGHT = 3
SUMMARY_WEIGHT = 1
ID_WEIGHT = 2
MAX_RESULTS = 5
MAX_QUERY_CHARS = 500
STOP = set(
	"a an and are as at be by for from has have in into is it its of on or that the "
	"this to was were will with we you your i our not no do does did can could should would may must".split()
)  # same family as the compiler's list; question words that carry no topic are added here
_TOKEN = re.compile(r"[a-z0-9][a-z0-9\-_.]*[a-z0-9]|[a-z0-9]")


def _fold(token: str) -> str:
	"""A light stem so that payments / payment and applied / apply meet: plural s, `ied` -> `y`, `ed`, `ing`.
	Words ending in ss, us or is are left alone."""
	if len(token) > 4 and token.endswith("ied"):
		return token[:-3] + "y"
	if len(token) > 5 and token.endswith("ing"):
		return token[:-3]
	if len(token) > 4 and token.endswith("ed") and not token.endswith("eed"):
		return token[:-2]
	if len(token) > 3 and token.endswith("s") and not token.endswith(("ss", "us", "is")):
		return token[:-1]
	return token


def tokens(text) -> list[str]:
	"""Lower-case tokens; a hyphenated or dotted compound also yields its parts (`non-performing`, `non`, `performing`)."""
	out: list[str] = []
	for raw in _TOKEN.findall(str(text or "").lower()):
		raw = raw.strip(".-_")
		if not raw:
			continue
		parts = [p for p in re.split(r"[\-_.]", raw) if p]
		pieces = [raw] if len(parts) <= 1 else [raw, *parts]
		for piece in pieces:
			if piece not in STOP:
				out.append(_fold(piece))
	return out


def _build(st) -> dict:
	docs: dict[str, dict] = {}
	for cid, entry in st.cards.items():
		tf: dict[str, float] = {}
		for token in tokens(entry.get("title")):
			tf[token] = tf.get(token, 0) + TITLE_WEIGHT
		for token in tokens(entry.get("summary")):
			tf[token] = tf.get(token, 0) + SUMMARY_WEIGHT
		for key, count in st.map("keywords").get(cid, {}).items():
			for token in tokens(key):
				tf[token] = tf.get(token, 0) + count
		for token in tokens(cid):
			tf[token] = tf.get(token, 0) + ID_WEIGHT
		docs[cid] = {"tf": tf, "len": sum(tf.values())}
	df: dict[str, int] = {}
	for doc in docs.values():
		for token in doc["tf"]:
			df[token] = df.get(token, 0) + 1
	total = sum(doc["len"] for doc in docs.values())
	return {"docs": docs, "df": df, "n": len(docs), "avgdl": total / len(docs) if docs else 0.0}


def _model(st) -> dict:
	model = st.derived.get("bm25")
	if model is None:
		model = st.derived["bm25"] = _build(st)
	return model


def bm25_scores(query, st=None, only_type: str | None = None) -> dict[str, float]:
	"""id -> BM25 score for every card with a positive score."""
	st = st or store.load()
	if not isinstance(query, str):
		return {}
	query_tokens = sorted(set(tokens(query[:MAX_QUERY_CHARS])))
	if not query_tokens:
		return {}
	model = _model(st)
	n, avgdl, df = model["n"], model["avgdl"], model["df"]
	idf = {t: math.log(1 + (n - df[t] + 0.5) / (df[t] + 0.5)) for t in query_tokens if t in df}
	scores: dict[str, float] = {}
	for cid, doc in model["docs"].items():
		if only_type and st.cards[cid]["type"] != only_type:
			continue
		total = 0.0
		for token, weight in idf.items():
			freq = doc["tf"].get(token)
			if freq:
				total += weight * freq * (K1 + 1) / (freq + K1 * (1 - B + B * doc["len"] / avgdl))
		if total > 0:
			scores[cid] = total
	return scores


def ranked(query, st=None, only_type: str | None = None) -> list[tuple[str, float]]:
	"""(id, score) best first. Ties: higher score, then shorter id, then id (deterministic)."""
	scores = bm25_scores(query, st, only_type)
	return sorted(scores.items(), key=lambda item: (-round(item[1], 9), len(item[0]), item[0]))


def search(query, type=None, limit: int = MAX_RESULTS, st=None) -> list[dict]:
	"""Top 5 approved cards for `query`, as summaries (never bodies). Unknown `type` or an empty query gives []."""
	st = st or store.load()
	if type is not None and type not in store.TYPES:
		return []
	limit = max(0, min(int(limit), MAX_RESULTS)) if isinstance(limit, int) else MAX_RESULTS
	out = []
	for cid, score in ranked(query, st, type)[:limit]:
		item = st.summary(cid)
		item["score"] = round(score, 3)
		out.append(item)
	return out
