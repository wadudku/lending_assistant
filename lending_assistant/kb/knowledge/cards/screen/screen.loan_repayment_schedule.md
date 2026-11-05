---
id: screen.loan_repayment_schedule
type: screen
title: "Screen: Loan Repayment Schedule"
summary: "The Loan Repayment Schedule screen shows the instalments of a loan, row by row, with principal, interest, total and balance."
br_ids: [BR-LMS-123, BR-LMS-155, BR-LMS-159]
brd_section: 7.3
doctypes: [Loan Repayment Schedule]
dev_items: []
fields: [Loan Repayment Schedule.Loan, Loan Repayment Schedule.Status, Loan Repayment Schedule.Loan Amount, Loan Repayment Schedule.Rate Of Interest, Loan Repayment Schedule.Repayment Start Date, Loan Repayment Schedule.Maturity Date, Loan Repayment Schedule.Repayment Schedule, Loan Repayment Schedule.Loan Partner, Loan Repayment Schedule.Moratorium Tenure]
options: [Loan Repayment Schedule.Status=Active, Loan Repayment Schedule.Status=Outdated, Loan Repayment Schedule.Status=Restructured]
menus: [Lending > Loan Management > Loan Repayment Schedule]
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_repayment_schedule/loan_repayment_schedule.json]
images: [/assets/lending_assistant/kb_img/J1/J1-S3-02_schedule-header-active.png, /assets/lending_assistant/kb_img/J1/J1-S3-04_schedule-12-rows.png]
sources:
  - "sources/verification/walkthroughs/J1_walkthrough.md#stage-3"
  - "sources/verification/walkthroughs/J1_walkthrough.md#3.1"
  - "sources/verification/walkthroughs/J1_walkthrough.md#3.2"
  - "sources/verification/walkthroughs/J1_walkthrough.md#3.3"
  - "sources/verification/walkthroughs/J1_walkthrough.md#3.4"
  - "sources/verification/reqs.json#BR-LMS-123"
related: [howto.loan_repayment_schedule.view, howto.loan.submit, screen.loan, screen.loan_disbursement, brd_section.7.3, bridge.BR-LMS-123, bridge.BR-LMS-155, bridge.BR-LMS-159, glossary.schedule-version]
version: 1
status: approved
approved_by: Owner
---
**In short:** The Loan Repayment Schedule screen shows the instalments of a loan, row by row, with principal, interest, total and balance.

## What this screen is for

**Loan Repayment Schedule** lists the instalments a loan will bill (menu: Lending > Loan Management > Loan Repayment Schedule). The system builds it when a term loan is disbursed; the officer normally opens it from the loan's Connections tab rather than creating one. When a loan is paid out in several draws, each draw rebuilds the schedule: the old one becomes **Outdated** and a new one is **Active** (J1 walkthrough 3.3, shown on a loan checked in verification).

## Before and after

Before: the loan is disbursed (`screen.loan_disbursement`). After: the daily jobs read the schedule's rows to accrue interest and to raise demands (`screen.loan_interest_accrual`, `screen.loan_demand`). To read a schedule step by step, see `howto.loan_repayment_schedule.view`.

## Key fields

**Loan**, **Status** (the options include Active, Outdated and Restructured), **Loan Amount**, **Rate Of Interest**, **Repayment Start Date**, **Maturity Date** and the **Repayment Schedule** table. In the J1 example a 100,000 loan at 14% over 12 months showed 12 rows. Each row shows the payment date, days, principal, interest, total and balance; interest follows actual days, so rows differ and the last row takes the rounding. The **Co Lending** tab holds **Loan Partner** and the partner's rate and share; in the example no partner was set, so those were zero or blank.

![The schedule header, status Active](/assets/lending_assistant/kb_img/J1/J1-S3-02_schedule-header-active.png)

![All 12 schedule rows](/assets/lending_assistant/kb_img/J1/J1-S3-04_schedule-12-rows.png)

## BRD needs it serves

BR-LMS-123 in BRD 7.3 (see `brd_section.7.3`), and BR-LMS-155 and 159 in the restructuring rows; the bridges hold the verdicts. The installed doctype gives System Manager and Loan Manager read, write, create, submit and delete, and Loan Reporter read only.
