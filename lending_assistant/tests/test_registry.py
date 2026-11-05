"""M4a registry and dispatcher: every tool is registered with a strict-compatible schema; `dispatch` validates, gates on
the switches, runs in the read-only context, runs the identity check, and wraps or verifies the result.

Test doubles are added with `mock.patch.dict(registry.TOOLS, ...)` and named `AST-TEST-...` so the guard's violation log
rows they provoke are removed by GuardTestCase.tearDown.
"""

import json
from contextlib import contextmanager
from unittest import mock

import frappe

from lending_assistant.assistant import guard
from lending_assistant.assistant.tools import registry
from lending_assistant.tests.base import ToolTestCase

PLAN_TOOLS = {
	"lookup_knowledge", "get_card", "search_knowledge", "get_screen_help", "check_my_access", "find_records",
	"get_record", "search_code", "read_code",
}  # fmt: skip
BANNED_KEYWORDS = {
	"maxLength", "minLength", "pattern", "minimum", "maximum", "exclusiveMinimum", "exclusiveMaximum", "multipleOf",
	"minItems", "maxItems", "uniqueItems", "format", "default",
}  # fmt: skip


def walk(schema, path="input_schema"):
	"""Yield (path, node) for every schema node."""
	yield path, schema
	for key, sub in (schema.get("properties") or {}).items():
		yield from walk(sub, f"{path}.{key}")
	if isinstance(schema.get("items"), dict):
		yield from walk(schema["items"], f"{path}[]")


class TestRegistryShape(ToolTestCase):
	def test_the_registry_has_exactly_the_plan_tools_and_none_of_the_later_ones(self):
		self.assertEqual(set(registry.TOOLS), PLAN_TOOLS)
		for later in ("get_loan_dues", "search_findings", "suggest_finding", "web_search"):
			self.assertNotIn(later, registry.TOOLS)

	def test_every_entry_has_the_keys_a_valid_switch_and_a_valid_source(self):
		for name, entry in registry.TOOLS.items():
			with self.subTest(tool=name):
				self.assertEqual(set(entry), {"function", "schema", "description", "needs_switch", "source"})
				self.assertTrue(callable(entry["function"]))
				self.assertEqual(entry["schema"]["name"], name)
				self.assertEqual(entry["description"], entry["schema"]["description"])
				self.assertIn(entry["needs_switch"], registry.SWITCHES)
				self.assertIn(entry["source"], registry.SOURCES)

	def test_the_switches_and_sources_are_the_decided_ones(self):
		expected = {
			"lookup_knowledge": (None, "analysis"), "get_card": (None, "analysis"), "search_knowledge": (None, "analysis"),
			"get_screen_help": (None, "live_site"), "check_my_access": (None, "live_site"),
			"find_records": ("live_data", "live_site"), "get_record": ("live_data", "live_site"),
			"search_code": ("code_reader", "code"), "read_code": ("code_reader", "code"),
		}  # fmt: skip
		actual = {n: (e["needs_switch"], e["source"]) for n, e in registry.TOOLS.items()}
		self.assertEqual(actual, expected)

	def test_every_schema_is_strict_compatible(self):
		for name, entry in registry.TOOLS.items():
			schema = entry["schema"]
			self.assertIs(schema["strict"], True, name)
			self.assertEqual(schema["input_schema"]["type"], "object", name)
			for path, node in walk(schema["input_schema"]):
				with self.subTest(tool=name, path=path):
					self.assertFalse(
						BANNED_KEYWORDS & set(node), f"{name} {path}: {BANNED_KEYWORDS & set(node)}"
					)
					if node.get("type") == "object":
						self.assertIs(node["additionalProperties"], False)
						self.assertEqual(
							sorted(node["required"]), sorted(node["properties"]), "every property is required"
						)
					self.assertIn("type", node)

	def test_a_nullable_argument_is_typed_with_null_and_the_others_are_not(self):
		optional = registry.TOOLS["find_records"]["schema"]["input_schema"]["properties"]
		self.assertIn("null", optional["limit"]["type"])
		self.assertIn("null", optional["order_by"]["type"])
		self.assertNotIn("null", registry._types(optional["doctype"]))

	def test_no_tool_function_is_whitelisted_and_no_tool_takes_an_identity_argument(self):
		for name, entry in registry.TOOLS.items():
			self.assertFalse(hasattr(entry["function"], "whitelisted"), name)
			props = set(entry["schema"]["input_schema"]["properties"])
			self.assertFalse(
				props & {"user", "role", "roles", "company", "owner", "ignore_permissions"}, name
			)

	def test_tool_definitions_is_a_copy_and_follows_the_switches(self):
		defs = registry.tool_definitions()
		self.assertEqual({d["name"] for d in defs}, PLAN_TOOLS)
		defs[0]["description"] = "CHANGED"
		defs[0]["input_schema"]["properties"].clear()
		self.assertNotEqual(registry.TOOLS[defs[0]["name"]]["schema"]["description"], "CHANGED")
		self.assertTrue(registry.TOOLS[defs[0]["name"]]["schema"]["input_schema"]["properties"])
		self.configure(live_data=0)
		self.assertEqual(
			{d["name"] for d in registry.tool_definitions()}, PLAN_TOOLS - {"find_records", "get_record"}
		)
		self.configure(live_data=1, code_reader=0)
		self.assertEqual(
			{d["name"] for d in registry.tool_definitions()}, PLAN_TOOLS - {"search_code", "read_code"}
		)


class TestValidation(ToolTestCase):
	def refused(self, tool, args, fragment=None):
		result = registry.dispatch(tool, args)
		message = self.error(result)
		if fragment:
			self.assertIn(fragment, message)
		return message

	def test_unknown_tools_are_refused_without_listing_the_real_ones(self):
		for name in (
			"get_loan_dues",
			"__import__",
			"",
			"GET_RECORD",
			None,
			5,
			["get_record"],
			{"a": 1},
			"find_records ",
			"web_search",
		):
			with self.subTest(name=name):
				message = self.refused(name, {})
				self.assertEqual(message, "Unknown tool.")

	def test_unknown_missing_and_wrongly_typed_arguments_are_refused(self):
		ok = {"doctype": "Loan", "name": "x"}
		self.refused("get_record", {**ok, "user": "Administrator"}, "Unknown argument")
		self.refused("get_record", {"doctype": "Loan"}, "Missing argument")
		self.refused("get_record", {**ok, "name": 5}, "wrong type")
		self.refused("get_record", {**ok, "name": ["a"]}, "wrong type")
		self.refused("get_record", {**ok, "name": None}, "wrong type")
		self.refused("get_record", {**ok, "name": "x" * 201}, "too long")
		self.refused("get_record", ["Loan", "x"], "must be an object")
		self.refused("get_record", "Loan", "must be an object")

	def test_integers_are_not_strings_and_not_booleans(self):
		base = {"doctype": "Loan", "filters": [], "fields": ["name"], "order_by": None}
		for bad in ("5", True, False, 2.5, [5]):
			with self.subTest(limit=bad):
				self.refused("find_records", {**base, "limit": bad}, "wrong type")

	def test_enum_values_are_checked(self):
		self.refused(
			"check_my_access",
			{"doctype": "Loan", "actions": ["read", "drop"], "docname": None},
			"allowed values",
		)
		self.refused("search_knowledge", {"query": "loan", "type": "not-a-type"}, "allowed values")
		self.refused(
			"find_records",
			{
				"doctype": "Loan",
				"filters": [{"field": "name", "operator": "~", "value": "x", "values": None}],
				"fields": ["name"],
				"order_by": None,
				"limit": None,
			},
			"allowed values",
		)

	def test_null_is_refused_where_the_type_does_not_allow_it(self):
		self.refused("check_my_access", {"doctype": None, "actions": ["read"], "docname": None}, "wrong type")
		self.refused("check_my_access", {"doctype": "Loan", "actions": None, "docname": None}, "wrong type")

	def test_lists_have_a_count_limit(self):
		self.refused(
			"check_my_access", {"doctype": "Loan", "actions": ["read"] * 7, "docname": None}, "too many"
		)
		self.refused(
			"find_records",
			{
				"doctype": "Loan",
				"filters": [],
				"fields": [f"f{i}" for i in range(31)],
				"order_by": None,
				"limit": None,
			},
			"too many",
		)
		many = [{"field": "name", "operator": "=", "value": "x", "values": None}] * 11
		self.refused(
			"find_records",
			{"doctype": "Loan", "filters": many, "fields": ["name"], "order_by": None, "limit": None},
			"too many",
		)

	def test_a_missing_nullable_argument_becomes_none(self):
		cleaned = registry.validate_args(
			registry.TOOLS["find_records"]["schema"]["input_schema"],
			{"doctype": "Loan", "filters": [], "fields": ["name"]},
			"find_records",
		)
		self.assertIsNone(cleaned["limit"])
		self.assertIsNone(cleaned["order_by"])
		self.assertEqual(
			registry.validate_args(registry.TOOLS["get_card"]["schema"]["input_schema"], {"card_id": "x"}),
			{"card_id": "x"},
		)

	def test_none_arguments_count_as_empty(self):
		self.assertEqual(
			registry.validate_args({"type": "object", "properties": {}, "required": []}, None), {}
		)

	def test_an_error_never_echoes_the_value(self):
		secret = "S3CR3T-VALUE-" + "x" * 300
		message = self.refused("get_record", {"doctype": "Loan", "name": secret})
		self.assertNotIn("S3CR3T", message)
		message = self.refused(
			"get_record", {"doctype": "Loan", "name": "x", "bad key with spaces <script>": 1}
		)
		self.assertNotIn("script", message)  # a key that is not a plain name is not repeated

	def test_the_schemas_hold_no_limit_that_python_does_not_check_for_lengths(self):
		# the schema says nothing about 200; Python does
		self.refused("get_card", {"card_id": "x" * 201}, "too long")
		self.refused("search_knowledge", {"query": "x" * 501, "type": None}, "too long")


class TestSwitches(ToolTestCase):
	def test_live_data_off_refuses_find_records_and_get_record_and_runs_nothing(self):
		self.configure(live_data=0)
		self.as_user("senior")
		with (
			mock.patch.object(guard, "list_records") as listing,
			mock.patch.object(guard, "read_doc") as reading,
		):
			result = self.call(
				"find_records", doctype="Loan", filters=[], fields=["name"], order_by=None, limit=None
			)
			self.assertEqual(self.error(result), guard.LIVE_DATA_OFF)
			result = self.call("get_record", doctype="Loan", name="x")
			self.assertEqual(self.error(result), guard.LIVE_DATA_OFF)
		listing.assert_not_called()
		reading.assert_not_called()

	def test_code_reader_off_refuses_the_code_tools(self):
		self.configure(code_reader=0)
		self.as_user("senior")
		from lending_assistant.assistant import codereader

		self.assertEqual(
			self.error(self.call("search_code", query="hooks", app=None, path_glob=None)), codereader.OFF
		)
		self.assertEqual(
			self.error(
				self.call("read_code", path="lending/lending/hooks.py", start_line=None, end_line=None)
			),
			codereader.OFF,
		)

	def test_the_knowledge_tools_and_the_meta_tools_work_with_both_switches_off(self):
		self.configure(live_data=0, code_reader=0)
		self.as_user("senior")
		self.data(self.call("search_knowledge", query="loan repayment", type=None))
		self.data(self.call("get_screen_help", doctype="Loan", search="product"))
		self.data(self.call("check_my_access", doctype="Loan", actions=["read"], docname=None))

	def test_check_my_access_with_a_docname_needs_live_data(self):
		visible, _hidden = self.loan_names()
		self.configure(live_data=0)
		self.as_user("senior")
		self.assertEqual(
			self.error(self.call("check_my_access", doctype="Loan", actions=["read"], docname=visible)),
			guard.LIVE_DATA_OFF,
		)


def noop_context(tool=""):
	"""Stands in for read_only_tool_context: checks nothing."""

	@contextmanager
	def manager():
		yield mock.Mock(
			summary=lambda: dict.fromkeys(
				(
					"db_writes",
					"trap_hits",
					"callbacks_dropped",
					"callbacks_restored",
					"identity_changes",
					"savepoint_gone",
				),
				0,
			)
		)

	return manager()


class TestWritesAndIdentity(ToolTestCase):
	def setUp(self):
		super().setUp()
		self.as_user("senior")
		self.rogues = []

	def tearDown(self):
		for rogue in self.rogues:
			try:
				rogue.close()
			except Exception:
				pass
		super().tearDown()

	def run_double(self, function, source="live_site"):
		entry = self.tool_entry(function, source)
		with mock.patch.dict(registry.TOOLS, {"AST-TEST-double": entry}):
			return registry.dispatch("AST-TEST-double", {})

	def category_count(self):
		return frappe.db.count("Loan Category")

	def test_a_tool_that_inserts_is_stopped_by_the_trap_and_the_model_gets_an_error(self):
		before = self.category_count()

		def writer():
			frappe.get_doc(
				{
					"doctype": "Loan Category",
					"loan_category_code": "AST-TEST-W",
					"loan_category_name": "AST-TEST-W",
				}
			).insert()
			return guard.as_data({"ok": True})

		result = self.run_double(writer)
		self.assertEqual(self.error(result), guard.READ_ONLY_MESSAGE)
		self.assertEqual(self.category_count(), before)

	def test_a_tool_that_swallows_the_trap_error_and_returns_normally_is_still_refused(self):
		"""#49 I1: the dispatcher reads ctx.violation, so a caught PermissionError does not hide the attempt."""
		before = self.category_count()

		def sneaky():
			try:
				frappe.get_doc(
					{
						"doctype": "Loan Category",
						"loan_category_code": "AST-TEST-S",
						"loan_category_name": "AST-TEST-S",
					}
				).insert()
			except frappe.PermissionError:
				pass
			return guard.as_data({"ok": "it looked fine"})

		result = self.run_double(sneaky)
		self.assertEqual(self.error(result), guard.READ_ONLY_MESSAGE)
		self.assertNotIn("looked fine", result.content)
		self.assertEqual(self.category_count(), before)

	def test_a_raw_write_that_gets_past_the_trap_is_rolled_back_and_fails_closed(self):
		name = frappe.get_all("Loan Category", pluck="name", limit=1)[0]
		before = frappe.db.get_value("Loan Category", name, "loan_category_name")

		def raw():
			frappe.db.sql(
				"update `tabLoan Category` set loan_category_name=%s where name=%s", ("AST-TEST-RAW", name)
			)
			return guard.as_data({"ok": True})

		with self.assertRaises(guard.AssistantGuardError):
			self.run_double(raw)
		self.assertEqual(frappe.db.get_value("Loan Category", name, "loan_category_name"), before)

	def test_a_commit_callback_queued_by_a_tool_is_dropped_and_fails_closed(self):
		def queue():
			frappe.db.after_commit.add(lambda: None)
			return guard.as_data({"ok": True})

		with self.assertRaises(guard.AssistantGuardError):
			self.run_double(queue)

	def test_the_identity_check_fires_when_a_tool_swaps_the_database_connection(self):
		original = frappe.local.db

		def swap():
			frappe.connect()
			self.rogues.append(frappe.local.db)
			return guard.as_data({"ok": True})

		with self.assertRaises(guard.AssistantGuardError):
			self.run_double(swap)
		self.assertIs(frappe.local.db, original)
		self.assertEqual(frappe.session.user, "ast-senior@example.com")

	def test_the_identity_check_fires_when_a_tool_double_swaps_frappe_local_db_for_a_different_object(self):
		original = frappe.local.db

		def swap():
			frappe.local.db = mock.MagicMock()
			return guard.as_data({"ok": True})

		with self.assertRaises(guard.AssistantGuardError):
			self.run_double(swap)
		self.assertIs(frappe.local.db, original)

	def test_the_dispatchers_own_check_catches_it_when_the_context_is_replaced_by_a_no_op(self):
		original = frappe.local.db
		user = frappe.session.user

		def swap_db():
			frappe.connect()
			self.rogues.append(frappe.local.db)
			return guard.as_data({"ok": True})

		def swap_user():
			frappe.set_user("Administrator")
			return guard.as_data({"ok": True})

		def swap_session():
			frappe.local.session = frappe._dict(
				user="Administrator", sid="Administrator", data=frappe._dict()
			)
			return guard.as_data({"ok": True})

		def swap_flags():
			frappe.local.flags = frappe._dict()
			return guard.as_data({"ok": True})

		for label, function in (
			("db", swap_db),
			("user", swap_user),
			("session", swap_session),
			("flags", swap_flags),
		):
			with self.subTest(swap=label):
				with mock.patch.object(guard, "read_only_tool_context", noop_context):
					with self.assertRaises(guard.AssistantGuardError):
						self.run_double(function)
				self.assertIs(frappe.local.db, original)
				self.assertEqual(frappe.session.user, user)
				self.assertNotIn("System Manager", frappe.get_roles())
				self.assertTrue(frappe.local.flags is not None)

	def test_an_unexpected_exception_propagates_and_is_not_mapped(self):
		def broken():
			raise RuntimeError("internal")

		with self.assertRaises(RuntimeError):
			self.run_double(broken)

	def test_a_guard_error_inside_a_tool_propagates(self):
		def broken():
			raise guard.AssistantGuardError("integrity")

		with self.assertRaises(guard.AssistantGuardError):
			self.run_double(broken)


class TestResultChecks(ToolTestCase):
	def setUp(self):
		super().setUp()
		self.as_user("senior")

	def run_double(self, function, source="live_site"):
		with mock.patch.dict(registry.TOOLS, {"AST-TEST-double": self.tool_entry(function, source)}):
			return registry.dispatch("AST-TEST-double", {})

	def test_a_wrong_source_label_is_a_guard_failure(self):
		with self.assertRaises(guard.AssistantGuardError):
			self.run_double(lambda: guard.as_data({"a": 1}, "code"), source="live_site")
		with self.assertRaises(guard.AssistantGuardError):
			self.run_double(lambda: guard.as_data({"a": 1}, "live_site"), source="analysis")

	def test_a_result_that_is_not_an_envelope_is_a_guard_failure(self):
		with self.assertRaises(guard.AssistantGuardError):
			self.run_double(lambda: "plain text")

	def test_a_result_over_the_cap_is_refused(self):
		big = guard.as_data({"text": "x" * (guard.MAX_CHARS + 10)})
		with self.assertRaises(guard.AssistantGuardError):
			self.run_double(lambda: big)

	def test_a_dict_result_is_wrapped_with_the_tools_source(self):
		result = self.run_double(lambda: {"hello": "world"}, source="code")
		self.assertFalse(result.is_error)
		self.assertEqual(result.source, "code")
		self.assertEqual(guard.unwrap(result.content), {"hello": "world", "source": "code"})

	def test_a_successful_result_carries_its_source_and_is_an_envelope(self):
		result = self.call("search_knowledge", query="loan repayment", type=None)
		self.assertFalse(result.is_error)
		self.assertEqual(result.source, "analysis")
		self.assertTrue(result.content.startswith('<data source="analysis">'))

	def test_an_error_result_is_json_with_one_key_and_no_source(self):
		result = self.call("nope")
		self.assertEqual(json.loads(result.content), {"error": "Unknown tool."})
		self.assertTrue(result.is_error)
		self.assertIsNone(result.source)

	def test_expected_errors_from_a_tool_are_returned_not_raised(self):
		def invalid():
			frappe.throw("That filter is wrong.")

		def denied():
			raise frappe.PermissionError("secret detail")

		def missing():
			raise frappe.DoesNotExistError("Loan XYZ not found")

		self.assertEqual(self.error(self.run_double(invalid)), "That filter is wrong.")
		self.assertEqual(self.error(self.run_double(denied)), registry.PERMISSION_MESSAGE)
		self.assertEqual(self.error(self.run_double(missing)), guard.NOT_FOUND)

	def test_a_long_validation_message_is_cut(self):
		def long():
			raise frappe.ValidationError("x" * 1000)

		self.assertLessEqual(len(self.error(self.run_double(long))), registry.MAX_MESSAGE)

	def test_refusals_are_logged_with_the_tool_and_kind_only(self):
		with mock.patch.object(registry, "_logger") as logger:
			self.call("get_record", doctype="Loan", name="SECRET-NAME-" + "x" * 300)
			self.call("nope")
		lines = [call.args[0] for call in logger.return_value.warning.call_args_list]
		self.assertEqual(len(lines), 2)
		self.assertIn("tool=get_record bad_arguments", lines[0])
		self.assertIn("unknown_tool", lines[1])
		self.assertFalse(any("SECRET" in line for line in lines))


class TestLoggingEnvelopeAndColdConnection(ToolTestCase):
	"""Fix-up #149: M4a-R1 (cold connection through dispatch), R2 (the log line is really written), R5 (bad envelope)."""

	def setUp(self):
		super().setUp()
		self.as_user("senior")
		self.rogues = []

	def tearDown(self):
		for rogue in self.rogues:
			try:
				rogue.close()
			except Exception:
				pass
		super().tearDown()

	def run_double(self, function, source="live_site"):
		with mock.patch.dict(registry.TOOLS, {"AST-TEST-double": self.tool_entry(function, source)}):
			return registry.dispatch("AST-TEST-double", {})

	def violation_rows(self):
		return frappe.db.sql(
			"select count(*) from `tabError Log` where method=%s and error like %s",
			("AST write blocked", "%tool=AST-TEST-double%"),
		)[0][0]

	def test_internal_errors_are_logged_at_error_level_without_the_detail(self):
		def broken():
			raise RuntimeError("SECRET-DETAIL")

		with mock.patch.object(registry, "_logger") as logger:
			with self.assertRaises(RuntimeError):
				self.run_double(broken)
		self.assertEqual(logger.return_value.warning.call_count, 0)
		line = logger.return_value.error.call_args.args[0]
		self.assertIn("tool=AST-TEST-double internal_error", line)
		self.assertNotIn("SECRET", line)

	def test_a_refusal_really_reaches_the_log_file(self):
		"""M4a-R2: no mock. Frappe's logger drops `info`, so the line must be written at warning or above."""
		import logging
		import os

		logger = registry._logger()
		self.assertTrue(logger.isEnabledFor(logging.WARNING))
		files = [h.baseFilename for h in logger.handlers if hasattr(h, "baseFilename")]
		self.assertTrue(files, "the logger has no file handler")
		marker = f"user={frappe.session.user} tool=get_record bad_arguments"

		def count():
			for handler in logger.handlers:
				handler.flush()
			return open(files[0]).read().count(marker) if os.path.exists(files[0]) else 0

		before = count()
		self.call("get_record", doctype="Loan", name="SECRET-NAME-" + "x" * 300)
		self.assertEqual(count(), before + 1)
		self.assertNotIn("SECRET-NAME", open(files[0]).read())

	def test_two_concatenated_envelopes_are_a_guard_failure(self):
		joined = guard.as_data({"a": 1}) + guard.as_data({"b": 2})
		with self.assertRaises(guard.AssistantGuardError):
			self.run_double(lambda: joined)

	def test_an_envelope_with_invalid_json_inside_is_a_guard_failure(self):
		with self.assertRaises(guard.AssistantGuardError):
			self.run_double(lambda: '<data source="live_site">{not json</data>')

	def no_query_before_the_watch(self):
		"""`_switch_message` reads Assistant Settings, which can open the connection before the watch starts."""
		return mock.patch.object(registry, "_switch_message", return_value=None)

	def cold(self):
		original = frappe.local.db
		frappe.connect(set_admin_as_user=False)  # a new Database object that has not opened its connection
		cold = frappe.local.db
		self.rogues.append(cold)
		self.assertIsNone(cold._conn)
		return original, cold

	def test_a_tool_whose_first_query_is_on_a_cold_connection_is_not_a_swap(self):
		original, cold = self.cold()
		try:  # no query here: it would warm the connection
			with self.no_query_before_the_watch():
				result = self.run_double(lambda: {"n": frappe.db.sql("select 1")[0][0]})
			self.assertFalse(result.is_error)
			self.assertEqual(guard.unwrap(result.content)["n"], 1)
			self.assertIs(frappe.local.db, cold)
			self.assertIsNotNone(cold._conn)  # the request's own socket was not closed
			self.assertEqual(frappe.db.sql("select 2")[0][0], 2)
		finally:
			frappe.local.db = original
		self.assertEqual(self.violation_rows(), 0)  # no false violation row

	def test_check_my_access_on_a_cold_connection_returns_a_result(self):
		original, _ = self.cold()
		try:
			with self.no_query_before_the_watch():
				result = self.call("check_my_access", doctype="Loan", actions=["read"], docname=None)
			self.assertFalse(result.is_error)
		finally:
			frappe.local.db = original

	def test_a_swap_after_a_warm_connection_still_raises(self):
		original = frappe.local.db
		frappe.db.sql("select 1")  # warm
		self.assertIsNotNone(original._conn)

		def swap():
			frappe.connect(set_admin_as_user=False)
			self.rogues.append(frappe.local.db)
			return {"a": 1}

		try:
			with self.assertRaises(guard.AssistantGuardError):
				self.run_double(swap)
			self.assertIs(frappe.local.db, original)
		finally:
			frappe.local.db = original

	def test_a_new_socket_on_the_same_warm_object_still_raises(self):
		db = frappe.local.db
		frappe.db.sql("select 1")
		warm_conn = db._conn

		def new_socket():
			db._conn = db.get_connection()  # a second socket on the same Database object
			return {"a": 1}

		try:
			with self.assertRaises(guard.AssistantGuardError):
				self.run_double(new_socket)
			self.assertIs(db._conn, warm_conn)
		finally:
			db._conn = warm_conn
