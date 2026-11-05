---
id: bridge.BR-LMS-123
type: bridge
title: Keep a partner's plan for co-lent loans
summary: Covered. A co-lent loan's schedule carries the partner rate and share and a Co-Lender Schedule table with one row per instalment.
br_ids: [BR-LMS-123]
brd_section: 7.3
doctypes: [Loan Repayment Schedule, Co-Lender Schedule, Loan Partner]
verdict: covered
analysis_status: verified
dev_items: []
fields: [Loan Repayment Schedule.Partner Loan Share Percentage]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_repayment_schedule/loan_repayment_schedule.json:319", "lending/loan_management/doctype/loan_repayment_schedule/loan_repayment_schedule.py:101"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-123"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p48"
  - "sources/verification/reqs.json#BR-LMS-123"
  - "sources/verification/verification_report.md#BR-LMS-123"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-123"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-123"
related: [concept.BR-LMS-123, brd_section.7.3, bridge.BR-LMS-116, glossary.partner]
version: 1
status: approved
approved_by: Owner
---
**In short:** Covered. A co-lent loan's schedule carries the partner rate and share and a Co-Lender Schedule table with one row per instalment.

## Business need

The bank wants a partner schedule maintained next to the borrower schedule on a co-lent loan (BR-LMS-123, BRD 7.3, PDF page 48). See `concept.BR-LMS-123`.

## Frappe Lending today

The **Loan Repayment Schedule** has **Loan Partner**, **Loan Partner Rate Of Interest** and **Partner Loan Share Percentage** (`loan_repayment_schedule.json` lines 326-351) and a **Co-Lender Schedule** table (line 319). Each row of the table holds date, days, principal, interest, total and balance. The schedule's validate calls `make_co_lender_schedule` (`loan_repayment_schedule.py` line 101). The partner itself is set up as described in `bridge.BR-LMS-116`.

## Match or gap, and why

This is **covered**. In the test, a co-lent loan had a schedule with partner share 20%, partner rate 10 and a partner EMI of 1,759.00, plus a Co-Lender Schedule of 12 rows next to the 12 borrower rows (verification_report.md:775). Row 1 and the totals were hand-checked: the partner's principal was 20,000 and its interest 1,096.71 over 12 rows. The coverage analysis rated this row covered, and verification confirmed it live. The Loan Partner record is flagged beta in the file, which matters for readiness (see `bridge.BR-LMS-116`).

## What to do today

Link the partner on the product, book the loan, and read the partner plan from the Co-Lender Schedule table of the schedule.

## Planned fix

Nothing is needed for the schedule itself.
