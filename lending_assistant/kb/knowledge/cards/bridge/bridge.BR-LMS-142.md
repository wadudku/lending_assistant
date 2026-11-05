---
id: bridge.BR-LMS-142
type: bridge
title: Interest for odd days (broken period)
summary: "Covered. The product chooses how the interest for the odd days is recovered, and the test showed it added to the first instalment."
br_ids: [BR-LMS-142]
brd_section: 7.5
doctypes: [Loan Product, Loan Disbursement]
verdict: covered
analysis_status: verified
dev_items: []
fields: [Loan Product.BPI Recovery Method]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_product/loan_product.json:541"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-142"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p49"
  - "sources/verification/reqs.json#BR-LMS-142"
  - "sources/verification/verification_report.md#BR-LMS-142"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-142"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-142"
related: [concept.BR-LMS-142, brd_section.7.5, glossary.bpi, bridge.BR-LMS-121]
version: 1
status: approved
approved_by: Owner
---
**In short:** Covered. The product chooses how the interest for the odd days is recovered, and the test showed it added to the first instalment.

## Business need

The bank wants broken-period interest handled at disbursement, at a change of terms and at closure (BR-LMS-142, BRD 7.5, PDF page 49). See `concept.BR-LMS-142`.

## Frappe Lending today

The **Loan Product** has a **BPI Recovery Method** with four options: Upfront Deduction, Amortized Over Tenure, Add to First EMI and Add to Last EMI (`loan_product.json` lines 541-544). The site's products use Add to First EMI (verification_report.md:1022). The analysis notes that a restructure handles unaccrued interest and that closure accrues interest to the date; the live test covered the payout case.

## Match or gap, and why

This is **covered**. In the test, a loan paid out on 2 June with its first due date on 5 July (33 days) had row 1 interest of 632.87 against 547.97 for a regular month, and a first EMI of 4,547.53 against the regular 4,490, the extra days added to the first instalment (verification_report.md:182). One caveat from the test: a back-dated disbursement ignored the loan's repayment start date unless it was also set on the disbursement (F-J3-1). The coverage analysis rated this row covered, and verification confirmed it for the payout case. Restructure and closure were not run in this test.

## What to do today

Choose the BPI Recovery Method on the product. When back-dating a disbursement, set the repayment start date on the disbursement too.

## Planned fix

Nothing is needed for the payout case.
