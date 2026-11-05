---
id: bridge.BR-LMS-101
type: bridge
title: One record holds everything about a loan
summary: "Covered. The Loan form links the schedule, bills, payments, security, adjustments, logs and accounting records. Accounting entries are reached through the ledger rather than the form."
br_ids: [BR-LMS-101]
brd_section: 7.1
doctypes: [Loan]
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan/loan_dashboard.py:1"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-101"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p46"
  - "sources/verification/reqs.json#BR-LMS-101"
  - "sources/verification/verification_report.md#BR-LMS-101"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-101"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-101"
related: [concept.BR-LMS-101, brd_section.7.1, glossary.demand, lifecycle.ACTIVE]
version: 1
status: approved
approved_by: Owner
---
**In short:** Covered. The Loan form links the schedule, bills, payments, security, adjustments, logs and accounting records. Accounting entries are reached through the ledger rather than the form.

## Business need

The bank wants every funded loan to have one retrievable record holding the borrower, product, terms, balances, schedule, demands, postings, classification and history (BR-LMS-101, BRD 7.1, PDF page 46). See `concept.BR-LMS-101`.

## Frappe Lending today

The **Loan** form carries the borrower, product, terms and balances, and its Connections panel groups the linked records (`loan_dashboard.py`). The groups are: Schedule & Disbursement (repayment schedule, disbursement, demand); Repayment (repayment, interest accrual, refund, repayment repost); Security (assignment, shortfall, deposit, release); Adjustments (restructure, write off, adjustment, balance adjustment); Logs (days past due, NPA, freeze, limit change); and Accounting (Journal Entry, Sales Invoice).

## Match or gap, and why

This is **covered**. In the test, the Connections panel of a booked loan showed those groups (verification_report.md:104). One detail: the General Ledger entries are not a link on the form; they are reached through the ledger view. The coverage analysis says the panel links GL entries, which verification did not find.

A caveat from the restructure test (verification_report.md:563-570): after a restructure the Loan form's own totals restart (the Total Principal Paid and Total Amount Paid showed 0 and Loan Amount showed the new principal), but every record stays linked and the full payment history remains in Loan Repayment. The Loan Statement of Account was wrong after a restructure (DEF-25). The verdict stays covered with that caveat.

## What to do today

Start from the Loan form and use its Connections panel. For ledger entries, open the General Ledger report filtered on the loan. After a restructure, read the totals from the Loan Restructure record and Loan Repayment, not from the Loan form alone.

## Planned fix

Nothing is planned for the linking itself. The statement fault after a restructure is logged as DEF-25 in the verification report.
