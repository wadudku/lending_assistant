---
id: bridge.BR-LMS-160
type: bridge
title: Record a confirmed payment with full details
summary: Covered. The Loan Repayment form has a field for every item the BRD lists. The one limit is that Posting Date is always set by the system.
br_ids: [BR-LMS-160]
brd_section: 7.7
doctypes: [Loan Repayment]
verdict: covered
analysis_status: verified
dev_items: []
fields: [Loan Repayment.Mode Of Payment, Loan Repayment.Reference Number, Loan Repayment.Reference Date, Loan Repayment.Amount Paid, Loan Repayment.Value Date, Loan Repayment.Posting Date]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_repayment/loan_repayment.py:120"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-160"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p50"
  - "sources/verification/reqs.json#BR-LMS-160"
  - "sources/verification/verification_report.md#BR-LMS-160"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-160"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-160"
related: [concept.BR-LMS-160, bridge.BR-LMS-162, devitem.D12, screen.loan_repayment]
version: 1
status: approved
approved_by: Owner
---
**In short:** Covered. The Loan Repayment form has a field for every item the BRD lists. The one limit is that Posting Date is always set by the system.

## Business need

The bank must be able to trace every payment to a CBS transaction and see both the date the money arrived and the date it was recorded (BR-LMS-160, BRD 7.7.1, PDF page 50). See `concept.BR-LMS-160` for the plain-words version.

## Frappe Lending today

The **Loan Repayment** document holds **Mode Of Payment** (the channel), **Reference Number** and **Reference Date** (the CBS reference), **Amount Paid**, **Value Date** and **Posting Date**. The team checked the field list on the running 16.5.1 site and used it to enter repayments.

## Match or gap, and why

This is **covered**. Every item the BRD names has a field. The BRD defines the posting date as the date an entry is recorded (BRD 1.5), and Frappe Lending sets it to the moment of entry.

One thing to know: **Posting Date** cannot be chosen. `loan_repayment.py` line 120 sets it to the current time whenever the document is validated (only a Data Import skips this), so only Value Date is typed by the user. The accounting entries of the repayment carry that posting date, which is the day of entry and not the value date. For month-end reports this matters, and the verification logged it as a separate development need (ND-12).

## What to do today

Type the real arrival day in **Value Date**, the CBS transaction number in **Reference Number**, and pick the **Mode Of Payment**. Do not try to back-date Posting Date. Check the reference by eye, because the system does not check it for duplicates (see `bridge.BR-LMS-162`).

## Planned fix

Nothing is needed for the fields themselves. The accounting-date issue is tracked as ND-12 in the verification report. The reference checks belong to D12 (`devitem.D12`).
