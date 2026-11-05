---
id: bridge.BR-LMS-187
type: bridge
title: Track a security deposit
summary: "Covered. A Loan Security Deposit is created at disbursement, used by a repayment type and paid back through a Loan Refund. A Loan Closure repayment does not touch it, and the deposit is a per-disbursement tick, not a product setting."
br_ids: [BR-LMS-187]
brd_section: 7.9
doctypes: [Loan Security Deposit, Loan Disbursement, Loan Repayment, Loan Refund]
verdict: covered
analysis_status: verified
dev_items: []
fields: [Loan Disbursement.Withhold Security Deposit, Loan Refund.Is Security Amount Refund]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_disbursement/loan_disbursement.py:375-386", "lending/loan_management/doctype/loan_repayment/loan_repayment.py:916-930"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-187"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p53"
  - "sources/verification/reqs.json#BR-LMS-187"
  - "sources/verification/verification_report.md#BR-LMS-187"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-187"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-187"
related: [concept.BR-LMS-187, bridge.BR-LMS-186]
version: 1
status: approved
approved_by: Owner
---
**In short:** Covered. A Loan Security Deposit is created at disbursement, used by a repayment type and paid back through a Loan Refund. A Loan Closure repayment does not touch it, and the deposit is a per-disbursement tick, not a product setting.

## Business need

Where a product takes a security deposit, the platform must track its receipt, allocation, remaining availability and refund (BR-LMS-187 in section 7.9, BRD PDF page 53). See `concept.BR-LMS-187`.

## Frappe Lending today

A **Loan Disbursement** has a tick **Withhold Security Deposit**. When it is ticked, the disbursement creates a **Loan Security Deposit** for the loan with a deposit amount and an available amount both equal to the monthly repayment amount, which is one EMI (`lending/loan_management/doctype/loan_disbursement/loan_disbursement.py:375-386`). The record holds the deposit, allocated, refunded and available amounts and their dates. A **Loan Repayment** of type Security Deposit Adjustment uses the deposit to pay what is due: the amount cannot exceed the available deposit (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:916-930`), and the available amount falls and the allocated amount rises (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:1594-1608`). A **Loan Refund** with Is Security Amount Refund paid back the rest and cannot exceed the available amount (`lending/loan_management/doctype/loan_refund/loan_refund.py:95-99`). In the test, a loan disbursed with the tick got a deposit of 10,413.00 (one EMI), and a refund of 10,413.00 set the available amount to 0 and the refunded amount to 10,413, with the entry posted to the Borrower Security Deposit account.

## Match or gap, and why

This is **covered**, with these points from the test (J9).

- An early Loan Closure did not touch the deposit: it was still available (10,413) right after closing. Someone must remember to refund it.
- The tick is on the disbursement. The Loan Product and the Loan have no such field, so the BRD's "where a product takes a deposit" is a choice made at each disbursement.
- The amount is fixed by the code at one EMI.

## What to do today

Tick Withhold Security Deposit at disbursement for products that take one. At closure, refund what is left with a Loan Refund and Is Security Amount Refund ticked.

## Planned fix

No development item is assigned.
