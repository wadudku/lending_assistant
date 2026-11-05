---
id: concept.BR-LMS-120
type: concept
title: Build the first repayment plan
summary: "When a funded loan is booked, the system builds its first repayment plan from the amount, rate, term, dates, payment frequency and any payment holiday."
br_ids: [BR-LMS-120]
brd_section: 7.3
doctypes: []
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-120"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p47"
  - "sources/verification/reqs.json#BR-LMS-120"
  - "sources/verification/verification_report.md#BR-LMS-120"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-120"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-120"
related: [bridge.BR-LMS-120, brd_section.7.3, devitem.D1, glossary.moratorium, glossary.emi, lifecycle.BOOKED]
version: 1
status: approved
approved_by: Owner
---
**In short:** When a funded loan is booked, the system builds its first repayment plan from the amount, rate, term, dates, payment frequency and any payment holiday.

## What the rule says

BR-LMS-120 (priority Must, BRD 7.3, PDF page 47) says that on booking the platform generates the initial repayment schedule from the confirmed funded amount, the rate, the tenor, the start and due dates, the payment frequency and any moratorium.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that every later bill, interest figure and statement is read from the schedule, so it has to exist from the first day and rest on the figures that were actually paid out.

## Example

A loan of 100,000 BDT at 14% for 12 months, paid monthly with the first due date on 5 July 2026, gives 12 rows of about 8,979 each, from 5 July 2026 to 5 June 2027.

## Terms to know

- **Repayment schedule:** the table of due dates and amounts for the whole loan.
- **Tenor:** the length of the loan.
- **Moratorium:** a payment holiday. See `glossary.moratorium`.
- **EMI:** the equal monthly instalment. See `glossary.emi`.
