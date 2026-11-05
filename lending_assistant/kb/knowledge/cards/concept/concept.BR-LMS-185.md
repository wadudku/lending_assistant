---
id: concept.BR-LMS-185
type: concept
title: Manual corrections need two people and a full record
summary: "A manual change to what a borrower owes (a waiver, capitalising interest, carrying an amount forward, or correcting a balance) needs a second person to approve it and must record the amount before and after, the reason, the approver and a reference."
br_ids: [BR-LMS-185]
brd_section: 7.9
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-185"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p53"
  - "sources/verification/reqs.json#BR-LMS-185"
  - "sources/verification/verification_report.md#BR-LMS-185"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-185"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-185"
related: [bridge.BR-LMS-185, brd_section.7.9, glossary.waiver, glossary.maker-checker, decision.waiver]
version: 1
status: approved
approved_by: Owner
---
**In short:** A manual change to what a borrower owes (a waiver, capitalising interest, carrying an amount forward, or correcting a balance) needs a second person to approve it and must record the amount before and after, the reason, the approver and a reference.

## What the rule says

BR-LMS-185 in section 7.9 (Must, BRD PDF page 53) says manual adjustments shall be supported under maker-checker. They are waiver, capitalisation, carry-forward and approved balance correction. Each records the amounts before and after, the reason, the approver and a supporting reference.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that these changes alter what the bank is owed without a payment, so they are the easiest place for an error or abuse to hide.

## Example

A penalty of 500 is waived: before 500, after 0, reason "borrower hospitalised", approved by the branch manager, reference memo M-12.

## Terms to know

- **Waiver:** forgiving an amount. See `glossary.waiver`.
- **Capitalisation:** adding unpaid interest to the principal.
- **Carry-forward:** moving an amount due to a later date.
- **Balance correction:** a ledger entry that fixes a balance.
- **Maker-checker:** one person prepares, another approves. See `glossary.maker-checker`.
