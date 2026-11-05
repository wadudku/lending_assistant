---
id: bridge.BR-LMS-220
type: bridge
title: Move loans between branches in bulk
summary: "Covered. This verdict comes from reading the code and was not tested live. A Loan Transfer sets a new branch on many loans and keeps the same record, but it works only after Branch is set up as an accounting dimension."
br_ids: [BR-LMS-220]
brd_section: 7.13
doctypes: [Loan Transfer, Loan Transfer Detail, Loan, Journal Entry]
verdict: covered
analysis_status: code_reading
dev_items: []
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_transfer/loan_transfer.py:57-67", "lending/loan_management/doctype/loan_transfer/loan_transfer.py:92-105"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-220"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p55"
  - "sources/verification/reqs.json#BR-LMS-220"
  - "sources/verification/verification_report.md#BR-LMS-220"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-220"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-220"
related: [concept.BR-LMS-220, bridge.BR-LMS-184]
version: 1
status: approved
approved_by: Owner
---
**In short:** Covered. This verdict comes from reading the code and was not tested live. A Loan Transfer sets a new branch on many loans and keeps the same record, but it works only after Branch is set up as an accounting dimension.

## Business need

The platform must move loans between branches in bulk, keeping the same loan record and its complete history (BR-LMS-220 in section 7.13, BRD PDF page 55). See `concept.BR-LMS-220`.

## Frappe Lending today

A **Loan Transfer** has a from-branch, a to-branch, a transfer date and a table of loans. If the table is left empty on save, the code fills it with every submitted loan of the from-branch, or only one applicant's loans in that branch (`lending/loan_management/doctype/loan_transfer/loan_transfer.py:46-55`, `lending/loan_management/doctype/loan_transfer/loan_transfer.py:178-191`). On submit, the code writes the new branch into the branch field of each loan with a direct database update, so the loan keeps its name and number (`lending/loan_management/doctype/loan_transfer/loan_transfer.py:92-105`). In a background job, when accounting is on, it then posts one Journal Entry per loan to move the balances of the profit and loss accounts from the old branch to the new one (`lending/loan_management/doctype/loan_transfer/loan_transfer.py:171-174`). The Loan Transfer document is the record of the move.

## Match or gap, and why

This is **covered**, but only from reading the code. It was not tested live. The verification report says why: the test site has no Branch accounting dimension, and the owner decided not to add one site-wide just for the test. In the test, saving a Loan Transfer was refused with "Please set up Branch as an Accounting Dimension before transferring loans between branches", which the code raises on every save while Branch is not an accounting dimension (`lending/loan_management/doctype/loan_transfer/loan_transfer.py:57-67`). So the real run, with a branch on the loans and the journal entries, was never seen.

- The loans are chosen from the from-branch, optionally narrowed to one applicant. A free selection of loans across branches is not how the list is built.
- The Loan has no branch field of its own; the field exists only after the Branch dimension is created.
- This is not a defect in the app. It is a setup step outside the loan app that the bank must do first.

## What to do today

Before any transfer, set up Branch as an accounting dimension and test one small transfer on a copy of the data: check that each loan keeps its number and history and that the journal entries move the right balances.

## Planned fix

No development item is assigned. The configuration step (the Branch dimension) must come first.
