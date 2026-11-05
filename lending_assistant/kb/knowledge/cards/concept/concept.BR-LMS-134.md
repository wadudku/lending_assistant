---
id: concept.BR-LMS-134
type: concept
title: Send bills to the CBS and keep its journal number
summary: "Where the CBS keeps the ledger, the loan system sends it each bill and its accounting effect, and keeps the CBS journal number against the loan."
br_ids: [BR-LMS-134]
brd_section: 7.4
doctypes: []
verdict: gap_cbs
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-134"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p48"
  - "sources/verification/reqs.json#BR-LMS-134"
  - "sources/verification/verification_report.md#BR-LMS-134"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-134"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-134"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
related: [bridge.BR-LMS-134, brd_section.7.4, devitem.D13, glossary.cbs, glossary.rpa]
version: 1
status: approved
approved_by: Owner
---
**In short:** Where the CBS keeps the ledger, the loan system sends it each bill and its accounting effect, and keeps the CBS journal number against the loan.

## What the rule says

BR-LMS-134 (priority Must, BRD 7.4, PDF page 48) says that where the Core Banking System (CBS) owns the ledger, the platform exports or posts the resulting demand and accounting effects to it. It also retains the returned journal reference against the loan.

## Why the bank wants it

The BRD gives the background in its principle that the CBS is authoritative for every financial fact after booking (BRD 3.3, PDF page 19). A journal reference is how each bill can be traced to the CBS entry that recorded it.

## Example

A penalty bill of 44 is posted to the CBS by the robot. The CBS returns JV-2026-000123, and the loan system stores it against that bill.

## Terms to know

- **CBS:** the bank's main system. See `glossary.cbs`.
- **Journal reference:** the number the CBS gives to an entry it posts.
- **RPA:** the software robot that types entries into the CBS. See `glossary.rpa`.
