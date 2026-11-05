---
id: concept.BR-LMS-184
type: concept
title: Limits on how much can be restructured
summary: "Each branch can restructure only up to a set share of its loans in a period, and the platform keeps a log of how much of the limit has been used."
br_ids: [BR-LMS-184]
brd_section: 7.9
doctypes: []
verdict: gap
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-184"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p53"
  - "sources/verification/reqs.json#BR-LMS-184"
  - "sources/verification/verification_report.md#BR-LMS-184"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-184"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-184"
related: [bridge.BR-LMS-184, brd_section.7.9, glossary.restructuring, decision.restructure]
version: 1
status: approved
approved_by: Owner
---
**In short:** Each branch can restructure only up to a set share of its loans in a period, and the platform keeps a log of how much of the limit has been used.

## What the rule says

BR-LMS-184 in section 7.9 (Must, BRD PDF page 53) says the platform shall enforce configured restructuring limits by branch and by period, and shall retain a utilisation log against those limits.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that restructuring hides weak loans, so the bank and the regulator cap how much of a branch's book can be restructured.

## Example

The Gulshan branch may restructure up to 10% of its book per year. The log shows 7.2% used, so 2.8% is left.

## Terms to know

- **Restructuring limit:** the share of the book a branch may restructure in a period.
- **Utilisation log:** the dated record of how much of that limit is used.
- **Branch:** the office that holds the loan.
