"""M2b-R8 run-time layer and M2b-R9: the context notices when identity or the connection changed, undoes it, and
snapshots the callback queues by contents.

`frappe.set_user`, `frappe.connect` and direct writes to `frappe.local` are used here to play the part of a
careless tool. That is allowed in tests/ only.
"""

from collections import deque

import frappe

from lending_assistant.assistant import guard
from lending_assistant.tests.base import GuardTestCase

LOAN = "Loan"


def error_logs():
	return frappe.db.sql("select count(*) from `tabError Log` where method=%s", "AST write blocked")[0][0]


class TestIdentityCheck(GuardTestCase):
	def setUp(self):
		super().setUp()
		self.logs = error_logs()
		self.as_user("limited")
		self.user = frappe.session.user
		self.db = frappe.local.db
		self.rogues = []

	def tearDown(self):
		for rogue in self.rogues:
			try:
				rogue.close()
			except Exception:
				pass
		super().tearDown()

	def assertIdentityIntact(self):
		self.assertEqual(frappe.session.user, self.user)
		self.assertIs(frappe.local.db, self.db)
		self.assertNotIn("System Manager", frappe.get_roles())  # the permission caches are the limited user's again

	# --- the session user

	def test_switching_the_user_is_reversed_and_raises(self):
		with self.assertRaises(guard.AssistantGuardError) as caught:
			with guard.read_only_tool_context("AST-TEST-user-switch") as ctx:
				frappe.set_user("Administrator")
				self.assertIn("System Manager", frappe.get_roles())  # the tool really is Administrator in here
		self.assertIn("identity or connection changed", str(caught.exception))
		self.assertEqual(ctx.identity_changes, ["session user"])
		self.assertTrue(ctx.violation)
		self.assertIdentityIntact()
		self.assertEqual(error_logs(), self.logs + 1)

	def test_the_permissions_after_the_swap_are_the_limited_users(self):
		"""set_user() cached Administrator's permissions; the restore must clear them, not only the name."""
		visible = len(frappe.get_list(LOAN, pluck="name", limit=100))
		user_write = frappe.has_permission("Customer", "create")
		roles = sorted(frappe.get_roles())
		with self.assertRaises(guard.AssistantGuardError):
			with guard.read_only_tool_context("AST-TEST-user-switch"):
				frappe.set_user("Administrator")
				frappe.get_list(LOAN, pluck="name", limit=1)  # warms Administrator's caches
				self.assertEqual(frappe.get_user().name, "Administrator")  # frappe.local.user_perms is now Administrator's
		self.assertEqual(len(frappe.get_list(LOAN, pluck="name", limit=100)), visible)
		self.assertEqual(frappe.has_permission("Customer", "create"), user_write)
		self.assertEqual(sorted(frappe.get_roles()), roles)
		self.assertEqual(frappe.get_user().name, self.user)  # not the UserPermissions object cached for Administrator

	def test_assigning_the_session_user_directly_is_reversed(self):
		with self.assertRaises(guard.AssistantGuardError):
			with guard.read_only_tool_context("AST-TEST-user-assign"):
				frappe.session.user = "Administrator"
		self.assertIdentityIntact()

	def test_replacing_the_whole_session_object_is_reversed(self):
		original = frappe.local.session
		with self.assertRaises(guard.AssistantGuardError):
			with guard.read_only_tool_context("AST-TEST-session-swap"):
				frappe.local.session = frappe._dict(user="Administrator", sid="Administrator", data=frappe._dict())
		self.assertIs(frappe.local.session, original)
		self.assertIdentityIntact()

	def test_the_ignore_permissions_flag_is_reversed(self):
		self.assertFalse(frappe.flags.ignore_permissions)
		with self.assertRaises(guard.AssistantGuardError):
			with guard.read_only_tool_context("AST-TEST-flag"):
				frappe.flags.ignore_permissions = True
		self.assertFalse(frappe.flags.ignore_permissions)

	def test_replacing_the_flags_object_is_reversed(self):
		flags = frappe.local.flags
		with self.assertRaises(guard.AssistantGuardError):
			with guard.read_only_tool_context("AST-TEST-flags-swap"):
				frappe.local.flags = frappe._dict()  # the trap flag would be gone with it
		self.assertIs(frappe.local.flags, flags)
		self.assertFalse(frappe.flags.ast_read_only)

	def test_changing_the_site_is_reversed(self):
		site = frappe.local.site
		with self.assertRaises(guard.AssistantGuardError):
			with guard.read_only_tool_context("AST-TEST-site"):
				frappe.local.site = "some_other_site"
		self.assertEqual(frappe.local.site, site)

	# --- the connection

	def test_swapping_in_a_new_connection_is_reversed_and_raises(self):
		with self.assertRaises(guard.AssistantGuardError):
			with guard.read_only_tool_context("AST-TEST-connect") as ctx:
				frappe.connect()  # a new connection, and Administrator as the session user
				self.rogues.append(frappe.local.db)
				self.assertIsNot(frappe.local.db, self.db)
				self.assertEqual(frappe.session.user, "Administrator")
		self.assertEqual(ctx.identity_changes, ["database connection", "session user"])
		self.assertIdentityIntact()
		self.assertEqual(error_logs(), self.logs + 1)

	def test_the_original_connection_still_works_and_still_rolls_back(self):
		"""After a swap the original is back, its savepoint is intact, and the usual read works as before."""
		with self.assertRaises(guard.AssistantGuardError):
			with guard.read_only_tool_context("AST-TEST-connect"):
				frappe.connect()
				self.rogues.append(frappe.local.db)
		self.assertTrue(frappe.get_list(LOAN, pluck="name", limit=1))
		with guard.read_only_tool_context("AST-TEST-after-swap") as ctx:
			self.assertEqual(len(guard.unwrap(guard.list_records(LOAN, limit=2))["rows"]), 2)
		self.assertFalse(ctx.violation)

	def test_a_swapped_socket_on_the_same_connection_object_is_reversed(self):
		conn, cursor = frappe.local.db._conn, frappe.local.db._cursor
		with self.assertRaises(guard.AssistantGuardError):
			with guard.read_only_tool_context("AST-TEST-socket"):
				frappe.local.db._conn = object()
				frappe.local.db._cursor = object()
		self.assertIs(frappe.local.db._conn, conn)
		self.assertIs(frappe.local.db._cursor, cursor)

	def test_the_transaction_counters_are_restored_after_a_swap(self):
		control = frappe.db._disable_transaction_control
		with self.assertRaises(guard.AssistantGuardError):
			with guard.read_only_tool_context("AST-TEST-connect"):
				frappe.connect()
				self.rogues.append(frappe.local.db)
		self.assertEqual(frappe.db._disable_transaction_control, control)
		self.assertFalse(frappe.flags.ast_read_only)

	# --- no false positives

	def test_normal_reads_raise_nothing_and_log_nothing(self):
		visible, _hidden = self.loan_names()
		with guard.read_only_tool_context("AST-TEST-normal") as ctx:
			guard.read_doc(LOAN, visible)
			guard.list_records(LOAN, limit=5)
			frappe.get_list(LOAN, pluck="name", limit=3)
			frappe.get_meta(LOAN)
		self.assertEqual(ctx.identity_changes, [])
		self.assertFalse(ctx.violation)
		self.assertEqual(error_logs(), self.logs)
		self.assertIdentityIntact()

	def test_normal_reads_in_nested_contexts_raise_nothing(self):
		with guard.read_only_tool_context("AST-TEST-outer") as outer:
			with guard.read_only_tool_context("AST-TEST-inner") as inner:
				guard.list_records(LOAN, limit=2)
			guard.list_records(LOAN, limit=2)
		self.assertFalse(outer.violation or inner.violation)

	def test_a_hidden_or_missing_record_inside_the_context_is_not_an_identity_change(self):
		_visible, hidden = self.loan_names()
		with guard.read_only_tool_context("AST-TEST-g4") as ctx:
			with self.assertRaises(guard.RecordNotAvailable):
				guard.read_doc(LOAN, hidden)
		self.assertEqual(ctx.identity_changes, [])

	# --- nesting

	def test_a_swap_in_an_inner_context_is_caught_by_the_inner_one(self):
		with guard.read_only_tool_context("AST-TEST-outer") as outer:
			with self.assertRaises(guard.AssistantGuardError):
				with guard.read_only_tool_context("AST-TEST-inner") as inner:
					frappe.set_user("Administrator")
			self.assertEqual(frappe.session.user, self.user)  # back in the outer context, as the limited user
			self.assertTrue(frappe.flags.ast_read_only)  # and the outer context is still active
		self.assertEqual(inner.identity_changes, ["session user"])
		self.assertTrue(outer.violation)  # passed up
		self.assertEqual(outer.summary()["identity_changes"], 1)
		self.assertEqual(error_logs(), self.logs + 1)  # logged once, by the outermost context
		self.assertIdentityIntact()

	def test_the_identity_error_wins_over_the_tools_own_exception_but_state_is_restored(self):
		with self.assertRaises(guard.AssistantGuardError):
			with guard.read_only_tool_context("AST-TEST-err"):
				frappe.set_user("Administrator")
				raise ValueError("tool failed")
		self.assertIdentityIntact()
		self.assertFalse(frappe.flags.ast_read_only)

	def test_the_write_trap_still_holds_after_a_user_switch(self):
		"""Changing the user does not switch the trap off: a save as Administrator inside the context is refused."""
		category = "Loan Category"
		with self.assertRaises(guard.AssistantGuardError):
			with guard.read_only_tool_context("AST-TEST-switch-then-write") as ctx:
				frappe.set_user("Administrator")
				with self.assertRaises(frappe.PermissionError):
					frappe.get_doc({"doctype": category, "loan_category_code": "AST-NEW-X", "loan_category_name": "AST-NEW-X"}).insert()
		self.assertEqual(ctx.trap_hits, 1)


class TestCallbackSnapshot(GuardTestCase):
	"""M2b-R9: the queues are snapshotted by contents, so consuming earlier callbacks does not hide new ones."""

	MANAGERS = ("before_commit", "after_commit", "before_rollback", "after_rollback")

	def setUp(self):
		super().setUp()
		for name in self.MANAGERS:
			getattr(frappe.db, name).reset()
		self.logs = error_logs()
		self.ran = []

	def tearDown(self):
		for name in self.MANAGERS:
			getattr(frappe.db, name).reset()
		super().tearDown()

	def mark(self, label):
		return lambda: self.ran.append(label)

	def test_the_reviewers_sequence(self):
		"""add(PRE-X); inside: run() then add(INSIDE-SWAP); exit; commit -> PRE-X once, INSIDE-SWAP never."""
		frappe.db.after_commit.add(self.mark("PRE-X"))
		with guard.read_only_tool_context("AST-TEST-r9") as ctx:
			frappe.db.after_commit.run()  # consumes PRE-X inside the trap (its effect would be rolled back)
			frappe.db.after_commit.add(self.mark("INSIDE-SWAP"))
		self.assertEqual(self.ran, ["PRE-X"])  # it ran once, inside the context
		self.assertEqual(ctx.callbacks_dropped, 1)  # INSIDE-SWAP
		self.assertEqual(ctx.callbacks_restored, 1)  # PRE-X put back for the real commit
		self.assertTrue(ctx.violation)
		self.ran.clear()
		frappe.db.after_commit.run()  # what the real commit does
		self.assertEqual(self.ran, ["PRE-X"])  # exactly once at the real commit, INSIDE-SWAP never
		text = frappe.db.sql("select error from `tabError Log` where method=%s order by creation desc limit 1", "AST write blocked")[0][0]
		self.assertIn("callbacks_dropped=1", text)
		self.assertIn("callbacks_restored=1", text)

	def test_the_same_count_swapped_for_new_functions_is_not_hidden(self):
		"""The old length comparison missed this: one callback consumed and one added is still length 1."""
		frappe.db.after_commit.add(self.mark("PRE"))
		with guard.read_only_tool_context("AST-TEST-r9") as ctx:
			frappe.db.after_commit.reset()
			frappe.db.after_commit.add(self.mark("NEW"))
		frappe.db.after_commit.run()
		self.assertEqual(self.ran, ["PRE"])
		self.assertEqual((ctx.callbacks_dropped, ctx.callbacks_restored), (1, 1))

	def test_a_replaced_queue_object_is_put_back(self):
		frappe.db.before_commit.add(self.mark("PRE"))
		queue = frappe.db.before_commit._functions
		with guard.read_only_tool_context("AST-TEST-r9") as ctx:
			frappe.db.before_commit._functions = deque([self.mark("EVIL")])
		self.assertIs(frappe.db.before_commit._functions, queue)
		frappe.db.before_commit.run()
		self.assertEqual(self.ran, ["PRE"])
		self.assertEqual((ctx.callbacks_dropped, ctx.callbacks_restored), (1, 1))

	def test_the_same_function_added_twice_counts_as_one_added(self):
		fn = self.mark("PRE")
		frappe.db.after_commit.add(fn)
		with guard.read_only_tool_context("AST-TEST-r9") as ctx:
			frappe.db.after_commit.add(fn)  # same object, a second entry
		self.assertEqual(ctx.callbacks_dropped, 1)
		frappe.db.after_commit.run()
		self.assertEqual(self.ran, ["PRE"])

	def test_earlier_callbacks_run_exactly_once_when_nothing_happened(self):
		for name in self.MANAGERS:
			getattr(frappe.db, name).add(self.mark("pre-" + name))
		with guard.read_only_tool_context("AST-TEST-r9") as ctx:
			frappe.get_meta("Loan")
		self.assertFalse(ctx.violation)
		for name in self.MANAGERS:
			getattr(frappe.db, name).run()
		self.assertEqual(sorted(self.ran), sorted("pre-" + n for n in self.MANAGERS))

	def test_order_of_earlier_callbacks_is_kept(self):
		for label in ("a", "b", "c"):
			frappe.db.after_commit.add(self.mark(label))
		with guard.read_only_tool_context("AST-TEST-r9"):
			frappe.db.after_commit.add(self.mark("x"))
		frappe.db.after_commit.run()
		self.assertEqual(self.ran, ["a", "b", "c"])

	def test_callbacks_on_a_swapped_connection_leave_with_it(self):
		"""A callback registered on the new connection (after frappe.connect) never reaches the restored one."""
		frappe.db.after_commit.add(self.mark("PRE"))
		self.as_user("limited")
		rogue = None
		with self.assertRaises(guard.AssistantGuardError):
			with guard.read_only_tool_context("AST-TEST-r9-connect"):
				frappe.connect()
				rogue = frappe.local.db
				frappe.db.after_commit.add(self.mark("ROGUE"))
		rogue.close()
		frappe.db.after_commit.run()
		self.assertEqual(self.ran, ["PRE"])
