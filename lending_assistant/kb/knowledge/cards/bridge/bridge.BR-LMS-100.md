---
id: bridge.BR-LMS-100
type: bridge
title: Accept only loans that are really paid out
summary: "Partly covered. A loan and its payout record can be created. In the test, nothing checked that the handover was complete and nothing refused an incomplete one."
br_ids: [BR-LMS-100]
brd_section: 7.1
doctypes: [Loan, Loan Disbursement]
verdict: partial
analysis_status: verified
dev_items: [D1]
fields: [Loan Disbursement.Reference Number, Loan.Auto create disbursement on loan booking, Loan.Loan Application]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_disbursement/loan_disbursement.json:180", "lending/loan_management/doctype/loan/loan.py:424", "lending/loan_management/doctype/loan/loan.json:131"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-100"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p46"
  - "sources/verification/reqs.json#BR-LMS-100"
  - "sources/verification/verification_report.md#BR-LMS-100"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-100"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-100"
related: [concept.BR-LMS-100, brd_section.7.1, devitem.D1, lifecycle.BOOKED]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. A loan and its payout record can be created. In the test, nothing checked that the handover was complete and nothing refused an incomplete one.

## Business need

The bank wants the loan system to take on only a loan that is confirmed as paid out and arrives with its approved terms, a disbursement reference and the origination audit data (BR-LMS-100, BRD 7.1, PDF page 46). See `concept.BR-LMS-100` for the plain-words version.

## Frappe Lending today

Frappe Lending has a **Loan** and a **Loan Disbursement**. The disbursement has a **Reference Number** field that is optional (`loan_disbursement.json` line 180), and nothing checks that it is filled or unique. The only code that reads it is the bank clearance and bank reconciliation code, which shows it as the cheque number and ranks a bank-statement match on it (`lending/loan_management/utils.py` lines 23, 108, 125, 195 and 268, wired in `hooks.py` lines 212-225). A grep for `reference_number` over the whole app (Python and JavaScript, outside tests) finds, for the Loan Disbursement, only those `utils.py` lines and the type line `loan_disbursement.py` line 89. The Loan has a checkbox **Auto create disbursement on loan booking**: when ticked, submitting the loan also creates and submits the disbursement (`loan.py` lines 424-425). There is no dedicated booking API in 16.5.1; a booking is an ordinary record insert through the standard REST interface. The coverage analysis lists a booking API among what exists, and verification found none in 16.5.1 or in develop (verification_report.md:1477).

The loan has a **Loan Application** link (`loan.json` line 131) but no field for the origination audit reference.

## Match or gap, and why

This is **partly covered**. The pieces for a funded loan exist: the loan, the disbursement and the optional reference. What is missing is the check on the package as a whole. In the test, a loan was booked with auto-disbursement and no reference, and the disbursement was submitted with an empty Reference Number and no error (verification_report.md:83). In the test, nothing sent an incomplete handover to an exception queue, and neither the Loan nor the Loan Disbursement has an origination audit field. The coverage analysis rated it partly covered, and verification confirmed that.

## What to do today

Check by eye that **Reference Number** is filled on the Loan Disbursement before you submit it, and keep the origination record outside Frappe Lending. Use the **Loan Application** link to trace a loan back to its application where one exists.

## Planned fix

Dev item D1 (`devitem.D1`) adds an intake API that checks the whole package, rejects incomplete ones into an exception queue, and books the loan and its payout together.
