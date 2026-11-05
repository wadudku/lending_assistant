---
id: bridge.BR-LMS-144
type: bridge
title: Stop counting interest as income on bad loans
summary: "Covered. When a loan becomes NPA, the unpaid interest and charges move to suspense. Catch-up runs move too little."
br_ids: [BR-LMS-144]
brd_section: 7.5
doctypes: [Loan, Journal Entry]
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan/loan.py:1610", "lending/loan_management/doctype/loan/loan.py:1625"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-144"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p49"
  - "sources/verification/reqs.json#BR-LMS-144"
  - "sources/verification/verification_report.md#BR-LMS-144"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-144"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-144"
related: [concept.BR-LMS-144, brd_section.7.5, glossary.npa, glossary.income-suspense, lifecycle.NPA, decision.write-off]
version: 1
status: approved
approved_by: Owner
---
**In short:** Covered. When a loan becomes NPA, the unpaid interest and charges move to suspense. Catch-up runs move too little.

## Business need

The bank wants unpaid interest and charges moved to suspense when a loan becomes non-performing, as Bangladesh Bank rules require (BR-LMS-144, BRD 7.5, PDF page 49). See `concept.BR-LMS-144`.

## Frappe Lending today

When classification marks a loan NPA, the code calls `move_unpaid_interest_to_suspense_ledger` and `move_receivable_charges_to_suspense_ledger` for the loan (`loan.py` lines 1610-1611), and for the borrower's other active loans that were not yet NPA (`loan.py` lines 1625-1626). The step is described in `lifecycle.NPA`.

## Match or gap, and why

This is **covered**, with a caveat. In the test, one classification run on the day (days past due 91) moved 2,052.44 to suspense: the billed unpaid interest of 1,627.88 plus the accrued unbilled 424.56, and each later daily accrual was moved by its own entry (verification_report.md:328). The caveat is catch-up processing. In the test of a back-dated loan, the NPA run dated in the past moved only the unbilled 424.56, because the billed interest was posted on a later date (DEF-9). In the test, the penal "additional interest" had no real suspense account on the site's product, and the penalty line was negative (DEF-10). Whether the treatment matches Bangladesh Bank's rules was not tested; the analysis says to confirm that the rules match the configuration.

## What to do today

Run classification on the business date, not back-dated. After a catch-up run, check the suspense balance against the unpaid interest. Ask NRB to confirm the treatment against the Bangladesh Bank rules.

## Planned fix

DEF-9 is logged in the verification report, to be fixed with the general-ledger date issue (ND-12). This row has no D item.
