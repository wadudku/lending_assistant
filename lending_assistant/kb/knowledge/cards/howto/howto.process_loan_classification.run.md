---
id: howto.process_loan_classification.run
type: howto
title: How to run loan classification for a date
summary: "Classification counts days past due and sets the grade; in production the nightly job runs it for yesterday, and an officer can run it for one loan and a past date."
br_ids: [BR-LMS-163, BR-LMS-190, BR-LMS-144]
brd_section: 7.9
doctypes: [Process Loan Classification]
dev_items: []
journeys: [J3, J4, J6, J8]
actions: ["Process Loan Classification:run"]
fields: [Process Loan Classification.Posting Date, Process Loan Classification.Loan, Process Loan Classification.Force Update DPD in Loan, Process Loan Classification.Is Backdated]
options: []
menus: []
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J3/J3-S4-04_classification-run-filled.png, /assets/lending_assistant/kb_img/J3/J3-S4-05_classification-run-submitted.png]
sources:
  - "sources/verification/walkthroughs/J3_walkthrough.md#stage-4"
  - "sources/verification/walkthroughs/J3_walkthrough.md#4.2"
  - "sources/verification/walkthroughs/J4_walkthrough.md#1.3"
  - "sources/verification/walkthroughs/J4_walkthrough.md#2.1"
  - "sources/verification/walkthroughs/J4_walkthrough.md#4.2"
related: [howto.days_past_due_log.view, bridge.BR-LMS-190, bridge.BR-LMS-144, journey.J3]
version: 1
status: approved
approved_by: Owner
---
**In short:** Classification counts days past due and sets the grade; in production the nightly job runs it for yesterday, and an officer can run it for one loan and a past date.

## Before you start

⚠ You need permission to create and submit a **Process Loan Classification**. The scheduler is paused on the dev site, so the walkthroughs ran it from the form. Names in the screenshots are test records.

## Steps

1. Type Process Loan Classification in the search bar and click + Add.
2. Enter **Posting Date**, the date to count days past due for.
3. Pick the **Loan**. It is required for a back-dated run.
4. Tick **Force Update DPD in Loan** when the date is not yesterday, otherwise the loan itself is not updated. The J4 and J8 walkthroughs ticked it for dates in the past and for today.
5. Click **Save**, then **Submit** and **Yes**. The loan can take several seconds to update.

![The run, filled](/assets/lending_assistant/kb_img/J3/J3-S4-04_classification-run-filled.png)

## What you should see

The run is Submitted with the posting date. The Days Past Due Log gets a row for that date, and the loan's days past due and grade follow (`howto.days_past_due_log.view`). For a loan paid on its due date the count is 0.

![The run, submitted](/assets/lending_assistant/kb_img/J3/J3-S4-05_classification-run-submitted.png)

## If it looks wrong

When the date is in the past and Force Update DPD in Loan is off, the run only rewrites the log rows from that date. If the loan still shows an old count, run it again with the tick on. Submitting a repayment also creates a classification run by itself, so a log row may already exist when you look. See `bridge.BR-LMS-190` for the days-past-due requirement.
