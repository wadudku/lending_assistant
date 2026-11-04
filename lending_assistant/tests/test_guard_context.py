"""R1 and G1: the read-only context blocks writes, rolls everything back, and is inert outside itself."""

import uuid
import warnings

import frappe
from frappe.utils import today
from frappe.utils.background_jobs import get_job

from lending_assistant.assistant import audit, guard
from lending_assistant.tests.base import GuardTestCase

CATEGORY = "Loan Category"


def row(name):
	"""Fresh raw read, outside any cache."""
	return frappe.db.sql("select name, loan_category_name, modified from `tabLoan Category` where name=%s", name)


def category_count():
	return frappe.db.sql("select count(*) from `tabLoan Category`")[0][0]


def error_logs():
	return frappe.db.sql("select count(*) from `tabError Log` where method=%s", "AST write blocked")[0][0]


class TestReadOnlyContext(GuardTestCase):
	def setUp(self):
		super().setUp()
		frappe.set_user("Administrator")
		tag = "AST-CAT-" + uuid.uuid4().hex[:8]  # tests share one transaction per class: names must be unique
		self.cat = frappe.get_doc({"doctype": CATEGORY, "loan_category_code": tag, "loan_category_name": tag}).insert()
		self.before = row(self.cat.name)
		self.count = category_count()
		self.logs = error_logs()
		self.as_user("senior")  # a user who really can write

	def assertUnchanged(self):
		frappe.set_user("Administrator")
		self.assertEqual(row(self.cat.name), self.before)
		self.assertEqual(category_count(), self.count)
		self.as_user("senior")

	# --- the trap (layer 2) refuses and nothing is written

	def test_insert_blocked(self):
		with guard.read_only_tool_context("AST-TEST-t") as ctx:
			with self.assertRaises(frappe.PermissionError):
				frappe.get_doc({"doctype": CATEGORY, "loan_category_code": "AST-NEW", "loan_category_name": "AST-NEW"}).insert()
		self.assertEqual(ctx.trap_hits, 1)
		self.assertUnchanged()

	def test_save_blocked_and_ignore_validate_does_not_help(self):
		for ignore_validate in (False, True):
			doc = frappe.get_doc(CATEGORY, self.cat.name)
			doc.loan_category_name = "AST-CHANGED"
			doc.flags.ignore_validate = ignore_validate
			with guard.read_only_tool_context("AST-TEST-t"):
				with self.assertRaises(frappe.PermissionError):
					doc.save()
			self.assertUnchanged()

	def test_save_of_an_existing_loan_blocked(self):
		name = frappe.get_list("Loan", pluck="name", limit=1)[0]
		before = frappe.db.sql("select modified, status from `tabLoan` where name=%s", name)
		loan = frappe.get_doc("Loan", name)
		with guard.read_only_tool_context("AST-TEST-t"):
			with self.assertRaises(frappe.PermissionError):
				loan.save()
		self.assertEqual(frappe.db.sql("select modified, status from `tabLoan` where name=%s", name), before)

	def test_submit_and_cancel_blocked(self):
		je = frappe.get_doc(
			{
				"doctype": "Journal Entry",
				"company": "Polygon Technology",
				"posting_date": today(),
				"voucher_type": "Journal Entry",
				"accounts": [
					{"account": "Administrative Expenses - PT", "debit_in_account_currency": 1, "cost_center": "Main - PT"},
					{"account": "Cash - PT", "credit_in_account_currency": 1, "cost_center": "Main - PT"},
				],
			}
		).insert()
		with guard.read_only_tool_context("AST-TEST-t") as ctx:
			with self.assertRaises(frappe.PermissionError):
				je.submit()
		self.assertEqual(frappe.db.get_value("Journal Entry", je.name, "docstatus"), 0)
		je = frappe.get_doc("Journal Entry", je.name)
		je.submit()  # outside the context it works: the trap is inert
		self.assertEqual(frappe.db.get_value("Journal Entry", je.name, "docstatus"), 1)
		with guard.read_only_tool_context("AST-TEST-t"):
			with self.assertRaises(frappe.PermissionError):
				frappe.get_doc("Journal Entry", je.name).cancel()
		self.assertEqual(frappe.db.get_value("Journal Entry", je.name, "docstatus"), 1)

	def test_delete_and_rename_blocked(self):
		with guard.read_only_tool_context("AST-TEST-t"):
			with self.assertRaises(frappe.PermissionError):
				frappe.delete_doc(CATEGORY, self.cat.name)
			with self.assertRaises(frappe.PermissionError):
				frappe.delete_doc(CATEGORY, self.cat.name, force=1)
			with self.assertRaises(frappe.PermissionError):
				frappe.rename_doc(CATEGORY, self.cat.name, "AST-CAT-RENAMED")
		self.assertUnchanged()

	# --- layers 3-5: writes that run no hooks are counted, undone and reported

	def test_db_set_value_rolled_back_and_recorded(self):
		with guard.read_only_tool_context("AST-TEST-set_value_tool") as ctx:
			frappe.db.set_value(CATEGORY, self.cat.name, "loan_category_name", "AST-HACKED")
			self.assertEqual(frappe.db.get_value(CATEGORY, self.cat.name, "loan_category_name"), "AST-HACKED")
		self.assertEqual(ctx.trap_hits, 0)  # the trap never fired: no hook runs for db.set_value
		self.assertGreaterEqual(ctx.db_writes, 1)
		self.assertTrue(ctx.violation)
		self.assertUnchanged()
		self.assertEqual(error_logs(), self.logs + 1)

	def test_raw_sql_update_rolled_back_and_recorded(self):
		with guard.read_only_tool_context("AST-TEST-sql_tool") as ctx:
			frappe.db.sql("update `tabLoan Category` set loan_category_name='AST-HACKED' where name=%s", self.cat.name)
		self.assertGreaterEqual(ctx.db_writes, 1)
		self.assertUnchanged()

	def test_save_rolled_back_even_if_the_trap_is_bypassed(self):
		"""Layer 5 on its own: switch the flag off inside the context so no hook fires.

		Since M2b rework 4 (I4) the flag change itself is also a violation, so the context raises on exit."""
		with self.assertRaises(guard.AssistantGuardError):
			with guard.read_only_tool_context("AST-TEST-t") as ctx:
				frappe.flags.ast_read_only = False  # simulate a bypass of the trap
				doc = frappe.get_doc(CATEGORY, self.cat.name)
				doc.loan_category_name = "AST-BYPASS"
				doc.save()
				frappe.get_doc({"doctype": CATEGORY, "loan_category_code": "AST-B2", "loan_category_name": "AST-B2"}).insert()
		self.assertGreaterEqual(ctx.db_writes, 2)
		self.assertIn("guard flag changed inside the context", ctx.identity_changes)
		self.assertUnchanged()

	def test_commit_is_a_no_op_and_the_write_is_still_rolled_back(self):
		with guard.read_only_tool_context("AST-TEST-t") as ctx:
			frappe.db.set_value(CATEGORY, self.cat.name, "loan_category_name", "AST-COMMITTED?")
			with warnings.catch_warnings():
				warnings.simplefilter("ignore")
				frappe.db.commit()
		self.assertTrue(ctx.violation)
		self.assertUnchanged()

	def test_savepoint_gone_raises(self):
		flag_before = frappe.flags.ast_read_only
		control_before = frappe.db._disable_transaction_control
		with self.assertRaises(guard.AssistantGuardError):
			with guard.read_only_tool_context("AST-TEST-t") as ctx:
				frappe.db.sql(f"release savepoint {ctx.savepoint}")  # what a raw COMMIT does to it
		self.assertEqual(frappe.flags.ast_read_only, flag_before)
		self.assertEqual(frappe.db._disable_transaction_control, control_before)

	# --- exact restore, nesting

	def test_state_restored_after_success_and_after_error(self):
		flag, control, writes = frappe.flags.ast_read_only, frappe.db._disable_transaction_control, frappe.db.transaction_writes
		with guard.read_only_tool_context("AST-TEST-t"):
			self.assertTrue(frappe.flags.ast_read_only)
			self.assertEqual(frappe.db._disable_transaction_control, control + 1)
		self.assertEqual((frappe.flags.ast_read_only, frappe.db._disable_transaction_control), (flag, control))
		with self.assertRaises(ValueError):
			with guard.read_only_tool_context("AST-TEST-t"):
				frappe.get_doc(CATEGORY, self.cat.name)
				raise ValueError("tool failed")
		self.assertEqual((frappe.flags.ast_read_only, frappe.db._disable_transaction_control), (flag, control))
		self.assertEqual(frappe.db.transaction_writes, writes)
		with self.assertRaises(ValueError):  # an error AND a write: the write is still undone
			with guard.read_only_tool_context("AST-TEST-t"):
				frappe.db.set_value(CATEGORY, self.cat.name, "loan_category_name", "AST-X")
				raise ValueError("tool failed")
		self.assertEqual((frappe.flags.ast_read_only, frappe.db._disable_transaction_control), (flag, control))
		self.assertUnchanged()

	def test_nested_context_keeps_the_outer_flag(self):
		with guard.read_only_tool_context("AST-TEST-outer") as outer:
			with guard.read_only_tool_context("AST-TEST-inner") as inner:
				frappe.db.set_value(CATEGORY, self.cat.name, "loan_category_name", "AST-INNER")
			self.assertTrue(frappe.flags.ast_read_only)  # the inner exit did not clear it
			self.assertEqual(len(frappe.flags.ast_guard_stack), 1)
			with self.assertRaises(frappe.PermissionError):
				frappe.get_doc(CATEGORY, self.cat.name).save()
		self.assertTrue(inner.violation)
		self.assertTrue(outer.violation)  # the inner violation is passed up
		self.assertFalse(frappe.flags.ast_read_only)
		self.assertEqual(error_logs(), self.logs + 1)  # logged once, by the outermost context
		self.assertUnchanged()

	def test_writes_before_the_context_survive_it(self):
		frappe.set_user("Administrator")
		tag = "AST-CAT-" + uuid.uuid4().hex[:8]
		other = frappe.get_doc({"doctype": CATEGORY, "loan_category_code": tag, "loan_category_name": tag}).insert()
		self.as_user("senior")
		with guard.read_only_tool_context("AST-TEST-t"):
			frappe.db.set_value(CATEGORY, other.name, "loan_category_name", "AST-LATER")
		self.assertEqual(row(other.name)[0][1], other.name)

	def test_log_has_no_record_data(self):
		with guard.read_only_tool_context("AST-TEST-log_tool"):
			frappe.db.set_value(CATEGORY, self.cat.name, "loan_category_name", "AST-SECRET-VALUE")
		frappe.set_user("Administrator")
		text = frappe.db.sql("select error from `tabError Log` where method=%s order by creation desc limit 1", "AST write blocked")[0][0]
		self.assertIn("AST-TEST-log_tool", text)
		self.assertNotIn("AST-SECRET-VALUE", text)
		self.assertNotIn(self.cat.name, text)

	# --- M2b-R3: commit / rollback callbacks registered inside the context are dropped

	CALLBACK_MANAGERS = ("before_commit", "after_commit", "before_rollback", "after_rollback")

	def _clean_callbacks(self):
		for name in self.CALLBACK_MANAGERS:
			getattr(frappe.db, name).reset()

	def test_callbacks_added_inside_the_context_never_run(self):
		self._clean_callbacks()
		ran = []
		kept = {name: (lambda n=name: ran.append("before-" + n)) for name in self.CALLBACK_MANAGERS}
		for name, fn in kept.items():
			getattr(frappe.db, name).add(fn)  # registered BEFORE the context: must survive it
		job = "AST-TEST-ping-" + uuid.uuid4().hex[:8]
		with guard.read_only_tool_context("AST-TEST-callbacks") as ctx:
			for name in self.CALLBACK_MANAGERS:
				getattr(frappe.db, name).add(lambda n=name: ran.append("inside-" + n))
			frappe.enqueue("frappe.ping", enqueue_after_commit=True, job_id=job)
		self.assertEqual(ctx.callbacks_dropped, 5)  # four lambdas + the deferred enqueue
		self.assertTrue(ctx.violation)
		self.assertEqual(ctx.db_writes, 0)
		self.assertEqual(ctx.trap_hits, 0)
		# what a real commit does with the queues: before_commit, then after_commit
		frappe.db.before_commit.run()
		frappe.db.after_commit.run()
		frappe.db.before_rollback.run()
		frappe.db.after_rollback.run()
		self.assertEqual(sorted(ran), sorted("before-" + n for n in self.CALLBACK_MANAGERS))
		self.assertIsNone(get_job(job), "the job deferred to after-commit was queued")
		self.assertEqual(error_logs(), self.logs + 1)
		text = frappe.db.sql("select error from `tabError Log` where method=%s order by creation desc limit 1", "AST write blocked")[0][0]
		self.assertIn("callbacks_dropped=5", text)

	def test_the_job_check_can_see_a_job(self):
		"""Control for the test above: outside the context the same deferred enqueue does queue the job."""
		self._clean_callbacks()
		job = "AST-TEST-control-" + uuid.uuid4().hex[:8]
		frappe.enqueue("frappe.ping", enqueue_after_commit=True, job_id=job)
		frappe.db.after_commit.run()
		queued = get_job(job)
		self.assertIsNotNone(queued)
		queued.delete()

	def test_callbacks_in_a_nested_context_are_dropped_by_the_context_that_made_them(self):
		self._clean_callbacks()
		ran = []
		with guard.read_only_tool_context("AST-TEST-outer") as outer:
			frappe.db.after_commit.add(lambda: ran.append("outer"))
			with guard.read_only_tool_context("AST-TEST-inner") as inner:
				frappe.db.after_commit.add(lambda: ran.append("inner"))
			self.assertEqual(inner.callbacks_dropped, 1)
			self.assertEqual(len(frappe.db.after_commit._functions), 1)  # the outer one is still queued
		self.assertEqual(outer.callbacks_dropped, 1)
		self.assertTrue(outer.violation)
		self.assertEqual(outer.summary()["callbacks_dropped"], 2)
		frappe.db.after_commit.run()
		self.assertEqual(ran, [])

	def test_a_clean_context_drops_nothing_and_logs_nothing(self):
		self._clean_callbacks()
		ran = []
		frappe.db.after_commit.add(lambda: ran.append("kept"))
		with guard.read_only_tool_context("AST-TEST-clean") as ctx:
			frappe.get_doc(CATEGORY, self.cat.name)
		self.assertEqual(ctx.callbacks_dropped, 0)
		self.assertFalse(ctx.violation)
		frappe.db.after_commit.run()
		self.assertEqual(ran, ["kept"])
		self.assertEqual(error_logs(), self.logs)

	# --- M2b-R2: the tests leave no violation logs behind

	def test_violation_logs_made_by_tests_are_removed_by_teardown(self):
		with guard.read_only_tool_context("AST-TEST-cleanup-check"):
			frappe.db.set_value(CATEGORY, self.cat.name, "loan_category_name", "AST-HACKED")
		self.assertEqual(error_logs(), self.logs + 1)
		self.remove_violation_logs()
		self.assertEqual(error_logs(), self.logs)
		self.as_user("senior")

	def test_a_log_row_from_a_real_tool_name_is_not_removed(self):
		frappe.set_user("Administrator")
		frappe.log_error(title="AST write blocked", message="user=x tool=real_tool db_writes_rolled_back=1 trap_refusals=0")
		kept = error_logs()
		self.remove_violation_logs()
		self.assertEqual(error_logs(), kept)
		frappe.db.delete("Error Log", {"method": "AST write blocked", "error": ["like", "%tool=real_tool %"]})  # this test's own row

	# --- the trap does nothing outside the context

	def test_trap_is_registered_for_all_eight_events(self):
		events = frappe.get_hooks("doc_events")["*"]
		for event in ("before_insert", "before_validate", "before_save", "on_update", "before_submit", "before_cancel", "on_trash", "before_rename"):
			self.assertIn("lending_assistant.assistant.guard.block_if_read_only", events[event], event)

	def test_trap_is_inert_outside_the_context(self):
		doc = frappe.get_doc({"doctype": CATEGORY, "loan_category_code": "AST-OUT", "loan_category_name": "AST-OUT"}).insert()
		doc.loan_category_name = "AST-OUT-2"
		doc.save()
		self.assertEqual(row(doc.name)[0][1], "AST-OUT-2")
		frappe.rename_doc(CATEGORY, doc.name, "AST-OUT-RENAMED")
		frappe.delete_doc(CATEGORY, "AST-OUT-RENAMED")
		self.assertFalse(row("AST-OUT-RENAMED"))

	def test_audit_still_works_outside_the_context(self):
		conversation = audit.start_conversation("Form/Loan/X", "AST trap check")
		audit.log_exchange(conversation, question="AST q", answer="AST a", route="Form/Loan/X")
		self.assertEqual(frappe.db.get_value("Assistant Conversation", conversation, "message_count"), 1)
