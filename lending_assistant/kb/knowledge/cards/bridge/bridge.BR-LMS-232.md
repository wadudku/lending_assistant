---
id: bridge.BR-LMS-232
type: bridge
title: Release collateral at closure
summary: "Partly covered. A Loan Security Release works and shows in the Loan Security Ledger report, but approving it overwrites the loan's closure date with today's date. Any Loan Manager can set the approval."
br_ids: [BR-LMS-232]
brd_section: 7.14
doctypes: [Loan Security Release, Unpledge, Loan]
verdict: partial
analysis_status: verified
dev_items: []
fields: [Loan Security Release.Status]
options: [Loan Security Release.Status=Requested, Loan Security Release.Status=Approved]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_security_release/loan_security_release.py:154-167"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-232"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p56"
  - "sources/verification/reqs.json#BR-LMS-232"
  - "sources/verification/verification_report.md#BR-LMS-232"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-232"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-232"
  - "sources/verification/FINAL_REPORT.md#new-items-found-in-verification-nd-1-...-nd-47"
related: [concept.BR-LMS-232, lifecycle.CLOSED, lifecycle.CLOSURE_REQUESTED, bridge.BR-LMS-230, bridge.BR-LMS-171c]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. A Loan Security Release works and shows in the Loan Security Ledger report, but approving it overwrites the loan's closure date with today's date. Any Loan Manager can set the approval.

## Business need

Collateral must be released after approval and the release recorded in the security ledger (BR-LMS-232 in section 7.14, BRD PDF page 56). See `concept.BR-LMS-232`.

## Frappe Lending today

A **Loan Security Release** is a submittable document with a **Status** of Requested or Approved and a table of securities with quantities (**Unpledge**). On save it checks the quantity against what is pledged and that the loan-to-value ratio still holds after the release (`lending/loan_management/doctype/loan_security_release/loan_security_release.py`). When the Status is set to Approved after submit, the approval step stamps the unpledge time and calls `update_loan_status` (`lending/loan_management/doctype/loan_security_release/loan_security_release.py:140-167`). When no pledged quantity is left, that call sets the loan to Closed with a closure date of today's date. The Loan Security Ledger report reads the Pledge and Unpledge rows (`lending/loan_management/report/loan_security_ledger/loan_security_ledger.py:77-111`).

## Match or gap, and why

This is **partly covered**. The original analysis said covered, and the verification moved it (J9).

- Approving a release after the loan is closed overwrites the closure date with today's date (DEF-37). In the test, Loan G closed on 1 November and showed 3 November after the release was approved; L7-1 moved from 6 December to 3 November.
- The status update runs even when the loan is already Closed.
- The approval is a field on the same document, set by a user who can write it. The role list has Loan Manager with submit and write, which is the same role that creates the release, so there is no separate approver step (checked in the definition).
- In the test, the closure did not wait for the collateral: L7-1 closed with 143 units still pledged, and the release came afterwards.

## What to do today

Record the release approval in a register outside the system with the approver's name. After every release, check the loan's closure date against the date of the closing repayment and correct it by hand.

## Planned fix

Dev item ND-35 (closure control, including a closure date set once, medium) is proposed in the final report, and ND-39 (a refund must not close the loan, small). Question Q9 to NRB asks whether the closure date is the value date, approval date or release date.
