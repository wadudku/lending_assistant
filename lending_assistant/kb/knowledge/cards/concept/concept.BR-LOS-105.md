---
id: concept.BR-LOS-105
type: concept
title: A partner's first-loss guarantee terms are recorded for servicing to use
summary: "For each partner, the platform records any first-loss default guarantee or other risk-sharing terms and gives them to servicing for partner economics."
br_ids: [BR-LOS-105]
brd_section: 6.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-105"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p29"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-100"
related: [bridge.BR-LOS-105, glossary.fldg, glossary.partner]
version: 1
status: approved
approved_by: Owner
---
**In short:** For each partner, the platform records any first-loss default guarantee or other risk-sharing terms and gives them to servicing for partner economics.

## What the rule says

BR-LOS-105 (Should, BRD 6.1, PDF page 29) says the platform records, for each partner, the first-loss default guarantee terms or other risk-sharing arrangement where one exists, and makes those terms available to servicing for partner economics. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a guarantee changes who bears a loss, so servicing needs the terms to work out what the Bank and the partner each earn or lose.

## Example

A partner agrees to cover the first 5% of losses on its portfolio. The terms are stored on the partner record, and servicing reads them to work out what the partner owes after a default.

## Terms to know

- **First-loss guarantee (FLDG):** the partner covers the first share of any loss. See `glossary.fldg`.
- **Risk-sharing:** an agreement on who bears a loss.
- **Partner economics:** what the Bank and the partner each earn or lose on the portfolio.
- **Should:** a requirement with priority Should, not Must.
