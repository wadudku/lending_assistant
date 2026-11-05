"""M3b ingest: approved cards only, idempotent, manifest hashes, image links rewritten, writes only to its two folders."""

import hashlib
import json
import os
import re
import tempfile

from lending_assistant.kb import ingest, store
from lending_assistant.tests import kb_fixtures as fx
from lending_assistant.tests.base import AssistantTestCase


class TestIngest(AssistantTestCase):
	def setUp(self):
		super().setUp()
		self.source = fx.make_source()
		self.out = tempfile.mkdtemp(prefix="ast_kb_out_")
		self.dest = os.path.join(self.out, "knowledge")
		self.img = os.path.join(self.out, "kb_img")
		self.addCleanup(fx.cleanup, os.path.dirname(self.source), self.out)

	def run_ingest(self, **kw):
		return ingest.run(self.source, dest=self.dest, img_dest=self.img, commit=kw.pop("commit", fx.COMMIT), **kw)

	def test_copies_approved_cards_only(self):
		result = self.run_ingest()
		self.assertEqual(result["cards"], 2)
		self.assertEqual(result["drafts_skipped"], 1)
		self.assertTrue(os.path.exists(os.path.join(self.dest, "cards", "howto", "howto.a.b.md")))
		self.assertFalse(os.path.exists(os.path.join(self.dest, "cards", "glossary", "glossary.draft.md")))
		index = json.load(open(os.path.join(self.dest, "index.json")))
		self.assertEqual(sorted(index["cards"]), ["glossary.term", "howto.a.b"])
		self.assertEqual(index["by_term"]["term"], ["glossary.term"])  # the draft is filtered out of every map
		self.assertNotIn("glossary.draft", index["keywords"])

	def test_refuses_a_card_file_that_is_not_approved(self):
		fx.cleanup(self.source)
		self.source = fx.make_source(draft_file_says_approved=False)
		fx.rewrite_index(self.source, lambda ix: ix["cards"]["glossary.draft"].update(status="approved"))  # index says approved, file says draft
		with self.assertRaises(ingest.IngestRefused) as caught:
			self.run_ingest()
		self.assertIn("glossary.draft", str(caught.exception))
		self.assertFalse(os.path.exists(self.dest), "a refused run writes nothing")
		self.assertFalse(os.path.exists(self.img))

	def test_refuses_a_version_mismatch_and_a_missing_file_and_a_missing_image(self):
		for edit, word in (
			(lambda ix: ix["cards"]["howto.a.b"].update(version=9), "version"),
			(lambda ix: ix["cards"].__setitem__("glossary.ghost", {**ix["cards"]["glossary.term"], "path": "cards/glossary/glossary.ghost.md"}), "missing"),
		):
			fx.cleanup(os.path.dirname(self.source))
			self.source = fx.make_source()
			fx.rewrite_index(self.source, edit)
			with self.assertRaises(ingest.IngestRefused) as caught:
				self.run_ingest()
			self.assertIn(word, str(caught.exception))
		os.remove(os.path.join(self.source, "img", "J1", "one.png"))
		with self.assertRaises(ingest.IngestRefused):
			self.run_ingest()

	def test_commit_is_required_and_must_look_like_a_hash(self):
		for bad in (None, "", "HEAD", "../x", "zz" * 20):
			with self.subTest(bad=bad), self.assertRaises(ingest.IngestRefused):
				ingest.run(self.source, dest=self.dest, img_dest=self.img, commit=bad)

	def test_second_run_is_idempotent(self):
		first = self.run_ingest()
		self.assertEqual((first["new"], first["changed"], first["removed"]), (5, 0, 0))  # 2 cards, index, manifest, 1 image
		before = {**fx.tree_files(self.dest), **{"img/" + k: v for k, v in fx.tree_files(self.img).items()}}
		second = self.run_ingest()
		self.assertEqual((second["new"], second["changed"], second["removed"]), (0, 0, 0))
		after = {**fx.tree_files(self.dest), **{"img/" + k: v for k, v in fx.tree_files(self.img).items()}}
		self.assertEqual(before, after, "no file was rewritten")

	def test_a_removed_source_card_is_removed_and_a_new_commit_changes_only_the_manifest(self):
		self.run_ingest()
		third = self.run_ingest(commit="b" * 40)
		self.assertEqual((third["new"], third["changed"], third["removed"]), (0, 1, 0))
		os.remove(os.path.join(self.source, "cards", "glossary", "glossary.term.md"))
		fx.rewrite_index(self.source, lambda ix: ix["cards"].pop("glossary.term"))
		gone = self.run_ingest()
		self.assertEqual(gone["removed"], 1)
		self.assertFalse(os.path.exists(os.path.join(self.dest, "cards", "glossary", "glossary.term.md")))

	def test_manifest_hashes_match_the_files_on_disk(self):
		self.run_ingest()
		manifest = json.load(open(os.path.join(self.dest, "ingest_manifest.json")))
		self.assertEqual(manifest["source_commit"], fx.COMMIT)
		self.assertEqual(manifest["counts"], {"cards": 2, "images": 1})
		for row in manifest["cards"]:
			data = open(os.path.join(self.dest, "cards", row["type"], row["id"] + ".md"), "rb").read()
			self.assertEqual(hashlib.sha256(data).hexdigest(), row["sha256"])
			source = open(os.path.join(self.source, "cards", row["type"], row["id"] + ".md"), "rb").read()
			self.assertEqual(hashlib.sha256(source).hexdigest(), row["sha256_source"])
		index_bytes = open(os.path.join(self.dest, "index.json"), "rb").read()
		self.assertEqual(hashlib.sha256(index_bytes).hexdigest(), manifest["index_sha256"])
		for row in manifest["images"]:
			data = open(os.path.join(self.img, *row["path"].split("/")), "rb").read()
			self.assertEqual(hashlib.sha256(data).hexdigest(), row["sha256"])

	def test_image_links_are_rewritten_and_unused_images_are_not_copied(self):
		self.run_ingest()
		text = open(os.path.join(self.dest, "cards", "howto", "howto.a.b.md"), encoding="utf-8").read()
		self.assertIn("](/assets/lending_assistant/kb_img/J1/one.png)", text)
		self.assertIn("images: [/assets/lending_assistant/kb_img/J1/one.png]", text)
		self.assertNotIn("../../img", text)
		self.assertTrue(os.path.exists(os.path.join(self.img, "J1", "one.png")))
		self.assertFalse(os.path.exists(os.path.join(self.img, "J1", "unused.png")))

	def test_a_link_that_does_not_follow_the_pattern_stops_the_run(self):
		path = os.path.join(self.source, "cards", "glossary", "glossary.term.md")
		text = open(path, encoding="utf-8").read().replace("Body text.", "![x](../img/J1/one.png)")
		open(path, "w", encoding="utf-8").write(text)
		with self.assertRaises(ingest.IngestRefused):
			self.run_ingest()

	def test_it_cannot_write_outside_its_two_folders(self):
		with self.assertRaises(ingest.IngestRefused):
			ingest._write_bytes(self.dest, os.path.join(self.out, "elsewhere.txt"), b"x")
		with self.assertRaises(ingest.IngestRefused):
			ingest._write_bytes(self.dest, os.path.join(self.dest, "..", "evil.txt"), b"x")
		self.assertFalse(os.path.exists(os.path.join(self.out, "evil.txt")))

	def test_the_ingested_app_copy_matches_the_manifest(self):
		"""The real set: 941 approved cards, no draft, hashes match, images equal the ones the cards use."""
		manifest = json.load(open(os.path.join(store.KB_ROOT, "ingest_manifest.json")))
		self.assertEqual(manifest["counts"]["cards"], 941)
		self.assertRegex(manifest["source_commit"], r"^[0-9a-f]{40}$")
		on_disk = {name for kind in os.listdir(os.path.join(store.KB_ROOT, "cards")) for name in os.listdir(os.path.join(store.KB_ROOT, "cards", kind))}
		self.assertEqual(len(on_disk), 941)
		self.assertEqual(on_disk, {row["id"] + ".md" for row in manifest["cards"]})
		for row in manifest["cards"]:
			data = open(os.path.join(store.KB_ROOT, "cards", row["type"], row["id"] + ".md"), "rb").read()
			self.assertEqual(hashlib.sha256(data).hexdigest(), row["sha256"], row["id"])
			self.assertIn(b"\nstatus: approved\n", data)
		used = set()
		for row in manifest["cards"]:
			text = open(os.path.join(store.KB_ROOT, "cards", row["type"], row["id"] + ".md"), encoding="utf-8").read()
			used.update(m.split("/kb_img/", 1)[1] for m in re.findall(r"/assets/lending_assistant/kb_img/[^)\s,\]]+", text))
		img_root = os.path.join(os.path.dirname(os.path.dirname(store.KB_ROOT)), "public", "kb_img")
		files = {f"{d}/{n}" for d in os.listdir(img_root) for n in os.listdir(os.path.join(img_root, d))}
		self.assertEqual(files, used)
		self.assertEqual(files, {row["path"] for row in manifest["images"]})
