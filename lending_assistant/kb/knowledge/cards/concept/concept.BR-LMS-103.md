---
id: concept.BR-LMS-103
type: concept
title: "Rules come from the product, not from each loan"
summary: "A loan product is a template. Schedule method, rate, charges and accounting mappings come from it, so staff do not type them again on every loan."
br_ids: [BR-LMS-103]
brd_section: 7.1
doctypes: []
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-103"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p46"
  - "sources/verification/reqs.json#BR-LMS-103"
  - "sources/verification/verification_report.md#BR-LMS-103"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-103"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-103"
related: [bridge.BR-LMS-103, brd_section.7.1, brd_section.7.2, glossary.maker-checker, glossary.emi]
version: 1
status: approved
approved_by: Owner
---
**In short:** A loan product is a template. Schedule method, rate, charges and accounting mappings come from it, so staff do not type them again on every loan.

## What the rule says

BR-LMS-103 (priority Must, BRD 7.1, PDF page 46) says servicing rules, the schedule method, the rate and charge configuration and the accounting mappings are applied from the loan product configuration. They are not entered per loan.

## Why the bank wants it

The BRD gives no reason in this row. BRD 7.2 states the aim of product-driven servicing: a new product can be introduced, or an existing one amended, by authorised business users under maker-checker, without a software release (PDF page 46). The BRD does not say more about why per-loan entry is ruled out; the usual reason is that loans of one product then behave the same way, and no officer can quietly change terms on a single loan.

## Example

Every "Personal Loan - Monthly EMI" loan uses 14% interest and a 5-day grace period because the product says so. A branch officer cannot quietly type 13% on one loan.

## Terms to know

- **Loan product:** the template that holds the rules for one kind of loan.
- **Maker-checker:** one person prepares a change and another approves it. See `glossary.maker-checker`.
- **Schedule method:** the way repayments are worked out, such as a fixed monthly instalment (EMI). See `glossary.emi`.
