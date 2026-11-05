---
id: devitem.D16
type: devitem
title: D16 Bangladesh Bank treatment
summary: "A planned add-on to Frappe Lending that records how Bangladesh Bank classifies each restructure or reschedule and reports it, without re-ageing the loan. Verification made it larger."
br_ids: [BR-LMS-182, BR-LMS-188]
brd_section: 7.9
doctypes: [Loan Restructure, Loan]
dev_items: [D16]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D16"
  - "sources/verification/FINAL_REPORT.md#D16"
  - "sources/verification/reqs.json#BR-LMS-182"
  - "sources/verification/reqs.json#BR-LMS-188"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-182"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-188"
  - "sources/verification/verification_report.md#BR-LMS-182"
  - "sources/NRB_LMS_Team_Discussion_Summary.md#4.-proposed-development-custom-app-no-core-changes"
  - "sources/verification/FINAL_REPORT.md#revised-suggested-order"
related: [lifecycle.NPA]
version: 1
status: approved
approved_by: Owner
---
**In short:** A planned add-on to Frappe Lending that records how Bangladesh Bank classifies each restructure or reschedule and reports it, without re-ageing the loan. Verification made it larger.

## What we plan to build

D16 adds custom fields on the Loan Restructure for the Bangladesh Bank category (reschedule, restructure, one-time exit and similar) and the regulatory treatment applied. It adds a Bangladesh Bank report on restructures, reschedules and waivers. It needs the list of Bangladesh Bank circulars from NRB. It is built in a custom app.

## The gap it closes

BR-LMS-182 asks for restructuring with the restructure type recorded, and BR-LMS-188 asks that a restructure, reschedule or waiver is reported to Bangladesh Bank and flagged in the classification treatment. In the test, Frappe Lending offered Normal Restructure, Pre Payment and Advance Payment, with no reschedule-versus-restructure category, no regulatory-treatment field and no Bangladesh Bank report. A restructure of an overdue loan set days past due to 0, and on an NPA loan it sent the uncollected suspense interest to income and cleared the customer's NPA flag (DEF-22).

## Requirements it closes

BR-LMS-182 (partly covered) and BR-LMS-188 (gap).

## How, size and dependencies

Size: M in the analysis, now L. Verification says 16.5.1 re-ages arrears and moves suspense to income on a restructure (DEF-22), so D16 needs a Bangladesh Bank model that blocks re-ageing (ND-22). The team summary lists the circular list as an open item for D16. See `decision.restructure`. The final report places D16 in step 3, schedule and regulatory.
