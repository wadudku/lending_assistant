---
id: howto.loan_repayment_schedule.compare_plans
type: howto
title: How to compare draft plans and read the old and new plan after a restructure
summary: "Each draft restructure builds a draft plan; after approval the old plan is kept as Restructured or Rescheduled and a new plan is Active, with no link from the old plan to the new one."
br_ids: [BR-LMS-152, BR-LMS-125, BR-LMS-126, BR-LMS-183]
brd_section: 7.6
doctypes: [Loan Repayment Schedule, Loan Restructure]
dev_items: [D6, D11]
journeys: [J5, J6]
actions: ["Loan Repayment Schedule:compare_plans"]
fields: [Loan Repayment Schedule.Status, Loan Repayment Schedule.Loan Restructure]
options: [Loan Repayment Schedule.Status=Active, Loan Repayment Schedule.Status=Restructured]
menus: [Lending > Loan Management > Loan Repayment Schedule]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J5/J5-S3-09_draft-a-schedule-header.png, /assets/lending_assistant/kb_img/J5/J5-S3-10_draft-a-schedule-rows.png, /assets/lending_assistant/kb_img/J5/J5-S3-11_draft-b-schedule-rows.png, /assets/lending_assistant/kb_img/J5/J5-S5-07_plans-list.png, /assets/lending_assistant/kb_img/J5/J5-S5-03_old-plan-restructured.png, /assets/lending_assistant/kb_img/J5/J5-S5-05_new-plan-active.png, /assets/lending_assistant/kb_img/J5/J5-S5-06_new-plan-rows.png, /assets/lending_assistant/kb_img/J6/J6-S5-02_old-plan-restructured-no-link.png]
sources:
  - "sources/verification/walkthroughs/J5_walkthrough.md#stage-3"
  - "sources/verification/walkthroughs/J5_walkthrough.md#stage-5"
  - "sources/verification/walkthroughs/J5_walkthrough.md#3.4"
  - "sources/verification/walkthroughs/J5_walkthrough.md#5.2"
  - "sources/verification/walkthroughs/J5_walkthrough.md#5.3"
  - "sources/verification/walkthroughs/J5_walkthrough.md#5.4"
  - "sources/verification/walkthroughs/J6_walkthrough.md#stage-5"
  - "sources/verification/walkthroughs/J6_walkthrough.md#5.1"
related: [howto.loan_repayment_schedule.view, howto.loan_restructure.create, howto.loan_restructure.approve, bridge.BR-LMS-152, bridge.BR-LMS-125, bridge.BR-LMS-126, bridge.BR-LMS-183, journey.J5, screen.loan_repayment_schedule, screen.loan_restructure]
version: 1
status: approved
approved_by: Owner
---
**In short:** Each draft restructure builds a draft plan; after approval the old plan is kept as Restructured or Rescheduled and a new plan is Active, with no link from the old plan to the new one.

## Before you start

⚠ This card is view only. You need read permission on **Loan Repayment Schedule**. The drafts come from `howto.loan_restructure.create`. For a normal schedule see the J1 card `howto.loan_repayment_schedule.view`. Names in the screenshots are test records on the dev site.

## Steps

1. Open a draft restructure and follow its Connections to the Loan Repayment Schedule. The status is Initiated and the plan is a draft.
2. Compare the monthly amount, the number of rows and the last date between the two drafts.
3. After approval, open Lending > Loan Management > Loan Repayment Schedule, filter by loan, and open the old and the new plan.

![A draft plan: header](/assets/lending_assistant/kb_img/J5/J5-S3-09_draft-a-schedule-header.png)

## What you should see

In the J5 example, option A has 7 rows at 9,013 and option B has 8 rows at 8,979 with a small last instalment of 198.46. The first row of both holds interest carried over from the old rate.

![Option A plan: 7 rows](/assets/lending_assistant/kb_img/J5/J5-S3-10_draft-a-schedule-rows.png)

![Option B plan: 8 rows](/assets/lending_assistant/kb_img/J5/J5-S3-11_draft-b-schedule-rows.png)

After approval there are two plans: the old one with status Restructured and the new one Active. The old plan keeps all its rows, and the paid rows stay unchanged and ticked as billed; the repayments and demands still point to it. No ledger entry was posted by the approval. A payment-driven restructure marks the old plan Rescheduled instead.

![Old and new plan](/assets/lending_assistant/kb_img/J5/J5-S5-07_plans-list.png)

![The old plan, Restructured](/assets/lending_assistant/kb_img/J5/J5-S5-03_old-plan-restructured.png)

![The new plan, Active](/assets/lending_assistant/kb_img/J5/J5-S5-05_new-plan-active.png)

![New plan rows](/assets/lending_assistant/kb_img/J5/J5-S5-06_new-plan-rows.png)

## If it looks wrong

The old plan has no field pointing to the new plan or to the restructure; only the new plan points to its restructure (BR-LMS-125, partly covered). The chain has to be rebuilt by loan and date.

![The old plan: no link forward](/assets/lending_assistant/kb_img/J6/J6-S5-02_old-plan-restructured-no-link.png)

The walkthrough also reports that the interest carried into the first row is added to principal as well, so the borrower would be billed it twice (DEF-18, ND-20; BR-LMS-152, partly covered). A plan can also be rebuilt without an approved change (BR-LMS-126, not covered; ND-19, D6). The verification found a loan with two Active plans in that way. Keep plan-creation rights to the restructure screen. See `bridge.BR-LMS-152`, `bridge.BR-LMS-125` and `bridge.BR-LMS-126`.
