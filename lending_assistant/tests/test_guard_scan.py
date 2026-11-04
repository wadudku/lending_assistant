"""The scanner (scripts/guard_scan.py) is clean on the app and fails on bad code."""

import subprocess
import sys
import tempfile
import textwrap
from pathlib import Path

import frappe

from lending_assistant.tests.base import AssistantTestCase

SCRIPT = Path(frappe.get_app_path("lending_assistant")).parent / "scripts" / "guard_scan.py"


def run(*args):
	return subprocess.run([sys.executable, str(SCRIPT), *args], capture_output=True, text=True, timeout=120)


def tree(files: dict[str, str]) -> str:
	root = Path(tempfile.mkdtemp(prefix="ast_scan_"))
	for rel, source in files.items():
		path = root / "lending_assistant" / rel
		path.parent.mkdir(parents=True, exist_ok=True)
		path.write_text(textwrap.dedent(source))
	return str(root)


BAD_TOOL = """
	import frappe
	from pathlib import Path

	def tool(doc):
	    frappe.get_all("Loan")
	    frappe.db.get_all("Loan")
	    frappe.db.get_list("Loan")
	    frappe.get_list("Loan")
	    frappe.db.get_value("Loan", "x", "status")
	    frappe.db.get_values("Loan", "x", "status")
	    frappe.db.sql("select 1")
	    frappe.db.count("Loan")
	    frappe.db.exists("Loan", "x")
	    frappe.get_doc("Loan", "x")
	    frappe.get_cached_doc("Loan", "x")
	    frappe.get_list("Loan", ignore_permissions=True)
	    frappe.flags.ignore_permissions = True
	    frappe.set_user("Administrator")
	    doc.insert()
	    doc.save()
	    doc.submit()
	    doc.cancel()
	    doc.delete()
	    frappe.delete_doc("Loan", "x")
	    frappe.db.set_value("Loan", "x", "status", "y")
	    frappe.rename_doc("Loan", "x", "y")
	    frappe.db.commit()
	    frappe.db.rollback()
	    frappe.db.savepoint("s")
	    frappe.db._disable_transaction_control = 0
	    eval("1")
	    exec("1")
	    open("/etc/passwd")
	    Path("x").read_text()
	    __import__("os").system("ls")
"""

EXPECTED_RULES = ("get-list", "db-read", "get-doc", "ignore-permissions", "user-switch", "write", "txn-control", "generic-exec", "file-access")


class TestGuardScan(AssistantTestCase):
	def test_app_is_clean(self):
		result = run()
		self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
		self.assertIn("clean", result.stdout)

	def test_bad_tree_fails_for_every_rule(self):
		root = tree(
			{
				"assistant/tools/bad.py": BAD_TOOL,
				"api/other.py": """
					import frappe

					@frappe.whitelist()
					def sneaky():
					    return 1

					@frappe.whitelist(allow_guest=True)
					def guest():
					    return 1
				""",
				"api/chat.py": """
					import frappe

					@frappe.whitelist(methods=["POST"])
					def ask():
					    return 1

					@frappe.whitelist(methods=["POST"])
					def delete_everything():
					    return 1
				""",
				"install.py": 'import frappe\n\ndef f(name):\n    return frappe.db.exists("DocType", name)\n',
				"assistant/audit.py": "import frappe\n\ndef f(doc):\n    doc.insert(ignore_permissions=True)  # AST-ALLOWED:\n",
				"assistant/findings.py": "import frappe\n\ndef f(doc):\n    doc.insert(ignore_permissions=True)  # AST-ALLOWED: ok here\n    frappe.db.sql('select 1')  # AST-ALLOWED: not allowed in this file\n",
				"public/js/w.js": "node.innerHTML = reply;\n$(el).html(reply);\ndocument.write(x);\nok.textContent = reply;\nel.innerHTML = '';  // AST-ALLOWED: static\n",
			}
		)
		result = run("--root", root)
		self.assertEqual(result.returncode, 1, result.stdout)
		out = result.stdout
		for rule in EXPECTED_RULES + ("whitelist", "guest", "js-html"):
			self.assertIn(f"[{rule}]", out, rule)
		for text in (
			"frappe.get_all()", "frappe.db.sql()", "frappe.db.get_value()", "frappe.db.count()", "frappe.set_user()", ".insert()", ".save()",
			".submit()", ".cancel()", ".delete()", "frappe.delete_doc()", "frappe.db.set_value()", "frappe.rename_doc()", "frappe.db.commit()",
			"eval()", "open()", ".read_text()", "ignore_permissions",
		):
			self.assertIn(text, out, text)
		# the M2a-R3 case: an unmarked db.exists in install.py is flagged
		self.assertRegex(out, r"lending_assistant/install\.py:4: \[db-read\]")
		# the whitelisted endpoints in api/chat.py are fine; the extra function is not
		self.assertIn("api/chat.py:8", out)
		self.assertNotIn("api/chat.py:4", out)
		# a marker without a reason, and a marker in a file that may not use that rule
		self.assertIn("needs a reason", out)
		self.assertIn("not permitted in assistant/findings.py", out)
		# JS: textContent is fine; no marker is accepted for a raw HTML sink
		self.assertNotIn("w.js:4", out)
		self.assertIn("w.js:1", out)
		self.assertIn("not permitted in public/js/w.js", out)

	def test_marked_lines_in_allowed_files_pass(self):
		root = tree(
			{
				"assistant/audit.py": "import frappe\n\ndef f(doc):\n    doc.insert(ignore_permissions=True)  # AST-ALLOWED: own log\n",
				"install.py": 'import frappe\n\ndef f(n):\n    return frappe.db.exists("DocType", n)  # AST-ALLOWED: install seed, meta check\n',
				"api/chat.py": 'import frappe\n\n@frappe.whitelist(methods=["POST"])\ndef ask():\n    return 1\n\n@frappe.whitelist(methods=["POST"])\ndef feedback():\n    return 1\n',
				"api/findings.py": "import frappe\n\n@frappe.whitelist(methods=['POST'])\ndef save():\n    return 1\n",
			}
		)
		result = run("--root", root)
		self.assertEqual(result.returncode, 0, result.stdout)

	def test_missing_package_is_an_error(self):
		self.assertEqual(run("--root", tempfile.mkdtemp()).returncode, 2)
