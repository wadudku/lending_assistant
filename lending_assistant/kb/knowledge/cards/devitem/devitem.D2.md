---
id: devitem.D2
type: devitem
title: D2 Servicing status and log
summary: "A planned add-on to Frappe Lending that gives each loan one BRD servicing status and keeps a log of every change, without touching Frappe's own status field."
br_ids: [BR-LMS-001, BR-LMS-002, BR-LMS-003, BR-LMS-102]
brd_section: 5.3
doctypes: [Loan]
dev_items: [D2]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D2"
  - "sources/verification/FINAL_REPORT.md#D2"
  - "sources/verification/reqs.json#BR-LMS-102"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-001"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-002"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-003"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#5.3"
  - "sources/verification/verification_report.md#BR-LMS-102"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#5.2-the-main-difference"
  - "sources/verification/FINAL_REPORT.md#revised-suggested-order"
related: [lifecycle.OVERDUE, lifecycle.NPA, brd_section.5.3, devitem.D12]
version: 1
status: approved
approved_by: Owner
---
**In short:** A planned add-on to Frappe Lending that gives each loan one BRD servicing status and keeps a log of every change, without touching Frappe's own status field.

## What we plan to build

D2 adds a separate Servicing Status field on the loan with the BRD's 12 values, set by hooks on the Loan, classification, freeze, restructure and write-off events. Each change is written to a Servicing Status Log with the date, the reason and the source document. Frappe's own status field is left alone, because Frappe Lending's code depends on its values. The coverage analysis proposes a fixed priority order to pick the one status when several apply (a design proposal, not a BRD rule): WRITTEN_OFF, SETTLED, CLOSED, CLOSURE_REQUESTED, FROZEN, NPA, SMA, RESTRUCTURED while in its watch period, OVERDUE, PARTIALLY_DISBURSED, ACTIVE, BOOKED. Because the field is ours, renaming the values later is safe.

## The gap it closes

BR-LMS-001 asks for exactly one current servicing status per loan, with the full history of earlier statuses. In Frappe Lending 16.5.1 a loan can be Disbursed, NPA, frozen and restructured at once, and the names differ from the BRD (Sanctioned against BOOKED). In the test there was no status history: the Version log recorded only Draft to Sanctioned, because later statuses are written with db_set.

## Requirements it closes

BR-LMS-102 (the stages of a loan's life), verified as covered with the history caveat above. The coverage analysis also links BR-LMS-001, BR-LMS-002 (a status change never deletes or overwrites earlier records) and BR-LMS-003 (names aligned with the Bank's own vocabulary). Those three are in BRD 5.3, outside the 103 analysed rows, so they carry no verified verdict. See `lifecycle.OVERDUE` and `lifecycle.NPA` for two of the states.

## How, size and dependencies

Size: M (one to three weeks), unchanged by verification. Verification added ND-3, a loan status history log, and noted that the log must hook the code paths that use db_set. The analysis puts D2 in the first group to build, with D1, D8 and D12; the final report keeps it in the foundation pack (Pack B).
