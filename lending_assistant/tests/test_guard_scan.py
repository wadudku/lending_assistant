"""The scanner (scripts/guard_scan.py) is clean on the app and fails on bad code."""

import importlib.util
import shutil
import subprocess
import sys
import tempfile
import textwrap
from pathlib import Path

import frappe

from lending_assistant.tests.base import AssistantTestCase
from lending_assistant.tests.scan_fixtures_r2 import (
	BINDING,
	DUNDER_NAMES,
	FLAGS,
	METHODS,
	NOT_ALLOWED,
	REVIEWER_50,
)

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


# --- M2b-R1 (DECISIONS #40, #41): every evasion the Reviewer tried, plus the (c)-(f) forms of the rework task.
# (id, expected rule, code). Each one is written into its own tree and must fail the scan on its own.
VARIANTS = [
	# the Reviewer's 20 (M2b review, "Static scan")
	("rv01 from-import get_all", "db-read", "from frappe import get_all\n\ndef f():\n    get_all('Loan')\n"),
	("rv02 from-import set_user", "user-switch", "from frappe import set_user\n\ndef f():\n    set_user('Administrator')\n"),
	("rv03 from-import get_doc", "get-doc", "from frappe import get_doc\n\ndef f():\n    get_doc('Loan', 'x')\n"),
	("rv04 from-import delete_doc", "write", "from frappe import delete_doc\n\ndef f():\n    delete_doc('Loan', 'x')\n"),
	("rv05 frappe.get_value", "db-read", "import frappe\n\ndef f():\n    frappe.get_value('Loan', 'x', 'status')\n"),
	("rv06 qb select", "qb", "import frappe\n\ndef f():\n    frappe.qb.from_('Loan').select('*').run()\n"),
	("rv07 qb update", "qb", "import frappe\n\ndef f():\n    frappe.qb.update('Loan').set('x', 1).run()\n"),
	("rv08 session subscript", "user-switch", "import frappe\n\ndef f():\n    frappe.session['user'] = 'Administrator'\n"),
	("rv09 local.session.update", "user-switch", "import frappe\n\ndef f():\n    frappe.local.session.update({'user': 'Administrator'})\n"),
	("rv10 db.add_index", "db-other", "import frappe\n\ndef f():\n    frappe.db.add_index('Loan', ['status'])\n"),
	("rv11 db.create_table", "db-other", "import frappe\n\ndef f():\n    frappe.db.create_table('Loan')\n"),
	("rv12 db.set_default", "db-other", "import frappe\n\ndef f():\n    frappe.db.set_default('k', 'v')\n"),
	("rv13 getattr on db", "dynamic", "import frappe\n\ndef f():\n    getattr(frappe.db, 'sql')('select 1')\n"),
	("rv14 alias then call", "alias", "import frappe\n\ndef f():\n    d = frappe.db\n    d.sql('select 1')\n"),
	("rv15 importlib", "generic-exec", "import importlib\n\ndef f():\n    importlib.import_module('os')\n"),
	("rv16 sendmail", "side-effect", "import frappe\n\ndef f():\n    frappe.sendmail(recipients=['a@b.c'], message='x')\n"),
	("rv17 background_jobs.enqueue", "side-effect", "import frappe\n\ndef f():\n    frappe.utils.background_jobs.enqueue('frappe.ping')\n"),
	("rv18 frappe.client.get", "client-api", "import frappe\n\ndef f():\n    frappe.client.get('Loan', 'x')\n"),
	("rv19 frappe.client.get_list", "client-api", "import frappe\n\ndef f():\n    frappe.client.get_list('Loan')\n"),
	("rv20 reportview.get", "client-api", "import frappe\n\ndef f():\n    frappe.desk.reportview.get()\n"),
	# (a) imports and later bare calls
	("a1 from-import qb", "qb", "from frappe import qb\n"),
	("a2 from-import db", "alias", "from frappe import db\n"),
	("a3 db alias call", "db-read", "from frappe import db\n\ndef f():\n    db.sql('select 1')\n"),
	("a4 import frappe.db as d", "alias", "import frappe.db as d\n"),
	("a5 import frappe.qb as q", "qb", "import frappe.qb as q\n"),
	("a6 from-import enqueue", "side-effect", "from frappe import enqueue\n\ndef f():\n    enqueue('frappe.ping')\n"),
	("a7 from background_jobs import enqueue", "side-effect", "from frappe.utils.background_jobs import enqueue\n"),
	("a8 from-import sendmail", "side-effect", "from frappe import sendmail\n"),
	("a9 from-import get_value", "db-read", "from frappe import get_value\n"),
	("a10 from-import rename_doc", "write", "from frappe import rename_doc\n"),
	("a11 import as alias then call", "db-read", "import frappe as fr\n\ndef f():\n    fr.get_all('Loan')\n"),
	("a12 star import", "alias", "from frappe import *\n"),
	("a13 from-import local", "alias", "from frappe import local\n"),
	("a14 from-import session", "alias", "from frappe import session\n"),
	("a15 from os import system", "generic-exec", "from os import system\n\ndef f():\n    system('ls')\n"),
	("a16 from subprocess import run", "generic-exec", "from subprocess import run\n"),
	("a17 from importlib import import_module", "generic-exec", "from importlib import import_module\n"),
	("a18 from frappe.desk import reportview", "client-api", "from frappe.desk import reportview\n"),
	("a19 from frappe import client", "client-api", "from frappe import client\n"),
	# (b) banned frappe APIs
	("b1 frappe.get_single_value", "db-read", "import frappe\n\ndef f():\n    frappe.get_single_value('System Settings', 'x')\n"),
	("b2 db.get_single_value", "db-read", "import frappe\n\ndef f():\n    frappe.db.get_single_value('System Settings', 'x')\n"),
	("b3 db.exists outside install.py", "db-read", "import frappe\n\ndef f():\n    frappe.db.exists('Loan', 'x')\n"),
	("b4 db.delete", "write", "import frappe\n\ndef f():\n    frappe.db.delete('Loan', {})\n"),
	("b5 db.bulk_insert", "write", "import frappe\n\ndef f():\n    frappe.db.bulk_insert('Loan', [], [])\n"),
	("b6 db.set_single_value", "write", "import frappe\n\ndef f():\n    frappe.db.set_single_value('System Settings', 'x', 1)\n"),
	("b7 db.multisql", "db-read", "import frappe\n\ndef f():\n    frappe.db.multisql({'mariadb': 'select 1'})\n"),
	("b8 qb as a value", "qb", "import frappe\n\ndef f():\n    return frappe.qb\n"),
	("b9 frappe.local.db.sql", "db-read", "import frappe\n\ndef f():\n    frappe.local.db.sql('select 1')\n"),
	# (c) identity, every assignment shape
	("c1 assign session.user", "user-switch", "import frappe\n\ndef f():\n    frappe.session.user = 'Administrator'\n"),
	("c2 assign local.user", "user-switch", "import frappe\n\ndef f():\n    frappe.local.user = 'Administrator'\n"),
	("c3 augmented assign", "user-switch", "import frappe\n\ndef f():\n    frappe.session.user += 'x'\n"),
	("c4 annotated assign", "user-switch", "import frappe\n\ndef f():\n    frappe.session.user: str = 'Administrator'\n"),
	("c5 tuple assign", "user-switch", "import frappe\n\ndef f():\n    frappe.session.user, x = 'Administrator', 1\n"),
	("c6 local.session subscript", "user-switch", "import frappe\n\ndef f():\n    frappe.local.session['user'] = 'Administrator'\n"),
	("c7 session.update", "user-switch", "import frappe\n\ndef f():\n    frappe.session.update({'user': 'Administrator'})\n"),
	("c8 session.setdefault", "user-switch", "import frappe\n\ndef f():\n    frappe.session.setdefault('user', 'Administrator')\n"),
	("c9 session.pop", "user-switch", "import frappe\n\ndef f():\n    frappe.session.pop('user')\n"),
	("c10 local.session.clear", "user-switch", "import frappe\n\ndef f():\n    frappe.local.session.clear()\n"),
	("c11 flags.ignore_permissions", "user-switch", "import frappe\n\ndef f():\n    frappe.flags.ignore_permissions = True\n"),
	("c12 flags subscript", "user-switch", "import frappe\n\ndef f():\n    frappe.flags['ignore_permissions'] = True\n"),
	("c13 local.flags.ignore_permissions", "user-switch", "import frappe\n\ndef f():\n    frappe.local.flags.ignore_permissions = True\n"),
	("c14 del session key", "user-switch", "import frappe\n\ndef f():\n    del frappe.session['user']\n"),
	("c15 alias then write", "user-switch", "import frappe\n\ndef f():\n    s = frappe.local.session\n    s['user'] = 'Administrator'\n"),
	("c16 rebind frappe.local", "user-switch", "import frappe\n\ndef f():\n    frappe.local = None\n"),
	# (d) frappe.db is denied by default
	("d1 db.sql_ddl", "db-read", "import frappe\n\ndef f():\n    frappe.db.sql_ddl('create table x (a int)')\n"),
	("d2 db.commit", "db-other", "import frappe\n\ndef f():\n    frappe.db.commit()\n"),
	("d3 db.begin", "db-other", "import frappe\n\ndef f():\n    frappe.db.begin()\n"),
	("d4 db.truncate", "write", "import frappe\n\ndef f():\n    frappe.db.truncate('Loan')\n"),
	("d5 db.add_unique", "db-other", "import frappe\n\ndef f():\n    frappe.db.add_unique('Loan', ['x'])\n"),
	("d6 db.change_column_type", "db-other", "import frappe\n\ndef f():\n    frappe.db.change_column_type('Loan', 'x', 'text')\n"),
	("d7 db.get_global", "db-other", "import frappe\n\ndef f():\n    frappe.db.get_global('x')\n"),
	("d8 db.rollback unmarked", "txn-control", "import frappe\n\ndef f():\n    frappe.db.rollback()\n"),
	("d9 db.after_commit.add", "callbacks", "import frappe\n\ndef f():\n    frappe.db.after_commit.add(print)\n"),
	("d10 db.before_commit.add", "callbacks", "import frappe\n\ndef f():\n    frappe.db.before_commit.add(print)\n"),
	("d11 callback queue", "callbacks", "def f(manager):\n    manager._functions.clear()\n"),
	# (e) dynamic access and side effects
	("e1 getattr", "dynamic", "def f(x):\n    return getattr(x, 'sql')\n"),
	("e2 setattr", "dynamic", "def f(x):\n    setattr(x, 'sql', None)\n"),
	("e3 delattr", "dynamic", "def f(x):\n    delattr(x, 'sql')\n"),
	("e4 __import__", "generic-exec", "def f():\n    __import__('os')\n"),
	("e5 globals", "dynamic", "def f():\n    return globals()\n"),
	("e6 vars", "dynamic", "import frappe\n\ndef f():\n    return vars(frappe)\n"),
	("e7 attrgetter", "dynamic", "import operator\n\ndef f():\n    return operator.attrgetter('db.sql')\n"),
	("e8 sys.modules", "dynamic", "import sys\n\ndef f():\n    return sys.modules['frappe']\n"),
	("e9 enqueue", "side-effect", "import frappe\n\ndef f():\n    frappe.enqueue('frappe.ping')\n"),
	("e10 enqueue after commit", "side-effect", "import frappe\n\ndef f():\n    frappe.enqueue('frappe.ping', enqueue_after_commit=True)\n"),
	("e11 enqueue_doc", "side-effect", "import frappe\n\ndef f():\n    frappe.enqueue_doc('Loan', 'x', 'm')\n"),
	("e12 enqueue on a doc", "side-effect", "def f(doc):\n    doc.queue_action('submit')\n"),
	("e13 publish_realtime", "side-effect", "import frappe\n\ndef f():\n    frappe.publish_realtime('x', {})\n"),
	("e14 frappe.call", "generic-exec", "import frappe\n\ndef f():\n    frappe.call('frappe.ping')\n"),
	("e15 frappe.get_attr", "generic-exec", "import frappe\n\ndef f():\n    frappe.get_attr('frappe.ping')\n"),
	("e16 subprocess", "generic-exec", "import subprocess\n\ndef f():\n    subprocess.run(['ls'])\n"),
	("e17 os.system", "generic-exec", "import os\n\ndef f():\n    os.system('ls')\n"),
	("e18 os.popen", "generic-exec", "import os\n\ndef f():\n    os.popen('ls')\n"),
	("e19 eval", "generic-exec", "def f():\n    eval('1')\n"),
	("e20 exec", "generic-exec", "def f():\n    exec('x = 1')\n"),
	("e21 compile", "generic-exec", "def f():\n    compile('1', 'f', 'eval')\n"),
	("e23 builtins.getattr", "generic-exec", "import builtins\n\ndef f(x):\n    return builtins.getattr(x, 'sql')\n"),
	("e24 runpy", "generic-exec", "import runpy\n\ndef f():\n    runpy.run_path('x.py')\n"),
	("e25 ctypes", "generic-exec", "import ctypes\n"),
	("e22 safe_eval", "generic-exec", "import frappe\n\ndef f():\n    frappe.utils.safe_exec.safe_eval('1')\n"),
	# (f) aliases of the four objects
	("f1 d = frappe.db", "alias", "import frappe\n\nd = frappe.db\n"),
	("f2 q = frappe.qb", "qb", "import frappe\n\nq = frappe.qb\n"),
	("f3 l = frappe.local", "alias", "import frappe\n\nl = frappe.local\n"),
	("f4 s = frappe.session", "alias", "import frappe\n\ns = frappe.session\n"),
	("f5 db passed as an argument", "alias", "import frappe\n\ndef f(g):\n    g(frappe.db)\n"),
	("f6 db returned", "alias", "import frappe\n\ndef f():\n    return frappe.db\n"),
	("f7 alias of an alias", "alias", "import frappe\n\ndef f():\n    a = frappe.db\n    b = a\n"),
	("f8 annotated alias", "alias", "import frappe\n\nd: object = frappe.db\n"),
	("f9 bound method alias", "db-read", "import frappe\n\ndef f():\n    run = frappe.db.sql\n"),
]

# Forms the scanner must NOT flag. Path -> code. These are the uses the allowlist (DECISIONS #43) exists for.
CLEAN_FORMS = {
	"assistant/tools/ok1.py": """
		import frappe
		from frappe import _
		from frappe.utils import now_datetime, strip_html_tags

		def f(doc, values):
		    user = frappe.session.user
		    frappe.get_roles()
		    doc.update(values)
		    values.update({"a": 1})
		    if not user:
		        frappe.throw(_("x"), frappe.PermissionError)
		    try:
		        pass
		    except (frappe.ValidationError, frappe.DoesNotExistError, frappe.RateLimitExceededError):
		        raise frappe.PermissionError("no")
		    return user, _("x"), now_datetime(), strip_html_tags("<b>x</b>")

		class Refused(frappe.PermissionError):
		    pass
	""",
	"assistant/access.py": """
		import frappe

		def roles_that_can():
		    return frappe.get_meta("Loan").permissions  # AST-ALLOWED: permission rows from the meta
	""",
	"assistant/guard.py": """
		import frappe
		import frappe.permissions
		from frappe.model import get_permitted_fields

		def _set_ast_flag(doc):
		    stack = frappe.flags.get("ast_guard_stack")  # AST-ALLOWED: flags helper
		    frappe.flags["ast_read_only"] = True  # AST-ALLOWED: flags helper
		    size = len(frappe.local.message_log)  # AST-ALLOWED: message log snapshot
		    frappe.log_error(title="t", message="m")  # AST-ALLOWED: violation log
		    return stack, size, get_permitted_fields("Loan")
	""",
	"assistant/ratelimit.py": """
		import frappe

		def f():
		    pipe = frappe.cache.pipeline()
		    frappe.cache.expire(frappe.cache.make_key("k"), 60)
		    return pipe
	""",
	"assistant/codereader.py": "import frappe\n\ndef f():\n    return frappe.utils.get_bench_path()\n",
	"api/chat.py": """
		import frappe

		@frappe.whitelist(methods=["POST"])
		def ask():
		    return frappe.local.request_ip

		@frappe.whitelist(methods=["POST"])
		def feedback():
		    return 1
	""",
	"lending_assistant/doctype/thing/thing.py": "from frappe.model.document import Document\n\n\nclass Thing(Document):\n    pass\n",
	"assistant/tools/plain.py": """
		def f(t, items):
		    t.run()
		    items.append(1)
		    return sorted(items)
	""",
}

EXPECTED_RULES = ("get-list", "db-read", "get-doc", "ignore-permissions", "user-switch", "write", "txn-control", "generic-exec", "file-access")


class TestGuardScan(AssistantTestCase):
	def make_tree(self, files):
		root = tree(files)
		self.addCleanup(shutil.rmtree, root, True)
		return root

	def assertFlagged(self, name, rule, code, path="assistant/tools/x.py"):
		"""One tree for this one snippet: it must fail the scan on its own, with `rule` named."""
		root = self.make_tree({path: code})
		result = run("--root", root)
		self.assertEqual(result.returncode, 1, f"{name} was not flagged:\n{result.stdout}")
		self.assertIn(f"[{rule}]", result.stdout, f"{name}: expected rule [{rule}]\n{result.stdout}")

	def assertClean(self, files, msg=""):
		result = run("--root", self.make_tree(files))
		self.assertEqual(result.returncode, 0, f"{msg}\n{result.stdout}")

	def test_app_is_clean(self):
		result = run("--check-allowlist")
		self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
		self.assertIn("clean", result.stdout)

	def test_bad_tree_fails_for_every_rule(self):
		root = self.make_tree(
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

	def test_every_evasion_variant_fails_the_scan_on_its_own(self):
		"""M2b-R1: the Reviewer's 20 variants and the (a)-(f) forms. One tree each: no variant hides behind another."""
		self.assertGreaterEqual(len(VARIANTS), 100)
		for name, rule, code in VARIANTS:
			with self.subTest(name):
				root = self.make_tree({"assistant/tools/x.py": code})
				result = run("--root", root)
				self.assertEqual(result.returncode, 1, f"{name} was not flagged:\n{result.stdout}")
				self.assertIn(f"[{rule}]", result.stdout, f"{name}: expected rule [{rule}]\n{result.stdout}")

	# --- M2b-R8 (DECISIONS #43): the allowlist method

	def test_the_reviewers_50_variants_each_fail_on_their_own(self):
		self.assertEqual(len(REVIEWER_50), 50)
		for name, rule, code in REVIEWER_50:
			with self.subTest(name):
				self.assertFlagged(name, rule, code)

	def test_a_early_and_later_variants_total_159(self):
		"""109 from rework 1 (the Worker's) + 50 from its re-review (the Reviewer's): the full set is run."""
		self.assertEqual(len(VARIANTS) + len(REVIEWER_50), 159)

	def test_A_the_frappe_module_cannot_be_bound(self):
		for name, code in BINDING:
			with self.subTest(name):
				self.assertFlagged(name, "alias", code)

	def test_B_chains_not_on_the_allowlist_are_hits(self):
		for name, code in NOT_ALLOWED:
			with self.subTest(name):
				self.assertFlagged(name, "not-allowed", code)

	def test_B_a_marked_only_entry_needs_its_marker_and_its_file(self):
		code = "import frappe\n\ndef f():\n    return frappe.flags.get('ast_read_only')\n"
		self.assertFlagged("marked entry, no marker", "not-allowed", code, "assistant/guard.py")
		marked = code.replace("')\n", "')  # AST-ALLOWED: helper\n")
		self.assertClean({"assistant/guard.py": marked}, "marked, in guard.py")
		self.assertFlagged("marked entry in the wrong file", "not-allowed", marked, "assistant/access.py")
		self.assertFlagged("marked entry in a tool", "not-allowed", marked)
		self.assertFlagged("a marker without a reason", "not-allowed", code.replace("')\n", "')  # AST-ALLOWED:\n"), "assistant/guard.py")

	def test_B_each_file_restricted_entry_works_only_in_its_files(self):
		restricted = {
			"has_permission": ("import frappe\nimport frappe.permissions\n\ndef f():\n    return frappe.permissions.has_permission('Loan', 'read')\n", ("assistant/guard.py",)),
			"cache": ("import frappe\n\ndef f():\n    return frappe.cache.make_key('k')\n", ("assistant/ratelimit.py",)),
			"request_ip": ("import frappe\n\ndef f():\n    return frappe.local.request_ip\n", ("api/chat.py",)),
			"bench_path": ("import frappe\n\ndef f():\n    return frappe.utils.get_bench_path()\n", ("assistant/codereader.py",)),
			"whitelist": ("import frappe\n\n@frappe.whitelist(methods=['POST'])\ndef ask():\n    return 1\n", ("api/chat.py",)),
		}
		for name, (code, ok_files) in restricted.items():
			for rel in ok_files:
				self.assertClean({rel: code}, f"{name} in {rel}")
			self.assertFlagged(f"{name} in a tool", "not-allowed" if name != "whitelist" else "whitelist", code)

	def test_C_imports_are_allowlisted(self):
		bad = {
			"import frappe.model.document": "import frappe.model.document\n",
			"import frappe.utils": "import frappe.utils\n",
			"from frappe import throw": "from frappe import throw\n",
			"from frappe import local": "from frappe import local\n",
			"from frappe.utils import cint": "from frappe.utils import cint\n",
			"from frappe.permissions import has_permission": "from frappe.permissions import has_permission\n",
			"from frappe.model.document import Document in a tool": "from frappe.model.document import Document\n",
			"from frappe.database.query import Engine": "from frappe.database.query import Engine\n",
			"from frappe.auth import LoginManager": "from frappe.auth import LoginManager\n",
			"from frappe.query_builder import DocType": "from frappe.query_builder import DocType\n",
			"from frappe.model.document import get_doc": "from frappe.model.document import get_doc\n",
			"star import of another module": "from os.path import *\n",
		}
		for name, code in bad.items():
			with self.subTest(name):
				self.assertFlagged(name, "import", code)
		# an allowed import under another name is an alias (A), not a new import
		self.assertFlagged("from frappe import _ as t", "alias", "from frappe import _ as t\n")
		self.assertFlagged("now_datetime as n", "alias", "from frappe.utils import now_datetime as n\n")
		# an entry that is allowed only in some files
		self.assertFlagged("import frappe.permissions in a tool", "import", "import frappe.permissions\n")
		self.assertFlagged("get_permitted_fields in access.py", "import", "from frappe.model import get_permitted_fields\n", "assistant/access.py")
		self.assertFlagged("a marker never excuses an import", "import", "from frappe import throw  # AST-ALLOWED: because\n", "assistant/guard.py")

	def test_C_doctype_controllers_may_import_document_as_a_class_base_only(self):
		base = "from frappe.model.document import Document\n\n\nclass Thing(Document):\n    pass\n"
		self.assertClean({"lending_assistant/doctype/thing/thing.py": base}, "controller")
		self.assertClean({"other/doctype/thing/thing.py": base}, "any doctype folder")
		self.assertFlagged("Document in a tool", "import", base, "assistant/tools/thing.py")
		called = "from frappe.model.document import Document\n\n\ndef f():\n    return Document('Loan', 'x')\n"
		self.assertFlagged("Document(...) in a controller", "not-allowed", called, "lending_assistant/doctype/thing/thing.py")
		value = "from frappe.model.document import Document\n\nx = Document\n"
		self.assertFlagged("Document as a value", "not-allowed", value, "lending_assistant/doctype/thing/thing.py")

	def test_D_method_names_are_banned_whatever_the_receiver(self):
		for method, rule in METHODS:
			with self.subTest(method):
				self.assertFlagged(method, rule, f"def f(x):\n    return x.{method}()\n")
		self.assertFlagged("run on a query builder", "qb", "def f(q):\n    return q.from_('x').select('y').run()\n")
		self.assertFlagged("run on a query", "qb", "def f(query):\n    return query.run()\n")
		self.assertClean({"assistant/tools/plain.py": "def f(t):\n    return t.run()\n"}, "run on something that is not a query")

	def test_D_a_marker_excuses_a_method_only_in_the_file_that_may_use_it(self):
		self.assertClean({"assistant/audit.py": "def f(doc):\n    doc.insert()  # AST-ALLOWED: own log\n"})
		self.assertFlagged("insert marked in a tool", "write", "def f(doc):\n    doc.insert()  # AST-ALLOWED: please\n")
		self.assertFlagged("get_password marked in a tool", "secrets", "def f(doc):\n    doc.get_password('k')  # AST-ALLOWED: please\n")
		self.assertClean({"assistant/settings.py": "def f(doc):\n    return doc.get_password('k')  # AST-ALLOWED: the one key reader\n"})
		for method in ("connect", "init", "login_as", "set_user"):
			self.assertFlagged(f"{method} marked in guard.py", "identity-call", f"def f(x):\n    x.{method}()  # AST-ALLOWED: please\n", "assistant/guard.py")

	def test_E_dunders_and_builtins(self):
		for name in DUNDER_NAMES:
			with self.subTest(name):
				self.assertFlagged(f"attribute {name}", "dynamic", f"def f(x):\n    return x.{name}\n")
				self.assertFlagged(f"subscript {name}", "dynamic", f"def f(x):\n    return x['{name}']\n")
		self.assertFlagged("bare __builtins__", "dynamic", "def f():\n    return __builtins__\n")
		self.assertFlagged("getattr (kept)", "dynamic", "def f(x):\n    return getattr(x, 'a')\n")
		self.assertFlagged("importlib (kept)", "generic-exec", "import importlib\n")
		self.assertFlagged("builtins (kept)", "generic-exec", "import builtins\n")

	def test_E_frames_and_introspection_are_hits(self):
		for name, code in (
			("inspect", "import inspect\n"),
			("gc", "import gc\n\ndef f():\n    return gc.get_objects()\n"),
			("f_globals", "def f(fr):\n    return fr.f_globals['frappe']\n"),
			("f_back", "def f(fr):\n    return fr.f_back\n"),
			("tb_frame", "def f(tb):\n    return tb.tb_frame\n"),
			("sys._getframe", "import sys\n\ndef f():\n    return sys._getframe(1)\n"),
			("from inspect import currentframe", "from inspect import currentframe\n"),
		):
			with self.subTest(name):
				self.assertFlagged(name, "dynamic" if name in ("f_globals", "f_back", "tb_frame") else "generic-exec", code)
		self.assertFlagged("sys._getframe is dynamic access too", "generic-exec", "import sys\n\ndef f():\n    return sys._getframe(1)\n")

	def test_F_secrets_are_hits_outside_install(self):
		for code in (
			"import os\n\ndef f():\n    return os.environ['AST_ANTHROPIC_API_KEY']\n",
			"import os\n\ndef f():\n    return os.getenv('AST_ANTHROPIC_API_KEY')\n",
		):
			self.assertFlagged("environment read", "secrets", code)
		for code in (
			"import frappe\n\ndef f():\n    return frappe.conf.db_password\n",
			"import frappe\n\ndef f():\n    return frappe.conf['db_password']\n",
			"import frappe\n\ndef f():\n    return frappe.local.conf.db_password\n",
			"import frappe\n\ndef f():\n    return frappe.get_site_config()\n",
			"def f(x):\n    return x.get_site_config()\n",
		):
			with self.subTest(code):
				self.assertFlagged("secret", "secrets", code)
				self.assertFlagged("secret marked in guard.py", "secrets", code + "# AST-ALLOWED: please\n", "assistant/guard.py")
		marked = "import frappe\n\ndef f():\n    return frappe.conf.site_name  # AST-ALLOWED: install reads the site name\n"
		self.assertClean({"install.py": marked}, "install.py")
		self.assertFlagged("marked outside install.py", "secrets", marked, "assistant/guard.py")

	def test_G_flags_cannot_be_written_or_mutated(self):
		for name, code in FLAGS:
			with self.subTest(name):
				self.assertFlagged(name, "flags", code)
				marked_elsewhere = "\n".join(line + "  # AST-ALLOWED: please" if line.startswith("    ") else line for line in code.splitlines()) + "\n"
				self.assertFlagged(name + ", marked in a tool", "flags", marked_elsewhere)

	def test_a_new_allowlist_entry_is_needed_before_new_code_can_use_a_chain(self):
		"""The burden is reversed: unknown chains are hits, so new code needs an entry (and a review)."""
		self.assertFlagged("fresh chain", "not-allowed", "import frappe\n\ndef f():\n    return frappe.get_hooks('x')\n")

	def test_the_allowlist_has_no_dead_entries(self):
		spec = importlib.util.spec_from_file_location("guard_scan_for_test", SCRIPT)
		module = importlib.util.module_from_spec(spec)
		sys.modules[spec.name] = module
		spec.loader.exec_module(module)
		try:
			result = module.scan(SCRIPT.parent.parent, strict=True)
		finally:
			sys.modules.pop(spec.name, None)
		self.assertEqual(result.problems, [])
		self.assertEqual(result.unused_entries, [], "allowlist entries the app does not use widen the hole")
		self.assertGreater(len(module.ENTRIES), 20)

	def test_a_dead_entry_and_a_stale_marker_are_reported(self):
		root = self.make_tree({"assistant/x.py": "import frappe\n\ndef f():\n    return 1  # AST-ALLOWED: nothing here needs it\n"})
		result = run("--root", root, "--check-allowlist")
		self.assertEqual(result.returncode, 1)
		self.assertIn("dead entry", result.stdout)
		self.assertIn("excuses nothing", result.stdout)
		self.assertEqual(run("--root", root).returncode, 0)  # without the flag only real hits fail

	def test_every_marker_in_the_app_has_a_reason(self):
		package = Path(frappe.get_app_path("lending_assistant"))
		for path in list(package.rglob("*.py")) + list(package.rglob("*.js")):
			rel = path.relative_to(package).as_posix()
			if "tests/" in rel or "node_modules" in rel or "/dist/" in rel:
				continue
			for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
				if "AST-ALLOWED:" in line:
					reason = line.split("AST-ALLOWED:", 1)[1].strip()
					self.assertTrue(reason, f"{rel}:{number}: AST-ALLOWED without a reason")

	def test_ordinary_reads_are_not_flagged(self):
		root = self.make_tree(CLEAN_FORMS)
		result = run("--root", root)
		self.assertEqual(result.returncode, 0, result.stdout)

	def test_a_marker_only_works_in_the_file_that_may_use_that_rule(self):
		"""The new rules keep the per-file allowlist: alias and callbacks in guard.py only, the rest nowhere."""
		marked = {
			"alias": "import frappe\n\ndef _capture_identity():\n    d = frappe.db  # AST-ALLOWED: test\n",
			"callbacks": "import frappe\n\ndef _snapshot_callbacks():\n    m = frappe.db.after_commit  # AST-ALLOWED: test\n",
		}
		for rule, code in marked.items():
			ok = run("--root", self.make_tree({"assistant/guard.py": code}))
			self.assertEqual(ok.returncode, 0, f"{rule}: {ok.stdout}")
			bad = run("--root", self.make_tree({"assistant/access.py": code}))
			self.assertEqual(bad.returncode, 1, rule)
			self.assertIn("is not permitted in assistant/access.py", bad.stdout)
		for code in (
			"import frappe\n\ndef f():\n    frappe.qb.from_('Loan')  # AST-ALLOWED: test\n",
			"import frappe\n\ndef f():\n    frappe.db.add_index('Loan', ['x'])  # AST-ALLOWED: test\n",
			"def f(x):\n    getattr(x, 'a')  # AST-ALLOWED: test\n",
			"import frappe\n\ndef f():\n    frappe.enqueue('frappe.ping')  # AST-ALLOWED: test\n",
		):
			guard_file = run("--root", self.make_tree({"assistant/guard.py": code}))
			self.assertEqual(guard_file.returncode, 1, code)
			self.assertIn("is not permitted in assistant/guard.py", guard_file.stdout)

	def test_marked_lines_in_allowed_files_pass(self):
		root = self.make_tree(
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
		empty = tempfile.mkdtemp(prefix="ast_scan_")
		self.addCleanup(shutil.rmtree, empty, True)
		self.assertEqual(run("--root", empty).returncode, 2)
