---
id: concept.BR-LMS-114
type: concept
title: The order in which a payment is used
summary: "When a borrower pays, the system must decide which debt the money clears first: charges, penalty, interest or principal. The bank wants a different order for healthy, bad, written-off and settled loans."
br_ids: [BR-LMS-114]
brd_section: 7.2
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-114"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p47"
  - "sources/verification/reqs.json#BR-LMS-114"
  - "sources/verification/verification_report.md#BR-LMS-114"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-114"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-114"
related: [bridge.BR-LMS-114, brd_section.7.2, glossary.allocation-order, glossary.asset-classification, concept.BR-LMS-164]
version: 1
status: approved
approved_by: Owner
---
**In short:** When a borrower pays, the system must decide which debt the money clears first: charges, penalty, interest or principal. The bank wants a different order for healthy, bad, written-off and settled loans.

## What the rule says

BR-LMS-114 (priority Must, BRD 7.2, PDF page 47) says payment allocation sequences are configurable by asset classification and by collection type. They decide the priority in which charges, penalty, interest, principal and other components receive a payment.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the order decides how much of a payment reduces what the borrower owes in each category, and a bank treats a healthy loan and a bad one differently.

## Example

A borrower owes penalty 500, interest 2,000 and principal 10,000, and pays 3,000. On a healthy loan the order is penalty 500, then interest 2,000, then principal 500. On a bad loan with principal first, all 3,000 goes to principal.

## Terms to know

- **Allocation sequence (payment order):** the ranking of what a payment clears first. See `glossary.allocation-order`.
- **Asset classification:** the health grade of the loan. See `glossary.asset-classification`.
- **Collection type:** why the money is being collected, for example a normal payment, a payment after write-off, or a settlement.
