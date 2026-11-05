"""Assistant Finding: a team note saved by a user's click (G13). The rules live here so they hold for the form, the REST
API and `frappe.client` alike; the roles have no create, the only insert is `assistant/findings.py`.
"""

import frappe
from frappe.model.document import Document
from frappe.utils import now_datetime

from lending_assistant.assistant import finding_rules

REVIEWER = "Assistant Reviewer"
MAX_TITLE = 140
MAX_SUMMARY = 4000
PROVENANCE = (
	"question",
	"sources",
	"cards_used",
	"cards_basis",
	"lending_version",
	"author_name",
	"source_message",
	"owner",
)
CONTENT = ("title", "summary", "br_ids", "doctypes")
JSON_FIELDS = ("sources", "cards_used")


def _same(field, before, after) -> bool:
	if field in JSON_FIELDS:  # whitespace in the JSON text is not a change
		return finding_rules.parse_json_list(before) == finding_rules.parse_json_list(after)
	return (before or "") == (after or "")


class AssistantFinding(Document):
	def validate(self):
		before = self.get_doc_before_save()
		self._check_shape()
		self.br_ids = "\n".join(finding_rules.check_br_ids(self.br_ids))
		self.doctypes = "\n".join(finding_rules.check_doctypes(self.doctypes))
		if before is not None:
			self._provenance_unchanged(before)
		self._check_status(before)

	def _check_shape(self):
		self.title = " ".join((self.title or "").split())
		self.summary = (self.summary or "").strip()
		if not self.title or len(self.title) > MAX_TITLE:
			frappe.throw(f"The title is required and at most {MAX_TITLE} characters.")
		if not self.summary or len(self.summary) > MAX_SUMMARY:
			frappe.throw(f"The summary is required and at most {MAX_SUMMARY} characters.")
		if self.status not in ("Draft", "Confirmed"):
			frappe.throw("The status must be Draft or Confirmed.")

	def _provenance_unchanged(self, before):
		changed = [
			self.meta.get_label(f) or f for f in PROVENANCE if not _same(f, before.get(f), self.get(f))
		]
		if changed:
			frappe.throw("These fields can't be changed after saving: " + ", ".join(changed) + ".")

	def _check_status(self, before):
		reviewer = REVIEWER in frappe.get_roles()
		was_confirmed = before is not None and before.status == "Confirmed"
		if self.status != "Confirmed":
			self.confirmed_by = None
			self.confirmed_on = None
			return
		if not was_confirmed:
			if not reviewer:
				frappe.throw("Only an Assistant Reviewer can confirm a finding.", frappe.PermissionError)
			self.confirmed_by = frappe.session.user
			self.confirmed_on = now_datetime()
			return
		# already Confirmed: the confirmation fields are derived, never taken from the client
		self.confirmed_by = before.confirmed_by
		self.confirmed_on = before.confirmed_on
		if not reviewer and any(not _same(f, before.get(f), self.get(f)) for f in CONTENT):
			self.status = "Draft"
			self.confirmed_by = None
			self.confirmed_on = None
			frappe.msgprint("This finding was confirmed. Your change set it back to Draft.")

	def onload(self):
		self.set_onload("stale_reasons", finding_rules.stale_reasons(self.cards_used, self.lending_version))
