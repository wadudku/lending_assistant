"""`get_loan_dues` (PLAN §4, M4b, DECISIONS #148 option B): what is billed, paid, outstanding and overdue on one loan.

Built only from Loan Demand rows read through `guard.list_records` (the user's permissions and field filter) and the
readable fields of the Loan read through `guard.read_doc`. Nothing is imported from lending and nothing is wrapped: the
numbers are sums of rows the user can read, so a loan with rows the user cannot see gives smaller numbers, never more.

Overdue: a Loan Demand with `outstanding_amount > 0` whose `demand_date` (the due date; there is no `due_date` field)
falls before `as_on_date`. Rows due on `as_on_date` are reported apart as `due_on_date`. Demands after `as_on_date` are left
out. `outstanding_amount` is the stored current balance, so for a past date it is not a restatement of that day.
"""

from datetime import date
from decimal import Decimal

import frappe
from frappe.utils import now_datetime

from lending_assistant.assistant import guard

NOTE = (
	"Accrued-but-unbilled interest, future interest and unbooked penalty are NOT included. This covers only demands "
	"already raised on the loan."
)
OUTSTANDING_NOTE = "Outstanding is the current stored balance of each demand raised up to as_on_date, not a restatement of that day."
PAGE = guard.MAX_ROWS
MAX_PAGES = 10  # 200 rows per loan
ZERO = Decimal(0)
LOAN_FIELDS = (
	"status", "loan_product", "loan_amount", "disbursed_amount", "rate_of_interest", "penalty_charges_rate",
	"repayment_method", "repayment_start_date", "total_payment", "total_interest_payable", "total_principal_paid",
	"total_amount_paid", "days_past_due", "classification_code", "is_npa", "manual_npa", "written_off_amount",
)  # fmt: skip
DEMAND_FIELDS = (
	"name", "demand_date", "demand_type", "demand_subtype", "demand_amount", "paid_amount", "outstanding_amount",
)  # fmt: skip

GET_LOAN_DUES_SCHEMA = {
	"name": "get_loan_dues",
	"description": (
		"What is due on one loan, from the Loan Demand rows you may read: billed, paid, waived, outstanding and overdue "
		"amounts per demand type, plus the loan's status fields. Does NOT include accrued-but-unbilled interest, future "
		"interest or unbooked penalty. as_on_date is a YYYY-MM-DD date, or null for today."
	),
	"strict": True,
	"input_schema": {
		"type": "object",
		"properties": {
			"loan": {"type": "string", "description": "The Loan ID."},
			"as_on_date": {
				"type": ["string", "null"],
				"description": "YYYY-MM-DD, or null for today. Demands dated after it are left out.",
			},
		},
		"required": ["loan", "as_on_date"],
		"additionalProperties": False,
	},
}
SCHEMAS = (GET_LOAN_DUES_SCHEMA,)


def _parse_date(value) -> date:
	if value is None:
		return now_datetime().date()
	if not isinstance(value, str) or len(value) != 10:
		raise frappe.ValidationError("as_on_date must be a date written YYYY-MM-DD, or null.")
	try:
		return date.fromisoformat(value)
	except ValueError:
		raise frappe.ValidationError("as_on_date must be a date written YYYY-MM-DD, or null.") from None


def _money(value) -> Decimal:
	return Decimal(str(value)) if value not in (None, "") else ZERO


def _out(value: Decimal) -> float:
	return float(round(value, 2))


def _rows(loan: str, on: date, fields: list) -> tuple[list, bool]:
	"""Up to MAX_PAGES pages of this loan's submitted demands due on or before `on`, in name order (keyset on `name`)."""
	rows, last, incomplete = [], None, False
	for page in range(MAX_PAGES):
		filters = [
			["loan", "=", loan],
			["docstatus", "=", 1],
			["demand_date", "<=", f"{on.isoformat()} 23:59:59"],
		]
		if last is not None:
			filters.append(["name", ">", last])
		payload = guard.unwrap(
			guard.list_records("Loan Demand", filters=filters, fields=fields, order_by="name asc", limit=PAGE)
		)
		got = payload["rows"]
		rows.extend(got)
		if not got:
			break
		last = got[-1]["name"]
		if len(got) < PAGE and not payload.get("truncated"):
			break
		if page == MAX_PAGES - 1:
			incomplete = True
	return rows, incomplete


def get_loan_dues(loan, as_on_date=None) -> str:
	on = _parse_date(as_on_date)
	loan_payload = guard.unwrap(guard.read_doc("Loan", loan))  # G4: one reply for a missing and a hidden loan
	loan_data = loan_payload.get("data") or {}
	readable = set(guard.readable_fields("Loan Demand"))
	if not {"name", "loan", "docstatus", "demand_date", "outstanding_amount"} <= readable:
		raise guard.AssistantRefused("You can't read the demands of this loan.")
	fields = [f for f in DEMAND_FIELDS if f in readable]
	with_waived = "waived_amount" in readable
	if with_waived:
		fields.append("waived_amount")
	rows, incomplete = _rows(loan_payload["name"], on, fields)

	groups, totals = (
		{},
		dict.fromkeys(("billed", "paid", "waived", "outstanding", "overdue", "due_on_date"), ZERO),
	)
	oldest = None
	for row in rows:
		key = (row.get("demand_type"), row.get("demand_subtype"))
		g = groups.setdefault(
			key, dict.fromkeys(("billed", "paid", "waived", "outstanding", "overdue"), ZERO) | {"rows": 0}
		)
		billed, paid, left = (
			_money(row.get("demand_amount")),
			_money(row.get("paid_amount")),
			_money(row.get("outstanding_amount")),
		)
		waived = _money(row.get("waived_amount")) if with_waived else ZERO
		g["rows"] += 1
		due = str(row.get("demand_date") or "")[:10]
		overdue = left if left > 0 and due and due < on.isoformat() else ZERO
		due_today = left if left > 0 and due == on.isoformat() else ZERO
		for target in (g, totals):
			target["billed"] += billed
			target["paid"] += paid
			target["waived"] += waived
			target["outstanding"] += left
			target["overdue"] += overdue
		totals["due_on_date"] += due_today
		if overdue > 0 and (oldest is None or due < oldest):
			oldest = due

	by_demand = []
	for (dtype, subtype), g in sorted(groups.items(), key=lambda kv: (str(kv[0][0]), str(kv[0][1]))):
		item = {"demand_type": dtype, "demand_subtype": subtype, "rows": g["rows"]}
		for k in ("billed", "paid", "waived", "outstanding", "overdue"):
			if k != "waived" or with_waived:
				item[k] = _out(g[k])
		by_demand.append(item)
	totals_out = {k: _out(v) for k, v in totals.items() if k != "waived" or with_waived}
	result = {
		"loan": loan_payload["name"],
		"as_on_date": on.isoformat(),
		"loan_details": {f: loan_data[f] for f in LOAN_FIELDS if f in loan_data},
		"totals": totals_out,
		"oldest_overdue_date": oldest,
		"by_demand": by_demand,
		"rows_read": len(rows),
		"incomplete": incomplete,
		"truncated": False,
		"note": NOTE,
		"outstanding_note": OUTSTANDING_NOTE,
	}
	if incomplete:
		result["incomplete_note"] = (
			f"Only the first {MAX_PAGES * PAGE} demands were read; the totals are lower bounds."
		)
	cleaned = guard.unwrap(guard.as_data(result))
	guard.fit(cleaned, row_lists=lambda: [cleaned["by_demand"]], field_dicts=lambda: [])
	return guard.as_data(cleaned)
