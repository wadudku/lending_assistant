---
id: howto.process_loan_interest_accrual.run
type: howto
title: How to run the daily interest accrual for one loan
summary: "In production the nightly job accrues interest for yesterday on every loan; where the scheduler is paused, an officer runs the same job from the Process Loan Interest Accrual form, scoped to one loan."
br_ids: [BR-LMS-140]
brd_section: 7.4
doctypes: [Process Loan Interest Accrual]
dev_items: []
journeys: [J3, J4, J8, J11]
actions: ["Process Loan Interest Accrual:run"]
fields: [Process Loan Interest Accrual.Posting Date, Process Loan Interest Accrual.Company, Process Loan Interest Accrual.Loan]
options: []
menus: []
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J3/J3-S1-01_accrual-run-filled.png, /assets/lending_assistant/kb_img/J3/J3-S1-02_accrual-run-submitted.png]
sources:
  - "sources/verification/walkthroughs/J3_walkthrough.md#stage-1"
  - "sources/verification/walkthroughs/J3_walkthrough.md#1.1"
related: [howto.loan_interest_accrual.view, bridge.BR-LMS-140, journey.J3]
version: 1
status: approved
approved_by: Owner
---
**In short:** In production the nightly job accrues interest for yesterday on every loan; where the scheduler is paused, an officer runs the same job from the Process Loan Interest Accrual form, scoped to one loan.

## Before you start

⚠ You need permission to create and submit a **Process Loan Interest Accrual**. In production the daily scheduled job does this for yesterday, for all loans, so you normally do not run it by hand. On the dev site the scheduler is paused, so the walkthrough ran it from the form. Names in the screenshots are test records.

## Steps

1. Type Process Loan Interest Accrual in the search bar and click + Add.
2. Enter **Posting Date**: the day up to which interest should be counted, for example the day before the first due date.
3. Leave **Company** as it is.
4. Pick the **Loan**. Always set it, so the run touches only this loan.
5. Click **Save**, then **Submit** and **Yes**.

![The run, filled](/assets/lending_assistant/kb_img/J3/J3-S1-01_accrual-run-filled.png)

## What you should see

The run is Submitted with the posting date and the loan. It creates one accrual per day up to that date (`howto.loan_interest_accrual.view`).

![The run, submitted](/assets/lending_assistant/kb_img/J3/J3-S1-02_accrual-run-submitted.png)

## If it looks wrong

If no rows appear, check the posting date and that the loan is Disbursed. A loan that is Closed, Draft, Settled or Written Off cannot be picked in the Loan field of this form. To catch up several missed days, the verification ran the job once per day with the scheduled function. The same run is also used before billing a due date (`howto.process_loan_demand.run`).
