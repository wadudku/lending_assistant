---
id: bridge.BR-LMS-233
type: bridge
title: Refund what is left
summary: "Covered. A Loan Refund returns an excess payment or a security deposit, posts the entries and keeps a reference number. The reference number is not mandatory, and a full excess refund closes the loan."
br_ids: [BR-LMS-233]
brd_section: 7.14
doctypes: [Loan Refund, Loan Security Deposit, Loan]
verdict: covered
analysis_status: verified
dev_items: []
fields: [Loan Refund.Is Excess Amount Refund, Loan Refund.Is Security Amount Refund, Loan Refund.Reference Number]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_refund/loan_refund.py:59-112"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-233"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p56"
  - "sources/verification/reqs.json#BR-LMS-233"
  - "sources/verification/verification_report.md#BR-LMS-233"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-233"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-233"
  - "sources/verification/FINAL_REPORT.md#new-items-found-in-verification-nd-1-...-nd-47"
related: [concept.BR-LMS-233, bridge.BR-LMS-186, bridge.BR-LMS-187, bridge.BR-LMS-232]
version: 1
status: approved
approved_by: Owner
---
**In short:** Covered. A Loan Refund returns an excess payment or a security deposit, posts the entries and keeps a reference number. The reference number is not mandatory, and a full excess refund closes the loan.

## Business need

Any remaining security deposit or excess payment must be refunded, and the refund recorded with its external reference (BR-LMS-233 in section 7.14, BRD PDF page 56). See `concept.BR-LMS-233`.

## Frappe Lending today

A **Loan Refund** has the checks **Is Excess Amount Refund** and **Is Security Amount Refund**, a refund amount, a mandatory refund account and a **Reference Number** for the bank transaction (`lending/loan_management/doctype/loan_refund/loan_refund.json`). On submit it lowers the excess paid on the loan, or the available security deposit, and posts the general ledger entries (`lending/loan_management/doctype/loan_refund/loan_refund.py:59-112`). In the test, an excess refund of 1,000 with a reference number posted Dr Loan Customer Refund and Cr Loan Collection Bank, and a deposit refund of 10,413.00 on Loan H posted correctly.

## Match or gap, and why

This is **covered**, and the verification confirmed the verdict (J9). The card for BR-LMS-186 covers the approval and amount checks.

- The Reference Number field is not mandatory (checked in the definition), so a refund can be saved without the bank reference the BRD asks for.
- A refund that takes the excess to 0 closes the loan, with the refund date as the closure date (DEF-43). In the test, a *Settled* loan became *Closed* when its excess was refunded in full.
- Refund has no approval step (see BR-LMS-186).

## What to do today

Make the bank reference part of the refund checklist, and check the closure date after any refund that clears an excess.

## Planned fix

Dev items: ND-37 (refund approval, closure letter and notification, small) and ND-39 (a refund must not close the loan, small) are proposed in the final report.
