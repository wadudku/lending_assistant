---
id: howto.loan_repayment_schedule.view
type: howto
title: How to read a loan's repayment schedule
summary: "Open the Loan Repayment Schedule from the loan to see each instalment split into principal and interest, with the balance after it."
br_ids: []
brd_section: 7.3
doctypes: [Loan Repayment Schedule]
dev_items: []
journeys: [J1]
actions: ["Loan Repayment Schedule:view"]
fields: [Loan Repayment Schedule.Rate Of Interest, Loan Repayment Schedule.Repayment Start Date, Loan Repayment Schedule.Maturity Date, Loan Repayment Schedule.Repayment Schedule]
menus: [Lending > Loan Management > Loan Repayment Schedule]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J1/J1-S3-01_schedule-from-loan-connections.png, /assets/lending_assistant/kb_img/J1/J1-S3-02_schedule-header-active.png, /assets/lending_assistant/kb_img/J1/J1-S3-04_schedule-12-rows.png, /assets/lending_assistant/kb_img/J1/J1-S3-05_co-lending-tab-empty.png]
sources:
  - "sources/verification/walkthroughs/J1_walkthrough.md#stage-3"
  - "sources/verification/walkthroughs/J1_walkthrough.md#3.1"
  - "sources/verification/walkthroughs/J1_walkthrough.md#3.2"
  - "sources/verification/walkthroughs/J1_walkthrough.md#3.4"
  - "sources/verification/walkthroughs/J1_walkthrough.md#3.3"
  - "sources/verification/walkthroughs/J1_walkthrough.md#1.3"
related: [howto.loan.view, howto.loan.submit, journey.J1]
version: 1
status: approved
approved_by: Owner
---
**In short:** Open the Loan Repayment Schedule from the loan to see each instalment split into principal and interest, with the balance after it.

## Before you start

Read permission is enough. Names you see in the screenshots, such as customer and loan names, are test records on the dev site.

## Steps

1. Open the loan, then **Connections**, then **Loan Repayment Schedule**, and open the one schedule.
2. Read the header: **Loan**, **Loan Disbursement**, **Loan Amount**, **Rate Of Interest**, **Repayment Start Date**, **Maturity Date**.
3. Scroll to the **Repayment Schedule** table and read the rows.
4. Open the **Co Lending** tab to see partner details.

![Schedule found from the loan Connections tab](/assets/lending_assistant/kb_img/J1/J1-S3-01_schedule-from-loan-connections.png)

## What you should see

Status **Active** and, for a 12-month loan, 12 rows. Each row has **Payment Date**, **Principal Amount**, **Interest Amount**, **Total Payment** and **Balance Loan Amount**. In the example, row 1 is 7,828.32 principal plus 1,150.68 interest, 8,979.00 in total, and the last row takes the rounding (8,988.22). Interest follows the actual days in each month, so the split differs row by row.

![Schedule header, status Active](/assets/lending_assistant/kb_img/J1/J1-S3-02_schedule-header-active.png)

![All twelve schedule rows](/assets/lending_assistant/kb_img/J1/J1-S3-04_schedule-12-rows.png)

The **Co Lending** tab shows zeros and no partner when co-lending is not set up for the loan.

![Co Lending tab with no partner](/assets/lending_assistant/kb_img/J1/J1-S3-05_co-lending-tab-empty.png)

## If it looks wrong

If the first row is larger than the instalment, the disbursement did not fall on the cycle day and broken-period interest was added. When money is paid out in parts, each payout rebuilds the plan and the earlier schedule becomes Outdated. The system, not the user, creates the schedule when the loan is submitted (`howto.loan.submit`).
