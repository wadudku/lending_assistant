---
id: lifecycle.RESTRUCTURED
type: lifecycle
title: Loan state RESTRUCTURED
summary: "In the BRD, RESTRUCTURED is a loan whose terms were changed under approval and whose new schedule version is now authoritative. In Frappe Lending it is a restructure count and a watch period, not a status."
br_ids: [BR-LMS-182, BR-LMS-183, BR-LMS-188]
brd_section: 5.3
doctypes: [Loan, Loan Restructure]
dev_items: [D2, D16]
lifecycle_state: RESTRUCTURED
fields: [Loan.Loan Restructure Count, Loan.Watch Period End Date]
options: []
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_restructure/loan_restructure.py:328", "lending/loan_management/doctype/loan_restructure/loan_restructure.py:586"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#5.3"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p27"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#5.1-the-two-lifecycles-side-by-side"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#5.2-the-main-difference"
  - "sources/verification/reqs.json#BR-LMS-182"
  - "sources/verification/reqs.json#BR-LMS-183"
  - "sources/verification/reqs.json#BR-LMS-188"
  - "sources/verification/verification_report.md#BR-LMS-182"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-182"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-183"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-188"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D2"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D16"
  - "sources/verification/reqs.json#BR-LMS-188"
related: [brd_section.5.3, lifecycle.OVERDUE, lifecycle.NPA, glossary.restructuring, glossary.schedule-version, devitem.D16, devitem.D2]
version: 2
status: approved
approved_by: Owner
---
**In short:** In the BRD, RESTRUCTURED is a loan whose terms were changed under approval and whose new schedule version is now authoritative. In Frappe Lending it is a restructure count and a watch period, not a status.

## The BRD state

BRD 5.3 (PDF page 27) defines RESTRUCTURED as: terms modified under approval; a new schedule version is authoritative. BR-LMS-183 adds that the old schedule is kept, marked as restructured and superseded.

## The Frappe Lending equivalent

There is no Restructured loan status. A restructure is recorded in the **Loan Restructure** doctype. For a Normal Restructure only, the loan's **Loan Restructure Count** goes up (`lending/loan_management/doctype/loan_restructure/loan_restructure.py:328`). The old schedule is marked Restructured for a Normal Restructure and Rescheduled for the other types (`lending/loan_management/doctype/loan_restructure/loan_restructure.py:599`, `lending/loan_management/doctype/loan_restructure/loan_restructure.py:601`), and a new schedule becomes Active. In the restructure code, a **Watch Period End Date** is set only when the loan is NPA (`lending/loan_management/doctype/loan_restructure/loan_restructure.py:586`). The verified result is covered for BR-LMS-183 and partly covered for BR-LMS-182.

## Why they differ

The BRD describes one state; Frappe Lending spreads it over a count, a date and a schedule status. In the test, a Normal Restructure also set the days past due to 0 (`lending/loan_management/doctype/loan_restructure/loan_restructure.py:598`), so an overdue loan was re-aged, and on an NPA loan the uncollected suspense interest went to income and the customer's NPA flag was cleared (DEF-22). The test approver was the same user who requested the restructure. BR-LMS-188 asks that each restructure is reported to Bangladesh Bank with its treatment recorded; no such field or report exists (D16).

## How a loan enters and leaves it

A loan enters this state when a Normal Restructure is approved: the count rises and the new schedule takes over. The count stays on the loan. Where a watch period was set, the Unmark NPA option is refused before its end date (`lending/loan_management/doctype/loan/loan.py:486`). The Servicing Status proposal (D2) would show RESTRUCTURED only inside the watch period.

*Codes:* DEF = defect, ND = new item, both found in verification (final report, sections 5 and 7).
