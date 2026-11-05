"""Copy the approved knowledge cards into the app (M3b). A developer tool, run by hand:

    bench --site lending_site execute lending_assistant.kb.ingest.run \\
        --kwargs "{'source': '<BUILD_DIR>/knowledge', 'commit': '<git rev-parse HEAD of the build repo>'}"

It reads only the given source folder and writes only `kb/knowledge/` and `public/kb_img/`. It never touches the
database and is never called by a tool or an API. Only cards that are `status: approved` in the index AND in the card
file are copied; any other state stops the run before anything is written. A second run with the same source and
commit reports new 0 / changed 0 / removed 0.
"""

import hashlib
import json
import os
import re

from lending_assistant.kb import store

IMG_URL = "/assets/lending_assistant/kb_img/"
PACKAGE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DEST = os.path.join(PACKAGE_DIR, "kb", "knowledge")
DEFAULT_IMG_DEST = os.path.join(PACKAGE_DIR, "public", "kb_img")
IMAGE_NAME = re.compile(r"^[A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+\.(png|jpg|jpeg|gif|webp)$")
BODY_IMG = re.compile(r"\]\(\.\./\.\./img/([^)\s]+)\)")
ANY_IMG_LINK = re.compile(r"\]\(([^)\s]*\bimg/[^)\s]*)\)")
MAPS = ("by_doctype", "by_action", "by_br_id", "by_brd_section", "by_journey", "by_dev_item", "by_term")
MANIFEST = "ingest_manifest.json"


class IngestRefused(Exception):
	"""The source is not fit to ingest. Nothing was written."""


# --- the only file helpers (scanner-scoped) ------------------------------------------------------------------------


def _read_bytes(path: str) -> bytes:
	with open(path, "rb") as handle:  # AST-ALLOWED: ingest reads the given source folder and its own destination folders
		return handle.read()


def _write_bytes(root: str, path: str, data: bytes) -> None:
	"""Write `data` to `path`, which must sit inside `root` (one of the two destination folders)."""
	real_root = os.path.realpath(root)
	real = os.path.realpath(path)
	if not real.startswith(real_root + os.sep):
		raise IngestRefused(f"refusing to write outside {root}: {path}")
	os.makedirs(os.path.dirname(real), exist_ok=True)
	temp = real + ".tmp"
	with open(temp, "wb") as handle:  # AST-ALLOWED: ingest writes only under kb/knowledge/ and public/kb_img/ (checked above)
		handle.write(data)
	os.replace(temp, real)


def _list_dir(path: str) -> list[str]:
	if not os.path.isdir(path):
		return []
	return sorted(os.listdir(path))  # AST-ALLOWED: lists the source cards and the two destination folders


def _sha(data: bytes) -> str:
	return hashlib.sha256(data).hexdigest()


# --- plan: read, check and compute everything before the first write -------------------------------------------------


def _rewrite(text: str, card_id: str) -> tuple[str, list[str]]:
	"""Return (text with image links rewritten, image names used by the body and the front matter)."""
	head_end = text.find("\n---\n", 3)
	head, rest = text[: head_end + 1], text[head_end + 1 :]
	found: list[str] = []

	def body_link(match):
		found.append(match.group(1))
		return "](" + IMG_URL + match.group(1) + ")"

	rest = BODY_IMG.sub(body_link, rest)
	for link in ANY_IMG_LINK.findall(rest):
		if not link.startswith(IMG_URL):
			raise IngestRefused(f"{card_id}: image link {link!r} does not follow ../../img/<folder>/<file>")
	lines = []
	for line in head.split("\n"):
		if line.startswith("images:") and "[" in line and not line.rstrip().endswith("[]"):
			inner = line[line.index("[") + 1 : line.rindex("]")]
			names = [item.strip().strip('"') for item in inner.split(",") if item.strip()]
			for name in names:
				if not name.startswith("img/"):
					raise IngestRefused(f"{card_id}: front matter image {name!r} is not img/<folder>/<file>")
				found.append(name[4:])
			line = "images: [" + ", ".join(IMG_URL + name[4:] for name in names) + "]"
		lines.append(line)
	return "\n".join(lines) + rest, found


def _filter_index(index: dict, keep: dict) -> dict:
	out = {key: value for key, value in index.items() if key not in ("cards", "keywords", *MAPS)}
	out["cards"] = keep
	out["keywords"] = {cid: value for cid, value in index.get("keywords", {}).items() if cid in keep}
	for name in MAPS:
		filtered = {}
		for key, ids in index.get(name, {}).items():
			ids = [cid for cid in ids if cid in keep]
			if ids:
				filtered[key] = ids
		out[name] = filtered
	return out


def _plan(source: str, commit: str) -> dict:
	index = json.loads(_read_bytes(os.path.join(source, "index.json")))
	files: dict[str, bytes] = {}  # relative path under the knowledge folder -> bytes
	images: dict[str, bytes] = {}  # relative path under the image folder -> bytes
	cards, entries, used = [], {}, set()
	skipped = []
	for card_id in sorted(index["cards"]):
		entry = index["cards"][card_id]
		if entry.get("status") != "approved":
			skipped.append(card_id)
			continue
		if not store.CARD_ID.match(card_id) or entry.get("type") not in store.TYPES:
			raise IngestRefused(f"bad card id or type in the index: {card_id!r}")
		rel = f"cards/{entry['type']}/{card_id}.md"
		if entry.get("path") != rel:
			raise IngestRefused(f"{card_id}: index path {entry.get('path')!r} is not {rel}")
		try:
			raw = _read_bytes(os.path.join(source, *rel.split("/")))
		except OSError:
			raise IngestRefused(f"{card_id}: approved in the index but the card file is missing")
		text = raw.decode("utf-8")
		head, _body = store.parse_front_matter(text)
		for field in ("id", "type", "version", "status"):
			if head.get(field) != (card_id if field == "id" else entry.get(field)):
				raise IngestRefused(f"{card_id}: card file {field}={head.get(field)!r} differs from the index {entry.get(field)!r}")
		if head.get("status") != "approved":
			raise IngestRefused(f"{card_id}: the card file is not status: approved")
		new_text, names = _rewrite(text, card_id)
		data = new_text.encode("utf-8")
		files[rel] = data
		used.update(names)
		cards.append({
			"id": card_id, "type": entry["type"], "version": entry["version"], "status": "approved",
			"sha256_source": _sha(raw), "sha256": _sha(data),
		})  # fmt: skip
		entries[card_id] = {
			**entry, "images": [IMG_URL + name[4:] if name.startswith("img/") else name for name in entry.get("images", [])]
		}
	if not entries:
		raise IngestRefused("no approved cards in the source index")
	for name in sorted(used):
		if not IMAGE_NAME.match(name) or ".." in name:
			raise IngestRefused(f"image name {name!r} is not <folder>/<file>.png")
		try:
			images[name] = _read_bytes(os.path.join(source, "img", *name.split("/")))
		except OSError:
			raise IngestRefused(f"image img/{name} is used by a card but is missing from the source")
	kept = _filter_index(index, entries)
	index_bytes = (json.dumps(kept, sort_keys=True, ensure_ascii=False, indent=1) + "\n").encode("utf-8")
	files["index.json"] = index_bytes
	manifest = {
		"schema": 1,
		"lending_version": index.get("lending_version"),
		"source_commit": commit,
		"counts": {"cards": len(cards), "images": len(images)},
		"index_sha256": _sha(index_bytes),
		"cards": cards,
		"images": [{"path": name, "sha256": _sha(data)} for name, data in sorted(images.items())],
	}
	files[MANIFEST] = (json.dumps(manifest, sort_keys=True, ensure_ascii=False, indent=1) + "\n").encode("utf-8")
	return {"files": files, "images": images, "skipped": skipped}


# --- apply -------------------------------------------------------------------------------------------------------------


def _existing(root: str, subfolders) -> set[str]:
	"""Relative paths of the files we own under `root` (cards/<type>/*.md and index/manifest; or image folders)."""
	found = set()
	for sub in subfolders:
		for folder in _list_dir(os.path.join(root, sub)):
			path = os.path.join(root, sub, folder)
			if os.path.isdir(path):
				found.update(f"{sub}/{folder}/{name}" for name in _list_dir(path))
			else:
				found.add(f"{sub}/{folder}")
	return found


def _apply(root: str, wanted: dict[str, bytes], owned: set[str]) -> dict:
	new = changed = removed = 0
	for rel in sorted(wanted):
		path = os.path.join(root, *rel.split("/"))
		try:
			current = _read_bytes(path)
		except OSError:
			current = None
		if current == wanted[rel]:
			continue
		_write_bytes(root, path, wanted[rel])
		if current is None:
			new += 1
		else:
			changed += 1
	for rel in sorted(owned - set(wanted)):
		path = os.path.realpath(os.path.join(root, *rel.split("/")))
		if path.startswith(os.path.realpath(root) + os.sep):
			os.remove(path)
			removed += 1
	return {"new": new, "changed": changed, "removed": removed}


def run(source=None, dest=None, img_dest=None, commit=None):
	"""Ingest the approved cards of `source` (the build repo's `knowledge/` folder). `commit` is required."""
	if not source or not isinstance(source, str):
		raise IngestRefused("source= is required: the build repo's knowledge/ folder")
	if not commit or not isinstance(commit, str) or not re.fullmatch(r"[0-9a-f]{7,40}", commit):
		raise IngestRefused("commit= is required: the build repo commit the cards come from (git rev-parse HEAD)")
	dest = dest or DEFAULT_DEST
	img_dest = img_dest or DEFAULT_IMG_DEST
	plan = _plan(os.path.abspath(source), commit)
	owned_dest = _existing(dest, ["cards"]) | {name for name in _list_dir(dest) if name in ("index.json", MANIFEST)}
	owned_img = _existing(img_dest, [""]) if os.path.isdir(img_dest) else set()
	owned_img = {name.lstrip("/") for name in owned_img}
	first = _apply(dest, plan["files"], owned_dest)
	second = _apply(img_dest, plan["images"], owned_img)
	result = {key: first[key] + second[key] for key in first}
	result.update(cards=len(plan["files"]) - 2, images=len(plan["images"]), commit=commit, drafts_skipped=len(plan["skipped"]))
	store.reset_cache()
	print(
		f"ingest: new {result['new']} / changed {result['changed']} / removed {result['removed']}; "
		f"{result['cards']} approved cards, {result['images']} images, {result['drafts_skipped']} not approved and skipped"
	)
	return result
