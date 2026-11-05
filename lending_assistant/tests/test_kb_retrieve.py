"""M3b retrieve: lookup first, BM25 only when lookup gives fewer than 3 (or only doctype keys)."""

from lending_assistant.kb import retrieve, store
from lending_assistant.tests.base import AssistantTestCase


def methods(rows):
	return [row["method"] for row in rows]


class TestRetrieve(AssistantTestCase):
	def test_route_doctype_alone_puts_its_screen_card_in_the_top_three(self):
		st = store.load()
		screens = {entry["doctypes"][0]: cid for cid, entry in st.cards.items() if entry["type"] == "screen"}
		for doctype in ("Loan", "Loan Repayment", "Loan Demand", "Loan Write Off", "Loan Product", "Loan Restructure", "Loan Security Shortfall"):
			with self.subTest(doctype=doctype):
				rows = retrieve.retrieve("What is this?", route_doctype=doctype)
				self.assertIn(screens[doctype], [row["id"] for row in rows])

	def test_always_three_with_a_method_each(self):
		for question, route in (
			("Is BR-LMS-168 covered?", None), ("loan interest", None), ("What is this?", "Loan"), ("write-off", None), ("zzzz qqqq", None),
		):
			with self.subTest(question=question):
				rows = retrieve.retrieve(question, route)
				self.assertEqual(len(rows), 3 if question != "zzzz qqqq" else 0)
				self.assertTrue(all(row["method"] in ("lookup", "search") for row in rows))
				self.assertEqual(len({row["id"] for row in rows}), len(rows))

	def test_search_is_the_fallback_only_when_lookup_gives_fewer_than_three(self):
		strong = retrieve.retrieve_detail("Is BR-LMS-168 covered by Frappe Lending?")
		self.assertEqual(methods(strong["top"]), ["lookup"] * 3)
		self.assertGreaterEqual(len(strong["lookup"]), 3)
		none = retrieve.retrieve_detail("Why can't the system keep two copies of a rule with a start date?")
		self.assertEqual(none["lookup"], [])
		self.assertEqual(methods(none["top"]), ["search"] * 3)
		one = retrieve.retrieve_detail("What is dev item D14 about?")
		self.assertEqual(one["lookup"], ["devitem.D14"])
		self.assertEqual(methods(one["top"])[0], "lookup")
		self.assertEqual(methods(one["top"])[1:], ["search", "search"])

	def test_doctype_only_keys_give_two_lookup_cards_and_one_search_card(self):
		detail = retrieve.retrieve_detail("tell me more", "Loan Repayment")
		self.assertEqual(methods(detail["top"]), ["lookup", "lookup", "search"])
		self.assertEqual(len({row["id"] for row in detail["top"]}), 3)

	def test_unknown_route_doctype_and_odd_input_do_not_crash(self):
		self.assertEqual(len(retrieve.retrieve("write off a loan", "No Such Doctype")), 3)
		for question in ("", "   ", None, 5, ["x"], "x" * 5000):
			with self.subTest(question=str(question)[:20]):
				rows = retrieve.retrieve(question)
				self.assertLessEqual(len(rows), 3)

	def test_depth_changes_the_order_not_the_candidates(self):
		question = "What is a write-off?"
		both = retrieve.retrieve_detail(question)
		business = retrieve.retrieve_detail(question, depth="business")
		technical = retrieve.retrieve_detail(question, depth="technical")
		self.assertEqual(set(both["lookup"]), set(business["lookup"]))
		self.assertEqual(set(both["lookup"]), set(technical["lookup"]))
		self.assertNotEqual(business["lookup"], technical["lookup"])

	def test_key_extraction_rules(self):
		keys = retrieve.extract_keys("Check BR-LMS-212 and BR 170r, see section 7.10 and 7.7.1 of the BRD, journey J3 and J11, dev item D14.")
		self.assertEqual(keys["br_id"][0], "BR-LMS-212")
		self.assertIn("BR-LMS-170r", keys["br_id"])
		self.assertEqual(keys["section"], ["7.10", "7.7.1"])
		self.assertEqual(keys["journey"], ["J3", "J11"])
		self.assertEqual(keys["dev_item"], ["D14"])
		self.assertEqual(retrieve.extract_keys("the rate is 10.5% a year, or 1,000.50 taka")["section"], [])
		self.assertEqual(retrieve.extract_keys("a loan")["doctype"], [])  # bare "loan" is not a doctype key
		self.assertEqual(retrieve.extract_keys("the Loan screen")["doctype"], ["Loan"])
		self.assertEqual(retrieve.extract_keys("a customer paid")["doctype"], [])  # a one-word doctype needs its capital
		self.assertEqual(retrieve.extract_keys("a new Customer")["doctype"], ["Customer"])
		self.assertEqual(retrieve.extract_keys("what does sma mean")["term"], [])  # short terms need capitals
		self.assertEqual(retrieve.extract_keys("what does SMA mean")["term"], ["sma"])
		self.assertEqual(retrieve.extract_keys("how is the credit given")["term"], [])  # ordinary word, no state cue
		self.assertIn("written off", retrieve.extract_keys("a written-off loan")["term"])

	def test_no_question_specific_code(self):
		"""The retrieval module holds no card id and no eval question id (a defect if it did)."""
		import re

		source = open(retrieve.__file__, encoding="utf-8").read()
		self.assertFalse(re.search(r"\b(?:bridge|concept|howto|screen|journey|glossary|lifecycle|devitem|decision|brd_section)\.[A-Za-z0-9]", source.replace("brd_section.", "")))
		self.assertFalse(re.search(r"\bR[0-9]{2}\b", source))
