---
id: devitem.D3
type: devitem
title: D3 Migration control gate
summary: A planned add-on to Frappe Lending that checks the totals of an imported loan book against the old system and holds the loans out of daily processing until someone signs off. Verification made it larger.
br_ids: [BR-LMS-105, BR-GOV-031]
brd_section: 7.1
doctypes: [Loan]
dev_items: [D3]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D3"
  - "sources/verification/FINAL_REPORT.md#D3"
  - "sources/verification/reqs.json#BR-LMS-105"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-105"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-031"
  - "sources/verification/verification_report.md#BR-LMS-105"
  - "sources/verification/FINAL_REPORT.md#revised-suggested-order"
related: [howto.data_import.migrate_loan]
version: 1
status: approved
approved_by: Owner
---
**In short:** A planned add-on to Frappe Lending that checks the totals of an imported loan book against the old system and holds the loans out of daily processing until someone signs off. Verification made it larger.

## What we plan to build

D3 adds a Migration Batch record that holds the source control totals next to the imported totals, shows the difference, and needs a maker-checker sign-off. A hold flag keeps imported loans out of the daily processes until the batch is signed off. It is built in a custom app.

## The gap it closes

BR-LMS-105 asks to bring existing loans over and prove the totals match. In the test, no control-total check exists (an opening principal larger than the disbursed amount was accepted) and no sign-off gate stands before migrated loans become active. Repayment history is not imported. Verification also found the migration mapping itself wrong in 16.5.1 and in develop (DEF-6): opening principal outstanding is billed as one overdue demand on the migration date while later schedule rows still carry principal.

## Requirements it closes

BR-LMS-105 (verified partly covered). The coverage analysis also links BR-GOV-031.

## How, size and dependencies

Size: M in the analysis, now L. Verification says migration cannot go live on the standard code (DEF-6), so D3 needs a defined mapping and a patch of the opening-balance logic (ND-4, migration control totals and the opening principal check) before control totals mean anything. The final report places D3 with ND-4 in step 2, after the foundation pack, and groups ND-4 in Pack C (batch and migration).
