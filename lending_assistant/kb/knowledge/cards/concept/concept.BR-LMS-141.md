---
id: concept.BR-LMS-141
type: concept
title: "Penalty interest, kept separate"
summary: "Interest charged on overdue amounts (penal interest) is calculated and tracked apart from normal interest, at a rate and on a basis that can be configured."
br_ids: [BR-LMS-141]
brd_section: 7.5
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-141"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p49"
  - "sources/verification/reqs.json#BR-LMS-141"
  - "sources/verification/verification_report.md#BR-LMS-141"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-141"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-141"
related: [bridge.BR-LMS-141, brd_section.7.5, glossary.penal-interest, glossary.dpd]
version: 1
status: approved
approved_by: Owner
---
**In short:** Interest charged on overdue amounts (penal interest) is calculated and tracked apart from normal interest, at a rate and on a basis that can be configured.

## What the rule says

BR-LMS-141 (priority Must, BRD 7.5, PDF page 49) says penal interest on qualifying overdue amounts is calculated and tracked separately from normal interest accrual, under a configurable rate and basis.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that penal interest is a charge for being late, not the price of the loan, so the bank must be able to report, waive and treat it differently from normal interest.

## Example

EMI 1 of 8,979 is unpaid after the grace days. Penalty at 12% a year is about 2.95 BDT a day, tracked as penalty, not as normal interest.

## Terms to know

- **Penal interest:** the extra interest charged on late amounts. See `glossary.penal-interest`.
- **Grace days:** days after the due date during which no penalty is charged.
- **Basis:** the amount the penalty rate is applied to, such as the overdue instalment.
