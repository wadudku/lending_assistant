---
id: glossary.allocation-order
type: glossary
title: Allocation order (offset sequence)
summary: "The set order in which a payment clears what a borrower owes, for example penalty, then interest, then principal."
br_ids: []
brd_section: 1.5
doctypes: [Loan Demand Offset Order, Loan Product]
dev_items: []
terms: [allocation order, offset sequence, offset order, payment order, waterfall]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#1.5"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-164"
  - "sources/NRB_LMS_Requirements_Plain_English.md#glossary-of-abbreviations"
  - "sources/verification/verification_report.md#BR-LMS-164"
related: [concept.BR-LMS-164, bridge.BR-LMS-164]
version: 1
status: approved
approved_by: Owner
---
**In short:** The set order in which a payment clears what a borrower owes, for example penalty, then interest, then principal.

## Plain meaning

When a borrower owes several things and pays less than the total, the allocation order decides which are cleared first. The BRD calls it the offset sequence: the configured priority that decides which due components a payment is applied to first (BRD 1.5).

## Example

Rahim owes penalty 20, interest 1,151 and principal 7,828 and pays 1,000. With the order penalty, interest, principal, the 1,000 clears the penalty and part of the interest.

## Why it matters here

BR-LMS-164 requires the configured order and a visible split. In Frappe Lending the order is held in a **Loan Demand Offset Order** and set on the Company or the **Loan Product**. In the verified tests, an order using the plain Interest component never paid interest (see `bridge.BR-LMS-164`).

## See also

`concept.BR-LMS-164`, `bridge.BR-LMS-164`, `glossary.dpd`.
