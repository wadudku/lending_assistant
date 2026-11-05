---
id: concept.BR-LMS-212
type: concept
title: The partner's share of each plan and of charges
summary: The platform works out the partner's share of every repayment plan and shares one-off charges with the partner as agreed.
br_ids: [BR-LMS-212]
brd_section: 7.12
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-212"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p55"
  - "sources/verification/reqs.json#BR-LMS-212"
  - "sources/verification/verification_report.md#BR-LMS-212"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-212"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-212"
related: [bridge.BR-LMS-212, brd_section.7.12, glossary.partner, concept.BR-LMS-211]
version: 1
status: approved
approved_by: Owner
---
**In short:** The platform works out the partner's share of every repayment plan and shares one-off charges with the partner as agreed.

## What the rule says

BR-LMS-212 in section 7.12 (Must, BRD PDF page 55) says the platform shall generate the partner's share of each repayment schedule and shall share configured ad-hoc charges according to the agreed arrangement.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the partner is owed its part of every instalment on a fixed date, and the bank needs the figures before the money comes in, not after.

## Example

On Rahim's EMI of 8,979 the partner's share is shown for each month. A late fee of 500 is split 80 to the partner and 20 to the bank, if that was agreed.

## Terms to know

- **Partner schedule:** the partner's own repayment plan beside the borrower's. See `concept.BR-LMS-211`.
- **Ad-hoc charge:** a one-off fee, such as a late fee.
- **Share:** the part of each amount that belongs to the partner.
