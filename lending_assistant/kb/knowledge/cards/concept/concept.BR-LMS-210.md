---
id: concept.BR-LMS-210
type: concept
title: A list of co-lending partners
summary: "The platform keeps a list of co-lending partners with their details, their addresses and the kind of risk-sharing arrangement in force, such as a first-loss default guarantee."
br_ids: [BR-LMS-210]
brd_section: 7.12
doctypes: []
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-210"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p55"
  - "sources/verification/reqs.json#BR-LMS-210"
  - "sources/verification/verification_report.md#BR-LMS-210"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-210"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-210"
related: [bridge.BR-LMS-210, brd_section.7.12, glossary.partner, glossary.fldg]
version: 1
status: approved
approved_by: Owner
---
**In short:** The platform keeps a list of co-lending partners with their details, their addresses and the kind of risk-sharing arrangement in force, such as a first-loss default guarantee.

## What the rule says

BR-LMS-210 in section 7.12 (Must, BRD PDF page 55) says the platform shall maintain a partner master recording the partner, its addresses and the type of first-loss default guarantee or other risk-sharing arrangement in force.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that every co-lent loan is tied to a partner and to terms agreed with that partner, so the terms must be written down once and found easily.

## Example

Partner ABC Finance puts up a fixed deposit that covers the first 5% of losses on the loans they share.

## Terms to know

- **Co-lending partner:** another lender that funds part of a loan. See `glossary.partner`.
- **First-loss default guarantee (FLDG):** the partner covers the first part of any losses, for example the first 5%. See `glossary.fldg`.
- **Partner master:** the one record that holds a partner's details and terms.
