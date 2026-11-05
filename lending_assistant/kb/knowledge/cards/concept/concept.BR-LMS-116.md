---
id: concept.BR-LMS-116
type: concept
title: Link co-lending partners to the product
summary: "Where a product is funded together with another lender, the product records which partners take part and what share each one funds."
br_ids: [BR-LMS-116]
brd_section: 7.2
doctypes: []
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-116"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p47"
  - "sources/verification/reqs.json#BR-LMS-116"
  - "sources/verification/verification_report.md#BR-LMS-116"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-116"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-116"
related: [bridge.BR-LMS-116, brd_section.7.2, glossary.partner, glossary.fldg]
version: 1
status: approved
approved_by: Owner
---
**In short:** Where a product is funded together with another lender, the product records which partners take part and what share each one funds.

## What the rule says

BR-LMS-116 (priority Must, BRD 7.2, PDF page 47) says product configuration links co-lending partners and their share configuration where the product is offered on a shared-risk basis.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a loan funded by two lenders must split every payment and every balance between them, so the product has to say up front who the partners are and how the funding is shared.

## Example

"Agri Loan": the partner company funds 80% and NRB funds 20%.

## Terms to know

- **Co-lending:** two or more lenders fund the same loan.
- **Partner:** the other lender. See `glossary.partner`.
- **Share configuration:** the percentage each lender funds.
- **Shared-risk basis:** each lender carries its share of the risk of non-payment. See `glossary.fldg` for a related guarantee.
