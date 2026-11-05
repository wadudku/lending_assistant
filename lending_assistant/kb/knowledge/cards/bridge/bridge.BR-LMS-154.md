---
id: bridge.BR-LMS-154
type: bridge
title: A practice run first
summary: Gap. There is no batch dry run; a single loan can only be previewed through a draft Loan Restructure.
br_ids: [BR-LMS-154]
brd_section: 7.6
doctypes: [Loan Restructure]
verdict: gap
analysis_status: verified
dev_items: [D11]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-154"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p50"
  - "sources/verification/reqs.json#BR-LMS-154"
  - "sources/verification/verification_report.md#BR-LMS-154"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-154"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-154"
related: [concept.BR-LMS-154, brd_section.7.6, devitem.D11, bridge.BR-LMS-124]
version: 1
status: approved
approved_by: Owner
---
**In short:** Gap. There is no batch dry run; a single loan can only be previewed through a draft Loan Restructure.

## Business need

The bank wants a dry run before a repricing batch, with per-loan results and exclusions (BR-LMS-154, BRD 7.6, PDF page 50). See `concept.BR-LMS-154`.

## Frappe Lending today

For one loan, a draft **Loan Restructure** builds a draft schedule that can be read before approval (see `bridge.BR-LMS-124`).

## Match or gap, and why

This is a **gap**. In the test, there was no batch dry run; per loan there was only a draft restructure, which leaves draft records behind (verification_report.md, BR-LMS-154, J5). The coverage analysis rated it a gap, and verification confirmed that.

## What to do today

Preview each loan with a draft restructure, then delete the drafts. Keep the list of excluded loans and reasons outside the system.

## Planned fix

Dev item D11 (`devitem.D11`) adds a repricing run for floating-rate loans, with selection, effective date, a dry run, maker-checker, new schedule versions and a restartable batch.
