---
id: concept.BR-LMS-187
type: concept
title: Track a security deposit
summary: "Where a product keeps a cash deposit from the borrower as a guarantee, the platform tracks when it was received, how much was used, how much is left, and the refund."
br_ids: [BR-LMS-187]
brd_section: 7.9
doctypes: []
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-187"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p53"
  - "sources/verification/reqs.json#BR-LMS-187"
  - "sources/verification/verification_report.md#BR-LMS-187"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-187"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-187"
related: [bridge.BR-LMS-187, brd_section.7.9]
version: 1
status: approved
approved_by: Owner
---
**In short:** Where a product keeps a cash deposit from the borrower as a guarantee, the platform tracks when it was received, how much was used, how much is left, and the refund.

## What the rule says

BR-LMS-187 in section 7.9 (Must, BRD PDF page 53) says where a product takes a security deposit, the platform shall track its receipt, allocation, remaining availability and refund.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the deposit is the borrower's money held by the bank, so the bank must always be able to show what it holds and what it has used.

## Example

One EMI (8,979) is held at payout. It is used to pay a missed EMI in March, and nothing is left to refund at closure.

## Terms to know

- **Security deposit:** cash the borrower leaves with the bank as a guarantee. Not to be confused with collateral.
- **Allocation:** using part of the deposit to pay what is due.
- **Available amount:** the deposit not yet used or refunded.
