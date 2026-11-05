---
id: bridge.BR-LMS-145
type: bridge
title: Check that interest numbers agree everywhere
summary: "Gap. In the test, none of the lending reports reconciles interest between the plan, bills, accruals, income and the ledger."
br_ids: [BR-LMS-145]
brd_section: 7.5
doctypes: [Loan Interest Accrual, Loan Demand]
verdict: gap
analysis_status: verified
dev_items: [D10]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-145"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p49"
  - "sources/verification/reqs.json#BR-LMS-145"
  - "sources/verification/verification_report.md#BR-LMS-145"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-145"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-145"
related: [concept.BR-LMS-145, brd_section.7.5, devitem.D10, bridge.BR-LMS-134, glossary.gl]
version: 1
status: approved
approved_by: Owner
---
**In short:** Gap. In the test, none of the lending reports reconciles interest between the plan, bills, accruals, income and the ledger.

## Business need

The bank wants a reconciliation, and a report of differences, across schedule, demanded, accrued and collected interest and the ledger or CBS position (BR-LMS-145, BRD 7.5, PDF page 49). See `concept.BR-LMS-145`.

## Frappe Lending today

Frappe Lending ships eleven reports in the lending report folder: ALM Audit, Applicant-wise Loan Security Exposure, Disbursement Analysis, Future Cashflow, Loan Outstanding, Loan Repayment and Closure, Loan Security Exposure, Loan Security Ledger, Loan Security Status, Loan Statement of Account and Past Cashflow. None has a name that suggests an interest reconciliation, and the verification checked them (verification_report.md:238).

## Match or gap, and why

This is a **gap**. In the test, a check of those eleven reports found no interest reconciliation of accrued against billed against ledger against CBS (verification_report.md:238). The example in the test: accrued 632.94 against billed 632.87 on one loan, a difference that such a report would have to explain. The CBS side also needs the integration (`bridge.BR-LMS-134`). The coverage analysis rated it a gap, and verification confirmed that.

## What to do today

Compare accrued interest (Loan Interest Accrual) with billed interest (Loan Demand) and the ledger by hand, for a sample of loans, at each month end.

## Planned fix

Dev item D10 (`devitem.D10`) adds reports for the interest chain and an exception record for each unmatched item.
