"""M3b lookup: each key, BR id normalisation, terms, and the #103 dev-item rule."""

from lending_assistant.kb import lookup, retrieve, store
from lending_assistant.tests.base import AssistantTestCase


def ids(rows):
	return [row["id"] for row in rows]


class TestLookup(AssistantTestCase):
	def test_each_by_key_finds_its_cards(self):
		self.assertIn("howto.loan_repayment.create", ids(lookup.lookup(doctype="Loan Repayment", action="create")))
		self.assertIn("howto.loan_repayment.create", ids(lookup.lookup(action="Loan Repayment:create")))
		self.assertEqual(ids(lookup.lookup(br_id="BR-LMS-162"))[:2], ["bridge.BR-LMS-162", "concept.BR-LMS-162"])
		self.assertEqual(ids(lookup.lookup(brd_section="7.10"))[0], "brd_section.7.10")
		self.assertIn("glossary.sma", ids(lookup.lookup(term="SMA")))
		self.assertEqual(ids(lookup.lookup(journey="J3"))[0], "journey.J3")
		self.assertEqual(ids(lookup.lookup(dev_item="D12")), ["devitem.D12"])
		self.assertIn("screen.loan_repayment", ids(lookup.lookup(doctype="Loan Repayment")))

	def test_summaries_carry_the_fields_and_never_a_body(self):
		rows = lookup.lookup(br_id="BR-LMS-162")
		self.assertTrue(rows)
		for row in rows:
			self.assertEqual(sorted(row), sorted(store.SUMMARY_KEYS))
			self.assertEqual(row["status"], "approved")
			self.assertNotIn("body", row)
		self.assertLessEqual(len(lookup.lookup(doctype="Loan")), lookup.MAX_RESULTS)

	def test_br_id_normalisation(self):
		wanted = "bridge.BR-LMS-123"
		for text in ("BR-LMS-123", "br-lms-123", "BR LMS 123", "LMS-123", "BR_LMS_123", "  BR-LMS-123  "):
			with self.subTest(text=text):
				self.assertEqual(ids(lookup.lookup(br_id=text))[0], wanted)
		bare = ids(lookup.lookup(br_id="123"))
		self.assertEqual(bare[0], wanted)  # LMS first
		self.assertIn("bridge.BR-LOS-123", bare)  # the same number in another family
		self.assertEqual(ids(lookup.lookup(br_id="BR-LOS-002a"))[0], "bridge.BR-LOS-002a")

	def test_170r_and_170c(self):
		self.assertEqual(ids(lookup.lookup(br_id="170r")), ["bridge.BR-LMS-170r", "concept.BR-LMS-170r"])
		self.assertEqual(ids(lookup.lookup(br_id="BR-LMS-170c")), ["bridge.BR-LMS-170c", "concept.BR-LMS-170c"])
		plain = ids(lookup.lookup(br_id="BR-LMS-170"))
		self.assertTrue({"bridge.BR-LMS-170r", "bridge.BR-LMS-170c"} <= set(plain))

	def test_term_synonyms(self):
		for text in ("write off", "write-off", "Written Off", "WRITE_OFF", "written_off"):
			with self.subTest(text=text):
				self.assertIn("glossary.write-off", ids(lookup.lookup(term=text)))
		self.assertIn("glossary.penal-interest", ids(lookup.lookup(term="penalty interest")))
		self.assertIn("glossary.waiver", ids(lookup.lookup(term="waivers")))

	def test_dev_item_resolves_only_to_the_dev_item_card(self):
		self.assertEqual(ids(lookup.lookup(dev_item="D12")), ["devitem.D12"])
		for text in ("12", "d12", "D 12", "dev item 12", "development item D12", " D12 "):
			with self.subTest(text=text):
				self.assertEqual(ids(lookup.lookup(dev_item=text)), ["devitem.D12"])
		for text in ("D21", "D0", "D2a", "D", "DD12", "12.5", "devitem.D12", "J12", ""):
			with self.subTest(text=text):
				self.assertEqual(lookup.lookup(dev_item=text), [])
		# the index lists many cards under D12; none of them may come back
		st = store.load()
		self.assertGreater(len(st.map("by_dev_item")["D12"]), 3)

	def test_a_D_in_a_brd_quote_or_a_section_12_13_card_is_not_a_dev_item(self):
		"""#103: BRD section 12 and 13 use D1.. for NRB's own dependencies. Lookup reads keys, never card text."""
		for section in ("12", "13"):
			for cid, entry in store.load().cards.items():
				if entry["type"] == "brd_section" and entry["brd_section"].split(".")[0] == section:
					self.assertEqual(entry["dev_items"], [], cid)
		keys = retrieve.extract_keys("What does D3 in BRD section 12 mean?")
		self.assertEqual(keys["dev_item"], [])
		keys = retrieve.extract_keys("The risk D3 in the dependency table, what is it?")
		self.assertEqual(keys["dev_item"], [])
		self.assertEqual(retrieve.extract_keys("What is dev item D3 about?")["dev_item"], ["D3"])
		self.assertEqual(retrieve.extract_keys("What is D3 about?")["dev_item"], ["D3"])
		self.assertNotIn("devitem.D3", [item["id"] for item in retrieve.retrieve("What does D3 in BRD section 12 mean?")][:1])

	def test_unknown_or_hostile_input_gives_nothing(self):
		for kw in (
			{"br_id": "BR-LMS-999"}, {"br_id": "nonsense"}, {"br_id": 5}, {"brd_section": "99.9"}, {"brd_section": "../x"},
			{"journey": "J99"}, {"journey": "x"}, {"term": "no such term"}, {"doctype": "No Such Doctype"}, {"term": "x" * 1000},
			{"action": "nonexistent"}, {"doctype": ["Loan"]}, {"br_id": "BR-LMS-162\x00"},
		):
			with self.subTest(kw=str(kw)[:40]):
				self.assertEqual(lookup.lookup(**kw), [])
		self.assertEqual(lookup.lookup(), [])

	def test_section_walks_up_to_the_parent_when_the_exact_key_has_no_card(self):
		self.assertTrue(ids(lookup.lookup(brd_section="7.7.1")))
		self.assertEqual(lookup.normalise_section("section 7.7"), "7.7")
		self.assertEqual(lookup.normalise_section("§7.7.1"), "7.7.1")
