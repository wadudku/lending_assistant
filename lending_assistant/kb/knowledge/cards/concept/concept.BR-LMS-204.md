---
id: concept.BR-LMS-204
type: concept
title: Send settlements and write-offs to the CBS
summary: "The accounting for settlements, write-offs and recoveries goes to the bank's core banking system (CBS), and the journal number the CBS returns is kept on the record."
br_ids: [BR-LMS-204]
brd_section: 7.11
doctypes: []
verdict: gap_cbs
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-204"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p54"
  - "sources/verification/reqs.json#BR-LMS-204"
  - "sources/verification/verification_report.md#BR-LMS-204"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-204"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-204"
related: [bridge.BR-LMS-204, brd_section.7.11, glossary.cbs, glossary.rpa, decision.write-off]
version: 1
status: approved
approved_by: Owner
---
**In short:** The accounting for settlements, write-offs and recoveries goes to the bank's core banking system (CBS), and the journal number the CBS returns is kept on the record.

## What the rule says

BR-LMS-204 in section 7.11 (Must, BRD PDF page 54) says settlement, write-off and recovery accounting effects shall be sent to the Core Banking System and the returned journal reference retained.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the CBS holds the bank's official books, so every entry made here must also exist there and be traceable by its journal number.

## Example

A write-off of 92,172 is posted by the robot. The CBS returns JV-2027-004211, which is stored on the write-off.

## Terms to know

- **CBS:** the core banking system. See `glossary.cbs`.
- **Journal reference:** the number the CBS gives the posted entry.
- **Robot (RPA):** software that posts entries into the CBS screens. See `glossary.rpa`.
