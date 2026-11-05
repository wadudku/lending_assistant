"""M3b store and get_card: approved cards only; no id can build a path (G12)."""

import os
import tempfile

from lending_assistant.kb import ingest, store
from lending_assistant.tests import kb_fixtures as fx
from lending_assistant.tests.base import AssistantTestCase

BAD_IDS = [
	"../x",
	"..",
	"../../etc/passwd",
	"bridge/../../index",
	"/etc/passwd",
	"C:\\windows\\system.ini",
	"\\x",
	"..%2f..%2fetc",
	"%2e%2e%2f",
	"bridge.BR-LMS-162/../..",
	"bridge.BR-LMS-162\x00",
	"bridge.BR-LMS-162.md",
	"cards/bridge/bridge.BR-LMS-162.md",
	" bridge.BR-LMS-162",
	"bridge.BR-LMS-162 ",
	"",
	"x" * 10000,
	None,
	7,
	1.5,
	["bridge.BR-LMS-162"],
	{"id": "x"},
	b"bridge.BR-LMS-162",
	"file:///etc/passwd",
	"http://x/y",
	"index",
	"index.json",
	"ingest_manifest.json",
	"BRIDGE.BR-LMS-162",
	"bridge.br-lms-162",
]


class TestStore(AssistantTestCase):
	def test_known_id_returns_front_matter_and_body(self):
		card = store.get_card("bridge.BR-LMS-162")
		self.assertEqual(card["id"], "bridge.BR-LMS-162")
		self.assertEqual(card["status"], "approved")
		self.assertEqual(card["version"], 1)
		self.assertEqual(card["doctypes"], ["Loan Repayment"])
		self.assertIn("Apply each payment only once", card["title"])
		self.assertIn("Business need", card["body"])
		self.assertTrue(len(card["sources"]) >= 3)

	def test_unknown_and_hostile_ids_give_none(self):
		for bad in BAD_IDS:
			with self.subTest(bad=bad if not isinstance(bad, str) else bad[:40]):
				self.assertIsNone(store.get_card(bad))

	def test_store_has_no_path_argument_besides_the_root(self):
		"""get_card(card_id, root=None): a path argument exists only for tests and is never fed from a card id."""
		import inspect

		self.assertEqual(list(inspect.signature(store.get_card).parameters), ["card_id", "root"])
		self.assertEqual(list(inspect.signature(store.Store.card).parameters), ["self", "card_id"])

	def test_only_approved_cards_are_reachable(self):
		source = fx.make_source()
		out = tempfile.mkdtemp(prefix="ast_kb_out_")
		self.addCleanup(fx.cleanup, os.path.dirname(source), out)
		dest, img = os.path.join(out, "knowledge"), os.path.join(out, "kb_img")
		ingest.run(source, dest=dest, img_dest=img, commit=fx.COMMIT)
		# a draft file dropped on disk next to the approved ones, and listed in no index
		path = os.path.join(dest, "cards", "glossary", "glossary.draft.md")
		open(path, "w", encoding="utf-8").write(
			open(os.path.join(source, "cards", "glossary", "glossary.draft.md"), encoding="utf-8").read()
		)
		st = store.load(dest)
		self.addCleanup(store.reset_cache)
		self.assertIsNotNone(st.card("howto.a.b"))
		self.assertIsNone(st.card("glossary.draft"))
		self.assertEqual(sorted(st.cards), ["glossary.term", "howto.a.b"])

	def test_a_card_file_that_is_no_longer_approved_is_not_served(self):
		source = fx.make_source()
		out = tempfile.mkdtemp(prefix="ast_kb_out_")
		self.addCleanup(fx.cleanup, os.path.dirname(source), out)
		dest = os.path.join(out, "knowledge")
		ingest.run(source, dest=dest, img_dest=os.path.join(out, "kb_img"), commit=fx.COMMIT)
		path = os.path.join(dest, "cards", "glossary", "glossary.term.md")
		text = open(path, encoding="utf-8").read().replace("status: approved", "status: draft")
		open(path, "w", encoding="utf-8").write(text)
		self.addCleanup(store.reset_cache)
		self.assertIsNone(store.load(dest).card("glossary.term"))

	def test_an_index_entry_with_a_path_that_is_not_cards_type_id_is_refused(self):
		source = fx.make_source()
		fx.rewrite_index(source, lambda ix: ix["cards"]["howto.a.b"].update(path="../../etc/passwd"))
		self.addCleanup(fx.cleanup, os.path.dirname(source))
		self.addCleanup(store.reset_cache)
		with self.assertRaises(ValueError):
			store.load(source)

	def test_the_store_is_cached_once_per_process(self):
		store.reset_cache()
		self.assertIs(store.load(), store.load())
		first = store.load()
		store.reset_cache()
		self.assertIsNot(first, store.load())

	def test_the_real_set_is_941_approved_cards(self):
		st = store.load()
		self.assertEqual(len(st.cards), 941)
		self.assertTrue(all(entry["status"] == "approved" for entry in st.cards.values()))

	def test_front_matter_parser(self):
		head, body = store.parse_front_matter(
			'---\nid: a.b\ntitle: "Quoted: title, with comma"\nsummary: plain text\nversion: 3\nlist: [A, "B, C", D.E]\n'
			'empty: []\nsources:\n  - "one#1"\n  - "two#2"\nrelated: [x.y]\n---\nBody\n\n---\nnot front matter\n'
		)
		self.assertEqual(head["title"], "Quoted: title, with comma")
		self.assertEqual(head["version"], 3)
		self.assertEqual(head["list"], ["A", "B, C", "D.E"])
		self.assertEqual(head["empty"], [])
		self.assertEqual(head["sources"], ["one#1", "two#2"])
		self.assertEqual(head["related"], ["x.y"])
		self.assertEqual(body, "Body\n\n---\nnot front matter\n")
		self.assertEqual(store.parse_front_matter("no front matter"), ({}, "no front matter"))
