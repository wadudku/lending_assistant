---
id: bridge.BR-LMS-224
type: bridge
title: Work queues for things that went wrong
summary: "Gap. Failures go to Frappe's Error Log. An owner can be assigned by hand and an age can be read, but there is no queue for each kind of failure, no closure note and no count."
br_ids: [BR-LMS-224]
brd_section: 7.13
doctypes: [Loan]
verdict: gap
analysis_status: verified
dev_items: [D9]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-224"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p55"
  - "sources/verification/reqs.json#BR-LMS-224"
  - "sources/verification/verification_report.md#BR-LMS-224"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-224"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-224"
  - "sources/verification/FINAL_REPORT.md#new-items-found-in-verification-nd-1-...-nd-47"
  - "sources/verification/FINAL_REPORT.md#D9"
related: [concept.BR-LMS-224, bridge.BR-LMS-223, bridge.BR-LMS-225, devitem.D9, bridge.BR-LMS-166]
version: 1
status: approved
approved_by: Owner
---
**In short:** Gap. Failures go to Frappe's Error Log. An owner can be assigned by hand and an age can be read, but there is no queue for each kind of failure, no closure note and no count.

## Business need

The platform must show exception work queues for failed demands, repayments, postings, integrations and unreconciled items, each with an owner, an age and a documented closure (BR-LMS-224 in section 7.13, BRD PDF page 55). See `concept.BR-LMS-224`.

## Frappe Lending today

The lending app adds no work queue document or screen. The nearest record is the **Bulk Repayment Log** of the bulk payment call, which marks each loan Success or Failure with the error (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:3488-3518`; see `bridge.BR-LMS-166`), but it has no owner, age or closing note. A failure in a scheduled job is written to Frappe's own Error Log, with a title, a reference to the document and the first and last time seen. In the test the demand failures were Error Log rows titled "Term Loan Demand Generation Error", one per loan, with identical ones grouped under a count of occurrences. The test user could use Assign on a row, which made a ToDo allocated to the test user.

## Match or gap, and why

This is a **gap**, and the verification confirmed it, though it noted the case is on the border of partly covered (J11). The owner decided that the Error Log is not a business work queue.

- An owner and an age can be improvised from Assign and the first-seen date.
- Missing: a status or a closing note, a queue for each kind of failure (bills, payments, postings), counts and the oldest age on a dashboard, automatic assignment and escalation.
- Opening a row marks it as Seen, which is the only sign that someone has handled it.

## What to do today

Keep a daily checklist: open the Error Log, assign each new row to a named person, and record the closure in the ToDo. Keep the oldest-open count in a register.

## Planned fix

Dev item D9 (batch run and exception framework, sized large) covers this row. The final report proposes ND-44 (a failure queue and an alert, medium).
