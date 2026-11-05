---
id: concept.BR-LOS-101
type: concept
title: "Each partner and product pair has its own limits, rates and fields"
summary: "Every pairing of a partner and a product carries its own ticket size range, tenors, rate and fees, required application fields and optional sampling rate override."
br_ids: [BR-LOS-101]
brd_section: 6.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-101"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p29"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-100"
related: [bridge.BR-LOS-101, glossary.partner, glossary.sampling]
version: 1
status: approved
approved_by: Owner
---
**In short:** Every pairing of a partner and a product carries its own ticket size range, tenors, rate and fees, required application fields and optional sampling rate override.

## What the rule says

BR-LOS-101 (Must, BRD 6.1, PDF page 29) says each partner and product pairing carries its own configuration: minimum and maximum ticket size, permitted tenors, applicable rate and fees, required application fields, and any sampling rate override. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't say why in this row; the usual reason is that the same product is offered on different terms through different partners. The 6.1 introduction says commercial terms must be enforced by the platform (PDF page 29).

## Example

Partner A sells a product with loans from 20,000 to 100,000 over 6 to 12 months. Partner B sells the same product from 50,000 to 150,000 over 12 months only. Each partner's applications are checked against its own pair of settings.

## Terms to know

- **Ticket size:** the size of one loan, from smallest to largest allowed.
- **Tenor:** the length of a loan, in months.
- **Sampling:** the Bank picks some applications for manual review.
- **Override:** a value that replaces the usual default.
