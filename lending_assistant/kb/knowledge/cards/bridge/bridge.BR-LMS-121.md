---
id: bridge.BR-LMS-121
type: bridge
title: Each row shows the split
summary: "Covered. Each schedule row stores principal, interest, total payment and the balance left."
br_ids: [BR-LMS-121]
brd_section: 7.3
doctypes: [Loan Repayment Schedule]
verdict: covered
analysis_status: verified
dev_items: []
fields: [Repayment Schedule.Principal Amount, Repayment Schedule.Interest Amount, Repayment Schedule.Total Payment, Repayment Schedule.Balance Loan Amount]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/repayment_schedule/repayment_schedule.json:28"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-121"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p48"
  - "sources/verification/reqs.json#BR-LMS-121"
  - "sources/verification/verification_report.md#BR-LMS-121"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-121"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-121"
related: [concept.BR-LMS-121, brd_section.7.3, glossary.bpi]
version: 1
status: approved
approved_by: Owner
---
**In short:** Covered. Each schedule row stores principal, interest, total payment and the balance left.

## Business need

The bank wants each schedule line to show the instalment with its principal, interest and closing balance (BR-LMS-121, BRD 7.3, PDF page 48). See `concept.BR-LMS-121`.

## Frappe Lending today

Each row of the **Loan Repayment Schedule** has **Payment Date**, **Number of Days**, **Principal Amount**, **Interest Amount**, **Total Payment** and **Balance Loan Amount**, and also **Charges** and **Demand Generated** (`repayment_schedule.json` lines 20-79).

## Match or gap, and why

This is **covered**. In the test, row 1 of a 12-row plan showed principal 4,697.59 and interest 759.45, giving 5,457.04, with a balance of 55,302.41 (verification_report.md:97). The interest on the first row includes the extra days before the first due date, added to the first instalment (the broken-period interest). The coverage analysis rated this row covered, and verification confirmed it.

## What to do today

Read the split from the schedule rows on the Loan Repayment Schedule.

## Planned fix

Nothing is needed.
