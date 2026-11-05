---
id: bridge.BR-LMS-112
type: bridge
title: Payment holiday (moratorium) rules
summary: "Partly covered. The moratorium works on each loan, but the Loan Product has no moratorium field, so the rule is typed on the loan. The coverage analysis rated it covered."
br_ids: [BR-LMS-112]
brd_section: 7.2
doctypes: [Loan, Loan Product]
verdict: partial
analysis_status: verified
dev_items: []
fields: [Loan.Moratorium Type, Loan.Moratorium Tenure, Loan.Treatment of Interest]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan/loan.json:538", "lending/loan_management/doctype/loan/loan.json:612"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-112"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p47"
  - "sources/verification/reqs.json#BR-LMS-112"
  - "sources/verification/verification_report.md#BR-LMS-112"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-112"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-112"
related: [concept.BR-LMS-112, brd_section.7.2, concept.BR-LMS-103, glossary.moratorium, devitem.D1]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. The moratorium works on each loan, but the Loan Product has no moratorium field, so the rule is typed on the loan. The coverage analysis rated it covered.

## Business need

The bank wants the length of a payment holiday and the treatment of principal and interest to be configurable (BR-LMS-112, BRD 7.2, PDF page 47), as part of the product configuration. See `concept.BR-LMS-112`.

## Frappe Lending today

The **Loan** has **Moratorium Type** (EMI or Principal), **Moratorium Tenure** and **Treatment of Interest** (Capitalize, or Add to first repayment) (`loan.json` lines 538-547, line 612). The repayment schedule stores a Moratorium End Date and builds the holiday rows. The **Loan Product** has no field of this kind (a search of the Loan Product folder in 16.5.1 for "morator" finds no file).

## Match or gap, and why

This is **partly covered**. The coverage analysis rated it covered; verification found that the behaviour is right but only per loan (verification_report.md:50, 123). In the test, a loan with an EMI moratorium of 3 months and interest capitalised had three rows with no principal, then the balance grew to 31,093.15 (30,000 plus 1,093.15) before EMIs of 2,792 began. A loan with a principal moratorium had interest-only rows of 356.71 and then an EMI of 2,694. In the test, the Loan Product had no moratorium field. That conflicts with BR-LMS-103 (`concept.BR-LMS-103`): the type, length and treatment have to be keyed on the loan or sent by the origination system.

## What to do today

Enter the three moratorium fields on each loan that needs a holiday, and have a second person check them. Do not assume a product rule exists.

## Planned fix

ND-2 in the verification report asks for product-level moratorium fields that are fetched onto the loan and editable only with approval. It is also in the scope of dev item D1 (`devitem.D1`).
