---
id: howto.loan_demand.view_penalty
type: howto
title: How to see what an overdue loan is billed for being late
summary: "After a missed EMI, the system bills a daily Additional Interest demand on the overdue amount; there is no demand called Penalty, and the bill is not the product's penal rate."
br_ids: [BR-LMS-190, BR-LMS-141]
brd_section: 7.9
doctypes: [Loan Demand]
dev_items: []
journeys: [J4]
actions: ["Loan Demand:view_penalty"]
fields: [Loan Demand.Demand Type, Loan Demand.Demand Date]
options: [Loan Demand.Demand Type=Additional Interest, Loan Demand.Demand Type=EMI]
menus: [Lending > Loan Management > Loan Demand]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J4/J4-S1-09_additional-interest-demands.png, /assets/lending_assistant/kb_img/J4/J4-S1-10_emi-demands.png]
sources:
  - "sources/verification/walkthroughs/J4_walkthrough.md#stage-1"
  - "sources/verification/walkthroughs/J4_walkthrough.md#1.1"
  - "sources/verification/walkthroughs/J4_walkthrough.md#1.2"
  - "sources/verification/walkthroughs/J4_walkthrough.md#1.3"
  - "sources/verification/walkthroughs/J4_walkthrough.md#1.4"
  - "sources/verification/walkthroughs/J4_walkthrough.md#1.5"
related: [howto.process_loan_interest_accrual.run, howto.process_loan_demand.run, howto.process_loan_classification.run, bridge.BR-LMS-141, bridge.BR-LMS-190, journey.J4, screen.loan_demand]
version: 1
status: approved
approved_by: Owner
---
**In short:** After a missed EMI, the system bills a daily Additional Interest demand on the overdue amount; there is no demand called Penalty, and the bill is not the product's penal rate.

## Before you start

⚠ This card is view only. You need read permission on **Loan Demand**. The walkthrough brought a loan to this state by running, for each month, the interest accrual and the demand run (`howto.process_loan_interest_accrual.run`, `howto.process_loan_demand.run`) and then classification for day 1 (`howto.process_loan_classification.run`), with no payment in between. Names in the screenshots are test records on the dev site.

## Steps

1. Open Lending > Loan Management > Loan Demand.
2. Filter by loan and set **Demand Type** to Additional Interest.
3. Change the filter to EMI to see the unpaid instalments.

![Additional Interest demands, one per overdue day](/assets/lending_assistant/kb_img/J4/J4-S1-09_additional-interest-demands.png)

## What you should see

One Additional Interest demand for each overdue day, starting the day after the due date, and the two unpaid EMI demands. In e.g. Rahim's loan, the 31 days between the first and second due dates gave 31 small demands, 92.69 in all.

![The unpaid EMI demands](/assets/lending_assistant/kb_img/J4/J4-S1-10_emi-demands.png)

## If it looks wrong

The BRD wants penalty interest at the product's penal rate on the overdue amount, kept apart from contract interest (BR-LMS-141, partly covered). What is billed is contract-rate interest on the overdue principal, and the penal accrual shows only as a small, sometimes negative penalty line (DEF-10). The demands start the day after the due date even with grace days, and a payment made inside grace but entered after a later run still pays that penalty (DEF-11). On the product copied from the standard personal-loan product, the Additional Interest income, accrued, receivable and suspense accounts are all one account, so those postings net to zero in it (configuration note CF-2). The verification names ND-13 as the fix. See `bridge.BR-LMS-141`.
