---
id: bridge.BR-LMS-169
type: bridge
title: Fix wrong payment postings safely
summary: "Covered. Loan Repayment Repost redoes postings and keeps the originals. It has no approval step or reason field, which is configuration the bank must add."
br_ids: [BR-LMS-169]
brd_section: 7.7
doctypes: [Loan Repayment Repost]
verdict: covered
analysis_status: verified
dev_items: []
fields: [Loan Repayment Repost.Repost Date, Loan Repayment Repost.Status]
options: [Loan Repayment Repost.Status=Draft, Loan Repayment Repost.Status=Queued, Loan Repayment Repost.Status=In Process, Loan Repayment Repost.Status=Completed, Loan Repayment Repost.Status=Cancelled]
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_repayment_repost/loan_repayment_repost.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-169"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p51"
  - "sources/verification/reqs.json#BR-LMS-169"
  - "sources/verification/verification_report.md#BR-LMS-169"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-169"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-169"
related: [concept.BR-LMS-169, bridge.BR-LMS-163]
version: 1
status: approved
approved_by: Owner
---
**In short:** Covered. Loan Repayment Repost redoes postings and keeps the originals. It has no approval step or reason field, which is configuration the bank must add.

## Business need

Corrections must go through a controlled, resumable, approved repost that retains the original entries (BR-LMS-169, BRD 7.7.1, PDF page 51). See `concept.BR-LMS-169`.

## Frappe Lending today

The **Loan Repayment Repost** document has a **Repost Date** and a **Status** (Draft, Queued, In Process, Completed, Cancelled). In the live test it was created as Draft and became Completed on submit. The original accounting rows were cancelled, a reversing set and a new set were added, and the originals stayed visible. The Queued and In Process states are guarded in code, so the job is restartable by design.

## Match or gap, and why

This is **covered**, with caveats, as the original analysis said. The core idea of a repost (redoing the postings from a date) while keeping the original entries works. Two controls the BRD asks for are not in place. There is no reason field and no approval: only a System Manager can create it, the same user creates and submits it, and no workflow is configured. A side effect also surprised the test: after the repost, the system caught the loan up to today and created 29 Additional Interest accruals and bills.

## What to do today

Agree an approval step outside the system: someone else reviews the repost before it is submitted. Note the reason in a comment. After the repost, check the accruals and demands that were created.

## Planned fix

An approval workflow is part of D8 (the approval and audit pack). No new document is needed.
