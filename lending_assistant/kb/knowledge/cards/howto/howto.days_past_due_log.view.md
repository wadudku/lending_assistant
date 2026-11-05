---
id: howto.days_past_due_log.view
type: howto
title: "How to read a loan's days past due, in the log and on the loan"
summary: The Days Past Due Log keeps one row per loan per date; the loan itself shows the current days past due and grade.
br_ids: [BR-LMS-190, BR-LMS-132]
brd_section: 7.9
doctypes: [Days Past Due Log, Loan]
dev_items: [D7]
journeys: [J3, J4]
actions: ["Days Past Due Log:view"]
fields: [Days Past Due Log.Loan, Days Past Due Log.Posting Date, Days Past Due Log.Days Past Due, Loan.Days Past Due]
options: []
menus: [Lending > Loan Management > DPD Log]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J3/J3-S4-06_dpd-log-07-05-zero.png, /assets/lending_assistant/kb_img/J3/J3-S4-08_loan-dpd-zero.png]
sources:
  - "sources/verification/walkthroughs/J3_walkthrough.md#stage-4"
  - "sources/verification/walkthroughs/J3_walkthrough.md#4.3"
  - "sources/verification/walkthroughs/J3_walkthrough.md#4.4"
  - "sources/verification/walkthroughs/J4_walkthrough.md#2.2"
related: [howto.process_loan_classification.run, bridge.BR-LMS-190, journey.J3, screen.days_past_due_log, screen.loan]
version: 1
status: approved
approved_by: Owner
---
**In short:** The Days Past Due Log keeps one row per loan per date; the loan itself shows the current days past due and grade.

## Before you start

⚠ This card is view only. You need read permission on **Days Past Due Log** and **Loan**. The rows exist after a classification run (`howto.process_loan_classification.run`). Names in the screenshots are test records on the dev site.

## Steps

1. Open Lending > Loan Management > DPD Log.
2. Filter by **Loan** and by **Posting Date**.
3. Read **Days Past Due** on the row.
4. Open the loan and read Days Past Due under Loan Classification Details.

![The log row for the due date](/assets/lending_assistant/kb_img/J3/J3-S4-06_dpd-log-07-05-zero.png)

## What you should see

For a loan paid on its due date, the row for that date shows Days Past Due 0, with a link to the disbursement. The loan shows its Disbursed status, 0 days past due and a restructure count of 0. It is not marked NPA and has no classification code.

![The loan: days past due 0](/assets/lending_assistant/kb_img/J3/J3-S4-08_loan-dpd-zero.png)

## If it looks wrong

The loan's own days past due is its current value, so use the log for the count on a past date. This is what the BRD asks for when it wants the days past due at a date (BR-LMS-132 is partly covered, with D7 as the verification's fix). If the log has no row for the date, run classification for it. See `bridge.BR-LMS-190`.
