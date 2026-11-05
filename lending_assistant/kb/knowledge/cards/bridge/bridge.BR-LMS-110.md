---
id: bridge.BR-LMS-110
type: bridge
title: Five ways of working out repayments
summary: Covered. The Repayment Schedule Type offers a choice for each of the five methods. One defect was found in the flat-interest schedule.
br_ids: [BR-LMS-110]
brd_section: 7.2
doctypes: [Loan Product]
verdict: covered
analysis_status: verified
dev_items: []
fields: [Loan Product.Repayment Schedule Type]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_product/loan_product.json:199"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-110"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p47"
  - "sources/verification/reqs.json#BR-LMS-110"
  - "sources/verification/verification_report.md#BR-LMS-110"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-110"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-110"
related: [concept.BR-LMS-110, brd_section.7.2, glossary.emi, glossary.loc]
version: 1
status: approved
approved_by: Owner
---
**In short:** Covered. The Repayment Schedule Type offers a choice for each of the five methods. One defect was found in the flat-interest schedule.

## Business need

The bank needs at least five repayment methods: equated instalment, pro-rated, cycle-date, flat interest and revolving line of credit (BR-LMS-110, BRD 7.2, PDF page 47). See `concept.BR-LMS-110`.

## Frappe Lending today

The **Loan Product** has a **Repayment Schedule Type** with five options: Monthly as per repayment start date, Pro-rated calendar months, Monthly as per cycle date, Line of Credit and Flat Interest Rate (`loan_product.json` lines 199-203). Each of the BRD's five methods has an option: equated instalment, pro-rated, cycle-date, flat interest and line of credit.

## Match or gap, and why

This is **covered**. In the test, the type had the five options, and a loan on the flat-interest type showed the same interest of 1,166.67 every month, so interest did not shrink (verification_report.md:122). The coverage analysis rated this row covered and verification confirmed it, with one defect noted. In the test, the flat-interest schedule added a 13th row for a 0.04 rounding residue of principal and still charged a full month of interest on it, so the total interest was 15,281.78 against about 14,115 expected.

## What to do today

Pick the schedule type on the product. For flat-interest products, check the last schedule row of each new loan and correct the residue by hand until the defect is fixed.

## Planned fix

No dev item covers this row. The flat-interest defect is recorded in the verification report (line 122).
