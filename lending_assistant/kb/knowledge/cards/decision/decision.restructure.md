---
id: decision.restructure
type: decision
title: "Decision: restructuring or rescheduling a loan"
summary: "A restructure changes a loan's terms for a borrower who struggles to pay. The BRD wants two people, limits by branch and period, and reporting to Bangladesh Bank. Frappe Lending has none of the three controls."
br_ids: [BR-LMS-182, BR-LMS-183, BR-LMS-184, BR-LMS-185, BR-LMS-188, BR-GOV-008]
brd_section: 7.9
doctypes: [Loan Restructure, Loan]
dev_items: [D16, D6, D8]
decision: restructure
actions: ["Loan Restructure:submit"]
options: [Loan Restructure.Restructure Type=Normal Restructure, Loan Restructure.Restructure Type=Pre Payment, Loan Restructure.Restructure Type=Advance Payment]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_restructure/loan_restructure.py:322", "lending/loan_management/doctype/loan_restructure/loan_restructure.py:328"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-182"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-183"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-184"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-185"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-188"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-008"
  - "sources/verification/reqs.json#BR-LMS-182"
  - "sources/verification/reqs.json#BR-LMS-183"
  - "sources/verification/reqs.json#BR-LMS-184"
  - "sources/verification/reqs.json#BR-LMS-185"
  - "sources/verification/reqs.json#BR-LMS-188"
  - "sources/verification/verification_report.md#BR-LMS-182"
  - "sources/verification/FINAL_REPORT.md#D16"
  - "sources/verification/FINAL_REPORT.md#D6"
  - "sources/verification/FINAL_REPORT.md#D8"
  - "sources/verification/FINAL_REPORT.md#revised-suggested-order"
related: [glossary.restructuring, glossary.rescheduling, lifecycle.RESTRUCTURED, devitem.D16, devitem.D6, devitem.D8]
version: 2
status: approved
approved_by: Owner
---
**In short:** A restructure changes a loan's terms for a borrower who struggles to pay. The BRD wants two people, limits by branch and period, and reporting to Bangladesh Bank. Frappe Lending has none of the three controls.

## The rule

BR-LMS-182 asks for rescheduling of dates and tenor and broader modification of financial terms, with the restructure type recorded. BR-LMS-183 requires a new schedule and the prior one preserved as restructured and superseded. BR-LMS-184 requires restructuring limits by branch and by period, with a utilisation log. BR-LMS-188 requires a restructure, reschedule or waiver to be reported to Bangladesh Bank and flagged in classification treatment, with the regulatory treatment recorded. BR-GOV-008 lists restructuring among the controlled financial changes that need maker-checker approval by two different users. The BRD does not name the approvers or the limits.

## Options

A **Loan Restructure** has a **Restructure Type** of Normal Restructure, Pre Payment or Advance Payment. For a Normal Restructure, the loan's restructure count rises (`lending/loan_management/doctype/loan_restructure/loan_restructure.py:322`, `lending/loan_management/doctype/loan_restructure/loan_restructure.py:328`) and the old schedule is marked Restructured; for the other two types it is marked Rescheduled (`lending/loan_management/doctype/loan_restructure/loan_restructure.py:599-601`). The form lets the user choose how overdue interest, penalty and unaccrued interest are treated: Capitalize, Add To First EMI or Carry Forward, depending on the field. Capitalizing creates automatic Interest, Penalty and Principal Capitalization repayments. There is no Bangladesh Bank style reschedule-versus-restructure category and no field for the regulatory treatment.

## Who approves

The BRD wants a maker and a different checker. In the test, there was no approval step on the restructure: the same user who requested it approved it, and the installed Loan Restructure doctype gives the Loan Manager role both create and submit. The monthly job that should enforce a limit is scheduled but could not select anything on 16.5.1 (no branch on the Loan or the Loan Restructure, no limit fields on Branch), so no limit was checked at approval and the usage log stayed empty (DEF-23).

## How Frappe Lending does it today

The verified results are partly covered for BR-LMS-182 and BR-LMS-185, covered for BR-LMS-183, and a gap for BR-LMS-184 (changed from covered) and BR-LMS-188. In the test, a Normal Restructure re-aged an overdue loan to 0 days past due; on an NPA loan it moved the uncollected suspense interest to income and cleared the customer's NPA flag (DEF-22). In the test, a Normal Restructure failed on all four test products (DEF-17) and counted accrued interest twice (DEF-18); the Pre Payment and Advance Payment types ran without error. The plan is a Bangladesh Bank model that blocks re-ageing (D16, ND-22), a limit that works (ND-24), schedule fixes (D6, ND-20) and the approval pack (D8). See `glossary.restructuring`, `glossary.rescheduling` and `lifecycle.RESTRUCTURED`.

*Codes:* DEF = defect, ND = new item, both found in verification (final report, sections 5 and 7).
