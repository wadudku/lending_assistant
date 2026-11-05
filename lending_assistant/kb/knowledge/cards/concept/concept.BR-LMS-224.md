---
id: concept.BR-LMS-224
type: concept
title: Work queues for things that went wrong
summary: "Failed bills, failed payments, failed postings, failed connections and unmatched items each appear in a work queue with an owner, an age and a written note when they are closed."
br_ids: [BR-LMS-224]
brd_section: 7.13
doctypes: []
verdict: gap
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-224"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p55"
  - "sources/verification/reqs.json#BR-LMS-224"
  - "sources/verification/verification_report.md#BR-LMS-224"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-224"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-224"
related: [bridge.BR-LMS-224, brd_section.7.13, glossary.cbs, concept.BR-LMS-223]
version: 1
status: approved
approved_by: Owner
---
**In short:** Failed bills, failed payments, failed postings, failed connections and unmatched items each appear in a work queue with an owner, an age and a written note when they are closed.

## What the rule says

BR-LMS-224 in section 7.13 (Must, BRD PDF page 55) says the platform shall present exception work queues for failed demands, failed repayments, failed postings, failed integrations and unreconciled items, each with an owner, an ageing indicator and a documented closure.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a failure nobody owns is a failure nobody fixes, so each one needs a name, an age and a recorded ending.

## Example

"Failed CBS postings: 12 items, oldest 3 days, owner Finance Operations."

## Terms to know

- **Exception work queue:** a list of failed items waiting for a person to fix them.
- **Owner:** the person or team responsible for an item.
- **Ageing indicator:** how long an item has been waiting.
- **Documented closure:** a written note of how the item was resolved.
