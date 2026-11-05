---
id: bridge.BR-LMS-106
type: bridge
title: Each loan has a category for reports
summary: Covered. The product holds a Loan Category and each loan fetches it.
br_ids: [BR-LMS-106]
brd_section: 7.1
doctypes: [Loan, Loan Product, Loan Category]
verdict: covered
analysis_status: verified
dev_items: []
fields: [Loan.Loan Category, Loan Product.Loan Category]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan/loan.json:587"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-106"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p46"
  - "sources/verification/reqs.json#BR-LMS-106"
  - "sources/verification/verification_report.md#BR-LMS-106"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-106"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-106"
related: [concept.BR-LMS-106, brd_section.7.1, glossary.dpd]
version: 1
status: approved
approved_by: Owner
---
**In short:** Covered. The product holds a Loan Category and each loan fetches it.

## Business need

The bank wants every loan to carry a reporting and servicing category for portfolio segmentation (BR-LMS-106, BRD 7.1, PDF page 46). See `concept.BR-LMS-106`.

## Frappe Lending today

**Loan Category** is a link field on the **Loan Product** and on the **Loan**. The loan fetches it from the product (`loan.json` line 587).

## Match or gap, and why

This is **covered**. In the test, a booked loan received the category Retail from its product (verification_report.md:91). The coverage analysis rated this row covered, and verification confirmed it. The category on the loan is an ordinary link field, not read-only, so a user can change it on a draft loan.

## What to do today

Set the **Loan Category** on the product, so every loan of that product carries it. Group reports by the field.

## Planned fix

Nothing is needed.
