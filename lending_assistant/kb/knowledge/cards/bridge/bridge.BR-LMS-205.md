---
id: bridge.BR-LMS-205
type: bridge
title: "Full record for every settlement, waiver, write-off and recovery"
summary: "Partly covered. A Loan Repayment keeps a reference number, free-text remarks and the amounts payable and paid, but there is no approver, approval date, reason or before and after record. The Loan Write Off has no reference, reason or remarks field at all."
br_ids: [BR-LMS-205]
brd_section: 7.11
doctypes: [Loan Repayment, Loan Write Off]
verdict: partial
analysis_status: verified
dev_items: [D8]
fields: [Loan Repayment.Reference Number, Loan Repayment.Manual Remarks]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-205"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p54"
  - "sources/verification/reqs.json#BR-LMS-205"
  - "sources/verification/verification_report.md#BR-LMS-205"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-205"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-205"
  - "sources/verification/FINAL_REPORT.md#new-items-found-in-verification-nd-1-...-nd-47"
  - "sources/verification/FINAL_REPORT.md#D8"
related: [concept.BR-LMS-205, decision.waiver, decision.settlement, decision.write-off, devitem.D8, bridge.BR-LMS-185, bridge.BR-LMS-201]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. A Loan Repayment keeps a reference number, free-text remarks and the amounts payable and paid, but there is no approver, approval date, reason or before and after record. The Loan Write Off has no reference, reason or remarks field at all.

## Business need

Every settlement, waiver, write-off and recovery must keep before and after amounts, the reason, the maker, the checker, the approval date and any external reference (BR-LMS-205 in section 7.11, BRD PDF page 54). See `concept.BR-LMS-205`. The manual adjustments of section 7.9 are in `bridge.BR-LMS-185`.

## Frappe Lending today

A **Loan Repayment** keeps a **Reference Number** and **Reference Date**, **Manual Remarks** (free text), the payable and paid amounts, and an excess amount (`lending/loan_management/doctype/loan_repayment/loan_repayment.json`). Its Version log shows who submitted it. A **Loan Write Off** keeps the loan, dates, account, amount and an Is Settlement Write Off tick, and has change tracking on (`lending/loan_management/doctype/loan_write_off/loan_write_off.json`). A search of both definitions for approval, reason, maker and checker fields found none.

## Match or gap, and why

This is **partly covered**, and the verification confirmed the verdict (J8).

- The Loan Write Off has no reference, reason, remarks or approver field. In the test, the Version log of a settlement write-off had one row, and the only extra field was Is Settlement Write Off.
- On the Loan Repayment, the reference and remarks are optional. In the test a Full Settlement had a reference but empty remarks.
- Neither document has an approver, an approval date, or a stored before-and-after amount.
- The waivers and the write-off that a Full Settlement creates carry no field that links them back to the settlement repayment. The repayment has only a flag for a write-off waiver and the name of the job that made them.

## What to do today

Keep a register outside the system for each settlement, waiver, write-off and recovery with the amounts before and after, the reason, the maker, the checker, the approval date and the external reference. Put the reference in the Reference Number of the repayment.

## Planned fix

Dev item D8 (approval and audit pack, sized large) covers this row. The final report adds ND-32 (a settlement offer record and approval, medium) and ND-23 for the manual adjustments.
