---
id: bridge.BR-LMS-120
type: bridge
title: Build the first repayment plan
summary: "Covered. The repayment plan is built and submitted with the loan disbursement. In NRB's flow, booking and disbursement happen together, which D1 handles."
br_ids: [BR-LMS-120]
brd_section: 7.3
doctypes: [Loan Repayment Schedule, Loan Disbursement, Loan]
verdict: covered
analysis_status: verified
dev_items: [D1]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_disbursement/loan_disbursement.py:190"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-120"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p47"
  - "sources/verification/reqs.json#BR-LMS-120"
  - "sources/verification/verification_report.md#BR-LMS-120"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-120"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-120"
related: [concept.BR-LMS-120, brd_section.7.3, devitem.D1, lifecycle.BOOKED]
version: 1
status: approved
approved_by: Owner
---
**In short:** Covered. The repayment plan is built and submitted with the loan disbursement. In NRB's flow, booking and disbursement happen together, which D1 handles.

## Business need

The bank wants the first repayment plan built on booking, from the funded amount, rate, term, dates, frequency and any payment holiday (BR-LMS-120, BRD 7.3, PDF page 47). See `concept.BR-LMS-120`.

## Frappe Lending today

In Frappe Lending the plan is a **Loan Repayment Schedule**. For a term loan it is submitted when the **Loan Disbursement** is submitted (`loan_disbursement.py` line 190). The loan itself is booked earlier, so the plan appears at disbursement, not at booking.

## Match or gap, and why

This is **covered**. In the test, submitting a loan with auto-disbursement created the disbursement and a schedule with status Active and 12 rows in the same transaction (verification_report.md:96). The coverage analysis rated it covered, and verification confirmed that. The difference is timing: Frappe Lending books before the money moves, and NRB's loans arrive already funded, so booking and disbursement happen together. That is why the handoff intake (D1) creates both.

## What to do today

Tick **Auto create disbursement on loan booking** on the loan so the plan is built at once. Check the first row's dates against the origination record.

## Planned fix

Dev item D1 (`devitem.D1`) books the loan and its payout together. Verification added that the intake must also pass the repayment start date, because the schedule depends on it (DEF-5).
