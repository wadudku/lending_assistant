---
id: devitem.D20
type: devitem
title: D20 Small items
summary: "Three small planned add-ons to Frappe Lending: a tracked remedy for a collateral shortfall, a per-payment choice between a lower EMI and a shorter tenor, and a closure letter with a notification. Verification made two of them larger."
br_ids: [BR-LMS-173, BR-LMS-181, BR-LMS-235]
brd_section: 7.8
doctypes: [Loan Security Shortfall, Loan]
dev_items: [D20]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D20"
  - "sources/verification/FINAL_REPORT.md#D20"
  - "sources/verification/reqs.json#BR-LMS-173"
  - "sources/verification/reqs.json#BR-LMS-181"
  - "sources/verification/reqs.json#BR-LMS-235"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-173"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-181"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-235"
  - "sources/verification/FINAL_REPORT.md#revised-suggested-order"
related: []
version: 2
status: approved
approved_by: Owner
---
**In short:** Three small planned add-ons to Frappe Lending: a tracked remedy for a collateral shortfall, a per-payment choice between a lower EMI and a shorter tenor, and a closure letter with a notification. Verification made two of them larger.

## What we plan to build

D20 groups three items. First, a shortfall remedy type, owner and due date on the collateral shortfall record (BR-LMS-173). Second, a per-payment choice between keeping the EMI and shortening the tenor, or the other way round, on a Pre Payment (BR-LMS-181). Third, a closure letter print format and a notification (BR-LMS-235). It is built in a custom app.

## The gap it closes

In the test, a shortfall had no remedy type, owner, due date or approved exception, and applicant-wise shortfall records did not close (BR-LMS-173). In the test, a Pre Payment had no choice of EMI or tenor: it always kept the EMI and shortened the loan, and the product setting is used only by Advance Payment, where it is ignored (DEF-21) (BR-LMS-181). There was no closure letter print format and no closure notification set up (BR-LMS-235).

## Requirements it closes

BR-LMS-173, BR-LMS-181 and BR-LMS-235, all verified as partly covered.

## How, size and dependencies

Size: S each in the analysis. The final report resizes them: the shortfall workflow (BR-LMS-173) is M (ND-28), the EMI-or-tenor choice with the DEF-21 fix (BR-LMS-181) is M (ND-21), and the closure letter and notification (BR-LMS-235) stay S (ND-37). The remainder of D20 is in the last group.
