---
id: bridge.BR-LMS-188
type: bridge
title: Report restructures and waivers to Bangladesh Bank
summary: "Gap. Frappe Lending has no Bangladesh Bank report of restructures, reschedules or waivers and no field for the regulatory treatment. The only related feature is the watch period after a restructure of an NPA loan."
br_ids: [BR-LMS-188]
brd_section: 7.9
doctypes: [Loan Restructure, Loan Repayment]
verdict: gap
analysis_status: verified
dev_items: [D16]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_restructure/loan_restructure.py:583-594"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-188"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p53"
  - "sources/verification/reqs.json#BR-LMS-188"
  - "sources/verification/verification_report.md#BR-LMS-188"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-188"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-188"
  - "sources/verification/FINAL_REPORT.md#new-items-found-in-verification-nd-1-...-nd-47"
  - "sources/verification/FINAL_REPORT.md#D16"
related: [concept.BR-LMS-188, decision.restructure, lifecycle.RESTRUCTURED, bridge.BR-LMS-182, devitem.D16]
version: 1
status: approved
approved_by: Owner
---
**In short:** Gap. Frappe Lending has no Bangladesh Bank report of restructures, reschedules or waivers and no field for the regulatory treatment. The only related feature is the watch period after a restructure of an NPA loan.

## Business need

Each restructure, reschedule or waiver must be reported to Bangladesh Bank and carry a recorded regulatory treatment (BR-LMS-188 in section 7.9, BRD PDF page 53). See `concept.BR-LMS-188`. The other missing controls are in `decision.restructure`.

## Frappe Lending today

The lending app ships eleven report folders: ALM Audit, Applicant-Wise Loan Security Exposure, Disbursement Analysis, Future Cashflow, Loan Outstanding, Loan Repayment and Closure, Loan Security Exposure, Loan Security Ledger, Loan Security Status, Loan Statement of Account and Past Cashflow. None of them lists restructures, reschedules or waivers. Nothing in the app's code, fields or reports mentions Bangladesh Bank or a regulatory treatment. The one related feature is a watch period: approving a Normal Restructure on an NPA loan sets a watch end date from a Company setting (`lending/loan_management/doctype/loan_restructure/loan_restructure.py:583-594`), and the Unmark NPA option is refused until that date (`lending/loan_management/doctype/loan/loan.py:485-486`). The classification code can also set a watch date for an NPA loan that has a restructure on record (`lending/loan_management/doctype/loan/loan.py:1343-1352`). The Loan Restructure form's treatment fields (Treatment Of Penal Interest, Treatment Of Normal Interest) are about overdue amounts, not about the regulator.

## Match or gap, and why

This is a **gap**, and the verification confirmed it (J6).

- No report, field or tag records which rule was applied to a restructure, a reschedule or a waiver.
- A Normal Restructure re-ages the loan to 0 days past due, and in the test a loan graded SMA went back to STD within seconds (see `bridge.BR-LMS-182`). No field holds a grade because of a regulatory rule.
- In the test, an Advance Payment and a Pre Payment set no watch period. The watch period is the only feature that follows a restructure of an NPA loan, and it is a date, not a treatment.

## What to do today

Keep a register of every restructure, reschedule and waiver, with the Bangladesh Bank treatment applied, in a sheet outside the system, and file the report by hand.

## Planned fix

Dev item D16 (Bangladesh Bank treatment, sized large) covers this row. The final report proposes a restructure model with the regulator's categories that blocks re-ageing (ND-22), and some of it waits on answers from NRB (Q6).
