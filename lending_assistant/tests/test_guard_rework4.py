"""M2b rework 4: the write trap covers every Frappe document action (R18); the exit path cannot be cut short by a
broken callback queue (R19); a guard flag turned off inside the context is a violation (I4).

Administrator only creates the fixtures (DECISIONS #41). The actions inside the context run as `ast-senior` (a user
who really can write) or `ast-limited`. Everything is in the test transaction, rolled back at the end of the class;
the "AST write blocked" rows the tests provoke are removed by GuardTestCase.tearDown (tool names `AST-TEST-...`).
"""

import ast
import uuid
from pathlib import Path
from unittest import mock

import frappe
from frappe.utils import today

from lending_assistant.assistant import guard
from lending_assistant.tests.base import GuardTestCase

TRAP = "lending_assistant.assistant.guard.block_if_read_only"
CATEGORY = "Loan Category"

# Events Frappe fires that the trap deliberately does not hook. Each needs a reason.
NOT_TRAPPED = {
	"before_mapping": "frappe.model.mapper.get_mapped_doc builds a new document in memory and returns it unsaved; "
	"saving it later goes through before_insert / before_save, which are trapped",
	# M4a: `after_insert` and `after_rename` are trapped as well (#147). `after_mapping` stays untrapped, reason below.
	"after_mapping": "frappe.model.mapper.get_mapped_doc builds a new document in memory after before_mapping and returns it "
	"unsaved; saving it later goes through the trapped save events",
}


def fired_events() -> dict[str, list[str]]:
	"""Every `x.run_method("<literal>")` / `x.run_trigger("<literal>")` in frappe/model/*.py: {event: [file:line, ...]}."""
	found: dict[str, list[str]] = {}
	model = Path(frappe.get_app_path("frappe", "model"))
	for path in sorted(model.glob("*.py")):
		tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
		for node in ast.walk(tree):
			if (
				isinstance(node, ast.Call)
				and isinstance(node.func, ast.Attribute)
				and node.func.attr in ("run_method", "run_trigger")
				and node.args
				and isinstance(node.args[0], ast.Constant)
				and isinstance(node.args[0].value, str)
			):
				found.setdefault(node.args[0].value, []).append(f"{path.name}:{node.lineno}")
	return found


def error_logs():
	return frappe.db.sql("select count(*) from `tabError Log` where method=%s", "AST write blocked")[0][0]


def fresh_sql(query, *args):
	"""Run a read on a NEW connection: it sees only what was committed."""
	original = frappe.local.db
	frappe.connect(set_admin_as_user=False)
	fresh = frappe.local.db
	try:
		return fresh.sql(query, args)
	finally:
		try:
			fresh.close()
		finally:
			frappe.local.db = original


class TestEveryDocumentEventIsTrapped(GuardTestCase):
	def test_every_before_on_and_after_event_frappe_fires_is_trapped_or_exempt(self):
		fired = fired_events()
		for must_see in (
			"before_insert",
			"before_save",
			"before_update_after_submit",
			"before_discard",
			"before_change",
			"after_delete",
		):
			self.assertIn(must_see, fired, "the parser found nothing: it is broken, not Frappe")
		hooks = frappe.get_hooks("doc_events")["*"]
		missing = [
			f"{event} ({', '.join(where)})"
			for event, where in sorted(fired.items())
			if event.startswith(("before_", "on_", "after_"))
			and TRAP not in hooks.get(event, [])
			and event not in NOT_TRAPPED
		]
		self.assertEqual(missing, [], "add these to the trap in hooks.py, or to NOT_TRAPPED with a reason")

	def test_every_exemption_has_a_reason_and_is_still_fired(self):
		fired = fired_events()
		for event, reason in NOT_TRAPPED.items():
			self.assertGreater(len(reason), 20, event)
			self.assertIn(event, fired, f"{event} is no longer fired by Frappe: remove it from NOT_TRAPPED")
			self.assertNotIn(
				TRAP, frappe.get_hooks("doc_events")["*"].get(event, []), f"{event} is trapped AND exempt"
			)

	def test_the_eight_original_events_are_still_trapped(self):
		hooks = frappe.get_hooks("doc_events")["*"]
		for event in (
			"before_insert",
			"before_validate",
			"before_save",
			"on_update",
			"before_submit",
			"before_cancel",
			"on_trash",
			"before_rename",
			"after_delete",
			"after_insert",
			"after_rename",
		):
			self.assertIn(TRAP, hooks[event], event)


class TestNewlyTrappedActions(GuardTestCase):
	def setUp(self):
		super().setUp()
		frappe.set_user("Administrator")  # fixtures only (#41)
		tag = "AST-TEST-CAT-" + uuid.uuid4().hex[:8]
		self.cat = frappe.get_doc(
			{"doctype": CATEGORY, "loan_category_code": tag, "loan_category_name": tag}
		).insert()
		self.draft_je = self.journal_entry()
		self.submitted_je = self.journal_entry()
		self.submitted_je.submit()
		self.logs = error_logs()
		self.as_user("senior")

	def journal_entry(self):
		return frappe.get_doc(
			{
				"doctype": "Journal Entry",
				"company": "Polygon Technology",
				"posting_date": today(),
				"voucher_type": "Journal Entry",
				"user_remark": "AST-TEST-R18",
				"accounts": [
					{
						"account": "Administrative Expenses - PT",
						"debit_in_account_currency": 1,
						"cost_center": "Main - PT",
					},
					{"account": "Cash - PT", "credit_in_account_currency": 1, "cost_center": "Main - PT"},
				],
			}
		).insert()

	def je_row(self, name):
		return frappe.db.sql(
			"select docstatus, modified, user_remark from `tabJournal Entry` where name=%s", name
		)

	def test_saving_a_submitted_document_is_trapped(self):
		before = self.je_row(self.submitted_je.name)
		doc = frappe.get_doc("Journal Entry", self.submitted_je.name)
		with guard.read_only_tool_context("AST-TEST-update-after-submit") as ctx:
			with self.assertRaises(frappe.PermissionError):
				doc.save()
		self.assertGreaterEqual(ctx.trap_hits, 1)
		self.assertEqual(ctx.db_writes, 0)  # refused before any UPDATE ran
		self.assertEqual(self.je_row(self.submitted_je.name), before)
		self.assertEqual(
			error_logs(), self.logs + 1
		)  # the guard's own log still works with on_change trapped

	def test_saving_an_existing_submitted_loan_is_trapped_and_nothing_is_committed(self):
		name = frappe.get_list("Loan", filters={"docstatus": 1}, pluck="name", limit=1)[0]
		query = "select modified, status, docstatus from `tabLoan` where name=%s"
		before = fresh_sql(query, name)
		loan = frappe.get_doc("Loan", name)
		with guard.read_only_tool_context("AST-TEST-loan-uas") as ctx:
			with self.assertRaises(frappe.PermissionError):
				loan.save()
		self.assertGreaterEqual(ctx.trap_hits, 1)
		self.assertEqual(frappe.db.sql(query, name), before)
		self.assertEqual(fresh_sql(query, name), before)

	def test_discarding_a_draft_is_trapped(self):
		before = self.je_row(self.draft_je.name)
		doc = frappe.get_doc("Journal Entry", self.draft_je.name)
		with guard.read_only_tool_context("AST-TEST-discard") as ctx:
			with self.assertRaises(frappe.PermissionError):
				doc.discard()
		self.assertGreaterEqual(ctx.trap_hits, 1)
		self.assertEqual(self.je_row(self.draft_je.name), before)
		self.assertEqual(self.je_row(self.draft_je.name)[0][0], 0)

	def test_db_set_is_trapped(self):
		query = "select loan_category_name, modified from `tabLoan Category` where name=%s"
		before = frappe.db.sql(query, self.cat.name)
		doc = frappe.get_doc(CATEGORY, self.cat.name)
		with guard.read_only_tool_context("AST-TEST-db-set") as ctx:
			with self.assertRaises(frappe.PermissionError):
				doc.db_set("loan_category_name", "AST-TEST-CHANGED")
			with self.assertRaises(frappe.PermissionError):
				doc.db_set({"loan_category_name": "AST-TEST-CHANGED"}, update_modified=False)
		self.assertEqual(ctx.trap_hits, 2)
		self.assertEqual(ctx.db_writes, 0)  # before_change fires before the UPDATE
		self.assertEqual(frappe.db.sql(query, self.cat.name), before)

	def test_db_set_whose_hook_is_bypassed_is_still_counted_and_rolled_back(self):
		query = "select loan_category_name from `tabLoan Category` where name=%s"
		before = frappe.db.sql(query, self.cat.name)
		doc = frappe.get_doc(CATEGORY, self.cat.name)
		with mock.patch.object(guard, "block_if_read_only"):  # as if the trap were missing
			with guard.read_only_tool_context("AST-TEST-db-set-bypass") as ctx:
				doc.db_set("loan_category_name", "AST-TEST-CHANGED")
		self.assertGreaterEqual(ctx.db_writes, 1)
		self.assertEqual(frappe.db.sql(query, self.cat.name), before)

	def test_outside_the_context_on_change_fires_and_saves_work(self):
		with mock.patch.object(guard, "block_if_read_only", wraps=guard.block_if_read_only) as trap:
			doc = frappe.get_doc(CATEGORY, self.cat.name)
			doc.loan_category_name = "AST-TEST-SAVED"
			doc.save()
			doc.db_set("loan_category_name", "AST-TEST-DBSET")
			je = frappe.get_doc("Journal Entry", self.draft_je.name)
			je.discard()
		events = [call.args[1] for call in trap.call_args_list]
		for event in (
			"before_save",
			"on_update",
			"on_change",
			"before_change",
			"before_discard",
			"on_discard",
		):
			self.assertIn(event, events)
		self.assertEqual(frappe.db.get_value(CATEGORY, self.cat.name, "loan_category_name"), "AST-TEST-DBSET")
		self.assertEqual(frappe.db.get_value("Journal Entry", self.draft_je.name, "docstatus"), 2)
		submitted = frappe.get_doc("Journal Entry", self.submitted_je.name)
		submitted.save()  # update after submit, outside the context: allowed
		self.assertEqual(error_logs(), self.logs)


class TestExitPath(GuardTestCase):
	def setUp(self):
		super().setUp()
		self.logs = error_logs()
		self.as_user("limited")
		self.db = frappe.local.db

	def assertReset(self):
		self.assertFalse(frappe.flags.get("ast_read_only"))
		self.assertEqual(self.db._disable_transaction_control, 0)
		self.assertEqual(frappe.session.user, "ast-limited@example.com")

	def test_a_broken_callback_queue_cannot_skip_the_rest_of_the_exit(self):
		"""The Reviewer's cb_break case (M2b-R19)."""
		queue = frappe.db.after_commit._functions
		with mock.patch.object(self.db, "rollback", wraps=self.db.rollback) as rollback:
			with self.assertRaises(guard.AssistantGuardError) as caught:  # not TypeError
				with guard.read_only_tool_context("AST-TEST-cb-break") as ctx:
					frappe.db.sql(
						"update `tabLoan Category` set modified=modified where name='AST-TEST-none'"
					)
					frappe.db.after_commit._functions = 5
		self.assertIn("callbacks could not be checked", str(caught.exception))
		rollback.assert_called_once_with(save_point=ctx.savepoint)  # the rollback ran
		self.assertFalse(ctx.savepoint_gone)
		self.assertEqual(
			ctx.db_writes, 1
		)  # counted before the rollback (the violation row written after it adds its own)
		self.assertIs(frappe.db.after_commit._functions, queue)  # the original queue object is back
		self.assertReset()
		self.assertEqual(error_logs(), self.logs + 1)

	def test_a_restore_step_that_raises_still_lets_the_rest_run(self):
		with mock.patch.object(guard, "_restore_callbacks", side_effect=RuntimeError("boom")):
			with self.assertRaises(guard.AssistantGuardError):
				with guard.read_only_tool_context("AST-TEST-cb-raise") as ctx:
					frappe.db.sql(
						"update `tabLoan Category` set modified=modified where name='AST-TEST-none'"
					)
		self.assertEqual(ctx.identity_changes, ["callbacks could not be restored"])
		self.assertEqual(ctx.db_writes, 1)
		self.assertFalse(ctx.savepoint_gone)
		self.assertReset()
		self.assertEqual(error_logs(), self.logs + 1)

	def test_the_guard_flag_turned_off_inside_is_a_violation(self):
		"""I4."""
		with self.assertRaises(guard.AssistantGuardError) as caught:
			with guard.read_only_tool_context("AST-TEST-flag-off") as ctx:
				frappe.flags.ast_read_only = None
		self.assertIn("guard flag changed inside the context", str(caught.exception))
		self.assertEqual(ctx.identity_changes, ["guard flag changed inside the context"])
		self.assertReset()
		self.assertEqual(error_logs(), self.logs + 1)

	def test_a_clean_context_is_still_clean(self):
		with guard.read_only_tool_context("AST-TEST-clean-r4") as ctx:
			guard.list_records("Loan", limit=1)
		self.assertFalse(ctx.violation)
		self.assertReset()
		self.assertEqual(error_logs(), self.logs)

	def test_nested_contexts_do_not_trip_the_flag_check(self):
		with guard.read_only_tool_context("AST-TEST-outer-r4") as outer:
			with guard.read_only_tool_context("AST-TEST-inner-r4") as inner:
				pass
			self.assertTrue(frappe.flags.get("ast_read_only"))
		self.assertFalse(outer.violation or inner.violation)
		self.assertReset()
