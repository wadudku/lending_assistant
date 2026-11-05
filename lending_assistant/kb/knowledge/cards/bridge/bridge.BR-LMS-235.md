---
id: bridge.BR-LMS-235
type: bridge
title: "Closure letter, final statement and a message"
summary: "Partly covered. The Loan Statement of Account report and its scheduled email work. There is no closure letter, and no message is sent when a loan closes."
br_ids: [BR-LMS-235]
brd_section: 7.14
doctypes: [Loan, Process Loan Statement of Accounts]
verdict: partial
analysis_status: verified
dev_items: [D20]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-235"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p56"
  - "sources/verification/reqs.json#BR-LMS-235"
  - "sources/verification/verification_report.md#BR-LMS-235"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-235"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-235"
  - "sources/verification/FINAL_REPORT.md#new-items-found-in-verification-nd-1-...-nd-47"
  - "sources/verification/FINAL_REPORT.md#D20"
related: [concept.BR-LMS-235, bridge.BR-LMS-230, bridge.BR-LMS-233, devitem.D20]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. The Loan Statement of Account report and its scheduled email work. There is no closure letter, and no message is sent when a loan closes.

## Business need

On closure the platform must produce a payoff or closure confirmation and a final statement, and notify the borrower (BR-LMS-235 in section 7.14, BRD PDF page 56). See `concept.BR-LMS-235`.

## Frappe Lending today

The **Loan Statement of Account** report lists every posting on a loan with a running balance. **Process Loan Statement of Accounts** can schedule it and email it to the borrower. In the test the report ran on a closed loan, a Settled loan and a Written Off loan, and showed each posting with remarks. The lending app ships no print format and no notification. In the test, the site had no Print Format for the Loan and no Notification on the Loan.

## Match or gap, and why

This is **partly covered**, and the verification confirmed the verdict (J9). The final statement half is covered. The other two halves are not.

- There is no closure or payoff letter, so the borrower has no proof of closure from the system.
- No code in the lending app sends a message when a loan closes; its only sendmail is the scheduled statement of accounts (`lending/loan_management/doctype/process_loan_statement_of_accounts/process_loan_statement_of_accounts.py:330`).
- A closed loan's statement may not end at 0: on one test loan a waiver that was part of the closure left a balance of 18.93, because the credit counts the amount paid only (the same family as DEF-25).
- On one closed loan the statement listed the waiver above the repayment made on the same date.

## What to do today

Make the closure letter as a print format outside the lending app and send it by hand. Check each final statement's closing balance before sending it.

## Planned fix

Dev item D20 (small items, 235 sized small) covers this row. The final report proposes ND-37 (refund approval, closure letter and notification, small).
