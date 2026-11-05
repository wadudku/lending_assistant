---
id: devitem.D18
type: devitem
title: D18 Settlement proposal
summary: "A planned add-on to Frappe Lending that records a settlement offer, shows its make-up before any money moves, and creates the settlement entries only after approval. Verification made it larger."
br_ids: [BR-LMS-200]
brd_section: 7.11
doctypes: [Loan Repayment, Loan Write Off]
dev_items: [D18]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D18"
  - "sources/verification/FINAL_REPORT.md#D18"
  - "sources/verification/reqs.json#BR-LMS-200"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-200"
  - "sources/verification/verification_report.md#BR-LMS-200"
  - "sources/verification/FINAL_REPORT.md#revised-suggested-order"
related: [decision.waiver]
version: 1
status: approved
approved_by: Owner
---
**In short:** A planned add-on to Frappe Lending that records a settlement offer, shows its make-up before any money moves, and creates the settlement entries only after approval. Verification made it larger.

## What we plan to build

D18 adds a Loan Settlement Proposal that shows principal, interest, penalty, charges and waivers. The proposal goes through approval, and on approval it creates the settlement repayment and the waivers. It is built in a custom app.

## The gap it closes

BR-LMS-200 asks to work out a settlement figure and show its make-up before approval. In the test there was no proposal record and nothing held for approval, and the proposed waivers were not shown before money moved. The posting also had defects: with the test products' settlement order the interest was skipped (DEF-3), a Full Settlement that clears all the principal left the loan flagged NPA with its suspense (DEF-33), and an unbooked interest demand was left open (DEF-34).

## Requirements it closes

BR-LMS-200 (verified partly covered). See `decision.settlement` and `decision.waiver`.

## How, size and dependencies

Size: S to M in the analysis, now M. The posting fixes are added to the item: the settlement order, unbooked interest and the release of suspense (ND-32, ND-33 and ND-38). D18 sits with the settlement, write-off and closure controls in step 4 of the final report, controls round 2.
