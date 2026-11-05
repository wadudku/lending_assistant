---
id: concept.BR-LMS-130
type: concept
title: Raise the bills on their due dates
summary: "On each due date the system raises a bill (a demand) for the instalment and its parts: principal, interest, penalty, charges and broken-period interest."
br_ids: [BR-LMS-130]
brd_section: 7.4
doctypes: []
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-130"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p48"
  - "sources/verification/reqs.json#BR-LMS-130"
  - "sources/verification/verification_report.md#BR-LMS-130"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-130"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-130"
related: [bridge.BR-LMS-130, brd_section.7.4, glossary.demand, glossary.bpi, glossary.penal-interest]
version: 1
status: approved
approved_by: Owner
---
**In short:** On each due date the system raises a bill (a demand) for the instalment and its parts: principal, interest, penalty, charges and broken-period interest.

## What the rule says

BR-LMS-130 (priority Must, BRD 7.4, PDF page 48) says the platform raises demands on their due dates for the instalment, principal, interest, penalty, charge and broken-period interest components. It does so according to the product's processing path, one for term loans and one for demand or overdraft products.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a bill with a date and an amount is what makes lateness measurable: a payment is late only against a demand that was raised.

## Example

On 5 July 2026 the system raises a bill of 8,979 for Rahim. If he is late, a separate penalty bill follows.

## Terms to know

- **Demand:** a bill for an amount due on a date. See `glossary.demand`.
- **Component:** one part of a bill, such as principal or interest.
- **Broken-period interest (BPI):** interest for the odd days before the first full period. See `glossary.bpi`.
- **Term loan:** a loan repaid on a schedule, as against a demand or overdraft product.
