---
id: concept.BR-LMS-172
type: concept
title: Watch for a collateral shortfall
summary: "The platform compares the value of the collateral with the amount lent, on a schedule and on demand, and flags the gap when the collateral no longer covers the loan."
br_ids: [BR-LMS-172]
brd_section: 7.8
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-172"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p52"
  - "sources/verification/reqs.json#BR-LMS-172"
  - "sources/verification/verification_report.md#BR-LMS-172"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-172"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-172"
related: [bridge.BR-LMS-172, brd_section.7.8, glossary.ltv, concept.BR-LMS-170c]
version: 1
status: approved
approved_by: Owner
---
**In short:** The platform compares the value of the collateral with the amount lent, on a schedule and on demand, and flags the gap when the collateral no longer covers the loan.

## What the rule says

BR-LMS-172 in section 7.8 (Must, BRD PDF page 52) says the platform monitors security shortfall by comparing eligible collateral value with secured exposure. It does this through both scheduled and manually triggered evaluation.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that collateral prices move, so a loan that was well covered at the start can become under-covered without anyone noticing unless the bank checks regularly.

## Example

Rahim's pledged shares fall in price and are now worth 90,000 in eligible value against a 100,000 loan. The shortfall is 10,000.

## Terms to know

- **Shortfall:** the amount by which collateral value falls below what the loan needs.
- **Eligible value:** the collateral value after the haircut. See `concept.BR-LMS-170c`.
- **Secured exposure:** the part of the loan that the collateral is meant to cover.
- **LTV:** loan to value, the ratio the bank allows. See `glossary.ltv`.
