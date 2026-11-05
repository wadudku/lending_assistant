---
id: bridge.BR-LMS-134
type: bridge
title: Send bills to the CBS and keep its journal number
summary: "Gap (needs the CBS link). 16.5.1 has no code that sends bills to the CBS, and no field holds a CBS journal number."
br_ids: [BR-LMS-134]
brd_section: 7.4
doctypes: [Loan Demand, Loan Repayment, Loan Interest Accrual]
verdict: gap_cbs
analysis_status: verified
dev_items: [D13]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-134"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p48"
  - "sources/verification/reqs.json#BR-LMS-134"
  - "sources/verification/verification_report.md#BR-LMS-134"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-134"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-134"
related: [concept.BR-LMS-134, brd_section.7.4, devitem.D13, bridge.BR-LMS-115, glossary.cbs, glossary.rpa]
version: 1
status: approved
approved_by: Owner
---
**In short:** Gap (needs the CBS link). 16.5.1 has no code that sends bills to the CBS, and no field holds a CBS journal number.

## Business need

Where the CBS owns the ledger, the bank wants each demand and its accounting effect sent to it, and the returned journal reference kept against the loan (BR-LMS-134, BRD 7.4, PDF page 48). See `concept.BR-LMS-134`.

## Frappe Lending today

Frappe Lending has no connection to the CBS. A search of the installed 16.5.1 code (Python, JSON and JavaScript, outside tests) for CBS, core banking and RPA finds no match. Its journal links are internal only: Journal Entry links on the Loan Interest Accrual (**Normal Interest Journal Entry**, `loan_interest_accrual.json` line 272, and the additional-interest suspense entry), and links to the batch **Process Loan Accounting** run (`process_loan_accounting_voucher` on the Loan Demand, `loan_demand.json` line 314, and on the Loan Interest Accrual). A read of every Link field of `loan_demand.json` and `loan_interest_accrual.json` finds none that holds a CBS reference.

## Match or gap, and why

This is a **gap (needs the CBS link)**, so it cannot be closed inside Frappe Lending. In the test, a check of Loan Demand, Loan Repayment, Loan Write Off, Loan Disbursement, Loan Restructure and Loan Repayment Detail found no field for a CBS journal or posting reference, and no custom field with "cbs" or "journal" (verification_report.md:189). The Reference Number and Reference Date on a repayment belong to the payment, not to a CBS journal. The coverage analysis rated it a gap that needs the CBS link, and verification confirmed that.

## What to do today

Keep the CBS journal numbers in a register outside Frappe Lending until the link exists.

## Planned fix

Dev item D13 (`devitem.D13`) builds the outbox that sends entries to the CBS through a robot and writes back the CBS journal number.
