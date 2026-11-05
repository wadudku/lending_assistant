---
id: concept.BR-LOS-100
type: concept
title: A partner organisation is recorded with its legal and commercial details
summary: "The Bank can onboard a partner organisation and record its legal name, licence and tax numbers, address, contacts, agreement, permitted products, batch and exposure limits and status."
br_ids: [BR-LOS-100]
brd_section: 6.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-100"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p29"
related: [bridge.BR-LOS-100, glossary.partner, glossary.batch]
version: 1
status: approved
approved_by: Owner
---
**In short:** The Bank can onboard a partner organisation and record its legal name, licence and tax numbers, address, contacts, agreement, permitted products, batch and exposure limits and status.

## What the rule says

BR-LOS-100 (Must, BRD 6.1, PDF page 29) says the Bank can onboard a partner organisation and record: legal name, trade licence number, TIN or BIN, registered address, contact persons, agreement reference and date, permitted loan products, maximum applications per batch, maximum aggregate exposure and status. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD gives the reason in the 6.1 introduction: partner-sourced origination only works if the commercial relationship is modelled in the system. Exposure ceilings, batch limits and permitted products are commercial terms, and the platform must enforce them rather than rely on operational vigilance (PDF page 29).

## Example

A farm-input company is signed as a partner. The Bank records its licence and tax numbers, the agreement date, the one product it may sell, a limit of 200 applications per batch and a total exposure ceiling. Its status is set to active.

## Terms to know

- **Partner:** an outside organisation that brings borrowers to the Bank. See `glossary.partner`.
- **TIN / BIN:** the tax and business identification numbers.
- **Exposure:** the total amount lent through the partner that is still owed.
- **Batch:** a group of applications sent together. See `glossary.batch`.
