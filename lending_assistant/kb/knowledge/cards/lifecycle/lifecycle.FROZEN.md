---
id: lifecycle.FROZEN
type: lifecycle
title: Loan state FROZEN
summary: "In the BRD, FROZEN is a loan under an authorised freeze with its processing suspended. In Frappe Lending it is a tick on the loan with a log, and it has no approver or reason."
br_ids: [BR-LMS-196]
brd_section: 5.3
doctypes: [Loan, Loan Freeze Log]
dev_items: [D2, D8]
lifecycle_state: FROZEN
fields: [Loan.Freeze Account, Loan.Freeze Date, Loan Freeze Log.Reason For Freezing]
options: []
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan/loan.py:504", "lending/loan_management/doctype/loan/loan.py:510"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#5.3"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p27"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#5.1-the-two-lifecycles-side-by-side"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#5.2-the-main-difference"
  - "sources/verification/reqs.json#BR-LMS-196"
  - "sources/verification/verification_report.md#BR-LMS-196"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-196"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D2"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D8"
related: [brd_section.5.3, lifecycle.OVERDUE, lifecycle.NPA, devitem.D8, devitem.D2]
version: 2
status: approved
approved_by: Owner
---
**In short:** In the BRD, FROZEN is a loan under an authorised freeze with its processing suspended. In Frappe Lending it is a tick on the loan with a log, and it has no approver or reason.

## The BRD state

BRD 5.3 (PDF page 27) defines FROZEN as: authorised freeze in force; configured processing suspended. BR-LMS-196 asks that freeze and unfreeze periods are recorded, that the suspended processing is stated explicitly and that the authorising approval is kept.

## The Frappe Lending equivalent

There is no Frozen status. The loan has a **Freeze Account** check and a **Freeze Date**, and each change is logged in the **Loan Freeze Log** (loan, freeze date, reason for freezing, unfreeze date). When the box is ticked, the code writes the log, cancels demands and reverses interest accruals from the freeze date (`lending/loan_management/doctype/loan/loan.py:505`, `lending/loan_management/doctype/loan/loan.py:506`). When it is unticked, it clears the date, runs accrual up to today and writes a second log row (`lending/loan_management/doctype/loan/loan.py:512`, `lending/loan_management/doctype/loan/loan.py:513`).

## Why they differ

The verified result is partly covered. In the test, the freeze had no approver and no reason: the code reads a freeze reason that the Loan does not have, so the log reason was empty. What is suspended is not written on the record. Unfreezing back-charged the whole frozen period (DEF-12), so in the end the freeze stopped nothing. The proposed approval pack (D8) adds an approver, a reason and a scope.

## How a loan enters and leaves it

A loan enters this state when someone ticks Freeze Account on a submitted loan and saves; it leaves when the box is unticked. The coverage analysis rates the match as partly covered: a flag, not a status, with no approver.

*Codes:* DEF = defect, ND = new item, both found in verification (final report, sections 5 and 7).
