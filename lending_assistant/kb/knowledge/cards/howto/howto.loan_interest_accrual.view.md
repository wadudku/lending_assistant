---
id: howto.loan_interest_accrual.view
type: howto
title: How to see a loan's daily interest accruals
summary: "Each day of a loan has its own accrual row; the amount is the principal times the yearly rate over 365, and a month's accruals add up to the schedule's interest."
br_ids: [BR-LMS-140, BR-LMS-142]
brd_section: 7.4
doctypes: [Loan Interest Accrual]
dev_items: []
journeys: [J3]
actions: ["Loan Interest Accrual:view"]
fields: [Loan Interest Accrual.Loan, Loan Interest Accrual.Interest Amount]
options: []
menus: [Lending > Loan Management > Loan Interest Accrual]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J3/J3-S1-03_accrual-list.png, /assets/lending_assistant/kb_img/J3/J3-S1-04_accrual-one-day-38-36.png]
sources:
  - "sources/verification/walkthroughs/J3_walkthrough.md#stage-1"
  - "sources/verification/walkthroughs/J3_walkthrough.md#1.2"
  - "sources/verification/walkthroughs/J3_walkthrough.md#1.3"
related: [howto.process_loan_interest_accrual.run, bridge.BR-LMS-140, bridge.BR-LMS-142, journey.J3, screen.loan_interest_accrual]
version: 1
status: approved
approved_by: Owner
---
**In short:** Each day of a loan has its own accrual row; the amount is the principal times the yearly rate over 365, and a month's accruals add up to the schedule's interest.

## Before you start

⚠ This card is view only. You need read permission on **Loan Interest Accrual**. Names in the screenshots are test records on the dev site.

## Steps

1. Open Lending > Loan Management > Loan Interest Accrual.
2. Filter the list by **Loan**.
3. Open any row to see its **Interest Amount**.

![The accrual list, one row per day](/assets/lending_assistant/kb_img/J3/J3-S1-03_accrual-list.png)

## What you should see

For e.g. Rahim's 100,000 loan at 14%, there is one Submitted accrual per day, all Normal Interest and Regular. One day is 100,000 × 14% / 365 = 38.36. A 30-day month adds up to 1,150.80, against 1,150.68 for the same month in the repayment schedule: the small difference is daily rounding.

![One day's accrual](/assets/lending_assistant/kb_img/J3/J3-S1-04_accrual-one-day-38-36.png)

Each accrual is posted to the ledger as a debit to Interest Accrued and a credit to Interest Income on Loans.

Broken-period interest sits in the first instalment. A loan disbursed on its cycle day has no odd days, so the first row equals a regular month and the disbursement shows zero broken-period interest. For a loan with odd days, the verification's example added the extra interest to the first EMI (BR-LMS-142, covered).

## If it looks wrong

The 0.12 gap between accrued and billed interest stays in Interest Accrued and no report shows it (see `howto.loan_outstanding_report.view`). Only the first 20 rows show by default: use the page-size or Load More control to see them all.
