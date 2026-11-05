"""M4b patch (#145): default_effort high -> medium only while it still holds the seeded `high`."""

import frappe

from lending_assistant import install
from lending_assistant.patches import set_default_effort_medium
from lending_assistant.tests.base import AssistantTestCase


class TestEffortPatch(AssistantTestCase):
	def stored(self, value=None):
		settings = frappe.get_doc("Assistant Settings")
		if value is not None:
			settings.default_effort = value
			settings.save(ignore_permissions=True)
		return frappe.get_doc("Assistant Settings").default_effort

	def test_a_seeded_high_becomes_medium(self):
		self.stored("high")
		self.assertTrue(install.lower_default_effort())
		self.assertEqual(self.stored(), "medium")

	def test_any_other_value_is_left_alone(self):
		for value in ("low", "medium", "xhigh", "max"):
			with self.subTest(value=value):
				self.stored(value)
				self.assertFalse(install.lower_default_effort())
				self.assertEqual(self.stored(), value)

	def test_the_second_run_is_a_no_op_and_deep_effort_is_untouched(self):
		self.stored("high")
		deep = frappe.get_doc("Assistant Settings").deep_effort
		set_default_effort_medium.execute()
		set_default_effort_medium.execute()
		self.assertEqual(self.stored(), "medium")
		self.assertEqual(frappe.get_doc("Assistant Settings").deep_effort, deep)

	def test_the_patch_is_listed_after_the_model_sync(self):
		text = open(frappe.get_app_path("lending_assistant", "patches.txt")).read()
		post = text.split("[post_model_sync]")[1]
		self.assertIn("lending_assistant.patches.set_default_effort_medium", post)

	def test_a_fresh_install_seeds_medium(self):
		self.assertEqual(install.DEFAULT_EFFORT, "medium")
		settings = frappe.get_doc("Assistant Settings")
		settings.default_effort = ""
		settings.save(ignore_permissions=True)
		install.seed_defaults()
		self.assertEqual(self.stored(), "medium")
