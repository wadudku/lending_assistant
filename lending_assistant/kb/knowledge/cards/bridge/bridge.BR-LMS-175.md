---
id: bridge.BR-LMS-175
type: bridge
title: Collateral reports
summary: "Covered. Four standard reports show the status, the exposure, the exposure by borrower and the ledger of collateral. They have gaps in the detail but each ran on live data."
br_ids: [BR-LMS-175]
brd_section: 7.8
doctypes: [Loan Security Assignment, Loan Security Release]
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/report/loan_security_status/loan_security_status.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-175"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p53"
  - "sources/verification/reqs.json#BR-LMS-175"
  - "sources/verification/verification_report.md#BR-LMS-175"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-175"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-175"
  - "sources/verification/FINAL_REPORT.md#new-items-found-in-verification-nd-1-...-nd-47"
related: [concept.BR-LMS-175, bridge.BR-LMS-172, bridge.BR-LMS-174]
version: 1
status: approved
approved_by: Owner
---
**In short:** Covered. Four standard reports show the status, the exposure, the exposure by borrower and the ledger of collateral. They have gaps in the detail but each ran on live data.

## Business need

The platform must report collateral exposure by applicant and in total, the event ledger and the status of every pledged item (BR-LMS-175 in section 7.8, BRD PDF page 53). See `concept.BR-LMS-175`.

## Frappe Lending today

Four reports ship with the app: Loan Security Status, Loan Security Exposure, Applicant-Wise Loan Security Exposure and Loan Security Ledger. In the test, run as an ordinary user, they all ran on live data. The exposure reports were net of releases and correct: for one security, 143 units at 143,000 or 53.6% of the portfolio. The ledger filtered by loan showed a pledge of 230 and a release of 87.

## Match or gap, and why

This is **covered**. The caveats found in the test:

- The status report is gross: it does not net off releases (one loan still showed 200 + 10 + 20 units although 87 were released) and it values each row at the price on the pledge day.
- The ledger merges the three pledges into one row, dated at the first pledge, so it is not a list of each movement.
- No report shows loan outstanding against collateral value and loan-to-value, and no report lists shortfalls with their age or remedy. Only the list view of the Loan Security Shortfall exists.
- The status report's filter offers only Pledge Requested, Pledged and Unpledged, not Released.

## What to do today

Use the exposure reports for totals and the ledger for events. For coverage, compare the Loan Security Exposure report with the loan balances by hand, and read the Loan Security Shortfall list for open gaps.

## Planned fix

No development item is assigned in the verified list. The final report proposes ND-31 (secured-loan integrity and a coverage report, medium).
