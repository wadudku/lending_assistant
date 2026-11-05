---
id: devitem.D6
type: devitem
title: "D6 Schedule versions, triggers and what-if"
summary: "A planned add-on to Frappe Lending that links each repayment plan to the one that replaced it, records what triggered the change, and shows a what-if view without saving anything."
br_ids: [BR-LMS-124, BR-LMS-125, BR-LMS-126]
brd_section: 7.3
doctypes: [Loan Repayment Schedule, Loan Restructure]
dev_items: [D6]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D6"
  - "sources/verification/FINAL_REPORT.md#D6"
  - "sources/verification/reqs.json#BR-LMS-124"
  - "sources/verification/reqs.json#BR-LMS-125"
  - "sources/verification/reqs.json#BR-LMS-126"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-124"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-125"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-126"
  - "sources/verification/verification_report.md#BR-LMS-126"
  - "sources/verification/FINAL_REPORT.md#revised-suggested-order"
related: []
version: 1
status: approved
approved_by: Owner
---
**In short:** A planned add-on to Frappe Lending that links each repayment plan to the one that replaced it, records what triggered the change, and shows a what-if view without saving anything.

## What we plan to build

D6 adds custom fields on the Loan Repayment Schedule: a version number, a link to the plan that replaced it, the trigger of the change and the trigger document. A Simulate button runs the restructure calculation without saving a record. It is built in a custom app.

## The gap it closes

BR-LMS-124 asks for a what-if view with nothing saved, BR-LMS-125 asks that an old plan is never overwritten and BR-LMS-126 asks that only an approved change may rebuild a plan. In the test, the draft restructure shows one option but leaves draft records behind. There is no direct link between versions, and the trigger is not stored for every path. Nothing stops a schedule being submitted without an approved event: a draft restructure's schedule could be submitted on its own, and a free schedule could be submitted as a second Active plan. BR-LMS-126 moved from partly covered to gap in verification.

## Requirements it closes

BR-LMS-124 and BR-LMS-125 (partly covered) and BR-LMS-126 (gap).

## How, size and dependencies

Size: S to M in the analysis, now M. The Simulate part shrinks, because a draft restructure and a draft Pre Payment or Advance Payment already show a what-if. Verification added ND-19 (one Active schedule, and an approved parent event) and ND-20 (the restructure fixes for DEF-17, DEF-18 and DEF-19). The final report places D6 in step 3, schedule and regulatory.
