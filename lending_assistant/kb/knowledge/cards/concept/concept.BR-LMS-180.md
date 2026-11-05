---
id: concept.BR-LMS-180
type: concept
title: Paying future EMIs early (advance payment)
summary: "When a borrower pays ahead of the due dates, the money is applied to the coming instalments in the way the loan product says."
br_ids: [BR-LMS-180]
brd_section: 7.9
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-180"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p53"
  - "sources/verification/reqs.json#BR-LMS-180"
  - "sources/verification/verification_report.md#BR-LMS-180"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-180"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-180"
related: [bridge.BR-LMS-180, brd_section.7.9, glossary.advance-payment, glossary.emi]
version: 1
status: approved
approved_by: Owner
---
**In short:** When a borrower pays ahead of the due dates, the money is applied to the coming instalments in the way the loan product says.

## What the rule says

BR-LMS-180 in section 7.9 (Must, BRD PDF page 53) says an advance payment shall be applied to future scheduled obligations according to the product's configured handling.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that borrowers sometimes pay more than is due, and the bank has to know in advance whether that money shortens the loan, lowers the instalment or simply waits.

## Example

Rahim pays 17,958 (two EMIs) in July. The money covers the August and September EMIs.

## Terms to know

- **Advance payment:** money received before the instalments it pays are due. See `glossary.advance-payment`.
- **EMI:** the fixed monthly instalment. See `glossary.emi`.
- **Configured handling:** the loan product decides whether early money shortens the term or lowers the instalment.
