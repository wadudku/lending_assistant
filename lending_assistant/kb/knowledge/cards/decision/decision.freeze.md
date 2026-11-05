---
id: decision.freeze
type: decision
title: "Decision: freezing a loan"
summary: "A freeze suspends a loan's processing for an authorised period. The BRD wants the approval, the period and the suspended processing recorded. Frappe Lending has a tick box with a log that has no approver and, in the test, no reason, and unfreezing charged the frozen days."
br_ids: [BR-LMS-196]
brd_section: 7.10
doctypes: [Loan, Loan Freeze Log]
dev_items: [D8]
decision: freeze
actions: ["Loan:freeze"]
options: []
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan/loan.py:505", "lending/loan_management/doctype/loan/loan.py:512"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-196"
  - "sources/verification/reqs.json#BR-LMS-196"
  - "sources/verification/verification_report.md#BR-LMS-196"
  - "sources/verification/FINAL_REPORT.md#D8"
  - "sources/verification/FINAL_REPORT.md#revised-suggested-order"
related: [lifecycle.FROZEN, devitem.D8]
version: 2
status: approved
approved_by: Owner
---
**In short:** A freeze suspends a loan's processing for an authorised period. The BRD wants the approval, the period and the suspended processing recorded. Frappe Lending has a tick box with a log that has no approver and, in the test, no reason, and unfreezing charged the frozen days.

## The rule

BR-LMS-196 says authorised freeze and unfreeze periods are recorded, the processing suspended during the freeze is stated explicitly and the authorising approval is retained. BRD 5.3 defines the FROZEN state as an authorised freeze in force with configured processing suspended. The BRD does not say who may authorise a freeze or which processing stops.

## Options

On the **Loan** there is a **Freeze Account** check and a **Freeze Date**. Ticking the box and saving a submitted loan writes a **Loan Freeze Log** row, cancels demands and reverses accruals from the freeze date and recalculates days past due (`lending/loan_management/doctype/loan/loan.py:505`, `lending/loan_management/doctype/loan/loan.py:507`). Unticking clears the freeze date, runs accrual up to today and writes a second log row with an unfreeze date (`lending/loan_management/doctype/loan/loan.py:512`, `lending/loan_management/doctype/loan/loan.py:513`). The log holds the loan, the freeze date, a reason for freezing and the unfreeze date.

## Who approves

The BRD wants an authorising approval. In the test, there was no approval step: the installed Loan doctype gives the Loan Manager role create, write and submit, so one person can freeze. The freeze log itself can be edited and deleted by the System Manager role (installed permissions). The planned approval pack (D8) adds a reason, an approver and a scope, and removes the Delete right.

## How Frappe Lending does it today

The verified result for BR-LMS-196 is partly covered. In the test, the log reason was always empty, because the code reads a freeze reason that the Loan does not have. What is suspended is not written on the record. Unfreezing back-charged interest and penalty for the whole frozen period (DEF-12), so the freeze stopped nothing in the end. The freeze was also off by one day and rewrote the days-past-due log (DEF-16). The unfreeze log row is not linked to the freeze row. See `lifecycle.FROZEN`.

*Codes:* DEF = defect, ND = new item, both found in verification (final report, sections 5 and 7).
