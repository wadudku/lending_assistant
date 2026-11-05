---
id: screen.loan_interest_accrual
type: screen
title: "Screen: Loan Interest Accrual"
summary: The Loan Interest Accrual screen holds one day's interest on a loan; the daily job creates these records and posts them to the ledger.
br_ids: [BR-LMS-134, BR-LMS-140, BR-LMS-168]
brd_section: 7.5
doctypes: [Loan Interest Accrual]
dev_items: []
fields: [Loan Interest Accrual.Loan, Loan Interest Accrual.Posting Date (End Date), Loan Interest Accrual.Interest Amount, Loan Interest Accrual.Accrual Type, Loan Interest Accrual.Interest Type, Loan Interest Accrual.Rate Of Interest, Loan Interest Accrual.Base Amount]
options: [Loan Interest Accrual.Accrual Type=Regular, Loan Interest Accrual.Interest Type=Normal Interest, Loan Interest Accrual.Interest Type=Penal Interest]
menus: [Lending > Loan Management > Loan Interest Accrual]
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_interest_accrual/loan_interest_accrual.json]
images: [/assets/lending_assistant/kb_img/J3/J3-S1-03_accrual-list.png, /assets/lending_assistant/kb_img/J3/J3-S1-04_accrual-one-day-38-36.png]
sources:
  - "sources/verification/walkthroughs/J3_walkthrough.md#stage-1"
  - "sources/verification/walkthroughs/J3_walkthrough.md#1.1"
  - "sources/verification/walkthroughs/J3_walkthrough.md#1.2"
  - "sources/verification/walkthroughs/J3_walkthrough.md#1.3"
  - "sources/verification/reqs.json#BR-LMS-140"
related: [howto.loan_demand.view, screen.loan, screen.loan_repayment_schedule, screen.loan_demand, brd_section.7.5, bridge.BR-LMS-140, bridge.BR-LMS-142, bridge.BR-LMS-168]
version: 1
status: approved
approved_by: Owner
---
**In short:** The Loan Interest Accrual screen holds one day's interest on a loan; the daily job creates these records and posts them to the ledger.

## What this screen is for

**Loan Interest Accrual** holds the interest a loan earned for a day (menu: Lending > Loan Management > Loan Interest Accrual). The nightly job (`Process Loan Interest Accrual`) creates and submits one record per loan per day; the walkthrough only looks at them. Each record posts a ledger entry on submit.

## Before and after

Before: the loan is disbursed and its schedule is active (`screen.loan_repayment_schedule`). After: on the due date the accrued interest is billed as a demand (`screen.loan_demand`).

## Key fields

**Loan**, **Interest Amount**, **Accrual Type** (the options include Regular), **Interest Type** (Normal Interest or Penal Interest), **Rate Of Interest** and **Base Amount**. In the J3 example a 100,000 loan at 14% accrued 38.36 a day (100,000 x 14% / 365): 30 daily records from 05-06-2026 to 04-07-2026, 1,150.80 in all, against 1,150.68 in the first schedule row (0.12 of daily rounding). Each accrual posts a debit to Interest Accrued and a credit to Interest Income on Loans, dated the day of the run, not the accrual day.

![Thirty daily accrual records for one loan](/assets/lending_assistant/kb_img/J3/J3-S1-03_accrual-list.png)

![One day's accrual record (rate 14%)](/assets/lending_assistant/kb_img/J3/J3-S1-04_accrual-one-day-38-36.png)

## BRD needs it serves

BR-LMS-140 in BRD 7.5 (see `brd_section.7.5`), plus BR-LMS-134 and 168 where verified text names this screen; the bridges hold the verdicts. The installed doctype gives System Manager and Loan Manager read, write, create, submit, cancel and delete, and Loan Reporter read only.
