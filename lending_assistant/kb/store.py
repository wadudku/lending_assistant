"""The ingested knowledge base, read once per process (PLAN §5.5, M3b).

`kb/knowledge/` holds the approved cards and an `index.json`, both written by `kb/ingest.py` (a developer tool run by
hand). This module loads the index into plain dicts and reads one card file on request.

G12: a model-supplied string is only ever a dict key. `get_card` looks the id up in the index; the file path comes
from the index entry (which `load` checked has the shape `cards/<type>/<id>.md`), joined to a fixed folder. No path
is ever built from a caller's string, so `..`, `/`, absolute paths and encoded forms are not keys and give `None`.
"""

import json
import os
import re

KB_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "knowledge")
TYPES = (
	"brd_section", "concept", "bridge", "lifecycle", "devitem", "screen", "howto", "journey", "decision", "glossary",
)  # fmt: skip
CARD_ID = re.compile(r"^[A-Za-z0-9_.\-]{1,120}$")
SUMMARY_KEYS = ("id", "type", "title", "summary", "version", "status")
_CACHE: dict = {}


def _read_text(path: str) -> str:
	with open(  # AST-ALLOWED: reads an ingested knowledge file; path from the checked index
		path, encoding="utf-8"
	) as handle:
		return handle.read()


# --- front matter: a flat YAML subset (scalars, quoted strings, inline lists, a block list) -------------------------


def _split_items(text: str) -> list[str]:
	"""Split the inside of `[a, "b, c", d]` on commas that are not inside double quotes."""
	items, current, quoted, escaped = [], [], False, False
	for char in text:
		if escaped:
			current.append(char)
			escaped = False
		elif char == "\\" and quoted:
			current.append(char)
			escaped = True
		elif char == '"':
			current.append(char)
			quoted = not quoted
		elif char == "," and not quoted:
			items.append("".join(current))
			current = []
		else:
			current.append(char)
	items.append("".join(current))
	return [item.strip() for item in items if item.strip()]


def _scalar(text: str):
	text = text.strip()
	if len(text) >= 2 and text[0] == '"' and text[-1] == '"':
		try:
			return json.loads(text)
		except ValueError:
			return text[1:-1]
	if len(text) >= 2 and text[0] == "'" and text[-1] == "'":
		return text[1:-1].replace("''", "'")
	return text


def parse_front_matter(text: str) -> tuple[dict, str]:
	"""`(front matter dict, body)`. Lists stay lists of strings; `version` becomes an int."""
	if not text.startswith("---\n"):
		return {}, text
	end = text.find("\n---\n", 3)
	if end == -1:
		return {}, text
	head, body = text[4:end], text[end + 5 :]
	data: dict = {}
	key = None
	for line in head.split("\n"):
		if not line.strip():
			continue
		if line.startswith((" ", "\t")) or line.startswith("- "):
			if key is not None and line.strip().startswith("- "):
				if not isinstance(data.get(key), list):
					data[key] = []
				data[key].append(_scalar(line.strip()[2:]))
			continue
		name, _, value = line.partition(":")
		key, value = name.strip(), value.strip()
		if value.startswith("[") and value.endswith("]"):
			data[key] = [_scalar(item) for item in _split_items(value[1:-1])]
		elif value == "":
			data[key] = ""
		else:
			data[key] = _scalar(value)
	if isinstance(data.get("version"), str) and data["version"].isdigit():
		data["version"] = int(data["version"])
	return data, body.lstrip("\n")


# --- the store -----------------------------------------------------------------------------------------------------


class Store:
	"""Approved cards only. `cards` maps id -> index entry (plain dict); the `by_*` maps are the index's own."""

	def __init__(self, root: str, index: dict):
		self.root = root
		self.index = index
		self.cards = {
			cid: dict(entry) for cid, entry in index["cards"].items() if entry.get("status") == "approved"
		}
		for cid, entry in self.cards.items():
			if not CARD_ID.match(cid) or entry.get("type") not in TYPES:
				raise ValueError(f"bad card entry in index.json: {cid!r}")
			if entry.get("path") != f"cards/{entry['type']}/{cid}.md":
				raise ValueError(f"index.json path for {cid!r} is not cards/<type>/<id>.md")
			if not cid.startswith(entry["type"] + "."):
				raise ValueError(f"card id {cid!r} does not start with its type")
			entry["id"] = cid
		self.derived: dict = {}  # caches built by search / lookup from the index (plain data)

	def map(self, name: str) -> dict:
		return self.index.get(name, {})

	def summary(self, card_id: str) -> dict | None:
		entry = self.cards.get(card_id) if isinstance(card_id, str) else None
		if entry is None:
			return None
		return {key: entry.get(key) for key in SUMMARY_KEYS}

	def card(self, card_id) -> dict | None:
		"""Front matter plus `body` of one approved card, or None. Never builds a path from `card_id`."""
		entry = self.cards.get(card_id) if isinstance(card_id, str) else None
		if entry is None:
			return None
		path = os.path.join(self.root, *entry["path"].split("/"))
		try:
			head, body = parse_front_matter(_read_text(path))
		except OSError:
			return None
		if head.get("id") != entry["id"] or head.get("status") != "approved":
			return None
		head["body"] = body
		return head


def load(root: str | None = None) -> Store:
	"""The store for `root` (default: the ingested folder), cached for the life of the process."""
	root = root or KB_ROOT
	store = _CACHE.get(root)
	if store is None:
		index_path = os.path.join(root, "index.json")
		try:
			index = json.loads(_read_text(index_path))
		except OSError:
			raise RuntimeError(
				"The knowledge base has not been ingested (kb/knowledge/index.json is missing)."
			)
		store = _CACHE[root] = Store(root, index)
	return store


def reset_cache() -> None:
	"""For tests, and after a re-ingest in a running process."""
	_CACHE.clear()


def get_card(card_id, root: str | None = None) -> dict | None:
	return load(root).card(card_id)
