---
id: bridge.BR-LMS-102
type: bridge
title: The stages of a loan's life
summary: "Covered. The loan has a Status field with a value for each BRD stage, under different names. In the test, it kept no history of status changes."
br_ids: [BR-LMS-102]
brd_section: 7.1
doctypes: [Loan]
verdict: covered
analysis_status: verified
dev_items: [D2]
fields: [Loan.Status]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan/loan.json:170", "lending/loan_management/doctype/loan/loan.py:471"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-102"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p46"
  - "sources/verification/reqs.json#BR-LMS-102"
  - "sources/verification/verification_report.md#BR-LMS-102"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-102"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-102"
related: [concept.BR-LMS-102, brd_section.7.1, devitem.D2, lifecycle.BOOKED, lifecycle.ACTIVE, lifecycle.PARTIALLY_DISBURSED, lifecycle.CLOSURE_REQUESTED, lifecycle.CLOSED, lifecycle.SETTLED, lifecycle.WRITTEN_OFF]
version: 1
status: approved
approved_by: Owner
---
**In short:** Covered. The loan has a Status field with a value for each BRD stage, under different names. In the test, it kept no history of status changes.

## Business need

The bank wants every loan to move through booked, active (or partially disbursed), closure requested, and then closed, settled or written off, with servicing starting only after confirmed funding (BR-LMS-102, BRD 7.1, PDF page 46). See `concept.BR-LMS-102`.

## Frappe Lending today

The **Loan** has a read-only **Status** field with nine options: Draft, Sanctioned, Partially Disbursed, Disbursed, Active, Loan Closure Requested, Closed, Written Off and Settled (`loan.json` lines 170-178). Submitting the loan sets Sanctioned (`loan.py` line 471). The names differ from the BRD (Sanctioned against BOOKED). The other stages have their own cards: `lifecycle.BOOKED`, `lifecycle.ACTIVE`, `lifecycle.PARTIALLY_DISBURSED`, `lifecycle.CLOSURE_REQUESTED`, `lifecycle.CLOSED`, `lifecycle.SETTLED` and `lifecycle.WRITTEN_OFF`.

## Match or gap, and why

This is **covered**. In the test, a loan went Draft, Sanctioned, Disbursed, and a tranche loan went Sanctioned, Partially Disbursed, Disbursed (verification_report.md:84). The caveat is history. In the test, the Version log recorded only Draft to Sanctioned, because later statuses are written directly with db_set and are not tracked. The BRD asks for a trail of status changes elsewhere (BR-LMS-001 in BRD 5.3), and that is the gap that D2 addresses. The coverage analysis rated this row covered, and verification confirmed it.

## What to do today

Read the stage from **Status** on the Loan and use the lifecycle cards to translate the name. Do not expect to see when a status changed; use the repayment, disbursement and write-off records for the dates.

## Planned fix

Dev item D2 (`devitem.D2`) adds a separate Servicing Status with the BRD's twelve values and a log of every change. Verification added a status history log as ND-3.
