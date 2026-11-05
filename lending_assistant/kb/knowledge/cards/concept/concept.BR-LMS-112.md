---
id: concept.BR-LMS-112
type: concept
title: Payment holiday (moratorium) rules
summary: "A moratorium is a payment holiday, usually at the start of a loan. The product must say how long it lasts and what happens to principal and interest during it."
br_ids: [BR-LMS-112]
brd_section: 7.2
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-112"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p47"
  - "sources/verification/reqs.json#BR-LMS-112"
  - "sources/verification/verification_report.md#BR-LMS-112"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-112"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-112"
related: [bridge.BR-LMS-112, brd_section.7.2, glossary.moratorium, glossary.emi]
version: 1
status: approved
approved_by: Owner
---
**In short:** A moratorium is a payment holiday, usually at the start of a loan. The product must say how long it lasts and what happens to principal and interest during it.

## What the rule says

BR-LMS-112 (priority Must, BRD 7.2, PDF page 47) says moratorium rules are configurable by duration and by the treatment of principal and interest during the moratorium. In the BRD, this sits under product and servicing configuration, so the rule is meant to be set once on the product.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a payment holiday changes what a borrower owes and when, so the bank wants the length and the treatment of interest decided by policy on the product, not by each officer on each loan.

## Example

A 3-month moratorium. Option A: Rahim pays nothing for 3 months and the interest is added on later. Option B: he pays only the interest, about 1,151 a month, and the full EMIs start in month 4.

## Terms to know

- **Moratorium:** a period at the start of a loan with reduced or no payments. See `glossary.moratorium`.
- **Principal moratorium:** only interest is paid during the holiday.
- **EMI moratorium:** nothing is paid during the holiday and the interest is added on later (capitalised) or added to the first repayment.
- **Capitalise:** add unpaid interest to the loan balance.
