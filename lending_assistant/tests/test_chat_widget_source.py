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
	"createContextualFragment",
	"srcdoc",
	'setAttribute("on',
	"setAttribute('on",
	".outerHTML",
	"$(",
	"jQuery(",
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
		# the one allowed jQuery call is the startup hook; same length, so offsets still match
		code = js_code()
		hook = '$(document).on("startup", init);'
		self.assertEqual(code.count(hook), 1)
		code = code.replace(hook, " " * len(hook))
		begin, end = function_span(code, "render_answer")
		for sink in SINKS:
			for m in re.finditer(re.escape(sink), code):
				self.assertTrue(begin < m.start() < end, f"{sink} outside render_answer at {m.start()}")
		# render_answer uses Frappe's sanitiser and our pass, in that order
		body = code[begin:end]
		self.assertLess(body.index("frappe.markdown("), body.index("harden("))
		# the parsed nodes are hardened before they are adopted, and only here
		self.assertLess(body.index("harden("), body.index("replaceChildren("))
		for m in re.finditer(r"parsed\.body", code):
			self.assertTrue(begin < m.start() < end, f"parsed.body outside render_answer at {m.start()}")

	def test_render_answer_is_the_only_caller_of_markdown(self):
		code = js_code()
		self.assertEqual(code.count("frappe.markdown("), 1)
		self.assertEqual(code.count("DOMParser()"), 2)  # render_answer and the server-message text extractor

	def test_history_reads_filter_on_the_session_user(self):
		code = js_code()
		self.assertEqual(code.count("method: LIST"), 3)  # conversations, messages, and the finding check (M6-R3)
		self.assertEqual(code.count("user: frappe.session.user"), 2)  # the finding check filters on names, read-perm checked
		self.assertNotIn("frappe.db.", code)

	def test_widget_calls_only_ask_feedback_and_the_client_list_api(self):
		code = js_code()
		self.assertEqual(code.count("fetch("), 1)  # the one POST helper, used for ask and feedback only
		self.assertEqual(code.count("post(ASK") + code.count("post(FEEDBACK") + code.count("post(SAVE"), 3)
		methods = set(re.findall(r'const (?:ASK|FEEDBACK|SAVE|LIST) = "([^"]+)"', code))
		self.assertEqual(
			methods,
			{
				"lending_assistant.api.chat.ask",
				"lending_assistant.api.chat.feedback",
				"lending_assistant.api.findings.save",
				"frappe.client.get_list",
			},
		)

	def test_exactly_three_whitelisted_methods(self):
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
		self.assertEqual(sorted(found), ["chat.ask", "chat.feedback", "findings.save"])


DOCTYPE_DIR = APP / "lending_assistant" / "doctype" / "assistant_finding"


class TestFindingsWidget(unittest.TestCase):
	def test_the_save_dialog_uses_no_markup_sink_and_only_fixed_labels(self):
		code = js_code()
		begin, end = function_span(code, "open_save_dialog")
		body = code[begin:end]
		self.assertIn('title: __("Save as finding")', code)
		for banned in ('fieldtype: "HTML"', "set_message", "$wrapper", ".html(", "description:", "innerHTML"):
			self.assertNotIn(banned, body)
		# every label is a literal translated string; no server text is a label or a title
		for label in re.findall(r"label: ([^,}]+)", body):
			self.assertRegex(label.strip(), r'^__\("[^"]+"\)$')
		# the values go in through set_value only
		self.assertEqual(body.count("dialog.set_value("), 3)

	def test_nothing_is_sent_without_the_click_and_only_through_the_post_helper(self):
		code = js_code()
		self.assertEqual(code.count("post(SAVE"), 1)
		begin, end = function_span(code, "open_save_dialog")
		self.assertLess(begin, code.index("post(SAVE"))
		self.assertLess(code.index("post(SAVE"), end)  # only inside the dialog's primary action
		b2, e2 = function_span(code, "finding_row")
		self.assertNotIn("post(", code[b2:e2])

	def test_history_shows_saved_only_for_a_finding_that_exists_and_matches_its_message(self):
		"""M6-R3: one get_list on Assistant Finding with name and source_message filters; no match = button again."""
		code = js_code()
		begin, end = function_span(code, "verify_findings")
		body = code[begin:end]
		self.assertEqual(body.count("frappe.call("), 1)
		self.assertIn("doctype: FINDING", body)
		self.assertIn('name: ["in"', body)
		self.assertIn('source_message: ["in"', body)
		self.assertIn('row.finding = ""', body)
		self.assertIn('const FINDING = "Assistant Finding";', code)
		b2, e2 = function_span(code, "open_conversation")
		self.assertIn("verify_findings(rows", code[b2:e2])

	def test_the_saved_link_is_text_and_a_checked_name(self):
		code = js_code()
		begin, end = function_span(code, "saved_row")
		body = code[begin:end]
		self.assertIn("FINDING_NAME.test(name)", body)
		self.assertIn("encodeURIComponent(name)", body)
		self.assertIn("const FINDING_NAME = /^AF-\\d{5,}$/;", code)
		self.assertNotIn("innerHTML", body)

	def test_the_desk_javascript_of_the_doctype_has_no_markup_sink(self):
		for name in ("assistant_finding.js", "assistant_finding_list.js"):
			text = (DOCTYPE_DIR / name).read_text()
			text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
			for sink in (
				"innerHTML",
				"outerHTML",
				"insertAdjacentHTML",
				"document.write",
				".html(",
				"createContextualFragment",
				"srcdoc",
			):
				self.assertNotIn(sink, text, f"{sink} in {name}")

	def test_the_list_export_uses_only_the_client_list_api(self):
		text = (DOCTYPE_DIR / "assistant_finding_list.js").read_text()
		self.assertIn('method: "frappe.client.get_list"', text)
		self.assertNotIn("lending_assistant.api", text)
		self.assertIn("limit_page_length: CAP", text)

	def test_links_to_this_site_are_limited_to_app_and_our_assets(self):
		code = js_code()
		begin, end = function_span(code, "safe_href")
		body = code[begin:end]
		self.assertIn('"/app"', body)
		self.assertIn("/assets/lending_assistant/", body)
		self.assertIn("window.location.hostname", body)
