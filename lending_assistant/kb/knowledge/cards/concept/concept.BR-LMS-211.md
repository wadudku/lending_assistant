---
id: concept.BR-LMS-211
type: concept
title: "Which products each partner joins, and its share"
summary: "For each partner the platform defines the products it takes part in, its share of the lending and its share of the collections."
br_ids: [BR-LMS-211]
brd_section: 7.12
doctypes: []
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-211"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p55"
  - "sources/verification/reqs.json#BR-LMS-211"
  - "sources/verification/verification_report.md#BR-LMS-211"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-211"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-211"
related: [bridge.BR-LMS-211, brd_section.7.12, glossary.partner, concept.BR-LMS-210]
version: 1
status: approved
approved_by: Owner
---
**In short:** For each partner the platform defines the products it takes part in, its share of the lending and its share of the collections.

## What the rule says

BR-LMS-211 in section 7.12 (Must, BRD PDF page 55) says the products in which each partner participates shall be defined, together with the share of loan amount and of collection applying to each.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a partner may fund one product and not another, and the bank must know what each loan owes the partner before it posts a single entry.

## Example

On the Agri Loan product, ABC Finance funds 80% of each loan and receives 80% of the collections.

## Terms to know

- **Partner share:** the part of a loan, and of its collections, that belongs to the partner.
- **Product:** the loan type a partner joins. See `concept.BR-LMS-210` for the partner master.
- **Collection share:** the part of each repayment that goes to the partner.
