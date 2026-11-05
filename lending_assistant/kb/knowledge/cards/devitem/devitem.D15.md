---
id: devitem.D15
type: devitem
title: D15 Classification history and override
summary: A planned add-on to Frappe Lending that records each change of a loan's grade and lets a named person override the grade with a reason and an approver. Verification made it larger.
br_ids: [BR-LMS-191, BR-LMS-192]
brd_section: 7.10
doctypes: [Loan, Loan NPA Log, Days Past Due Log, Loan Classification]
dev_items: [D15]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D15"
  - "sources/verification/FINAL_REPORT.md#D15"
  - "sources/verification/reqs.json#BR-LMS-191"
  - "sources/verification/reqs.json#BR-LMS-192"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-191"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-192"
  - "sources/verification/verification_report.md#BR-LMS-191"
  - "sources/NRB_LMS_Team_Discussion_Summary.md#4.-proposed-development-custom-app-no-core-changes"
related: [lifecycle.NPA, glossary.dpd]
version: 1
status: approved
approved_by: Owner
---
**In short:** A planned add-on to Frappe Lending that records each change of a loan's grade and lets a named person override the grade with a reason and an approver. Verification made it larger.

## What we plan to build

D15 adds a Loan Classification History record written on each class change, and a submittable Classification Override with a reason and an approver, which the daily classification run respects. It is built in a custom app.

## The gap it closes

BR-LMS-191 asks for a grade from DPD bands plus a qualitative override with a reason and an approver, and BR-LMS-192 asks for a history of grade changes. In the test, the only override is the Manual NPA tick, which is yes or no with no reason or approver, and the grade itself cannot be overridden. The grade and the NPA flag can disagree (DEF-7), and removing a manual NPA does not reverse its suspense (DEF-13). The grade changes leave no history: the grade is written without a Version record, only NPA in and out is logged, and the NPA and DPD logs could be edited or deleted without trace.

## Requirements it closes

BR-LMS-191 and BR-LMS-192, both verified as partly covered. See `decision.override`, `lifecycle.NPA` and `glossary.dpd`.

## How, size and dependencies

Size: S to M in the analysis, now M. Verification added ND-14 and ND-15 (NPA and suspense integrity, grade history, append-only logs, override with a reason) and the defects DEF-7, DEF-9, DEF-13 and DEF-15. The team summary puts D15 in its fourth phase, completion.
