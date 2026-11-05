---
id: concept.BR-LMS-131
type: concept
title: Attach fees to the loan
summary: "The bank can attach product fees, repayment fees, prepayment fees, restructuring fees and approved one-off fees to a loan as configured."
br_ids: [BR-LMS-131]
brd_section: 7.4
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-131"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p48"
  - "sources/verification/reqs.json#BR-LMS-131"
  - "sources/verification/verification_report.md#BR-LMS-131"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-131"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-131"
related: [bridge.BR-LMS-131, brd_section.7.4, glossary.prepayment, glossary.demand, concept.BR-LMS-113]
version: 1
status: approved
approved_by: Owner
---
**In short:** The bank can attach product fees, repayment fees, prepayment fees, restructuring fees and approved one-off fees to a loan as configured.

## What the rule says

BR-LMS-131 (priority Must, BRD 7.4, PDF page 48) says the platform attaches five kinds of charge to the loan as configured: product charges, repayment charges, prepayment charges, restructuring charges and approved ad-hoc charges.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that fees are part of what a borrower owes, so each one has to be tied to the loan and billed like any other amount.

## Example

Rahim prepays 20,000. The product has a 2% prepayment fee, so a fee of 400 is added to his loan.

## Terms to know

- **Charge (fee):** an amount the bank charges besides interest.
- **Ad-hoc charge:** a one-off fee approved for a single case.
- **Prepayment:** paying part of the loan before it is due. See `glossary.prepayment`.
