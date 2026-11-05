---
id: bridge.BR-LMS-161
type: bridge
title: A payment counts only after the CBS confirms it
summary: "Partly covered. A draft repayment changes nothing, which is a usable workaround, but there is no pending status and no CBS confirmation step."
br_ids: [BR-LMS-161]
brd_section: 7.7
doctypes: [Loan Repayment]
verdict: partial
analysis_status: verified
dev_items: [D12]
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_repayment/loan_repayment.json]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-161"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p50"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p51"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p52"
  - "sources/verification/reqs.json#BR-LMS-161"
  - "sources/verification/verification_report.md#BR-LMS-161"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-161"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-161"
related: [concept.BR-LMS-161, devitem.D12, bridge.BR-LMS-162]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. A draft repayment changes nothing, which is a usable workaround, but there is no pending status and no CBS confirmation step.

## Business need

An unconfirmed payment must never reduce what the borrower owes, and it must be visible as pending (BR-LMS-161, BRD 7.7.1, PDF page 50). See `concept.BR-LMS-161`.

## Frappe Lending today

A **Loan Repayment** that is saved but not submitted stays a draft. In the verification test, a draft repayment left the amount due unchanged and created no accounting entries. Frappe Lending has no CBS confirmation step. Loan Repayment has no status field and no workflow.

## Match or gap, and why

This is **partly covered**. The part that exists: a draft does not touch balances, so an unconfirmed payment can sit as a draft without effect. The part that is missing: nothing marks that draft as waiting for the CBS, and nothing links submitting it to a CBS confirmation. Anyone with submit permission on Loan Repayment (System Manager and Loan Manager in the installed doctype) can submit it at any time. The BRD wants the payment visible as pending, and a draft carries no such status.

The final design also depends on questions NRB has not answered yet. BRD section 7.7.2 asks how the platform will learn that a credit has arrived (PDF pages 51 and 52), and that decides how confirmation can work.

## What to do today

Keep unconfirmed payments as drafts. Submit a repayment only after the CBS shows the money. Write in the draft's remarks that it is waiting for the CBS, so colleagues know.

## Planned fix

D12 (`devitem.D12`) adds a CBS status field with the values Pending, Confirmed and Failed, and submits a repayment automatically only when it is Confirmed. It is sized medium and waits for NRB's answers to the BRD's open items (the BRD's own dependency D19, which is not our development item D19).
