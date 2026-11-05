---
id: bridge.BR-LMS-150
type: bridge
title: Choose which loans to reprice
summary: "Gap. There is no selection screen for repricing, and the bulk rate code found is a leftover class with no document type."
br_ids: [BR-LMS-150]
brd_section: 7.6
doctypes: [Loan Restructure]
verdict: gap
analysis_status: verified
dev_items: [D11]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/process_loan_interest_change/process_loan_interest_change.py:8"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-150"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p49"
  - "sources/verification/reqs.json#BR-LMS-150"
  - "sources/verification/verification_report.md#BR-LMS-150"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-150"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-150"
related: [concept.BR-LMS-150, brd_section.7.6, devitem.D11, bridge.BR-LMS-111, glossary.repricing]
version: 1
status: approved
approved_by: Owner
---
**In short:** Gap. There is no selection screen for repricing, and the bulk rate code found is a leftover class with no document type.

## Business need

The bank wants staff to select eligible loans for repricing by product, segment, branch or loan number (BR-LMS-150, BRD 7.6, PDF page 49). See `concept.BR-LMS-150`.

## Frappe Lending today

A **Loan Restructure** takes one loan. The folder process_loan_interest_change in 16.5.1 holds a Python class that updates the rate of the loans of a product or of a list (`process_loan_interest_change.py` lines 8-22), but the folder has no document type definition, so there is no form to use it.

## Match or gap, and why

This is a **gap**. In the test, no selection screen existed, and the existence check for the leftover document type returned nothing; the same leftover is in develop (verification_report.md, BR-LMS-150, J5). The leftover code does not check that a loan is floating (there is no such flag, see `bridge.BR-LMS-111`), and it overwrites the rate with no schedule rebuild. In the test, a Normal Restructure on the site's products crashed with a TypeError (DEF-17) and double-counted accrued interest (DEF-18). The coverage analysis rated it a gap, and verification confirmed that.

## What to do today

Reprice one loan at a time with a Loan Restructure, on a product that does not hit DEF-17, and list the loans by hand.

## Planned fix

Dev item D11 (`devitem.D11`) adds a repricing run for floating-rate loans, with selection, effective date, a dry run, maker-checker, new schedule versions and a restartable batch.
