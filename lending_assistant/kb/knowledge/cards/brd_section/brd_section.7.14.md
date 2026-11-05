---
id: brd_section.7.14
type: brd_section
title: BRD 7.14 Closure
summary: "Section 7.14 says a loan closes only after its balances are cleared, the CBS agrees, collateral is released and an authorised user has approved."
br_ids: []
brd_section: 7.14
doctypes: []
dev_items: [D8, D13, D20]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#7.14"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p55"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p56"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#7.14-closure"
  - "sources/NRB_LMS_Requirements_Plain_English.md#7.14-closure"
  - "sources/verification/reqs.json#BR-LMS-230"
related: [devitem.D8, devitem.D13, devitem.D20, lifecycle.CLOSURE_REQUESTED, lifecycle.CLOSED, lifecycle.SETTLED, glossary.cbs]
version: 2
status: approved
approved_by: Owner
---
**In short:** Section 7.14 says a loan closes only after its balances are cleared, the CBS agrees, collateral is released and an authorised user has approved.

## What this section says

BRD 7.14 (PDF pages 55 and 56, 6 requirements, BR-LMS-230 to BR-LMS-235) has the platform check that principal, interest, penalty, charges and every tracked receivable are cleared or formally resolved, and state any item that blocks closure (230). Where the CBS owns the books, the CBS account and ledger position are verified first (231). Eligible collateral is released after approval and the release is recorded (232). Any remaining security deposit or excess payment is refunded with its external reference (233). Closure follows an authorised workflow from closure requested to closed, with the user and time kept (234). On closure the platform produces a closure confirmation and a final statement and notifies the borrower (235).

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the bank wants to be sure nothing is still owed before it closes the books on the loan. BR-LMS-234 states the approval requirement (PDF page 56).

## How it meets Frappe Lending

Of the 6 requirements, the verified result on 16.5.1 is 1 covered (233); 4 partly covered (230, 232, 234, 235); 1 a gap that needs the CBS link (231). Verification moved 2 of these verdicts: 230, 232. Dev items: D8 (approval and audit pack), D13 (the CBS and RPA posting bridge) and D20 (small items).

## Related cards

Dev items: `devitem.D8`, `devitem.D13`, `devitem.D20`. States: `lifecycle.CLOSURE_REQUESTED`, `lifecycle.CLOSED`, `lifecycle.SETTLED`. Terms: `glossary.cbs`.
