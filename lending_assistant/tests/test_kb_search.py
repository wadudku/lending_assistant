"""M3b search: BM25 in plain Python."""

import math

from lending_assistant.kb import search, store
from lending_assistant.tests.base import AssistantTestCase


class TestSearch(AssistantTestCase):
	def test_an_exact_title_query_ranks_that_card_first(self):
		st = store.load()
		checked = 0
		for cid in ("bridge.BR-LMS-162", "screen.loan_write_off", "howto.loan_refund.create", "glossary.moratorium", "journey.J9", "devitem.D14"):
			title = st.cards[cid]["title"]
			top = search.search(title)
			self.assertEqual(top[0]["title"], title, f"{title!r} -> {[r['id'] for r in top]}")  # a concept and its bridge share a title
			checked += 1
		self.assertEqual(checked, 6)

	def test_top_five_with_summaries_only(self):
		rows = search.search("loan repayment")
		self.assertEqual(len(rows), 5)
		for row in rows:
			self.assertEqual(set(row), {*store.SUMMARY_KEYS, "score"})
		self.assertEqual(rows, sorted(rows, key=lambda r: -r["score"]))
		self.assertEqual(len(search.search("loan repayment", limit=50)), 5)

	def test_type_filter(self):
		for kind in ("glossary", "howto", "bridge"):
			rows = search.search("payment", type=kind)
			self.assertTrue(rows)
			self.assertTrue(all(row["type"] == kind for row in rows))
		self.assertEqual(search.search("payment", type="nonsense"), [])
		self.assertEqual(search.search("payment", type=3), [])

	def test_empty_and_odd_queries_give_nothing(self):
		for query in ("", "   ", "the of and", "!!!", None, 5, ["x"], "qqqqzzzz"):
			with self.subTest(query=str(query)):
				self.assertEqual(search.search(query), [])

	def test_order_is_deterministic(self):
		self.assertEqual(search.search("interest rate change"), search.search("interest rate change"))

	def test_hyphen_split_and_plural_fold(self):
		self.assertEqual(search.tokens("non-performing"), ["non-perform", "non", "perform"])
		self.assertEqual(search.tokens("Payments"), search.tokens("payment"))
		self.assertEqual(search.tokens("applied"), search.tokens("apply"))
		self.assertEqual(search.tokens("status"), ["status"])
		self.assertEqual(search.tokens("BR-LMS-162"), ["br-lms-162", "br", "lms", "162"])

	def test_bm25_arithmetic_on_a_tiny_corpus(self):
		class Tiny:
			cards = {"ca": {"type": "glossary", "title": "alpha beta", "summary": "", "version": 1, "status": "approved"},
				"cb": {"type": "glossary", "title": "beta gamma", "summary": "", "version": 1, "status": "approved"}}
			derived = {}

			def map(self, name):
				return {}

			def summary(self, cid):
				return dict(self.cards[cid], id=cid)

		st = Tiny()
		scores = search.bm25_scores("alpha", st)
		# documents: tf alpha=3, beta=3, + id token (a / b, weight 2) -> length 3 + 3 + 2 = 8 for ca; cb: 3 + 3 + 2 = 8
		n, df, avgdl, dl, freq = 2, 1, 8.0, 8.0, 3
		idf = math.log(1 + (n - df + 0.5) / (df + 0.5))
		expected = idf * freq * (search.K1 + 1) / (freq + search.K1 * (1 - search.B + search.B * dl / avgdl))
		self.assertEqual(list(scores), ["ca"])
		self.assertAlmostEqual(scores["ca"], expected, places=9)
