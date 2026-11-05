---
id: bridge.BR-LMS-185
type: bridge
title: Manual corrections need two people and a full record
summary: "Partly covered. Waivers, capitalisations, a carry-forward type and a Loan Balance Adjustment exist, but one user can make and submit each, no approver or before and after amounts are stored, and a balance adjustment accepts any account and any amount."
br_ids: [BR-LMS-185]
brd_section: 7.9
doctypes: [Loan Repayment, Loan Balance Adjustment, Loan Restructure]
verdict: partial
analysis_status: verified
dev_items: [D8]
fields: [Loan Repayment.Repayment Type]
options: [Loan Repayment.Repayment Type=Interest Waiver, Loan Repayment.Repayment Type=Penalty Waiver, Loan Repayment.Repayment Type=Interest Capitalization, Loan Repayment.Repayment Type=Interest Carry Forward]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_repayment/loan_repayment.py:1057", "lending/loan_management/doctype/loan_balance_adjustment/loan_balance_adjustment.py:46-50"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-185"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p53"
  - "sources/verification/reqs.json#BR-LMS-185"
  - "sources/verification/verification_report.md#BR-LMS-185"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-185"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-185"
  - "sources/verification/FINAL_REPORT.md#new-items-found-in-verification-nd-1-...-nd-47"
  - "sources/verification/FINAL_REPORT.md#D8"
related: [concept.BR-LMS-185, decision.waiver, devitem.D8, bridge.BR-LMS-182]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. Waivers, capitalisations, a carry-forward type and a Loan Balance Adjustment exist, but one user can make and submit each, no approver or before and after amounts are stored, and a balance adjustment accepts any account and any amount.

## Business need

Manual adjustments (waiver, capitalisation, carry-forward, approved balance correction) must run under maker-checker, recording amounts before and after, the reason, the approver and a reference (BR-LMS-185 in section 7.9, BRD PDF page 53). See `concept.BR-LMS-185`. What the app does about waivers in general is in `decision.waiver`.

## Frappe Lending today

A **Loan Repayment** can be of type Interest Waiver, Penalty Waiver, Charges Waiver, Interest Capitalization, Penalty Capitalization, Charges Capitalization, Principal Capitalization or Interest Carry Forward (`lending/loan_management/doctype/loan_repayment/loan_repayment.json:374`). A waiver larger than the overdue amount is refused (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:1057`). A **Loan Balance Adjustment** records a credit or debit adjustment against an account the user chooses, with a reference number and remarks. Its only checks are that the amount is not zero or negative and that no restructure is in process (`lending/loan_management/doctype/loan_balance_adjustment/loan_balance_adjustment.py:46-50`, `lending/loan_management/doctype/loan_balance_adjustment/loan_balance_adjustment.py:73-78`).

## Match or gap, and why

This is **partly covered**, and the verification confirmed the verdict (J6).

- In the test, an Interest Waiver of 500 and a Penalty Waiver of 100 were submitted directly by the test user, with no draft-and-approve step. The refusal of a waiver above the overdue amount was the only limit; there is no limit by role or amount.
- A Loan Balance Adjustment of 50 against Interest Income on Loans was accepted, and so was one of 50 against Interest Waiver. A draft credit adjustment of 10,000,000 against Cash was accepted when saved (it was deleted and never submitted).
- The reason and the reference are optional free text. There is no approver and no before and after amount on the record.
- A Loan Balance Adjustment is not reset by a later restructure and is deducted twice from the pending principal (DEF-24). It is also missing from the Loan Statement of Account (DEF-25).
- The waivers, the balance adjustment and the capitalisations seen on restructures were tested. Interest Carry Forward was not tested.

## What to do today

Have a second person approve every waiver, capitalisation and balance adjustment outside the system and attach the memo reference to the remarks. Restrict the Loan Manager role to people who may make these entries.

## Planned fix

Dev item D8 (approval and audit pack) covers this row. The final report names ND-23, maker-checker on waivers, capitalisation and balance adjustment (medium).
