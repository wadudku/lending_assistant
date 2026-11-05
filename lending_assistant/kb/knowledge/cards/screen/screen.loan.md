---
id: screen.loan
type: screen
title: "Screen: Loan"
summary: "The Loan screen is the record of one loan: the borrower, product, amount, rate and term, the totals and status; submitting it books the loan."
br_ids: [BR-LMS-100, BR-LMS-101, BR-LMS-102, BR-LMS-103, BR-LMS-104, BR-LMS-105, BR-LMS-106, BR-LMS-111, BR-LMS-112, BR-LMS-113, BR-LMS-117, BR-LMS-124, BR-LMS-125, BR-LMS-131, BR-LMS-135, BR-LMS-142, BR-LMS-152, BR-LMS-153, BR-LMS-159, BR-LMS-163, BR-LMS-168, BR-LMS-184, BR-LMS-185, BR-LMS-187, BR-LMS-190, BR-LMS-192, BR-LMS-194, BR-LMS-196, BR-LMS-198, BR-LMS-202, BR-LMS-203, BR-LMS-210, BR-LMS-211, BR-LMS-220, BR-LMS-222, BR-LMS-224, BR-LMS-230, BR-LMS-232, BR-LMS-233, BR-LMS-234, BR-LMS-235]
brd_section: 7.1
doctypes: [Loan]
dev_items: [D1, D2]
fields: [Loan.Applicant Type, Loan.Applicant, Loan.Loan Product, Loan.Posting Date, Loan.Status, Loan.Loan Amount, Loan.Rate of Interest (%) / Year, Loan.Repayment Method, Loan.Tenure, Loan.Repayment Start Date, Loan.Disbursed Amount, Loan.Loan Category, Loan.Auto create disbursement on loan booking, Loan.Is Secured Loan, Loan.Days Past Due, Loan.Classification Code, Loan.Moratorium Type]
options: [Loan.Status=Draft, Loan.Status=Sanctioned, Loan.Status=Disbursed, Loan.Status=Active, Loan.Status=Closed, Loan.Status=Written Off, Loan.Status=Settled, Loan.Repayment Method=Repay Over Number of Periods]
menus: [Lending > Loan Management > Loan]
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan/loan.py, lending/loan_management/doctype/loan/loan.json]
images: [/assets/lending_assistant/kb_img/J1/J1-S1-04_loan-filled-terms.png, /assets/lending_assistant/kb_img/J1/J1-S1-06_loan-submitted-disbursed.png, /assets/lending_assistant/kb_img/J1/J1-S4-01_loan-dashboard-connections.png]
sources:
  - "sources/verification/walkthroughs/J1_walkthrough.md#stage-1"
  - "sources/verification/walkthroughs/J1_walkthrough.md#1.2"
  - "sources/verification/walkthroughs/J1_walkthrough.md#1.3"
  - "sources/verification/walkthroughs/J1_walkthrough.md#stage-2"
  - "sources/verification/walkthroughs/J1_walkthrough.md#2.2"
  - "sources/verification/walkthroughs/J1_walkthrough.md#stage-4"
  - "sources/verification/walkthroughs/J1_walkthrough.md#4.1"
  - "sources/verification/verification_report.md#BR-LMS-100"
  - "sources/verification/reqs.json#BR-LMS-101"
  - "sources/verification/reqs.json#BR-LMS-102"
related: [howto.loan.create, howto.loan.submit, howto.loan.view, screen.customer, screen.loan_product, brd_section.7.1, bridge.BR-LMS-100, bridge.BR-LMS-101, bridge.BR-LMS-102, lifecycle.BOOKED, lifecycle.ACTIVE, devitem.D1, devitem.D2]
version: 1
status: approved
approved_by: Owner
---
**In short:** The Loan screen is the record of one loan: the borrower, product, amount, rate and term, the totals and status; submitting it books the loan.

## What this screen is for

**Loan** is the record that stands for one loan (menu: Lending > Loan Management > Loan). It holds the borrower, the product, the amount, the rate and the term, and it carries the totals and the status for the rest of the loan's life. Everything else hangs off it: the disbursement, the repayment schedule, the demands, the repayments and the logs. It is a submittable document. In the walkthrough the officer saved a Draft and submitted it with **Auto create disbursement on loan booking** ticked; the system then created the disbursement and the repayment schedule in the same action and the loan went Draft, Sanctioned, Disbursed.

## Before and after

Before: the borrower exists (`screen.customer`) and the product exists (`screen.loan_product`). After: the disbursement, the schedule and the daily jobs follow (`howto.loan_disbursement.view`, `howto.loan_repayment_schedule.view`, `howto.loan_demand.view`). To book a loan step by step, see `howto.loan.create` and `howto.loan.submit`.

## Key fields

**Applicant Type**, **Applicant**, **Loan Product**, **Posting Date**, **Loan Amount**, **Repayment Method**, **Tenure**, **Repayment Start Date** and **Status**. The product fills in **Rate of Interest (%) / Year**, **Loan Category** and the accounts, so the officer types none of them. While the loan is a Draft the rate can still be edited (ND-5). The **Status** options are Draft, Sanctioned, Partially Disbursed, Disbursed, Active, Loan Closure Requested, Closed, Written Off and Settled. **Is Secured Loan**, **Days Past Due**, **Classification Code** and **Moratorium Type** sit on the same form.

![The loan form with product, amount and terms](/assets/lending_assistant/kb_img/J1/J1-S1-04_loan-filled-terms.png)

![The loan after Submit, status Disbursed](/assets/lending_assistant/kb_img/J1/J1-S1-06_loan-submitted-disbursed.png)

The **Connections** tab shows Stats and links to the schedule, disbursement, repayments, security, adjustments, the DPD, NPA, Freeze and Limit Change logs, and the accounting entries.

![The Connections tab of a loan](/assets/lending_assistant/kb_img/J1/J1-S4-01_loan-dashboard-connections.png)

The installed doctype gives Loan Manager read, write, create, submit, cancel and delete, Loan Reporter read only, and Employee read.

## BRD needs it serves

The main rows are BR-LMS-100 to 106 in BRD 7.1 (see `brd_section.7.1`); the front matter lists every row whose verified text names the Loan screen, and the bridges hold the verdicts. Weak points to remember: the activity log shows only the Draft to Sanctioned change, so there is no full status history (ND-3, D2), and the loan has no origination audit field beyond the **Loan Application** link (D1, `bridge.BR-LMS-100`).
