"""M2b rework 3, run-time layer: R13 (identity layer correctness), R14, R15, R16.

`frappe.set_user`, `frappe.connect` and direct writes to `frappe.local` play the part of a careless tool, as in
test_guard_identity.py. That is allowed in tests/ only. Switch-and-back inside one call is NOT tested because it
cannot be seen from the end state: it is a documented known limit (DECISIONS #46).
"""

from unittest import mock

import frappe

from lending_assistant.assistant import guard
from lending_assistant.tests.base import GuardTestCase

LOAN = "Loan"


def error_logs():
	return frappe.db.sql("select count(*) from `tabError Log` where method=%s", "AST write blocked")[0][0]


class Rework3Case(GuardTestCase):
	def setUp(self):
		super().setUp()
		self.logs = error_logs()
		self.as_user("limited")
		self.user = frappe.session.user
		self.db = frappe.local.db
		self.flags_obj = frappe.local.flags
		self.rogues = []

	def tearDown(self):
		for rogue in self.rogues:
			try:
				rogue.close()
			except Exception:
				pass
		super().tearDown()

	def assertIntact(self):
		self.assertEqual(frappe.session.user, self.user)
		self.assertIs(frappe.local.db, self.db)
		self.assertNotIn("System Manager", frappe.get_roles())
		self.assertFalse(frappe.flags.get("ast_read_only"))
		self.assertEqual(frappe.db._disable_transaction_control, 0)


class TestR13IdentityLayer(Rework3Case):
	def test_user_switch_then_del_local_db_is_restored_and_raises(self):
		with self.assertRaises(guard.AssistantGuardError) as caught:
			with guard.read_only_tool_context("AST-TEST-del-db") as ctx:
				frappe.set_user("Administrator")
				del frappe.local.db
		self.assertIn(
			"identity or connection changed", str(caught.exception)
		)  # not RuntimeError: object is not bound
		self.assertEqual(sorted(ctx.identity_changes), ["database connection", "session user"])
		self.assertIntact()
		self.assertEqual(error_logs(), self.logs + 1)

	def test_the_context_is_usable_again_after_del_local_db(self):
		with self.assertRaises(guard.AssistantGuardError):
			with guard.read_only_tool_context("AST-TEST-del-db"):
				del frappe.local.db
		with guard.read_only_tool_context("AST-TEST-after") as ctx:
			self.assertEqual(len(guard.unwrap(guard.list_records(LOAN, limit=2))["rows"]), 2)
		self.assertFalse(ctx.violation)

	def test_del_local_session_and_flags_are_restored(self):
		with self.assertRaises(guard.AssistantGuardError):
			with guard.read_only_tool_context("AST-TEST-del-session") as ctx:
				del frappe.local.session
				del frappe.local.flags
		self.assertIn("session user", ctx.identity_changes)
		self.assertIn("flags", ctx.identity_changes)
		self.assertIs(frappe.local.flags, self.flags_obj)
		self.assertIntact()

	def test_the_real_connection_is_captured_not_the_proxy(self):
		"""`frappe.db` follows `frappe.local.db`; the context must keep hold of the object it started with."""
		seen = []
		with self.assertRaises(guard.AssistantGuardError):
			with guard.read_only_tool_context("AST-TEST-proxy"):
				frappe.connect()
				self.rogues.append(frappe.local.db)
				seen.append(frappe.local.db)
		self.assertIsNot(seen[0], self.db)
		self.assertIntact()
		self.assertEqual(
			frappe.db.sql("select 1")[0][0], 1
		)  # the original is back and has its savepoint released

	def test_a_context_on_a_cold_connection_opens_and_closes_cleanly(self):
		original = frappe.local.db
		frappe.connect(set_admin_as_user=False)  # a new Database object that has not opened its connection
		cold = frappe.local.db
		self.rogues.append(cold)
		try:
			self.assertIsNone(cold._conn)
			self.assertFalse(hasattr(cold, "_cursor"))
			with guard.read_only_tool_context("AST-TEST-cold") as ctx:
				self.assertIsNotNone(cold._conn)  # the savepoint opened it
			self.assertEqual(ctx.identity_changes, [])
			self.assertFalse(ctx.violation)
			self.assertIs(frappe.local.db, cold)
			self.assertEqual(cold._disable_transaction_control, 0)
			self.assertEqual(frappe.session.user, self.user)
		finally:
			frappe.local.db = original

	def test_a_cold_connection_swapped_inside_is_still_caught(self):
		original = frappe.local.db
		frappe.connect(set_admin_as_user=False)
		cold = frappe.local.db
		self.rogues.append(cold)
		try:
			with self.assertRaises(guard.AssistantGuardError):
				with guard.read_only_tool_context("AST-TEST-cold-swap") as ctx:
					frappe.local.db = original  # the tool replaces the connection that was just opened
			self.assertIn("database connection", ctx.identity_changes)
			self.assertIs(frappe.local.db, cold)
		finally:
			frappe.local.db = original

	def test_user_switch_plus_a_failed_rollback_still_restores_the_user(self):
		with mock.patch.object(self.db, "rollback", side_effect=RuntimeError("boom")):
			with self.assertRaises(guard.AssistantGuardError):
				with guard.read_only_tool_context("AST-TEST-rb-fail") as ctx:
					frappe.set_user("Administrator")
		self.assertEqual(ctx.identity_changes, ["session user"])
		self.assertTrue(ctx.savepoint_gone)  # the rollback did not happen: reported, not hidden
		self.assertEqual(frappe.session.user, self.user)
		self.assertNotIn("System Manager", frappe.get_roles())
		self.assertFalse(frappe.flags.get("ast_read_only"))
		self.assertEqual(frappe.db._disable_transaction_control, 0)

	def test_the_user_is_restored_even_when_the_rollback_raises_something_that_is_not_an_exception(self):
		with mock.patch.object(self.db, "rollback", side_effect=KeyboardInterrupt):
			with self.assertRaises(KeyboardInterrupt):
				with guard.read_only_tool_context("AST-TEST-rb-interrupt"):
					frappe.set_user("Administrator")
		self.assertEqual(frappe.session.user, self.user)
		self.assertFalse(frappe.flags.get("ast_read_only"))
		self.assertEqual(frappe.db._disable_transaction_control, 0)


class TestR14SavepointGone(Rework3Case):
	def test_a_raw_commit_is_a_violation_and_is_logged_before_the_raise(self):
		with self.assertRaises(guard.AssistantGuardError) as caught:
			with guard.read_only_tool_context("AST-TEST-raw-commit") as ctx:
				frappe.db.sql(f"release savepoint {ctx.savepoint}")  # what a raw COMMIT does to it
		self.assertIn("savepoint no longer exists", str(caught.exception))
		self.assertTrue(ctx.savepoint_gone)
		self.assertTrue(ctx.violation)
		self.assertEqual(ctx.summary()["savepoint_gone"], 1)
		self.assertEqual(error_logs(), self.logs + 1)
		text = frappe.db.sql(
			"select error from `tabError Log` where method=%s order by creation desc limit 1",
			"AST write blocked",
		)[0][0]
		self.assertIn("tool=AST-TEST-raw-commit", text)
		self.assertIn("savepoint_gone=1", text)
		self.assertNotIn("Loan", text)  # counts and the tool name only

	def test_a_normal_exit_is_not_a_violation(self):
		with guard.read_only_tool_context("AST-TEST-fine") as ctx:
			guard.list_records(LOAN, limit=1)
		self.assertFalse(ctx.savepoint_gone)
		self.assertEqual(error_logs(), self.logs)


class TestR15RogueConnection(Rework3Case):
	def assertClosed(self, conn):
		with self.assertRaises(Exception):
			cursor = conn.cursor()
			cursor.execute("select 1")

	def test_the_swapped_in_connection_is_closed_and_the_original_object_is_back(self):
		with self.assertRaises(guard.AssistantGuardError):
			with guard.read_only_tool_context("AST-TEST-rogue"):
				frappe.connect()
				rogue = frappe.local.db
				self.rogues.append(rogue)
				rogue.sql("select 1")  # open it for real
				raw = rogue._conn
		self.assertIs(frappe.local.db, self.db)
		self.assertIsNone(rogue._conn)  # the object no longer holds a connection
		self.assertClosed(raw)  # and the driver connection itself is closed

	def test_a_new_socket_on_the_same_object_is_closed_and_the_old_one_is_back(self):
		conn, cursor = self.db._conn, self.db._cursor
		with self.assertRaises(guard.AssistantGuardError):
			with guard.read_only_tool_context("AST-TEST-socket"):
				stray = self.db.get_connection()
				self.db._conn, self.db._cursor = stray, stray.cursor()
		self.assertIs(self.db._conn, conn)
		self.assertIs(self.db._cursor, cursor)
		self.assertClosed(stray)
		self.assertEqual(frappe.db.sql("select 1")[0][0], 1)

	def test_uncommitted_work_on_the_rogue_connection_is_rolled_back(self):
		marker = "AST-R15-ROLLBACK"
		with self.assertRaises(guard.AssistantGuardError):
			with guard.read_only_tool_context("AST-TEST-rogue-write"):
				frappe.connect()
				rogue = frappe.local.db
				self.rogues.append(rogue)
				rogue.sql(
					"insert into `tabDeleted Document` (name, deleted_doctype, deleted_name, creation, modified) values (%s, 'x', %s, now(), now())",
					(marker, marker),
				)
				raw = rogue._conn
		self.assertClosed(raw)
		fresh = frappe.db.sql("select count(*) from `tabDeleted Document` where name=%s", marker)[0][0]
		self.assertEqual(fresh, 0)


class TestR16FlagContents(Rework3Case):
	def test_a_security_relevant_flag_changed_inside_is_a_violation_and_is_restored(self):
		for key, value in (
			("in_install", "frappe"),
			("mute_emails", True),
			("ignore_links", True),
			("ast_something", 1),
			("ignore_permissions", True),
		):
			with self.subTest(key):
				before = frappe.flags.get(key)
				with self.assertRaises(guard.AssistantGuardError):
					with guard.read_only_tool_context("AST-TEST-flag") as ctx:
						frappe.flags[key] = value
				self.assertEqual(ctx.identity_changes, [f"flag {key}"])
				self.assertEqual(frappe.flags.get(key), before)
				self.assertIs(frappe.local.flags, self.flags_obj)

	def test_other_flags_are_restored_silently(self):
		try:
			with guard.read_only_tool_context("AST-TEST-quiet") as ctx:
				frappe.flags.cache_warm = True
				frappe.flags.some_counter = 7
			self.assertEqual(ctx.identity_changes, [])
			self.assertFalse(ctx.violation)
			self.assertNotIn("cache_warm", frappe.flags)
			self.assertNotIn("some_counter", frappe.flags)
		finally:
			frappe.flags.pop("cache_warm", None)
			frappe.flags.pop("some_counter", None)

	def test_a_neutral_flag_that_changes_is_put_back_without_a_violation(self):
		frappe.flags.test_neutral = "before"
		try:
			with guard.read_only_tool_context("AST-TEST-neutral") as ctx:
				frappe.flags.test_neutral = "after"
			self.assertFalse(ctx.violation)
			self.assertEqual(frappe.flags.test_neutral, "before")
		finally:
			frappe.flags.pop("test_neutral", None)

	def test_a_flag_removed_inside_is_put_back(self):
		frappe.flags.in_test_marker = 1
		try:
			with self.assertRaises(guard.AssistantGuardError):
				with guard.read_only_tool_context("AST-TEST-remove") as ctx:
					frappe.flags.pop("in_test_marker")
			self.assertEqual(ctx.identity_changes, ["flag in_test_marker"])
			self.assertEqual(frappe.flags.in_test_marker, 1)
		finally:
			frappe.flags.pop("in_test_marker", None)

	def test_the_guards_own_flags_are_not_a_violation(self):
		self.as_user(
			"senior"
		)  # a user who can really insert: the trap, not the permission check, must refuse
		self.user = frappe.session.user
		with guard.read_only_tool_context("AST-TEST-own") as ctx:
			with self.assertRaises(frappe.PermissionError):
				frappe.get_doc(
					{
						"doctype": "Loan Category",
						"loan_category_code": "AST-R16",
						"loan_category_name": "AST-R16",
					}
				).insert()
		self.assertEqual(ctx.identity_changes, [])
		self.assertEqual(ctx.trap_hits, 1)

	def test_normal_reads_do_not_touch_security_flags(self):
		visible, _hidden = self.loan_names()
		before = {k: v for k, v in frappe.flags.items() if k.startswith(guard._RISKY_FLAG_PREFIXES)}
		with guard.read_only_tool_context("AST-TEST-reads") as ctx:
			guard.read_doc(LOAN, visible)
			guard.list_records(LOAN, limit=3)
		self.assertEqual(ctx.identity_changes, [])
		self.assertEqual(
			{k: v for k, v in frappe.flags.items() if k.startswith(guard._RISKY_FLAG_PREFIXES)}, before
		)
