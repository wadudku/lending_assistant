"""M4b scanner: `anthropic` is importable in assistant/orchestrator.py only (#145), as `import anthropic`, and
`get_api_key` / the dispatcher are reachable from the orchestrator only."""

import shutil

from lending_assistant.tests.base import AssistantTestCase
from lending_assistant.tests.test_guard_scan import run, tree

OTHER = [
	"assistant/tools/live.py",
	"assistant/tools/registry.py",
	"assistant/tools/dues.py",
	"assistant/prompts.py",
	"assistant/trace.py",
	"assistant/guard.py",
	"assistant/audit.py",
	"api/chat.py",
	"kb/store.py",
	"install.py",
	"patches/seed_default_settings.py",
]
FORMS = [
	"import anthropic",
	"import anthropic as a",
	"import anthropic.types",
	"import anthropic.types as t",
	"from anthropic import Anthropic",
	"from anthropic import Anthropic as A",
	"from anthropic import *",
	"from anthropic.types import Message",
	"from anthropic.resources.beta import messages",
	"from . import anthropic",
	"if True:\n    import anthropic",
	"try:\n    import anthropic\nexcept ImportError:\n    anthropic = None",
	"def f():\n    import anthropic\n    return anthropic",
	"from typing import TYPE_CHECKING\nif TYPE_CHECKING:\n    import anthropic",
	"import importlib\nimportlib.import_module('anthropic')",
	"__import__('anthropic')",
]


class TestAnthropicScan(AssistantTestCase):
	def scan(self, rel, source):
		root = tree({rel: source})
		self.addCleanup(shutil.rmtree, root, True)
		return run("--root", root)

	def test_anthropic_is_a_hit_in_every_other_file_in_every_import_form(self):
		for rel in OTHER:
			for form in FORMS:
				with self.subTest(rel=rel, form=form):
					result = self.scan(rel, form + "\n")
					self.assertEqual(result.returncode, 1, f"{form!r} accepted in {rel}\n{result.stdout}")

	def test_a_marker_does_not_excuse_it(self):
		result = self.scan("assistant/audit.py", "import anthropic  # AST-ALLOWED: needed\n")
		self.assertEqual(result.returncode, 1, result.stdout)

	def test_plain_import_is_clean_in_the_orchestrator(self):
		result = self.scan(
			"assistant/orchestrator.py", "import anthropic\n\n\ndef f():\n    return anthropic\n"
		)
		self.assertEqual(result.returncode, 0, result.stdout)

	def test_aliases_and_from_forms_are_hits_even_in_the_orchestrator(self):
		for form in ("import anthropic as a", "from anthropic import Anthropic", "from anthropic import *"):
			with self.subTest(form=form):
				result = self.scan("assistant/orchestrator.py", form + "\n")
				self.assertEqual(result.returncode, 1, result.stdout)

	def test_httpx2_is_a_hit_everywhere_including_the_orchestrator(self):
		for rel in ("assistant/orchestrator.py", "api/chat.py", "assistant/tools/live.py"):
			for form in ("import httpx2", "from httpx2 import Client", "import httpx2 as h"):
				with self.subTest(rel=rel, form=form):
					result = self.scan(rel, form + "\n")
					self.assertEqual(result.returncode, 1, result.stdout)
					self.assertIn("[network-import]", result.stdout)

	def test_get_api_key_is_a_hit_outside_the_orchestrator(self):
		code = "from lending_assistant.assistant import settings\n\n\ndef f():\n    return settings.get_api_key()\n"
		for rel in OTHER:
			if rel == "assistant/settings.py":
				continue
			with self.subTest(rel=rel):
				result = self.scan(rel, code)
				self.assertEqual(result.returncode, 1, f"get_api_key accepted in {rel}\n{result.stdout}")
		result = self.scan("assistant/orchestrator.py", code)
		self.assertEqual(result.returncode, 0, result.stdout)
