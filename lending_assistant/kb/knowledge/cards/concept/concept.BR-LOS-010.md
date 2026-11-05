---
id: concept.BR-LOS-010
type: concept
title: One complete handoff package goes to servicing when a loan is paid out
summary: "When a payout is confirmed, the origination system sends the funded loan to servicing as one complete package with the borrower, terms, payout details, collateral and audit reference."
br_ids: [BR-LOS-010]
brd_section: 5.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-010"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p28"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-010"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-011"
related: [bridge.BR-LOS-010, glossary.los, glossary.lms, glossary.partner, concept.BR-LMS-010]
version: 1
status: approved
approved_by: Owner
---
**In short:** When a payout is confirmed, the origination system sends the funded loan to servicing as one complete package with the borrower, terms, payout details, collateral and audit reference.

## What the rule says

BR-LOS-010 (Must, BRD 5.4, PDF page 28) says on confirmed disbursement the LOS transmits the funded loan to the LMS as a single complete handoff package. The package holds borrower identity and KYC references, product code, approved terms, disbursed amount, disbursement reference, value date, target account, collateral references, partner and co-lending share where applicable, and the origination audit reference. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that servicing must start from one complete and consistent record, not from pieces collected from different places. BR-LMS-010 is the matching rule on the servicing side (PDF page 28).

## Example

Rahim's loan of 100,000 is paid out. The origination system sends one package with his identity and KYC references, the product code, the approved terms, the amount, the payout reference, the date, his account, any collateral, and the audit reference. It does not send them one by one.

## Terms to know

- **Handoff package:** the single record sent from origination to servicing.
- **KYC:** the checks that confirm who a customer is.
- **Disbursement reference:** the number the bank gave to the actual payout.
- **Co-lending share:** the part of a loan funded by a partner.
