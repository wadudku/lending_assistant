"""The scanner (scripts/guard_scan.py) is clean on the app and fails on bad code."""

import shutil
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

# Forms the rework must NOT flag: ordinary reads of the identity, the message log, the cache and the meta.
CLEAN_FORMS = {
	"assistant/tools/ok1.py": """
		import frappe
		import frappe.permissions
		from frappe import _
		from frappe.utils import now_datetime

		def f(doc, values):
		    user = frappe.session.user
		    log = frappe.local.message_log
		    del frappe.local.message_log[1:]
		    frappe.cache.set_value("k", 1)
		    frappe.get_meta("Loan")
		    frappe.permissions.has_permission("Loan", "read")
		    doc.update(values)
		    values.update({"a": 1})
		    return user, log, _("x"), now_datetime()
	""",
}

EXPECTED_RULES = ("get-list", "db-read", "get-doc", "ignore-permissions", "user-switch", "write", "txn-control", "generic-exec", "file-access")


class TestGuardScan(AssistantTestCase):
	def make_tree(self, files):
		root = tree(files)
		self.addCleanup(shutil.rmtree, root, True)
		return root

	def test_app_is_clean(self):
		result = run()
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

	def test_ordinary_reads_are_not_flagged(self):
		root = self.make_tree(CLEAN_FORMS)
		result = run("--root", root)
		self.assertEqual(result.returncode, 0, result.stdout)

	def test_a_marker_only_works_in_the_file_that_may_use_that_rule(self):
		"""The new rules keep the per-file allowlist: alias and callbacks in guard.py only, the rest nowhere."""
		marked = {
			"alias": "import frappe\n\nd = frappe.db  # AST-ALLOWED: test\n",
			"callbacks": "import frappe\n\nm = frappe.db.after_commit  # AST-ALLOWED: test\n",
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
