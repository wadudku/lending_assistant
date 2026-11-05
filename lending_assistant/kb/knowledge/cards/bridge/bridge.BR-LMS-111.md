---
id: bridge.BR-LMS-111
type: bridge
title: "Store the interest rate, how it is calculated, and whether it is fixed or floating"
summary: "Partly covered. The rate and the day-count method are stored, but there is no fixed or floating flag, no reference rate and no repricing frequency."
br_ids: [BR-LMS-111]
brd_section: 7.2
doctypes: [Loan Product, Loan, Company]
verdict: partial
analysis_status: verified
dev_items: [D4]
fields: [Loan Product.Rate of Interest (%) Yearly, Loan.Rate of Interest (%) / Year, Company.Interest Day-Count Convention]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_product/loan_product.json:96", "lending/install.py:67"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-111"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p47"
  - "sources/verification/reqs.json#BR-LMS-111"
  - "sources/verification/verification_report.md#BR-LMS-111"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-111"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-111"
related: [concept.BR-LMS-111, brd_section.7.2, devitem.D4, glossary.repricing]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. The rate and the day-count method are stored, but there is no fixed or floating flag, no reference rate and no repricing frequency.

## Business need

The bank wants the rate, the calculation method and the fixed or floating type stored, and for floating products the repricing frequency and reference rate (BR-LMS-111, BRD 7.2, PDF page 47). See `concept.BR-LMS-111`.

## Frappe Lending today

The **Loan Product** has **Rate of Interest (%) Yearly** and the **Loan** has **Rate of Interest (%) / Year**, each a plain number that is copied onto the loan at booking. The day-count method is a Company setting, **Interest Day-Count Convention** (`install.py` line 67); the site tested uses Actual/365, and the field offers Actual/365, Actual/Actual, 30/365, 30/360 and Actual/360. The partner record used for co-lending has its own base interest rate for the partner, which is a different thing.

## Match or gap, and why

This is **partly covered**. The rate and the calculation method are stored. In the test, a search of the Loan Product and the Loan for field names containing float, bench, repric, review, base_rate, spread, reference_rate or rate_type found nothing (verification_report.md:411). So a loan cannot be marked fixed or floating, and no reference rate or review frequency can be stored. The coverage analysis rated it partly covered, and verification confirmed that.

## What to do today

Record the rate type and the reference rate outside Frappe Lending, for example in the product description, and change floating rates through a repricing exercise run by hand.

## Planned fix

Dev item D4 (`devitem.D4`) adds a rate type, a benchmark, a spread, a repricing frequency and a next-repricing date on the product and the loan.
