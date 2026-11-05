---
id: bridge.BR-LMS-181
type: bridge
title: Paying extra to cut the loan (prepayment)
summary: "Partly covered. A Pre Payment type and a prepayment charge table exist, but the loan always keeps its EMI and ends sooner. There is no choice of a lower EMI, and the charge is typed in by hand."
br_ids: [BR-LMS-181]
brd_section: 7.9
doctypes: [Loan Repayment, Prepayment Charges, Loan Restructure, Loan Repayment Schedule]
verdict: partial
analysis_status: verified
dev_items: [D20]
fields: [Loan Repayment.Prepayment Charges]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_restructure/loan_restructure.py:955-961", "lending/loan_management/doctype/loan_repayment/loan_repayment.py:216-225"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-181"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p53"
  - "sources/verification/reqs.json#BR-LMS-181"
  - "sources/verification/verification_report.md#BR-LMS-181"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-181"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-181"
  - "sources/verification/FINAL_REPORT.md#new-items-found-in-verification-nd-1-...-nd-47"
  - "sources/verification/FINAL_REPORT.md#D20"
related: [concept.BR-LMS-181, bridge.BR-LMS-180, devitem.D20]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. A Pre Payment type and a prepayment charge table exist, but the loan always keeps its EMI and ends sooner. There is no choice of a lower EMI, and the charge is typed in by hand.

## Business need

A prepayment must cut principal early, take any configured prepayment charge, and then revise either the instalment or the tenor as the borrower elects and the bank approves (BR-LMS-181 in section 7.9, BRD PDF page 53). See `concept.BR-LMS-181`.

## Frappe Lending today

A **Loan Repayment** can be of type Pre Payment. The payment form has a table **Prepayment Charges** with a Charge Code and a Charge Amount per row (`lending/loan_management/doctype/prepayment_charges/prepayment_charges.json`). When accounting is on, the charges become a Sales Invoice on submit (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:216-225`). The charge is entered by hand for each payment: the Loan Product has no prepayment charge setting. As with an advance payment, a Pre Payment creates a **Loan Restructure** of type Pre Payment and a new **Loan Repayment Schedule**. The restructure is always built with a fixed amount per period, so the EMI stays and the loan ends sooner (`lending/loan_management/doctype/loan_restructure/loan_restructure.py:955-961`). A Pre Payment is refused during a moratorium (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:2589-2603`).

## Match or gap, and why

This is **partly covered**, and the verification confirmed the verdict (J6).

- In the test, a Pre Payment of 20,000 with value date 20 October was split into a fee of 200 (a charge row typed in by hand), interest 345.45 and principal 19,454.55. The new plan kept the EMI at 8,979 and ended on 5 March 2027 instead of 5 May 2027. That is the BRD's choice A.
- The BRD's choice B, a lower EMI and the same end date, is not possible. The Loan Repayment form has no field for the choice, and the code never reads the product setting for a Pre Payment. That setting, How to Handle Advance Payments, is read in one place only, and only for an Advance Payment (see `bridge.BR-LMS-180`, where it is also ignored).
- A Pre Payment is not counted as a restructure: the count stayed 0 and no watch period was set.
- Because nothing records an election, there is nothing for the bank to approve. The restructure was approved automatically in the test.

## What to do today

Agree the borrower's choice outside the system and check the new schedule after each prepayment. Enter the prepayment charge on the payment form every time, because nothing does it for you.

## Planned fix

Dev item D20 (small items) covers this row; the final report sizes it medium. The per-payment choice of EMI or tenor is ND-21.
