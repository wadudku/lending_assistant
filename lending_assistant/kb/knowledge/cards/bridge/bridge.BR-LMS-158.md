---
id: bridge.BR-LMS-158
type: bridge
title: "Skip loans that shouldn't be repriced, automatically"
summary: "Gap. There is no batch to skip loans from, and a single restructure checks neither the rate type, nor the freeze, nor the loan status."
br_ids: [BR-LMS-158]
brd_section: 7.6
doctypes: [Loan Restructure]
verdict: gap
analysis_status: verified
dev_items: [D11]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_restructure/loan_restructure.py:108"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-158"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p50"
  - "sources/verification/reqs.json#BR-LMS-158"
  - "sources/verification/verification_report.md#BR-LMS-158"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-158"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-158"
related: [concept.BR-LMS-158, brd_section.7.6, devitem.D11, decision.freeze, bridge.BR-LMS-111]
version: 1
status: approved
approved_by: Owner
---
**In short:** Gap. There is no batch to skip loans from, and a single restructure checks neither the rate type, nor the freeze, nor the loan status.

## Business need

The bank wants ineligible loans excluded automatically with the reason recorded (BR-LMS-158, BRD 7.6, PDF page 50). See `concept.BR-LMS-158`.

## Frappe Lending today

A **Loan Restructure** refuses a second restructure while another is Initiated (`loan_restructure.py` lines 108-112). A search of `loan_restructure.py` for freeze, Frozen, floating and written finds no match. A loan cannot be marked fixed or floating (see `bridge.BR-LMS-111`).

## Match or gap, and why

This is a **gap**. In the test, there was no batch to skip loans from, and the restructure had no fixed or floating check and no freeze or status check (verification_report.md, BR-LMS-158, J5). The coverage analysis rated it a gap, and verification confirmed that.

## What to do today

Check each loan's status, freeze and rate type by hand before a restructure.

## Planned fix

Dev item D11 (`devitem.D11`) adds a repricing run for floating-rate loans, with selection, effective date, a dry run, maker-checker, new schedule versions and a restartable batch.
