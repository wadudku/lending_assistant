"""M5 source checks on the chat widget (no browser): label parity with prompts.SOURCE_LABELS, one render function
as the only markup sink, the explicit user filter on both history reads, and no new whitelisted method."""

import ast
import pathlib
import re
import unittest

from lending_assistant.assistant import prompts

APP = pathlib.Path(__file__).resolve().parent.parent
JS = APP / "public" / "js" / "chat_widget.js"
SINKS = (
	"innerHTML",
	"outerHTML",
	"insertAdjacentHTML",
	"document.write",
	".html(",
	"$.parseHTML",
	'.append("<',
)


def js_code() -> str:
	"""The widget without // and /* */ comments (string literals stay)."""
	text = JS.read_text()
	text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
	return "\n".join(re.sub(r"(?<![:\"'\\])//.*$", "", line) for line in text.splitlines())


def function_span(code: str, name: str) -> tuple[int, int]:
	start = code.index(f"function {name}(")
	depth, i = 0, code.index("{", start)
	begin = i
	while True:
		if code[i] == "{":
			depth += 1
		elif code[i] == "}":
			depth -= 1
			if depth == 0:
				return begin, i
		i += 1


class TestChatWidgetSource(unittest.TestCase):
	def test_label_tokens_equal_prompts_source_labels(self):
		match = re.search(r"const LABELS = \[(.*?)\];", JS.read_text())
		self.assertTrue(match, "LABELS literal not found")
		tokens = tuple(re.findall(r'"([^"]+)"', match.group(1)))
		self.assertEqual(tokens, tuple(prompts.SOURCE_LABELS))

	def test_markup_sinks_only_inside_render_answer(self):
		code = js_code()
		begin, end = function_span(code, "render_answer")
		for sink in SINKS:
			for m in re.finditer(re.escape(sink), code):
				self.assertTrue(begin < m.start() < end, f"{sink} outside render_answer at {m.start()}")
		# render_answer uses Frappe's sanitiser and our pass, in that order
		body = code[begin:end]
		self.assertLess(body.index("frappe.markdown("), body.index("harden("))

	def test_render_answer_is_the_only_caller_of_markdown(self):
		code = js_code()
		self.assertEqual(code.count("frappe.markdown("), 1)
		self.assertEqual(code.count("DOMParser()"), 2)  # render_answer and the server-message text extractor

	def test_history_reads_filter_on_the_session_user(self):
		code = js_code()
		self.assertEqual(code.count("method: LIST"), 2)
		self.assertEqual(code.count("user: frappe.session.user"), 2)
		self.assertNotIn("frappe.db.", code)

	def test_widget_calls_only_ask_feedback_and_the_client_list_api(self):
		code = js_code()
		methods = set(re.findall(r'method:\s*"([^"]+)"', code)) | set(
			re.findall(r'const (?:ASK|FEEDBACK|LIST) = "([^"]+)"', code)
		)
		self.assertEqual(
			methods,
			{
				"lending_assistant.api.chat.ask",
				"lending_assistant.api.chat.feedback",
				"frappe.client.get_list",
			},
		)

	def test_still_exactly_two_whitelisted_methods(self):
		found = []
		for path in sorted(APP.rglob("*.py")):
			if "tests" in path.parts:
				continue
			tree = ast.parse(path.read_text())
			for node in ast.walk(tree):
				if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
					for dec in node.decorator_list:
						target = dec.func if isinstance(dec, ast.Call) else dec
						if isinstance(target, ast.Attribute) and target.attr == "whitelist":
							found.append(f"{path.stem}.{node.name}")
		self.assertEqual(sorted(found), ["chat.ask", "chat.feedback"])
