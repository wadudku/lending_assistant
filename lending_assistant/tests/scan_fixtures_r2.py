"""Scanner fixtures for M2b rework 2 (DECISIONS #43). Data only; `test_guard_scan.py` runs them.

Each row is (name, expected rule, code). Each is written into its own tree and must fail the scan on its own, with
the rule named. They are tool code (`assistant/tools/x.py`) unless the row says otherwise.
"""

# --- The Reviewer's 50 variants from the first rework review (M2b-R8, R10). n24-n26 are the flag mutators (R10).
REVIEWER_50 = [
	# the six the old scanner already caught
	("n01 from frappe import db as d", "alias", "from frappe import db as d\n"),
	("n02 frappe.db.__class__", "dynamic", "import frappe\n\ndef f():\n    return frappe.db.__class__\n"),
	("n03 type(frappe.db)", "alias", "import frappe\n\ndef f():\n    return type(frappe.db)\n"),
	("n04 doc.flags.ignore_permissions", "ignore-permissions", "def f(doc):\n    doc.flags.ignore_permissions = True\n"),
	("n05 get_list(**ignore_permissions)", "get-list", "import frappe\n\ndef f():\n    frappe.get_list(**{'ignore_permissions': True})\n"),
	("n06 frappe.qb", "qb", "import frappe\n\ndef f():\n    return frappe.qb\n"),
	# the module bound to another name, in every shape (the worst: `f = frappe; f.connect(); f.db.sql(...)`)
	("n07 f = frappe; f.db.sql", "alias", "import frappe\n\ndef f():\n    g = frappe\n    return g.db.sql('select count(*) from tabLoan')\n"),
	("n08 import as f; g = f", "alias", "import frappe as f\n\ng = f\ng.db.sql('select 1')\n"),
	("n09 [frappe][0]", "alias", "import frappe\n\ndef f():\n    return [frappe][0].db.sql('select 1')\n"),
	("n10 comprehension over [frappe]", "alias", "import frappe\n\ndef f():\n    return [m.db.sql('select 1') for m in [frappe]]\n"),
	("n11 for m in (frappe,)", "alias", "import frappe\n\ndef f():\n    for m in (frappe,):\n        m.get_value('Loan', 'x', 'status')\n"),
	("n12 default parameter", "alias", "import frappe\n\ndef t(fr=frappe):\n    return fr.db.get_value('Loan', 'x', 'status')\n"),
	("n13 match case object(db=d)", "alias", "import frappe\n\ndef f():\n    match frappe:\n        case object(db=d):\n            return d.sql('select 1')\n"),
	("n14 (lambda: frappe)()", "alias", "import frappe\n\ndef f():\n    return (lambda: frappe)().db.sql('select 1')\n"),
	("n15 walrus", "alias", "import frappe\n\ndef f():\n    return (f := frappe).db.sql('select 1')\n"),
	("n16 with nullcontext(frappe) as f", "alias", "import frappe\nfrom contextlib import nullcontext\n\ndef t():\n    with nullcontext(frappe) as f:\n        return f.db.sql('select 1')\n"),
	("n17 decorator passes frappe in", "alias", "import frappe\n\ndef deco(fn):\n    def wrapper(*a):\n        return fn(frappe, *a)\n    return wrapper\n\n@deco\ndef t(fr):\n    return fr.get_doc('Loan', 'x')\n"),
	("n18 class attribute K.f = frappe", "alias", "import frappe\n\nclass K:\n    pass\n\nK.f = frappe\n"),
	("n19 dict S['f']", "alias", "import frappe\n\nS = {'f': frappe}\n\ndef t():\n    return S['f'].db.sql('select 1')\n"),
	("n20 cache = frappe", "alias", "import frappe\n\ndef t():\n    cache = frappe\n    return cache.get_all('Loan')\n"),
	# the same APIs through another door
	("n21 frappe.local.qb", "qb", "import frappe\n\ndef t():\n    return frappe.local.qb.from_('Loan').select('*').run()\n"),
	("n22 frappe.local.__getattr__", "dynamic", "import frappe\n\ndef t():\n    return frappe.local.__getattr__('db').sql('select 1')\n"),
	("n23 from frappe.model.document import get_doc", "import", "from frappe.model.document import get_doc\n\ndef t():\n    return get_doc('Loan', 'x')\n"),
	("n24 flags.update(ignore_permissions)", "flags", "import frappe\n\ndef t():\n    frappe.flags.update({'ignore_permissions': True})\n"),
	("n25 flags.setdefault(ignore_permissions)", "flags", "import frappe\n\ndef t():\n    frappe.flags.setdefault('ignore_permissions', True)\n"),
	("n26 flags['ignore_' + 'permissions']", "flags", "import frappe\n\ndef t():\n    frappe.flags['ignore_' + 'permissions'] = True\n"),
	("n27 Document(...)", "import", "from frappe.model.document import Document\n\ndef t():\n    return Document('Loan', 'x')\n"),
	("n28 frappe.model.document.get_doc", "not-allowed", "import frappe\n\ndef t():\n    return frappe.model.document.get_doc('Loan', 'x')\n"),
	("n29 Engine().get_query().run()", "import", "from frappe.database.query import Engine\n\ndef t():\n    return Engine().get_query('Loan').run()\n"),
	("n30 frappe.query_builder.DocType", "qb", "import frappe\n\ndef t():\n    return frappe.query_builder.DocType('Loan')\n"),
	# identity
	("n31 frappe.connect()", "identity-call", "import frappe\n\ndef t():\n    frappe.connect()\n"),
	("n32 frappe.init()", "identity-call", "import frappe\n\ndef t():\n    frappe.init(site='x')\n"),
	("n33 frappe.local.login_manager.login_as", "identity-call", "import frappe\n\ndef t():\n    frappe.local.login_manager.login_as('Administrator')\n"),
	("n34 LoginManager().login_as", "import", "from frappe.auth import LoginManager\n\ndef t():\n    LoginManager().login_as('Administrator')\n"),
	("n35 the 8-line tool: alias, connect, sql, commit", "alias", "import frappe\n\ndef tool(name):\n    f = frappe\n    f.connect()\n    f.db.sql('update tabNote set content=%s where name=%s', ('x', name))\n    f.db.commit()\n    return f.get_doc('Loan', name).as_dict()\n"),
	# dynamic
	("n36 __builtins__['getattr']", "dynamic", "def t(x):\n    return __builtins__['getattr'](x, 'sql')\n"),
	("n37 __builtins__.getattr", "dynamic", "def t(x):\n    return __builtins__.getattr(x, 'sql')\n"),
	("n38 frappe.local.__dict__['db']", "dynamic", "import frappe\n\ndef t():\n    return frappe.local.__dict__['db']\n"),
	("n39 reduce(__getattribute__)", "dynamic", "import functools\nimport frappe\n\ndef t():\n    return functools.reduce(lambda o, a: o.__getattribute__(a), ['db', 'sql'], frappe)\n"),
	("n40 frappe.__dict__['get_all']", "dynamic", "import frappe\n\ndef t():\n    return frappe.__dict__['get_all']\n"),
	# secrets and low impact
	("n41 frappe.conf.db_password", "secrets", "import frappe\n\ndef t():\n    return frappe.conf.db_password\n"),
	("n42 frappe.get_site_config()", "secrets", "import frappe\n\ndef t():\n    return frappe.get_site_config()\n"),
	("n43 frappe.share.add", "not-allowed", "import frappe\n\ndef t():\n    frappe.share.add('Loan', 'x', user='a@b.c')\n"),
	("n44 frappe.flags.in_install = True", "flags", "import frappe\n\ndef t():\n    frappe.flags.in_install = True\n"),
	("n45 frappe.local.session_obj = None", "user-switch", "import frappe\n\ndef t():\n    frappe.local.session_obj = None\n"),
	("n46 cache = y(); cache.save()", "write", "def t(y):\n    cache = y()\n    cache.save()\n"),
	("n47 import frappe.database.database as dd", "alias", "import frappe.database.database as dd\n"),
	("n48 frappe.utils.get_attr", "not-allowed", "import frappe\n\ndef t():\n    return frappe.utils.get_attr('frappe.ping')\n"),
	# the two controls the Reviewer called "correctly clean": under the allowlist they are not (frappe.cache is
	# ratelimit.py only; get_link_to_form is not a listed helper)
	("n49 frappe.cache.set_value (stricter now)", "not-allowed", "import frappe\n\ndef t():\n    frappe.cache.set_value('k', 1)\n"),
	("n50 frappe.utils.get_link_to_form (stricter now)", "not-allowed", "import frappe\n\ndef t():\n    return frappe.utils.get_link_to_form('Loan', 'x')\n"),
]

# --- (A) the module cannot be bound: every shape
BINDING = [
	("A assignment", "import frappe\n\nf = frappe\n"),
	("A annotated assignment", "import frappe\n\nf: object = frappe\n"),
	("A walrus", "import frappe\n\ndef t():\n    return (f := frappe)\n"),
	("A argument", "import frappe\n\ndef t(g):\n    return g(frappe)\n"),
	("A keyword argument", "import frappe\n\ndef t(g):\n    return g(x=frappe)\n"),
	("A default parameter", "import frappe\n\ndef t(fr=frappe):\n    return fr\n"),
	("A keyword-only default", "import frappe\n\ndef t(*, fr=frappe):\n    return fr\n"),
	("A list element", "import frappe\n\nx = [frappe]\n"),
	("A tuple element", "import frappe\n\nx = (frappe,)\n"),
	("A dict value", "import frappe\n\nx = {'f': frappe}\n"),
	("A dict key", "import frappe\n\nx = {frappe: 1}\n"),
	("A set element", "import frappe\n\nx = {frappe}\n"),
	("A return", "import frappe\n\ndef t():\n    return frappe\n"),
	("A yield", "import frappe\n\ndef t():\n    yield frappe\n"),
	("A lambda", "import frappe\n\nx = lambda: frappe\n"),
	("A with-as", "import frappe\n\ndef t():\n    with frappe as f:\n        pass\n"),
	("A for iterable", "import frappe\n\ndef t():\n    for m in (frappe,):\n        pass\n"),
	("A for target", "import frappe\n\ndef t():\n    for frappe in (1, 2):\n        pass\n"),
	("A comprehension iterable", "import frappe\n\nx = [m for m in [frappe]]\n"),
	("A comprehension target", "import frappe\n\nx = [1 for frappe in range(2)]\n"),
	("A match subject", "import frappe\n\ndef t():\n    match frappe:\n        case _:\n            pass\n"),
	("A match capture", "def t(x):\n    match x:\n        case frappe:\n            pass\n"),
	("A match sequence capture", "def t(x):\n    match x:\n        case [frappe, *rest]:\n            pass\n"),
	("A match star capture", "def t(x):\n    match x:\n        case [*frappe]:\n            pass\n"),
	("A match mapping rest", "def t(x):\n    match x:\n        case {'a': 1, **frappe}:\n            pass\n"),
	("A class attribute", "import frappe\n\nclass K:\n    f = frappe\n"),
	("A attribute assignment", "import frappe\n\nclass K:\n    pass\n\nK.f = frappe\n"),
	("A decorator argument", "import frappe\n\n@deco(frappe)\ndef t():\n    pass\n"),
	("A decorator itself", "import frappe\n\n@frappe\ndef t():\n    pass\n"),
	("A global", "def t():\n    global frappe\n"),
	("A nonlocal", "def outer():\n    frappe = 1\n    def t():\n        nonlocal frappe\n"),
	("A import as", "import frappe as f\n"),
	("A import submodule as", "import frappe.utils as u\n"),
	("A from-import as", "from frappe import utils as u\n"),
	("A import another name as frappe", "import os as frappe\n"),
	("A from-import binds frappe", "from lending_assistant.assistant.guard import frappe\n"),
	("A function parameter named frappe", "def t(frappe):\n    return frappe\n"),
	("A def frappe", "def frappe():\n    pass\n"),
	("A class frappe", "class frappe:\n    pass\n"),
	("A except as frappe", "def t():\n    try:\n        pass\n    except Exception as frappe:\n        pass\n"),
	("A rebind", "import frappe\n\nfrappe = 1\n"),
	("A augmented rebind", "import frappe\n\nfrappe += 1\n"),
	("A del", "import frappe\n\ndel frappe\n"),
	("A module reached through another module", "from lending_assistant.assistant import guard\n\ndef t():\n    return guard.frappe.db.sql('select 1')\n"),
	("A isinstance argument", "import frappe\n\ndef t(x):\n    return isinstance(x, frappe)\n"),
	("A conditional expression", "import frappe\n\ndef t(c):\n    return frappe if c else None\n"),
	("A f-string", "import frappe\n\ndef t():\n    return f'{frappe}'\n"),
	("A starred", "import frappe\n\ndef t(g):\n    return g(*[frappe])\n"),
	("A await-free generator send", "import frappe\n\ndef t():\n    x = yield frappe\n"),
]

# --- (B) chains that are on no allowlist entry, whatever they are
NOT_ALLOWED = [
	("B utils helper not listed", "import frappe\n\ndef t():\n    return frappe.utils.cint('1')\n"),
	("B utils.now unlisted", "import frappe\n\ndef t():\n    return frappe.utils.today()\n"),
	("B session.user called", "import frappe\n\ndef t():\n    return frappe.session.user()\n"),
	("B session.data", "import frappe\n\ndef t():\n    return frappe.session.data\n"),
	("B get_roles stored", "import frappe\n\ndef t():\n    frappe.get_roles = None\n"),
	("B frappe.local.site read in a tool", "import frappe\n\ndef t():\n    return frappe.local.site\n"),
	("B request_ip outside api/chat.py", "import frappe\n\ndef t():\n    return frappe.local.request_ip\n"),
	("B flags read", "import frappe\n\ndef t():\n    return frappe.flags.in_test\n"),
	("B frappe.local.form_dict", "import frappe\n\ndef t():\n    return frappe.local.form_dict\n"),
	("B frappe.local.request", "import frappe\n\ndef t():\n    return frappe.local.request\n"),
	("B frappe.get_cached_value-like helper", "import frappe\n\ndef t():\n    return frappe.get_system_settings('x')\n"),
	("B frappe.as_json", "import frappe\n\ndef t():\n    return frappe.as_json({})\n"),
	("B frappe.render_template", "import frappe\n\ndef t():\n    return frappe.render_template('x', {})\n"),
	("B frappe.parse_json", "import frappe\n\ndef t():\n    return frappe.parse_json('{}')\n"),
	("B frappe.has_permission", "import frappe\n\ndef t():\n    return frappe.has_permission('Loan')\n"),
	("B frappe.permissions other function", "import frappe\nimport frappe.permissions\n\ndef t():\n    return frappe.permissions.get_roles('x')\n"),
	("B has_permission in a tool (guard.py and access.py only)", "import frappe\nimport frappe.permissions\n\ndef t():\n    return frappe.permissions.has_permission('Loan', 'read')\n"),
	("B get_bench_path outside codereader", "import frappe\n\ndef t():\n    return frappe.utils.get_bench_path()\n"),
	("B frappe.cache outside ratelimit", "import frappe\n\ndef t():\n    return frappe.cache.make_key('x')\n"),
	("B frappe.log_error outside guard", "import frappe\n\ndef t():\n    frappe.log_error('t', 'm')\n"),
	("B a marker does not excuse an unlisted chain", "import frappe\n\ndef t():\n    return frappe.share.add('Loan', 'x')  # AST-ALLOWED: please\n"),
]

# --- (D) method names, whatever the receiver is. (method, rule)
METHODS = [
	("sql", "db-read"), ("sql_ddl", "db-read"), ("multisql", "db-read"), ("get_value", "db-read"),
	("get_values", "db-read"), ("get_all", "db-read"), ("get_doc", "get-doc"), ("get_cached_doc", "get-doc"),
	("new_doc", "get-doc"), ("delete_doc", "write"), ("rename_doc", "write"), ("set_value", "write"),
	("db_set", "write"), ("insert", "write"), ("save", "write"), ("submit", "write"), ("cancel", "write"),
	("delete", "write"), ("commit", "txn-control"), ("rollback", "txn-control"), ("connect", "identity-call"),
	("init", "identity-call"), ("login_as", "identity-call"), ("set_user", "identity-call"),
	("enqueue", "side-effect"), ("sendmail", "side-effect"), ("get_site_config", "secrets"),
	("get_password", "secrets"),
]  # fmt: skip

# --- (E) dunders: attribute and string subscript
DUNDER_NAMES = [
	"__builtins__", "__dict__", "__class__", "__globals__", "__subclasses__", "__mro__", "__getattribute__", "__import__",
]  # fmt: skip

# --- (G) flags
FLAGS = [
	("G update", "import frappe\n\ndef t():\n    frappe.flags.update({'x': 1})\n"),
	("G setdefault", "import frappe\n\ndef t():\n    frappe.flags.setdefault('x', 1)\n"),
	("G pop", "import frappe\n\ndef t():\n    frappe.flags.pop('x')\n"),
	("G clear", "import frappe\n\ndef t():\n    frappe.flags.clear()\n"),
	("G __setitem__", "import frappe\n\ndef t():\n    frappe.flags.__setitem__('x', 1)\n"),
	("G constant subscript write", "import frappe\n\ndef t():\n    frappe.flags['x'] = 1\n"),
	("G computed subscript read", "import frappe\n\ndef t(k):\n    return frappe.flags[k]\n"),
	("G computed subscript write", "import frappe\n\ndef t(k):\n    frappe.flags[k] = 1\n"),
	("G attribute write", "import frappe\n\ndef t():\n    frappe.flags.x = 1\n"),
	("G attribute delete", "import frappe\n\ndef t():\n    del frappe.flags.x\n"),
	("G augmented write", "import frappe\n\ndef t():\n    frappe.flags.n += 1\n"),
	("G local.flags update", "import frappe\n\ndef t():\n    frappe.local.flags.update({'x': 1})\n"),
	("G local.flags write", "import frappe\n\ndef t():\n    frappe.local.flags.x = 1\n"),
	("G doc.flags update", "def t(doc):\n    doc.flags.update({'ignore_permissions': True})\n"),
]
