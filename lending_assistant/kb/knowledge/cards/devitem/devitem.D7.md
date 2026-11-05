---
id: devitem.D7
type: devitem
title: D7 Dues as on a date
summary: "A planned extension of Frappe Lending's existing outstanding report so that staff can see what a borrower owed on a chosen date, by component. Verification made it smaller than first planned."
br_ids: [BR-LMS-132]
brd_section: 7.4
doctypes: [Loan]
dev_items: [D7]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D7"
  - "sources/verification/FINAL_REPORT.md#D7"
  - "sources/verification/reqs.json#BR-LMS-132"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-132"
  - "sources/verification/verification_report.md#BR-LMS-132"
  - "sources/verification/FINAL_REPORT.md#revised-suggested-order"
related: []
version: 1
status: approved
approved_by: Owner
---
**In short:** A planned extension of Frappe Lending's existing outstanding report so that staff can see what a borrower owed on a chosen date, by component. Verification made it smaller than first planned.

## What we plan to build

The analysis proposed a button on the Loan and a script report that calls the existing dues API. Verification replaced the new screen with an extension of the Loan Outstanding Report, which already has an As On Date filter: add the penalty and charges columns and the as-at-date days past due (ND-8, owed as at a date).

## The gap it closes

BR-LMS-132 asks for a view of what is owed on a given date. In the test, the report had no penalty or charges columns and showed the current days past due and instalment counts instead of values as at the date, and there was no single staff screen of the amount owed on date X by component.

## Requirements it closes

BR-LMS-132 (verified partly covered).

## How, size and dependencies

Size: S in the analysis; the final report calls it S, smaller, because the new screen drops out. The final report puts D7 (with ND-8) in its last group, with Pack G, D10 and the rest of D20.
