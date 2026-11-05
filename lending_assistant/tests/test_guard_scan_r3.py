"""M2b rework 3 scanner rules: R11 (the app's own modules), R12 (reaching the Document class), R17 (marker scope).

The bar is DECISIONS #46: every direct or plausible misuse must fail the scan. Deliberate obfuscation is not tested
here; it is listed in the known-limits table of the rework report.
"""

import importlib
import importlib.util
import shutil
import sys

import frappe

from lending_assistant.tests.base import AssistantTestCase
from lending_assistant.tests.test_guard_scan import SCRIPT, run, tree

G = "lending_assistant.assistant.guard"
A = "lending_assistant.assistant.access"
TOOL = "assistant/tools/x.py"

# (name, rule, code, path). Each one is written into its own tree and must fail the scan on its own.
R11_APP_INTERNALS = [
	("private name imported", "app-api", f"from {G} import _restore_identity\n", TOOL),
	("private name imported, several", "app-api", f"from {G} import read_doc, _capture_identity\n", TOOL),
	("the frappe module through guard", "app-api", f"from {G} import frappe\n", TOOL),
	(
		"a name that is not listed (public in guard, not for tools)",
		"app-api",
		f"from {G} import require_doctype\n",
		TOOL,
	),
	("a name that was removed from the surface", "app-api", f"from {G} import load_readable\n", TOOL),
	("the old private fit", "app-api", f"from {G} import _fit\n", TOOL),
	(
		"private attribute through the module",
		"app-api",
		"from lending_assistant.assistant import guard\n\ndef f():\n    return guard._capture_identity()\n",
		TOOL,
	),
	(
		"guard.frappe attribute",
		"app-api",
		"from lending_assistant.assistant import guard\n\ndef f():\n    return guard.frappe.db\n",
		TOOL,
	),
	(
		"guard.load_readable attribute",
		"app-api",
		"from lending_assistant.assistant import guard\n\ndef f():\n    return guard.load_readable('Loan', 'x')\n",
		TOOL,
	),
	(
		"guard.settings attribute",
		"app-api",
		"from lending_assistant.assistant import guard\n\ndef f():\n    return guard.settings.get_api_key()\n",
		TOOL,
	),
	(
		"module alias with as",
		"app-api",
		"from lending_assistant.assistant import guard as g\n\ndef f():\n    return g._restore_identity({})\n",
		TOOL,
	),
	("import as", "app-api", f"import {G} as g\n\ndef f():\n    return g._restore_identity({{}})\n", TOOL),
	(
		"dotted import, no alias",
		"app-api",
		f"import {G}\n\ndef f():\n    return {G}._capture_identity()\n",
		TOOL,
	),
	(
		"dotted import, unlisted public name",
		"app-api",
		f"import {G}\n\ndef f():\n    return {G}.require_live_data()\n",
		TOOL,
	),
	(
		"module bound to another name",
		"app-api",
		"from lending_assistant.assistant import guard\n\ng = guard\n",
		TOOL,
	),
	(
		"module passed on as a value",
		"app-api",
		"from lending_assistant.assistant import guard\n\ndef f(x):\n    x(guard)\n",
		TOOL,
	),
	(
		"module returned",
		"app-api",
		"from lending_assistant.assistant import guard\n\ndef f():\n    return guard\n",
		TOOL,
	),
	("relative import of a private name", "app-api", "from .guard import _fit\n", "assistant/x.py"),
	(
		"relative module import, private use",
		"app-api",
		"from . import guard\n\ndef f():\n    return guard._fit({}, None, None)\n",
		"assistant/x.py",
	),
	(
		"two dots",
		"app-api",
		"from .. import assistant\n\ndef f():\n    return assistant.guard._capture_identity()\n",
		TOOL,
	),
	(
		"two dots, module import",
		"app-api",
		"from .. import guard\n\ndef f():\n    return guard._capture_identity()\n",
		TOOL,
	),
	("star import of an app module", "app-api", f"from {G} import *\n", TOOL),
	(
		"module that is not on the API table",
		"app-api",
		"from lending_assistant.install import seed_defaults\n",
		TOOL,
	),
	("another package", "app-api", "import lending_assistant.api.chat\n", TOOL),
	(
		"an app module that does not exist yet",
		"app-api",
		"from lending_assistant.assistant.tools import orchestrator\n",
		TOOL,
	),
	("the package as a value", "app-api", "import lending_assistant\n\nx = lending_assistant\n", TOOL),
	(
		"access private",
		"app-api",
		"from lending_assistant.assistant import access\n\ndef f():\n    return access._thing()\n",
		TOOL,
	),
	(
		"access unlisted",
		"app-api",
		"from lending_assistant.assistant import access\n\ndef f():\n    return access.ACTIONS\n",
		TOOL,
	),
	(
		"codereader private",
		"app-api",
		"from lending_assistant.assistant import codereader\n\ndef f():\n    return codereader._resolve('x')\n",
		TOOL,
	),
	(
		"codereader unlisted",
		"app-api",
		"from lending_assistant.assistant import codereader\n\ndef f():\n    return codereader.EXTENSIONS\n",
		TOOL,
	),
	(
		"get_api_key outside orchestrator.py",
		"app-api",
		"from lending_assistant.assistant import settings\n\ndef f():\n    return settings.get_api_key()\n",
		TOOL,
	),
	(
		"get_api_key by name outside orchestrator.py",
		"app-api",
		"from lending_assistant.assistant.settings import get_api_key\n",
		"api/chat.py",
	),
	(
		"audit outside chat.py",
		"app-api",
		"from lending_assistant.assistant import audit\n\ndef f():\n    return audit.log_exchange()\n",
		TOOL,
	),
	(
		"audit private inside chat.py",
		"app-api",
		"from lending_assistant.assistant import audit\n\ndef f():\n    return audit._json({})\n",
		"api/chat.py",
	),
	(
		"audit unlisted name inside chat.py",
		"app-api",
		"from lending_assistant.assistant import audit\n\ndef f():\n    return audit.make_title('x')\n",
		"api/chat.py",
	),
	(
		"ratelimit outside chat.py",
		"app-api",
		"from lending_assistant.assistant import ratelimit\n\ndef f():\n    return ratelimit.exceeded('a', 'b', 1, 1)\n",
		TOOL,
	),
	(
		"ratelimit.hit inside chat.py",
		"app-api",
		"from lending_assistant.assistant import ratelimit\n\ndef f():\n    return ratelimit.hit('k', 1)\n",
		"api/chat.py",
	),
	(
		"guard.fit outside codereader.py",
		"app-api",
		"from lending_assistant.assistant import guard\n\ndef f():\n    return guard.fit({}, None, None)\n",
		TOOL,
	),
	(
		"guard.check_actions in a tool",
		"app-api",
		"from lending_assistant.assistant import guard\n\ndef f():\n    return guard.check_actions('Loan', ['read'])\n",
		TOOL,
	),
	(
		"install from a tool",
		"app-api",
		"from lending_assistant import install\n\ndef f():\n    return install.seed_defaults()\n",
		TOOL,
	),
	(
		"install private from patches",
		"app-api",
		"from lending_assistant import install\n\ndef f():\n    return install._doctype_exists('x')\n",
		"patches/x.py",
	),
]

R12_DOCUMENT_CLASS = [
	("type(x)", "dynamic", "def f(x):\n    return type(x)\n", TOOL),
	(
		"type(get_settings())",
		"dynamic",
		"from lending_assistant.assistant import settings\n\ndef f():\n    return type(settings.get_settings())\n",
		TOOL,
	),
	(
		"type(meta).mro()[1]",
		"dynamic",
		"import frappe\n\ndef f():\n    return type(frappe.get_meta('Loan')).mro()[1]\n",
		TOOL,
	),
	("x.mro()", "dynamic", "def f(x):\n    return x.mro()\n", TOOL),
	("x.mro attribute", "dynamic", "def f(x):\n    return x.mro\n", TOOL),
	("mro by subscript", "dynamic", "def f(x):\n    return x['mro']\n", TOOL),
	(
		"type(x) anywhere, even in guard.py",
		"dynamic",
		"def f(x):\n    return type(x)\n",
		"assistant/guard.py",
	),
	("type(x) with a marker", "dynamic", "def f(x):\n    return type(x)  # AST-ALLOWED: because\n", TOOL),
	(
		"controller class import (this app)",
		"controller-import",
		"from lending_assistant.lending_assistant.doctype.assistant_message.assistant_message import AssistantMessage\n",
		TOOL,
	),
	(
		"controller module import (this app)",
		"controller-import",
		"from lending_assistant.lending_assistant.doctype.assistant_message import assistant_message\n",
		TOOL,
	),
	(
		"controller import in guard.py",
		"controller-import",
		"from lending_assistant.lending_assistant.doctype.assistant_message.assistant_message import AssistantMessage\n",
		"assistant/guard.py",
	),
	(
		"lending controller",
		"controller-import",
		"from lending.loan_management.doctype.loan.loan import Loan\n",
		TOOL,
	),
	(
		"erpnext controller",
		"controller-import",
		"from erpnext.accounts.doctype.sales_invoice.sales_invoice import SalesInvoice\n",
		TOOL,
	),
	(
		"dotted import of a controller",
		"controller-import",
		"import lending.loan_management.doctype.loan.loan\n",
		TOOL,
	),
	(
		"controller import with a marker",
		"controller-import",
		"from lending.loan_management.doctype.loan.loan import Loan  # AST-ALLOWED: because\n",
		TOOL,
	),
	(
		"get_meta in a tool",
		"not-allowed",
		"import frappe\n\ndef f():\n    return frappe.get_meta('Loan')\n",
		TOOL,
	),
	(
		"get_meta in a tool, marked",
		"not-allowed",
		"import frappe\n\ndef f():\n    return frappe.get_meta('Loan')  # AST-ALLOWED: because\n",
		TOOL,
	),
	(
		"get_meta in guard.py without a marker",
		"not-allowed",
		"import frappe\n\ndef f():\n    return frappe.get_meta('Loan')\n",
		"assistant/guard.py",
	),
	(
		"get_meta in codereader.py",
		"not-allowed",
		"import frappe\n\ndef f():\n    return frappe.get_meta('Loan')  # AST-ALLOWED: because\n",
		"assistant/codereader.py",
	),
]

# R17: a marker for these rules is accepted only inside the named functions of guard.py.
R17_OUT_OF_SCOPE = [
	(
		"user-switch in require_live_data",
		"user-switch",
		"import frappe\n\ndef require_live_data():\n    frappe.session.user = 'Administrator'  # AST-ALLOWED: because\n",
	),
	(
		"user-switch at module level",
		"user-switch",
		"import frappe\n\nfrappe.session.user = 'Administrator'  # AST-ALLOWED: because\n",
	),
	(
		"user-switch in the context manager",
		"user-switch",
		"import frappe\n\ndef read_only_tool_context():\n    frappe.local.site = 'x'  # AST-ALLOWED: because\n",
	),
	(
		"alias in the context manager",
		"alias",
		"import frappe\n\ndef read_only_tool_context():\n    db = frappe.db  # AST-ALLOWED: because\n",
	),
	(
		"alias in a reader",
		"alias",
		"import frappe\n\ndef read_doc():\n    return frappe.local.session  # AST-ALLOWED: because\n",
	),
	(
		"txn-control in a reader",
		"txn-control",
		"import frappe\n\ndef read_doc(db):\n    db._conn  # AST-ALLOWED: because\n",
	),
	(
		"callbacks in a reader",
		"callbacks",
		"import frappe\n\ndef read_doc():\n    return frappe.db.after_commit  # AST-ALLOWED: because\n",
	),
	(
		"flags in a reader",
		"flags",
		"import frappe\n\ndef read_doc():\n    frappe.flags['ast_read_only'] = None  # AST-ALLOWED: because\n",
	),
]
R17_IN_SCOPE = [
	(
		"user-switch in _restore_identity",
		"import frappe\n\ndef _restore_identity():\n    frappe.session.user = 'x'  # AST-ALLOWED: identity layer\n",
	),
	(
		"user-switch in a helper nested in _restore_identity",
		"import frappe\n\ndef _restore_identity():\n    def back():\n        frappe.session.user = 'x'  # AST-ALLOWED: identity layer\n    back()\n",
	),
	(
		"alias in _capture_identity",
		"import frappe\n\ndef _capture_identity():\n    return frappe.local.db  # AST-ALLOWED: identity layer\n",
	),
	(
		"txn-control in the context manager",
		"import frappe\n\ndef read_only_tool_context(db):\n    db._disable_transaction_control = 1  # AST-ALLOWED: transaction control\n",
	),
	(
		"callbacks in _snapshot_callbacks",
		"import frappe\n\ndef _snapshot_callbacks():\n    return frappe.db.after_commit  # AST-ALLOWED: callback layer\n",
	),
]


class TestScanR3(AssistantTestCase):
	def make_tree(self, files):
		root = tree(files)
		self.addCleanup(shutil.rmtree, root, True)
		return root

	def assertFlagged(self, name, rule, code, path=TOOL):
		result = run("--root", self.make_tree({path: code}))
		self.assertEqual(result.returncode, 1, f"{name} was not flagged:\n{result.stdout}")
		self.assertIn(f"[{rule}]", result.stdout, f"{name}: expected rule [{rule}]\n{result.stdout}")

	def assertClean(self, files, msg=""):
		result = run("--root", self.make_tree(files))
		self.assertEqual(result.returncode, 0, f"{msg}\n{result.stdout}")

	def test_R11_every_app_internal_variant_fails_the_scan_on_its_own(self):
		for name, rule, code, path in R11_APP_INTERNALS:
			with self.subTest(name):
				self.assertFlagged(name, rule, code, path)

	def test_R11_a_marker_never_excuses_an_app_api_hit(self):
		code = f"from {G} import _restore_identity  # AST-ALLOWED: because\n"
		for path in (TOOL, "assistant/access.py", "assistant/codereader.py", "api/chat.py"):
			self.assertFlagged(f"marker in {path}", "app-api", code, path)

	def test_R11_the_public_surface_and_the_grants_are_clean(self):
		self.assertClean(
			{
				TOOL: f"""
					from {G} import AssistantGuardError, RecordNotAvailable, as_data, list_records, read_doc, read_only_tool_context
					from lending_assistant.assistant import access, codereader, guard, settings

					def f(name):
					    with guard.read_only_tool_context("x") as ctx:
					        try:
					            guard.read_doc("Loan", name)
					            guard.list_records("Loan", limit=3)
					        except guard.RecordNotAvailable:
					            pass
					        access.check_my_access("Loan", ["read"])
					        access.roles_that_can("Loan", "submit")
					        codereader.read("lending/lending/hooks.py", 1, 5)
					        codereader.search("hooks")
					        return settings.get_settings().live_data, ctx, as_data({{}}), AssistantGuardError, RecordNotAvailable
				""",
				"assistant/access.py": "from lending_assistant.assistant import guard\n\ndef f():\n    return guard.require_doctype('x'), guard.check_actions('x', []), guard.SOURCE_LIVE\n",
				"assistant/codereader.py": "from lending_assistant.assistant import guard, settings\n\nclass R(guard.AssistantRefused):\n    pass\n\ndef f(r):\n    guard.fit(r, None, None, source='code')\n    return guard.as_data(r, source='code'), settings.get_settings()\n",
				"assistant/guard.py": "from lending_assistant.assistant import settings\n\ndef f():\n    return settings.get_settings()\n",
				"api/chat.py": "from lending_assistant.assistant import audit, ratelimit\nfrom lending_assistant.assistant.settings import get_settings\n\ndef f():\n    return audit.CONVERSATION, audit.MESSAGE, audit.start_conversation, audit.log_exchange, audit.set_feedback, ratelimit.exceeded, ratelimit.USER_PREFIX, ratelimit.IP_PREFIX, ratelimit.FEEDBACK_PREFIX, get_settings()\n",
				"patches/x.py": "from lending_assistant.install import raise_max_tokens_default, seed_defaults\n",
				"assistant/orchestrator.py": "from lending_assistant.assistant import settings\n\ndef f():\n    return settings.get_api_key()\n",
				"assistant/helper.py": "from . import guard\n\ndef f():\n    return guard.read_doc('Loan', 'x')\n",
			},
			"the public surface and the per-file grants",
		)

	def test_R11_the_app_api_tables_name_things_that_exist(self):
		spec = importlib.util.spec_from_file_location("guard_scan_for_r3", SCRIPT)
		scanner = importlib.util.module_from_spec(spec)
		sys.modules[spec.name] = scanner
		spec.loader.exec_module(scanner)
		try:
			for module, names in scanner.APP_API.items():
				imported = importlib.import_module(module)
				for name in names:
					self.assertTrue(
						hasattr(imported, name), f"APP_API lists {module}.{name}, which does not exist"
					)
			for module, name, _files, _reserved in scanner.APP_GRANTS:
				self.assertTrue(
					hasattr(importlib.import_module(module), name), f"grant for {module}.{name}: no such name"
				)
			# a grant is for the files it names and for nobody else
			# M4a: the reserved grants are the API key reader and the dispatcher, both for the orchestrator (M4b) only
			reserved = {g[:2] for g in scanner.APP_GRANTS if g[3]}
			self.assertEqual(
				reserved,
				{(f"{scanner.ASSISTANT}.settings", "get_api_key")}
				| {
					(f"{scanner.ASSISTANT}.tools.registry", n)
					for n in ("dispatch", "tool_definitions", "ToolResult", "ToolError")
				},
			)
			self.assertTrue(all(g[2] == ("assistant/orchestrator.py",) for g in scanner.APP_GRANTS if g[3]))
		finally:
			sys.modules.pop(spec.name, None)

	def test_R12_every_document_reaching_form_fails_the_scan_on_its_own(self):
		for name, rule, code, path in R12_DOCUMENT_CLASS:
			with self.subTest(name):
				self.assertFlagged(name, rule, code, path)

	def test_R12_get_meta_is_allowed_only_on_marked_lines_in_guard_access_and_install(self):
		code = "import frappe\n\ndef f():\n    return frappe.get_meta('Loan')  # AST-ALLOWED: meta facts\n"
		for path in ("assistant/guard.py", "install.py"):
			self.assertClean({path: code}, path)
		# access.py: only inside describe_doctype and roles_that_can (M4a scope)
		for function in ("describe_doctype", "roles_that_can"):
			self.assertClean({"assistant/access.py": code.replace("def f()", f"def {function}()")}, function)
		root = self.make_tree({"assistant/access.py": code})
		result = run("--root", root)
		self.assertEqual(result.returncode, 1, result.stdout)
		self.assertIn("accepted only inside describe_doctype, roles_that_can (R17)", result.stdout)

	def test_R12_ordinary_type_uses_are_not_flagged(self):
		self.assertClean(
			{
				TOOL: "def f(x):\n    return isinstance(x, type), type('X', (), {}), x.type, str(x)\n",
				"lending_assistant/doctype/thing/thing.py": "from frappe.model.document import Document\n\n\nclass Thing(Document):\n    pass\n",
			}
		)

	def test_R17_a_marker_outside_the_named_functions_is_refused(self):
		for name, rule, code in R17_OUT_OF_SCOPE:
			with self.subTest(name):
				root = self.make_tree({"assistant/guard.py": code})
				result = run("--root", root)
				self.assertEqual(result.returncode, 1, f"{name} was accepted:\n{result.stdout}")
				self.assertIn("(R17)", result.stdout, f"{name}: expected the scope message\n{result.stdout}")
				self.assertIn(f"[{rule}]", result.stdout)

	def test_R17_a_marker_inside_the_named_functions_passes(self):
		for name, code in R17_IN_SCOPE:
			with self.subTest(name):
				self.assertClean({"assistant/guard.py": code}, name)

	def test_R17_the_same_marker_is_not_scoped_by_function_in_the_other_files(self):
		"""Only guard.py is function-scoped; for every other file the existing per-file rule applies."""
		code = "import frappe\n\ndef read_doc():\n    frappe.session.user = 'x'  # AST-ALLOWED: because\n"
		result = run("--root", self.make_tree({"assistant/access.py": code}))
		self.assertEqual(result.returncode, 1)
		self.assertIn("is not permitted in assistant/access.py", result.stdout)
