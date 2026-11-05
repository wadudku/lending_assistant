"""M4a scanner entries: the grants the tool modules need are narrow. Each is accepted in its own file and is a hit in
every other file. The dispatcher is reserved for the orchestrator (M4b).
"""

import shutil

from lending_assistant.tests.base import AssistantTestCase
from lending_assistant.tests.test_guard_scan import run, tree

ASSIST = "from lending_assistant.assistant import {mod}\n\n\ndef f():\n    return {mod}.{name}\n"
TOOLS = "from lending_assistant.assistant.tools import {mod}\n\n\ndef f():\n    return {mod}.{name}\n"

# (import line template, module, name, files where it is accepted)
GRANTS = [
	(ASSIST, "guard", "identity_watch", ["assistant/tools/registry.py"]),
	(ASSIST, "guard", "unwrap", ["assistant/tools/live.py", "assistant/tools/registry.py"]),
	(
		ASSIST,
		"guard",
		"fit",
		["assistant/tools/live.py", "assistant/codereader.py", "assistant/tools/knowledge.py"],
	),
	(ASSIST, "guard", "neutralise", ["assistant/tools/registry.py"]),
	(ASSIST, "guard", "readable_fields", ["assistant/access.py"]),
	(ASSIST, "codereader", "controller_path", ["assistant/access.py"]),
	(ASSIST, "codereader", "OFF", ["assistant/tools/registry.py"]),
	(ASSIST, "access", "describe_doctype", ["assistant/tools/live.py"]),
	(ASSIST, "access", "ACTIONS", ["assistant/tools/live.py"]),
	(TOOLS, "live", "find_records", ["assistant/tools/registry.py"]),
	(TOOLS, "code", "read_code", ["assistant/tools/registry.py"]),
	(TOOLS, "knowledge", "get_card", ["assistant/tools/registry.py"]),
	(TOOLS, "registry", "dispatch", ["assistant/orchestrator.py"]),
	(TOOLS, "registry", "tool_definitions", ["assistant/orchestrator.py"]),
	(TOOLS, "registry", "ToolResult", ["assistant/orchestrator.py"]),
]
OTHER_FILES = [
	"assistant/tools/live.py", "assistant/tools/code.py", "assistant/tools/knowledge.py", "assistant/tools/registry.py",
	"assistant/access.py", "assistant/audit.py", "api/chat.py", "kb/lookup.py", "assistant/orchestrator.py",
]  # fmt: skip


class TestM4aGrants(AssistantTestCase):
	def scan(self, files):
		root = tree(files)
		self.addCleanup(shutil.rmtree, root, True)
		return run("--root", root)

	def test_each_grant_is_accepted_in_its_own_files(self):
		for template, mod, name, files in GRANTS:
			for rel in files:
				with self.subTest(grant=f"{mod}.{name}", file=rel):
					result = self.scan({rel: template.format(mod=mod, name=name)})
					self.assertEqual(result.returncode, 0, result.stdout)

	def test_each_grant_is_a_hit_in_every_other_file(self):
		for template, mod, name, files in GRANTS:
			for rel in OTHER_FILES:
				own = rel in (
					f"assistant/{mod}.py",
					f"assistant/tools/{mod}.py",
				)  # a module may use its own names
				if rel in files or own:
					continue
				with self.subTest(grant=f"{mod}.{name}", file=rel):
					result = self.scan({rel: template.format(mod=mod, name=name)})
					self.assertEqual(result.returncode, 1, f"{mod}.{name} was accepted in {rel}")
					self.assertTrue("[app-api]" in result.stdout, result.stdout)

	def test_the_dispatcher_is_reserved_for_the_orchestrator(self):
		for rel in ("assistant/tools/live.py", "api/chat.py", "assistant/tools/code.py"):
			result = self.scan({rel: TOOLS.format(mod="registry", name="dispatch")})
			self.assertNotEqual(result.returncode, 0, rel)

	def test_the_registry_may_not_be_reached_from_a_private_name(self):
		result = self.scan({"assistant/orchestrator.py": TOOLS.format(mod="registry", name="_entry")})
		self.assertEqual(result.returncode, 1)
		self.assertIn("private name", result.stdout)

	def test_frappe_logger_is_allowed_in_the_registry_only(self):
		code = "import frappe\n\n\ndef f():\n    frappe.logger('x').info('y')\n"
		self.assertEqual(self.scan({"assistant/tools/registry.py": code}).returncode, 0)
		for rel in (
			"assistant/tools/live.py",
			"assistant/tools/code.py",
			"assistant/guard.py",
			"api/chat.py",
		):
			result = self.scan({rel: code})
			self.assertEqual(result.returncode, 1, rel)
			self.assertIn("frappe.logger", result.stdout)

	def test_registry_imports_json_and_namedtuple_and_nothing_else_from_the_stdlib(self):
		self.assertEqual(
			self.scan(
				{"assistant/tools/registry.py": "import json\nfrom typing import NamedTuple\n"}
			).returncode,
			0,
		)
		for line in (
			"import copy",
			"import re",
			"import os",
			"from typing import Any",
			"from dataclasses import dataclass",
		):
			with self.subTest(line=line):
				self.assertEqual(self.scan({"assistant/tools/registry.py": line + "\n"}).returncode, 1)
		self.assertEqual(self.scan({"assistant/tools/live.py": "import json\n"}).returncode, 1)

	def test_get_meta_in_the_new_access_function_needs_its_marker(self):
		code = "import frappe\n\n\ndef describe_doctype(d):\n    return frappe.get_meta(d)\n"
		self.assertEqual(self.scan({"assistant/access.py": code}).returncode, 1)
		self.assertEqual(self.scan({"assistant/tools/live.py": code + "\n"}).returncode, 1)
		self.assertEqual(
			self.scan(
				{"assistant/tools/live.py": code.replace("(d)\n", "(d)  # AST-ALLOWED: meta\n", 1)}
			).returncode,
			1,
		)  # tool code never gets get_meta, marked or not
