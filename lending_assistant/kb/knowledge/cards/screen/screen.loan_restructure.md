---
id: screen.loan_restructure
type: screen
title: "Screen: Loan Restructure"
summary: "The Loan Restructure screen changes the terms of a loan, such as the rate, the term or the EMI, and builds the new repayment plan when it is approved."
br_ids: [BR-LMS-101, BR-LMS-124, BR-LMS-125, BR-LMS-134, BR-LMS-150, BR-LMS-152, BR-LMS-153, BR-LMS-154, BR-LMS-155, BR-LMS-156, BR-LMS-157, BR-LMS-158, BR-LMS-159, BR-LMS-162, BR-LMS-182, BR-LMS-184]
brd_section: 7.9
doctypes: [Loan Restructure]
dev_items: [D6, D11]
fields: [Loan Restructure.Loan, Loan Restructure.Restructure Date, Loan Restructure.Restructure Type, Loan Restructure.Reason for Restructure, Loan Restructure.New Rate Of Interest, Loan Restructure.New Repayment Method, Loan Restructure.New Repayment Period in Months, Loan Restructure.New Monthly Repayment Amount, Loan Restructure.Interest Treatment, Loan Restructure.Unaccrued Interest Treatment, Loan Restructure.Status]
options: [Loan Restructure.Restructure Type=Normal Restructure, Loan Restructure.Restructure Type=Pre Payment, Loan Restructure.Restructure Type=Advance Payment, Loan Restructure.Status=Initiated, Loan Restructure.Status=Approved, Loan Restructure.Status=Rejected, Loan Restructure.Interest Treatment=Add To First EMI, Loan Restructure.New Repayment Method=Repay Over Number of Periods, Loan Restructure.New Repayment Method=Repay Fixed Amount per Period]
menus: [Lending > Loan Management > Loan Restructure]
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_restructure/loan_restructure.json]
images: [/assets/lending_assistant/kb_img/J5/J5-S3-04_draft-a-filled-terms.png, /assets/lending_assistant/kb_img/J5/J5-S4-03_approved.png]
sources:
  - "sources/verification/walkthroughs/J5_walkthrough.md#stage-3"
  - "sources/verification/walkthroughs/J5_walkthrough.md#3.1"
  - "sources/verification/walkthroughs/J5_walkthrough.md#3.2"
  - "sources/verification/walkthroughs/J5_walkthrough.md#3.5"
  - "sources/verification/walkthroughs/J5_walkthrough.md#stage-4"
  - "sources/verification/walkthroughs/J5_walkthrough.md#4.2"
  - "sources/verification/walkthroughs/J5_walkthrough.md#stage-5"
  - "sources/verification/walkthroughs/J5_walkthrough.md#5.1"
  - "sources/verification/verification_report.md#BR-LMS-182"
  - "sources/verification/verification_report.md#BR-LMS-155"
  - "sources/verification/reqs.json#BR-LMS-154"
related: [screen.loan, screen.loan_repayment_schedule, brd_section.7.9, brd_section.7.6, decision.restructure, lifecycle.RESTRUCTURED, glossary.restructuring, bridge.BR-LMS-154, bridge.BR-LMS-155, bridge.BR-LMS-182, devitem.D11]
version: 1
status: approved
approved_by: Owner
---
**In short:** The Loan Restructure screen changes the terms of a loan, such as the rate, the term or the EMI, and builds the new repayment plan when it is approved.

## What this screen is for

**Loan Restructure** changes the terms of a running loan (menu: Lending > Loan Management > Loan Restructure). The officer picks the loan and a date and enters the new rate, term or EMI. Saving a draft also creates a draft repayment plan, so the officer can compare two options before choosing one. Submitting the chosen one sets its status to **Initiated**; setting **Status** to **Approved** applies it: the loan takes the new rate and amount, the old plan becomes Restructured and a new plan is Active (J5 walkthrough stage 5). The rules for when to use it are in `decision.restructure`.

## Before and after

Before: a loan with a running schedule (`screen.loan`, `screen.loan_repayment_schedule`). After: the loan's **Loan Restructure Count** goes up by one, except when a stale draft is approved a second time (DEF-19), and the new plan bills from the new start date.

## Key fields

**Loan**, **Restructure Date**, **Restructure Type** (Normal Restructure, Pre Payment or Advance Payment), **Reason for Restructure**, **New Rate Of Interest**, **New Repayment Method**, **New Repayment Period in Months**, **New Monthly Repayment Amount**, **Interest Treatment** and **Unaccrued Interest Treatment**, and **Status** (Initiated, Approved or Rejected). Two traps shown in the walkthrough: after the repayment method is chosen, **New Repayment Period in Months** shows 0, and a clerk who leaves it at 0 silently extends the loan back to its original term; and the carried interest can be billed twice (DEF-18).

![A draft restructure with the new rate, start date and term](/assets/lending_assistant/kb_img/J5/J5-S3-04_draft-a-filled-terms.png)

![The same restructure after approval](/assets/lending_assistant/kb_img/J5/J5-S4-03_approved.png)

The installed doctype gives System Manager and Loan Manager read, write, create, submit and delete, and Loan Reporter read only.

## BRD needs it serves

The main rows are BR-LMS-150 and 152 to 159 in BRD 7.6 (the repricing run, see `brd_section.7.6`) and BR-LMS-182 and 184 in BRD 7.9 (see `brd_section.7.9`); the bridges hold the verdicts. Weak points shown: there is no dry run for a batch (BR-LMS-154, D11), approval is a status edit with no workflow, so the same user submitted and approved (BR-LMS-155, D11), and a stale draft of the same change can be approved a second time (BR-LMS-157).
