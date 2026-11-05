---
id: concept.BR-LMS-113
type: concept
title: Rules for fees and charges
summary: "Each fee has rules for when it applies, how it is calculated and which accounts it goes to when it is billed, earned, forgiven or written off."
br_ids: [BR-LMS-113]
brd_section: 7.2
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-113"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p47"
  - "sources/verification/reqs.json#BR-LMS-113"
  - "sources/verification/verification_report.md#BR-LMS-113"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-113"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-113"
related: [bridge.BR-LMS-113, brd_section.7.2, glossary.waiver, glossary.write-off, decision.waiver]
version: 1
status: approved
approved_by: Owner
---
**In short:** Each fee has rules for when it applies, how it is calculated and which accounts it goes to when it is billed, earned, forgiven or written off.

## What the rule says

BR-LMS-113 (priority Must, BRD 7.2, PDF page 47) says charge configuration defines three things for each charge: its applicability (when it applies), its calculation basis, and the receivable, income, waiver and write-off accounts to which it maps.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a fee is a source of income that must be raised in the same way every time, and the books need to know in advance where each kind of fee is recorded when it is billed, forgiven or written off.

## Example

A processing fee of 1% of the loan, which is 1,000 BDT, is taken at payout and booked as fee income. If a manager forgives it, it goes to the waiver account instead.

## Terms to know

- **Applicability:** the event that triggers the fee, such as payout, a late payment or a prepayment.
- **Calculation basis:** a fixed amount or a percentage of something.
- **Receivable, income, waiver and write-off accounts:** the ledger accounts the fee is recorded in. See `glossary.waiver` and `glossary.write-off`.
