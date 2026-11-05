---
id: concept.BR-LMS-153
type: concept
title: Two repricing options
summary: "A repricing can either keep the end date and revise the instalment, or keep the instalment and revise the term."
br_ids: [BR-LMS-153]
brd_section: 7.6
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-153"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p49"
  - "sources/verification/reqs.json#BR-LMS-153"
  - "sources/verification/verification_report.md#BR-LMS-153"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-153"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-153"
related: [bridge.BR-LMS-153, brd_section.7.6, glossary.repricing, glossary.emi]
version: 1
status: approved
approved_by: Owner
---
**In short:** A repricing can either keep the end date and revise the instalment, or keep the instalment and revise the term.

## What the rule says

BR-LMS-153 (priority Must, BRD 7.6, PDF page 49) says the platform supports both repricing modes: fixed maturity with a revised instalment, and fixed instalment with a revised tenor.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a rate change can be absorbed in two ways, a higher payment or a longer loan, and the bank or the borrower may prefer either.

## Example

The rate moves from 14% to 15%. Option 1: the EMI rises from about 8,979 to about 9,019 and the end date stays the same. Option 2: the EMI stays 8,979 and the loan runs a little longer.

## Terms to know

- **Fixed maturity:** the end date does not move.
- **Fixed instalment:** the payment amount does not move.
- **Tenor:** the length of the loan. See `glossary.emi`.
