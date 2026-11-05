---
id: brd_section.7.1
type: brd_section
title: BRD 7.1 Funded-loan handoff and booking
summary: "Section 7.1 says the LMS starts only from a loan that is confirmed paid out, and that it keeps one complete record for each such loan."
br_ids: []
brd_section: 7.1
doctypes: []
dev_items: [D1, D2, D3]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#7.1"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p46"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#7.1-funded-loan-handoff-and-booking"
  - "sources/NRB_LMS_Requirements_Plain_English.md#7.1-funded-loan-handoff-and-booking"
  - "sources/verification/reqs.json#BR-LMS-100"
related: [devitem.D1, devitem.D2, devitem.D3, lifecycle.BOOKED, lifecycle.ACTIVE, lifecycle.PARTIALLY_DISBURSED, glossary.los]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 7.1 says the LMS starts only from a loan that is confirmed paid out, and that it keeps one complete record for each such loan.

## What this section says

BRD 7.1 (PDF page 46, 7 requirements, BR-LMS-100 to BR-LMS-106) covers the start of servicing. The LMS accepts only a confirmed funded loan with its approved terms, a disbursement reference and the origination audit data (100). It keeps one retrievable record for each loan (101). The loan runs from booked through active, including partially disbursed where a tranche product applies, to closure requested and then closed, settled or written off (102). Rules come from the product, not the loan (103). A sanctioned limit is tracked apart from the amount funded (104). An existing loan position can be migrated with its balances, and imported totals must reconcile before the loans go live (105). Each loan has a reporting category (106).

## Why the bank wants it

The BRD doesn't say why; the usual reason is a servicing record is only as good as its starting point, so the section lets in only loans confirmed as paid out. BR-LMS-102 states the same idea in one line: servicing ownership begins only after confirmed funding (PDF page 46).

## How it meets Frappe Lending

Of the 7 requirements, the verified result on 16.5.1 is 5 covered (101, 102, 103, 104, 106); 2 partly covered (100, 105). Verification confirmed every verdict from the analysis. Dev items: D1 (handoff intake), D2 (status and log) and D3 (migration control gate).

## Related cards

Dev items: `devitem.D1`, `devitem.D2` and `devitem.D3`. Loan states: `lifecycle.BOOKED`, `lifecycle.ACTIVE`, `lifecycle.PARTIALLY_DISBURSED`. Terms: `glossary.cbs`, `glossary.los`.
