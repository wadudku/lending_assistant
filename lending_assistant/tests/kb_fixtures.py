"""A tiny synthetic knowledge folder for the M3b tests: one approved card with an image, one approved card without,
one draft card. Built in a temp dir, so the tests never touch kb/knowledge/ or public/kb_img/."""

import json
import os
import shutil
import tempfile

PNG = b"\x89PNG\r\n\x1a\nfake"
COMMIT = "a" * 40


def card_text(card_id, kind, title, status="approved", version=1, body="Body text.\n", images=(), extra=""):
	images_line = "[" + ", ".join(images) + "]"
	return (
		f"---\nid: {card_id}\ntype: {kind}\ntitle: {title}\nsummary: \"Summary of {title}.\"\nbr_ids: []\nbrd_section: 7.7\n"
		f"doctypes: [Loan Repayment]\ndev_items: []\nlending_version: 16.5.1\ncode_refs: []\nimages: {images_line}\n"
		f"sources:\n  - \"sources/x.txt#1\"\nrelated: []\nversion: {version}\nstatus: {status}\n{extra}---\n{body}"
	)


def entry(card_id, kind, title, status="approved", version=1, images=()):
	return {
		"type": kind, "title": title, "summary": f"Summary of {title}.", "status": status, "version": version,
		"path": f"cards/{kind}/{card_id}.md", "br_ids": [], "brd_section": "7.7", "doctypes": ["Loan Repayment"],
		"dev_items": [], "images": list(images), "verdict": None, "analysis_status": None,
	}  # fmt: skip


def make_source(root=None, draft_file_says_approved=False):
	"""Returns the path of a `knowledge/` folder. The draft card is `draft` in the index and in its file."""
	root = root or tempfile.mkdtemp(prefix="ast_kb_src_")
	know = os.path.join(root, "knowledge")
	cards = {
		"howto.a.b": ("howto", "How to do a b", ["img/J1/one.png"]),
		"glossary.term": ("glossary", "A term", []),
		"glossary.draft": ("glossary", "Draft term", []),
	}
	index = {"schema": 1, "lending_version": "16.5.1", "cards": {}, "keywords": {}}
	for name in ("by_doctype", "by_action", "by_br_id", "by_brd_section", "by_journey", "by_dev_item", "by_term"):
		index[name] = {}
	for cid, (kind, title, images) in cards.items():
		draft = cid == "glossary.draft"
		index["cards"][cid] = entry(cid, kind, title, "draft" if draft else "approved", 1, images)
		index["keywords"][cid] = {"term": 1}
		body = "Body text.\n"
		if images:
			body += f"\n![alt](../../{images[0]})\n"
		path = os.path.join(know, "cards", kind, f"{cid}.md")
		os.makedirs(os.path.dirname(path), exist_ok=True)
		status = "approved" if draft and draft_file_says_approved else ("draft" if draft else "approved")
		with open(path, "w", encoding="utf-8") as handle:
			handle.write(card_text(cid, kind, title, status, 1, body, images))
	index["by_doctype"]["Loan Repayment"] = list(cards)
	index["by_term"]["term"] = ["glossary.term", "glossary.draft"]
	os.makedirs(os.path.join(know, "img", "J1"), exist_ok=True)
	for name in ("one.png", "unused.png"):
		with open(os.path.join(know, "img", "J1", name), "wb") as handle:
			handle.write(PNG + name.encode())
	with open(os.path.join(know, "index.json"), "w", encoding="utf-8") as handle:
		json.dump(index, handle)
	return know


def rewrite_index(know, edit):
	path = os.path.join(know, "index.json")
	with open(path, encoding="utf-8") as handle:
		index = json.load(handle)
	edit(index)
	with open(path, "w", encoding="utf-8") as handle:
		json.dump(index, handle)


def tree_files(root):
	out = {}
	for folder, _dirs, files in os.walk(root):
		for name in files:
			full = os.path.join(folder, name)
			out[os.path.relpath(full, root)] = os.path.getmtime(full)
	return out


def cleanup(*paths):
	for path in paths:
		shutil.rmtree(path, True)
