---
id: bridge.BR-LMS-183
type: bridge
title: A restructure makes a new plan and keeps the old one
summary: Covered. Approving a restructure marks the old Loan Repayment Schedule as Restructured or Rescheduled and activates a new one. The new plan's figures have flaws that the ledger does not share.
br_ids: [BR-LMS-183]
brd_section: 7.9
doctypes: [Loan Repayment Schedule, Loan Restructure]
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_restructure/loan_restructure.py:599-601"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-183"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p53"
  - "sources/verification/reqs.json#BR-LMS-183"
  - "sources/verification/verification_report.md#BR-LMS-183"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-183"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-183"
  - "sources/verification/FINAL_REPORT.md#new-items-found-in-verification-nd-1-...-nd-47"
related: [concept.BR-LMS-183, decision.restructure, lifecycle.RESTRUCTURED, bridge.BR-LMS-182]
version: 1
status: approved
approved_by: Owner
---
**In short:** Covered. Approving a restructure marks the old Loan Repayment Schedule as Restructured or Rescheduled and activates a new one. The new plan's figures have flaws that the ledger does not share.

## Business need

A restructure must generate a new schedule and keep the prior one marked as restructured and superseded (BR-LMS-183 in section 7.9, BRD PDF page 53). See `concept.BR-LMS-183`.

## Frappe Lending today

When a restructure is approved, the old **Loan Repayment Schedule** is set to Restructured for a Normal Restructure and to Rescheduled for the other two types, and the new schedule is Active (`lending/loan_management/doctype/loan_restructure/loan_restructure.py:599-601`). In the test, the schedule of the 60-day overdue loan became Restructured and the new one Active, and the same on the NPA loan. After an Advance Payment or a Pre Payment, the old plan became Rescheduled.

## Match or gap, and why

This is **covered**, with caveats from the test (J6). The BRD's word is "restructured"; the app uses Rescheduled for payments that change the plan, which is the same idea under another label.

- The new plan's principal is overstated after a restructure that adds interest to the first EMI (DEF-18).
- For an Advance Payment, the paid rows of the new plan show today's balance, and the excess principal of the advance appears on no row. The ledger is right; only the schedule view is wrong.

## What to do today

Read the ledger or the Loan Statement of Account for the balance, and use the schedule only for dates and the shape of the plan after a restructure.

## Planned fix

No development item is assigned. Schedule fixes are part of D6 and ND-20 (see `decision.restructure`).
