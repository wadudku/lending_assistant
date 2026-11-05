"""M2b-R11/R12: what the app's own modules hand to other modules is plain data, never a live object.

Every public function of `guard`, `access` and `codereader` has a sample call here. A new public function without one
fails `test_every_public_function_has_a_sample_call`, which forces a decision about what it returns.
"""

import importlib
import inspect

import frappe
from frappe.model.document import Document
from frappe.utils.password import set_encrypted_password

from lending_assistant.assistant import access, codereader, guard, settings
from lending_assistant.tests.base import GuardTestCase

PLAIN = (type(None), bool, int, float, str)


def assert_plain(testcase, value, where="result"):
	"""str / number / None, or a list, tuple or dict (str keys) of those. ReadOnlyContext is walked field by field."""
	if isinstance(value, PLAIN):
		return
	if isinstance(value, list | tuple):
		for i, item in enumerate(value):
			assert_plain(testcase, item, f"{where}[{i}]")
		return
	if isinstance(value, dict):
		for key, item in value.items():
			testcase.assertIsInstance(key, str, f"{where}: key {key!r}")
			assert_plain(testcase, item, f"{where}[{key!r}]")
		return
	if isinstance(value, guard.ReadOnlyContext):
		for key, item in vars(value).items():
			assert_plain(testcase, item, f"{where}.{key}")
		return
	testcase.fail(f"{where} is a {type(value).__name__}: a live object leaves the module")


def public_functions(module):
	return sorted(
		name
		for name, fn in inspect.getmembers(module, inspect.isfunction)
		if not name.startswith("_") and fn.__module__ == module.__name__
	)


class TestPlainDataSurface(GuardTestCase):
	MODULES = {"guard": guard, "access": access, "codereader": codereader}

	def samples(self):
		visible, _hidden = self.loan_names()
		result = {}
		result["guard"] = {
			"read_doc": lambda: guard.read_doc("Loan", visible),
			"list_records": lambda: guard.list_records("Loan", limit=2),
			"as_data": lambda: guard.as_data({"a": 1}),
			"neutralise": lambda: guard.neutralise("<data>"),
			"unwrap": lambda: guard.unwrap(guard.as_data({"a": 1})),
			"fit": lambda: guard.fit({"rows": []}, lambda: [], lambda: []),
			"require_live_data": lambda: guard.require_live_data(),
			"require_doctype": lambda: guard.require_doctype("Loan"),
			"readable_fields": lambda: guard.readable_fields("Loan"),
			"check_actions": lambda: guard.check_actions("Loan", ["read", "submit"]),
			"block_if_read_only": lambda: guard.block_if_read_only(),
			"read_only_tool_context": None,  # a context manager: the yielded object is checked below
			"identity_watch": None,  # a context manager that yields nothing
		}
		result["access"] = {
			"check_my_access": lambda: access.check_my_access("Loan", ["read"], visible),
			"roles_that_can": lambda: access.roles_that_can("Loan", "submit"),
			"describe_doctype": lambda: access.describe_doctype("Loan", "product"),
		}
		result["codereader"] = {
			"read": lambda: codereader.read("lending/lending/hooks.py", 1, 3),
			"search": lambda: codereader.search("hooks"),
			"controller_path": lambda: codereader.controller_path("Loan Management", "Loan"),
		}
		return result

	def test_every_public_function_has_a_sample_call(self):
		samples = self.samples()
		for name, module in self.MODULES.items():
			self.assertEqual(
				public_functions(module),
				sorted(samples[name]),
				f"{name}: a public function without a sample call (or a sample for one that is gone). "
				"Add it to samples() and decide what it returns.",
			)

	def test_every_public_function_returns_plain_data(self):
		self.as_user("senior")
		for module_name, calls in self.samples().items():
			for name, call in calls.items():
				if call is None:
					continue
				with self.subTest(f"{module_name}.{name}"):
					if name == "block_if_read_only":  # the doc_events hook: inside a context it raises by design
						assert_plain(self, call(), f"{module_name}.{name}()")
						continue
					with guard.read_only_tool_context("AST-TEST-surface"):
						assert_plain(self, call(), f"{module_name}.{name}()")

	def test_the_identity_watch_yields_nothing_so_no_live_object_leaves_guard(self):
		self.as_user("senior")
		with guard.identity_watch("AST-TEST-surface") as yielded:
			pass
		self.assertIsNone(yielded)

	def test_the_context_object_holds_plain_values_only(self):
		self.as_user("senior")
		with guard.read_only_tool_context("AST-TEST-outer") as outer:
			with guard.read_only_tool_context("AST-TEST-inner"):
				guard.list_records("Loan", limit=1)
		assert_plain(self, outer, "ReadOnlyContext")
		self.assertNotIn("callback_snapshots", vars(outer))
		assert_plain(self, outer.summary(), "summary()")

	def test_there_is_no_function_that_returns_a_document(self):
		"""The old `guard.load_readable` is private now; no public name of the three modules returns a Document."""
		self.assertFalse(hasattr(guard, "load_readable"))
		self.assertFalse(hasattr(guard, "_fit"))
		for module in self.MODULES.values():
			for name in public_functions(module):
				hints = inspect.signature(getattr(module, name)).return_annotation
				self.assertNotIn("Document", str(hints), f"{module.__name__}.{name}")

	def test_the_exceptions_hold_only_text(self):
		self.as_user("limited")
		_visible, hidden = self.loan_names()
		with self.assertRaises(guard.RecordNotAvailable) as caught:
			guard.read_doc("Loan", hidden)
		assert_plain(self, list(caught.exception.args), "RecordNotAvailable.args")


class TestSettingsIsAPlainCopy(GuardTestCase):
	def test_get_settings_is_a_dict_not_a_document(self):
		value = settings.get_settings()
		self.assertIsInstance(value, frappe._dict)
		self.assertNotIsInstance(value, Document)
		self.assertTrue(all(klass is not Document for klass in type(value).__mro__))

	def test_the_api_key_is_not_in_it_even_when_one_is_set(self):
		secret = "sk-ast-test-DUMMY-not-a-real-key"  # never a real key; rolled back with the class
		set_encrypted_password("Assistant Settings", "Assistant Settings", secret, "api_key")
		value = settings.get_settings()
		self.assertNotIn("api_key", value)
		self.assertNotIn(secret, repr(value))
		self.assertEqual(settings.get_api_key(), secret)  # the one reader of the key still has it

	def test_child_rows_are_plain_too(self):
		value = settings.get_settings()
		self.assertTrue(value.doctype_allowlist)
		for row in value.doctype_allowlist:
			self.assertNotIsInstance(row, Document)
			self.assertTrue(row.allowed_doctype)
		self.assertTrue(all(not isinstance(row, Document) for row in value.never_send_fields))

	def test_changing_the_copy_changes_nothing(self):
		first = settings.get_settings()
		was = first.live_data
		first.live_data = 0 if was else 1
		first.doctype_allowlist.clear()
		again = settings.get_settings()
		self.assertEqual(again.live_data, was)
		self.assertTrue(again.doctype_allowlist)
		self.assertIsNot(first, again)

	def test_the_modules_import_cleanly(self):
		for name in ("guard", "access", "codereader", "settings"):
			importlib.import_module(f"lending_assistant.assistant.{name}")
