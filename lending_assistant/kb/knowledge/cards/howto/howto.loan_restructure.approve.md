---
id: howto.loan_restructure.approve
type: howto
title: How to submit and approve a restructure
summary: "A restructure is submitted as Initiated and approved by setting its Status to Approved; the same user can do both, and approval changes the loan."
br_ids: [BR-LMS-155, BR-LMS-151, BR-LMS-157, BR-LMS-182, BR-LMS-184]
brd_section: 7.6
doctypes: [Loan Restructure, Loan, Loan Restructure Limit Log]
dev_items: [D11, D16]
journeys: [J5, J6]
actions: ["Loan Restructure:approve"]
fields: [Loan Restructure.Status, Loan.Rate of Interest (%) / Year, Loan.Loan Restructure Count]
options: [Loan Restructure.Status=Approved, Loan Restructure.Status=Initiated]
menus: [Lending > Loan Management > Loan Restructure]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J5/J5-S4-01_submitted-initiated.png, /assets/lending_assistant/kb_img/J5/J5-S4-02_status-approved-filled.png, /assets/lending_assistant/kb_img/J5/J5-S4-03_approved.png, /assets/lending_assistant/kb_img/J5/J5-S4-04_same-user-submits-and-approves.png, /assets/lending_assistant/kb_img/J5/J5-S5-08_loan-restructure-count-1.png, /assets/lending_assistant/kb_img/J6/J6-S3-08_capitalization-repayments.png, /assets/lending_assistant/kb_img/J6/J6-S3-13_gap-restructure-limit-log-empty.png]
sources:
  - "sources/verification/walkthroughs/J5_walkthrough.md#stage-4"
  - "sources/verification/walkthroughs/J5_walkthrough.md#stage-5"
  - "sources/verification/walkthroughs/J5_walkthrough.md#4.1"
  - "sources/verification/walkthroughs/J5_walkthrough.md#4.2"
  - "sources/verification/walkthroughs/J5_walkthrough.md#5.1"
  - "sources/verification/walkthroughs/J6_walkthrough.md#stage-3"
  - "sources/verification/walkthroughs/J6_walkthrough.md#3.2"
  - "sources/verification/walkthroughs/J6_walkthrough.md#3.3"
  - "sources/verification/walkthroughs/J6_walkthrough.md#3.5"
related: [howto.loan_restructure.create, howto.loan_repayment_schedule.compare_plans, bridge.BR-LMS-155, bridge.BR-LMS-184, journey.J5, screen.loan_restructure, screen.loan]
version: 1
status: approved
approved_by: Owner
---
**In short:** A restructure is submitted as Initiated and approved by setting its Status to Approved; the same user can do both, and approval changes the loan.

## Before you start

⚠ Submitting and approving change a live loan, so use a test loan. You need permission to **Submit** a **Loan Restructure** and to edit its Status. The Draft comes from `howto.loan_restructure.create`. Names in the screenshots are test records on the dev site.

## Steps

1. Open the chosen Draft restructure and click **Submit**, then **Yes** (the maker's step). The status becomes Initiated and the loan has not changed.
2. Set **Status** to Approved and click Update (the checker's step). The field stays editable after submit.
3. Open the loan and read the new rate, the tenure, the monthly repayment amount and **Loan Restructure Count**.

![Submitted, Initiated](/assets/lending_assistant/kb_img/J5/J5-S4-01_submitted-initiated.png)

![Status set to Approved](/assets/lending_assistant/kb_img/J5/J5-S4-02_status-approved-filled.png)

## What you should see

The restructure is Approved. The loan now carries the new rate (15% in the J5 example), and its restructure count goes from 0 to 1. When the loan had overdue amounts, the approval also creates Interest, Penalty and Principal Capitalization repayments for them and closes the overdue demands (J6). The new plan is described in `howto.loan_repayment_schedule.compare_plans`.

![Approved](/assets/lending_assistant/kb_img/J5/J5-S4-03_approved.png)

![Loan restructure count 1](/assets/lending_assistant/kb_img/J5/J5-S5-08_loan-restructure-count-1.png)

![Capitalization repayments created by the system](/assets/lending_assistant/kb_img/J6/J6-S3-08_capitalization-repayments.png)

## If it looks wrong

The Activity shows that the same user submitted and approved. The BRD wants a maker to create the run and a different checker to approve it (BR-LMS-155, not covered). Today approval is a plain status edit with no workflow. The workaround in the verification is that the checker signs the maker's spreadsheet by email or memo before the status is set, with a comment on the restructure (ND-18, D11).

![Same user submitted and approved](/assets/lending_assistant/kb_img/J5/J5-S4-04_same-user-submits-and-approves.png)

Everything here works for one loan at a time (BR-LMS-151 and BR-LMS-157 are described in the verification as gaps for a batch). A stale draft of the same change can be approved after the first, with no warning (DEF-19): delete unused drafts first. The J5 walkthrough raises the question whether Bangladesh Bank counts a rate change as a restructure (Q5): it counted here, so the loan uses the restructure limit.

The Restructure Limit Log has no records, and the restructure was approved with no limit check (BR-LMS-184, not covered; ND-24, DEF-23). The workaround is a branch-level register kept by Credit Risk. See `bridge.BR-LMS-155` and `bridge.BR-LMS-184`.

![Restructure Limit Log: empty](/assets/lending_assistant/kb_img/J6/J6-S3-13_gap-restructure-limit-log-empty.png)
