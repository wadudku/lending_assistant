---
id: concept.BR-LMS-221
type: concept
title: Credit-line limits and their change log
summary: "For credit lines, the platform tracks the maximum, used and available limit, and logs every change to the limit with its reason and its approver."
br_ids: [BR-LMS-221]
brd_section: 7.13
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-221"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p55"
  - "sources/verification/reqs.json#BR-LMS-221"
  - "sources/verification/verification_report.md#BR-LMS-221"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-221"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-221"
related: [bridge.BR-LMS-221, brd_section.7.13, glossary.loc, glossary.maker-checker]
version: 1
status: approved
approved_by: Owner
---
**In short:** For credit lines, the platform tracks the maximum, used and available limit, and logs every change to the limit with its reason and its approver.

## What the rule says

BR-LMS-221 in section 7.13 (Must, BRD PDF page 55) says for line-of-credit products the platform shall track maximum, utilised and available limit, with a change log recording every limit movement, its reason and its approver.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a credit line lets a borrower draw again and again, so the limit is a live number that changes, and each change in what the bank has promised to lend must be explained.

## Example

A limit is raised from 500,000 to 700,000 on 1 November 2026, with the reason "annual review", approved by the credit manager.

## Terms to know

- **Line of credit (LoC):** a limit the borrower can draw on and repay repeatedly. See `glossary.loc`.
- **Maximum, utilised and available limit:** the ceiling, the part drawn, and what is left.
- **Limit change log:** the dated list of every movement in these figures.
