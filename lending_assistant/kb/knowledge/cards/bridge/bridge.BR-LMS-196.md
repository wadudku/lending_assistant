---
id: bridge.BR-LMS-196
type: bridge
title: Freezing a loan
summary: "Partly covered. A freeze tick and a Loan Freeze Log stop accruals and bills, but the log has no approver, no reason and no record of what stopped, and unfreezing back-charges the frozen period."
br_ids: [BR-LMS-196]
brd_section: 7.10
doctypes: [Loan, Loan Freeze Log]
verdict: partial
analysis_status: verified
dev_items: [D8]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan/loan.py:505-513"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-196"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p54"
  - "sources/verification/reqs.json#BR-LMS-196"
  - "sources/verification/verification_report.md#BR-LMS-196"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-196"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-196"
  - "sources/verification/FINAL_REPORT.md#new-items-found-in-verification-nd-1-...-nd-47"
  - "sources/verification/FINAL_REPORT.md#D8"
related: [concept.BR-LMS-196, decision.freeze, lifecycle.FROZEN, devitem.D8]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. A freeze tick and a Loan Freeze Log stop accruals and bills, but the log has no approver, no reason and no record of what stopped, and unfreezing back-charges the frozen period.

## Business need

A freeze and unfreeze must be recorded with the processing suspended and the approval retained (BR-LMS-196 in section 7.10, BRD PDF page 54). See `concept.BR-LMS-196`. How the freeze works and who can do it is in `decision.freeze`; the state is `lifecycle.FROZEN`.

## Frappe Lending today

Ticking **Freeze Account** with a **Freeze Date** on a submitted **Loan** writes a **Loan Freeze Log** row and stops new accruals and bills from the freeze date. Unticking writes a second row (`lending/loan_management/doctype/loan/loan.py:505-513`). The detail of those steps is in `decision.freeze`. In the test, the demands dated on or after the freeze date were cancelled and the accruals after it were not created.

## Match or gap, and why

This is **partly covered**, and the verification confirmed the verdict (J4). What the approved decision card does not repeat:

- The log reason is always empty, because the code reads a freeze reason field that the Loan does not have. The log has no approver and does not say what was suspended.
- The unfreeze row is a separate row, not linked to the freeze row, and has no freeze date.
- Unfreezing back-charged the frozen period in the first test (307.23 of interest, penal accruals and 40 Additional Interest demands), so the freeze stopped nothing in the end (DEF-12). In the second test the unfreeze created nothing, but a penal amount cancelled at the freeze was never billed again.
- The freeze date itself was accrued and billed, and the days past due log was rewritten to 0 while the Loan kept 91 (DEF-16).
- The Loan Freeze Log can be edited and deleted by the System Manager without a trace.

## What to do today

Keep the authorising document and the list of what was stopped outside the system, and after an unfreeze check the accruals and demands for the frozen period against the instruction.

## Planned fix

Dev item D8 (approval and audit pack) covers the approval. The final report proposes ND-16 (a freeze with a reason, an approver and a scope, and no back-charge, medium).
