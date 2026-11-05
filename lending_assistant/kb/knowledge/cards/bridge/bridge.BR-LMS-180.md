---
id: bridge.BR-LMS-180
type: bridge
title: Paying future EMIs early (advance payment)
summary: "Partly covered. Frappe Lending has an Advance Payment type and a product setting, but it books the money as the next instalment paid early and does not cover the EMIs after it. The product's Reduce EMI choice is recorded and not applied. The original analysis said covered."
br_ids: [BR-LMS-180]
brd_section: 7.9
doctypes: [Loan Repayment, Loan Restructure, Loan Repayment Schedule, Loan Product]
verdict: partial
analysis_status: verified
dev_items: []
fields: [Loan Product.How to Handle Advance Payments]
options: [Loan Product.How to Handle Advance Payments=Reduce Tenure, Loan Product.How to Handle Advance Payments=Reduce EMI]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_restructure/loan_restructure.py:955-961", "lending/loan_management/doctype/loan_repayment_schedule/loan_repayment_schedule.py:131-140"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-180"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p53"
  - "sources/verification/reqs.json#BR-LMS-180"
  - "sources/verification/verification_report.md#BR-LMS-180"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-180"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-180"
  - "sources/verification/FINAL_REPORT.md#new-items-found-in-verification-nd-1-...-nd-47"
related: [concept.BR-LMS-180, bridge.BR-LMS-181, bridge.BR-LMS-183]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. Frappe Lending has an Advance Payment type and a product setting, but it books the money as the next instalment paid early and does not cover the EMIs after it. The product's Reduce EMI choice is recorded and not applied. The original analysis said covered.

## Business need

An advance payment must be applied to future scheduled obligations as the product is configured (BR-LMS-180 in section 7.9, BRD PDF page 53). See `concept.BR-LMS-180`.

## Frappe Lending today

A **Loan Repayment** can be of type Advance Payment. The **Loan Product** has a field **How to Handle Advance Payments** with the options Reduce Tenure (the default) and Reduce EMI (`lending/loan_management/doctype/loan_product/loan_product.json:223-228`). Submitting the payment makes a **Loan Restructure** of type Advance Payment and a new **Loan Repayment Schedule**. In the new schedule the first row that has no demand yet is taken as the instalment being paid early and is marked as demanded (`lending/loan_management/doctype/loan_repayment_schedule/loan_repayment_schedule.py:131-140`). The interest and principal demands for that row are then created, dated with the payment (lines 170 to 195 of the same file). For a product set to Reduce EMI, the restructure is built with the method Repay Over Number of Periods; for any other product it is built with a fixed amount per period (`lending/loan_management/doctype/loan_restructure/loan_restructure.py:955-961`). An Advance Payment is refused during a moratorium (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:2589-2603`). The restructure count does not rise for this type (`lending/loan_management/doctype/loan_restructure/loan_restructure.py:321-328`).

## Match or gap, and why

This is **partly covered**. The original analysis said covered, and the verification moved it (J6).

- In the test, a payment of 8,979 with value date 25 September turned the next instalment (due 5 October) into a demand dated 25 September, with interest only up to that date (523.60) and principal 8,455.40. A second payment of 15,000 paid the 5 November instalment and the remaining 6,021 only shrank the last instalment (to 2,512.07). The 5 December EMI was still due in full, so the money did not cover the following EMIs as the BRD example expects.
- The product choice had no effect in the test. A product set to Reduce EMI produced restructure records with an EMI of 5,369 and 4,102 over 12 periods, but the new schedules were identical to the Reduce Tenure ones, with an EMI of 8,979 (DEF-21).
- The restructure count stayed 0 and no watch period was set.

## What to do today

Do not expect an advance payment to settle the following EMIs. After each one, read the new schedule, not the restructure record. Treat the product choice as Reduce Tenure only, whatever it says.

## Planned fix

No development item is assigned in the verified list. The final report proposes ND-21 (a per-payment choice of EMI or tenor, with the DEF-21 fix, medium). It adds that a later develop release may already fix DEF-21 and that this was not verified live, so the fix is not counted on 16.5.1.
