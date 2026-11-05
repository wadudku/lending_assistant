---
id: bridge.BR-LMS-117
type: bridge
title: "Product rules have versions, start dates and approval"
summary: "Gap. A product edit is saved at once, with no effective date, no approval step and no version number on the loans."
br_ids: [BR-LMS-117]
brd_section: 7.2
doctypes: [Loan Product, Loan]
verdict: gap
analysis_status: verified
dev_items: [D5]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-117"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p47"
  - "sources/verification/reqs.json#BR-LMS-117"
  - "sources/verification/verification_report.md#BR-LMS-117"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-117"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-117"
related: [concept.BR-LMS-117, brd_section.7.2, devitem.D5, glossary.maker-checker]
version: 1
status: approved
approved_by: Owner
---
**In short:** Gap. A product edit is saved at once, with no effective date, no approval step and no version number on the loans.

## Business need

The bank wants product rules versioned, effective-dated and approved by a second person, and each loan to record the version it ran under (BR-LMS-117, BRD 7.2, PDF page 47). See `concept.BR-LMS-117`.

## Frappe Lending today

The **Loan Product** is not submittable (a search of `loan_product.json` for is_submittable finds nothing) and has no workflow. Frappe keeps a change log (Version) that records who changed a field, when, and the old and new values. Rates are copied onto the loan at booking.

## Match or gap, and why

This is a **gap**. In the test, a user with Loan Manager and System Manager roles changed the penalty rate from 12 to 18 on a copy of the product, and it saved at once with no approval, no warning and no effective date (verification_report.md:145). The Version log recorded only the old and new values. In the test, an existing loan kept its 12% because the rate had been copied at booking, so only new loans got 18%; the earlier analysis had expected existing loans to change. In the test, no loan stored which product version it was booked under. The coverage analysis rated this row a gap, and verification confirmed it.

## What to do today

Control product edits by permission: give write access on Loan Product to as few roles as possible, and keep the approval outside the system (for example a signed change request) until the fix is built.

## Planned fix

Dev item D5 (`devitem.D5`) adds change requests with a workflow and an effective date, and stamps the rule version on the loan, demand, accrual, repayment and classification.
