---
id: bridge.BR-LMS-156
type: bridge
title: Each repriced loan gets a new plan version
summary: "Partly covered. For one loan the old plan is kept and the new one is linked to its restructure, but not for a bulk run, and the old plan has no link forward."
br_ids: [BR-LMS-156]
brd_section: 7.6
doctypes: [Loan Repayment Schedule, Loan Restructure]
verdict: partial
analysis_status: verified
dev_items: [D11]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_restructure/loan_restructure.py:599"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-156"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p50"
  - "sources/verification/reqs.json#BR-LMS-156"
  - "sources/verification/verification_report.md#BR-LMS-156"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-156"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-156"
related: [concept.BR-LMS-156, brd_section.7.6, devitem.D11, bridge.BR-LMS-125, glossary.schedule-version]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. For one loan the old plan is kept and the new one is linked to its restructure, but not for a bulk run, and the old plan has no link forward.

## Business need

The bank wants each repriced loan to get a new schedule version with the earlier version kept and related (BR-LMS-156, BRD 7.6, PDF page 50). See `concept.BR-LMS-156`.

## Frappe Lending today

A **Loan Restructure** marks the old **Loan Repayment Schedule** as Restructured and creates a new Active one linked to the restructure (`loan_restructure.py` lines 599-602). The forward link from the old plan is covered in `bridge.BR-LMS-125`.

## Match or gap, and why

This is **partly covered**. In the test, a restructure left the 14% plan as Restructured and made a 15% plan Active, linked to the restructure, for that one loan (verification_report.md, BR-LMS-156, J5). There is no bulk run to carry the relationship. The coverage analysis rated it partly covered, and verification confirmed that.

## What to do today

Reprice loans one by one and read the chain of plans by loan and status.

## Planned fix

Dev item D11 (`devitem.D11`) adds a repricing run for floating-rate loans, with selection, effective date, a dry run, maker-checker, new schedule versions and a restartable batch.
