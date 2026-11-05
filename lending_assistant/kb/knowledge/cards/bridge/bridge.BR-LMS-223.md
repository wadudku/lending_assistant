---
id: bridge.BR-LMS-223
type: bridge
title: Every batch has a clear status
summary: "Partly covered. Only the Loan Repayment Repost has the five states, and only the bulk payment call keeps a result per loan. The runs for interest, bills, grades, accounting and shortfall have no status and no result per loan. A re-run after a failure was safe in the test."
br_ids: [BR-LMS-223]
brd_section: 7.13
doctypes: [Loan Repayment Repost, Process Loan Demand, Process Loan Interest Accrual, Process Loan Classification]
verdict: partial
analysis_status: verified
dev_items: [D9]
fields: [Loan Repayment Repost.Status]
options: [Loan Repayment Repost.Status=Draft, Loan Repayment Repost.Status=Queued, Loan Repayment Repost.Status=In Process, Loan Repayment Repost.Status=Completed, Loan Repayment Repost.Status=Cancelled]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-223"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p55"
  - "sources/verification/reqs.json#BR-LMS-223"
  - "sources/verification/verification_report.md#BR-LMS-223"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-223"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-223"
  - "sources/verification/FINAL_REPORT.md#new-items-found-in-verification-nd-1-...-nd-47"
  - "sources/verification/FINAL_REPORT.md#D9"
related: [concept.BR-LMS-223, bridge.BR-LMS-224, bridge.BR-LMS-225, devitem.D9, bridge.BR-LMS-166]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. Only the Loan Repayment Repost has the five states, and only the bulk payment call keeps a result per loan. The runs for interest, bills, grades, accounting and shortfall have no status and no result per loan. A re-run after a failure was safe in the test.

## Business need

Every batch must keep an explicit state and row-level outcomes and be resumable without double posting (BR-LMS-223 in section 7.13, BRD PDF page 55). See `concept.BR-LMS-223`.

## Frappe Lending today

A **Loan Repayment Repost** has a **Status** with the options Draft, Queued, In Process, Completed and Cancelled (`lending/loan_management/doctype/loan_repayment_repost/loan_repayment_repost.json`). The batch runners **Process Loan Demand**, **Process Loan Interest Accrual**, **Process Loan Classification**, **Process Loan Accounting**, **Process Loan Security Shortfall** and **Process Loan Restructure Limit**, and the **Loan Accrual Repost**, have no status field and no result field. The one batch with a result per loan is the bulk payment call: each loan gets a **Bulk Repayment Log** with a Success or Failure status and the error (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:3488-3518`; see `bridge.BR-LMS-166`). Each is a submittable document with date and scope fields.

## Match or gap, and why

This is **partly covered**, and the verification confirmed the verdict (J11).

- In the test, a nightly-style demand run failed for two loans because of a blank accrual account on a product copy. The Process Loan Demand stayed Submitted with no state, no count and no result per loan. The two failures existed only as Error Log rows.
- Restarting was safe. After the fix a re-run billed both loans once (31 and 4 demands, no duplicates).
- So the "resumable without double posting" half is met in the test, and the "explicit state with row-level outcomes" half is not.

## What to do today

After each run, open the Error Log and the list of demands for the date and count them against the loans you expect. Re-run for the failed loans only, with the run scoped to them.

## Planned fix

Dev item D9 (batch run and exception framework, sized large) covers this row. The final report proposes ND-43 (a run status and a result per loan for every Process runner, medium).
