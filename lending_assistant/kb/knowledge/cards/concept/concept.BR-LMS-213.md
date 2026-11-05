---
id: concept.BR-LMS-213
type: concept
title: Partner settlements and checks
summary: "The platform processes partner credit notes and checks the partner's position on a regular cycle, reporting anything that does not match."
br_ids: [BR-LMS-213]
brd_section: 7.12
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-213"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p55"
  - "sources/verification/reqs.json#BR-LMS-213"
  - "sources/verification/verification_report.md#BR-LMS-213"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-213"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-213"
related: [bridge.BR-LMS-213, brd_section.7.12, glossary.partner, concept.BR-LMS-212]
version: 1
status: approved
approved_by: Owner
---
**In short:** The platform processes partner credit notes and checks the partner's position on a regular cycle, reporting anything that does not match.

## What the rule says

BR-LMS-213 in section 7.12 (Must, BRD PDF page 55) says the platform shall process partner credit notes and shall reconcile the partner's position on a scheduled cycle, reporting any unmatched item.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the bank and the partner each keep their own books, and a regular check is the only way to find a payment that one side has and the other does not.

## Example

On the monthly check the platform says ABC Finance should receive 1,200,000, and the partner's statement says 1,195,000. The 5,000 difference is reported.

## Terms to know

- **Partner credit note:** a statement of an amount owed between the bank and the partner.
- **Reconciliation:** comparing the bank's figure with the partner's and listing the differences.
- **Unmatched item:** a line that appears on one side only, or with a different amount.
