---
id: bridge.BR-LMS-151
type: bridge
title: The new rate starts on a set date
summary: "Gap. For one loan the restructure date acts as the effective date, but there is no effective date for a bulk rate change."
br_ids: [BR-LMS-151]
brd_section: 7.6
doctypes: [Loan Restructure]
verdict: gap
analysis_status: verified
dev_items: [D11]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-151"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p49"
  - "sources/verification/reqs.json#BR-LMS-151"
  - "sources/verification/verification_report.md#BR-LMS-151"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-151"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-151"
related: [concept.BR-LMS-151, brd_section.7.6, devitem.D11, bridge.BR-LMS-150, glossary.effective-date]
version: 1
status: approved
approved_by: Owner
---
**In short:** Gap. For one loan the restructure date acts as the effective date, but there is no effective date for a bulk rate change.

## Business need

The bank wants a repricing to apply the old rate through the prior period and the new rate from an approved effective date (BR-LMS-151, BRD 7.6, PDF page 49). See `concept.BR-LMS-151`.

## Frappe Lending today

For one loan, the **Loan Restructure** has a restructure date. The leftover bulk class (see `bridge.BR-LMS-150`) sets the new rate with no date.

## Match or gap, and why

This is a **gap**. In the test, on one loan, an approved restructure charged interest to the restructure date at 14% (667.87 accrued and added to the first EMI) and 15% from the next day, and the date before the last accrual was refused ("Restructure Date cannot be before last due date"); a future date was accepted as a draft (verification_report.md, BR-LMS-151, J5). So a single-loan effective date works. A bulk effective date does not exist. The coverage analysis rated it a gap, and verification confirmed that.

## What to do today

Use the restructure date for a single loan. For several loans, run one restructure per loan with the same date.

## Planned fix

Dev item D11 (`devitem.D11`) adds a repricing run for floating-rate loans, with selection, effective date, a dry run, maker-checker, new schedule versions and a restartable batch.
