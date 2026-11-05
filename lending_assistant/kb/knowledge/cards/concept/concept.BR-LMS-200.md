---
id: concept.BR-LMS-200
type: concept
title: Work out a settlement offer and show its make-up
summary: "When the bank agrees to accept less than the full amount to close a loan, the platform shows what makes up the figure (principal, interest, penalties, charges and the waivers) before anyone approves it."
br_ids: [BR-LMS-200]
brd_section: 7.11
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-200"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p54"
  - "sources/verification/reqs.json#BR-LMS-200"
  - "sources/verification/verification_report.md#BR-LMS-200"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-200"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-200"
related: [bridge.BR-LMS-200, brd_section.7.11, glossary.waiver, decision.settlement]
version: 1
status: approved
approved_by: Owner
---
**In short:** When the bank agrees to accept less than the full amount to close a loan, the platform shows what makes up the figure (principal, interest, penalties, charges and the waivers) before anyone approves it.

## What the rule says

BR-LMS-200 in section 7.11 (Must, BRD PDF page 54) says the platform shall calculate a settlement figure comprising principal, interest, penalties, charges and any approved waivers. It shall present the composition of that figure before approval.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the person approving a settlement must see how much is being forgiven, and of what, before agreeing to it.

## Example

Rahim owes 95,000 in total. The bank agrees to take 80,000. The screen shows: 95,000 owed, 15,000 waived, 80,000 to pay.

## Terms to know

- **Settlement:** the bank accepts less than the full amount to close the loan.
- **Waiver:** the part the bank forgives. See `glossary.waiver`.
- **Make-up:** the split of the figure into principal, interest, penalties and charges.
