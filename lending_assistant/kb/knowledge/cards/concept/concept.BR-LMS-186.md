---
id: concept.BR-LMS-186
type: concept
title: "Refund overpayments, with approval"
summary: "If a borrower has paid too much, the extra can be refunded after approval, and the refund is recorded on the loan with its bank reference."
br_ids: [BR-LMS-186]
brd_section: 7.9
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-186"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p53"
  - "sources/verification/reqs.json#BR-LMS-186"
  - "sources/verification/verification_report.md#BR-LMS-186"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-186"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-186"
related: [bridge.BR-LMS-186, brd_section.7.9, glossary.maker-checker]
version: 1
status: approved
approved_by: Owner
---
**In short:** If a borrower has paid too much, the extra can be refunded after approval, and the refund is recorded on the loan with its bank reference.

## What the rule says

BR-LMS-186 in section 7.9 (Must, BRD PDF page 53) says eligible excess payment shall be refundable under approval, and the refund recorded against the loan with its external payment reference.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that giving money back is a payout of the bank's funds, so a second person must agree and the bank's own payment reference ties the entry to the bank statement.

## Example

Rahim overpaid by 80 at closure. 80 is refunded to his account, reference CBS-TXN0099.

## Terms to know

- **Excess payment:** money received above what the loan needed.
- **Refund:** paying that excess back to the borrower.
- **Payment reference:** the bank's transaction number for the payout.
