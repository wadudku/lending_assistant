---
id: howto.loan.submit
type: howto
title: How to submit a loan
summary: "Submitting the draft loan disburses it: Frappe Lending creates the disbursement and the repayment schedule in the same action."
br_ids: []
brd_section: 7.1
doctypes: [Loan]
dev_items: [D2]
journeys: [J1]
actions: ["Loan:submit"]
fields: [Loan.Status, Loan.Disbursed Amount]
options: [Loan.Status=Disbursed, Loan.Status=Sanctioned]
menus: [Lending > Loan Management > Loan]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J1/J1-S1-06_loan-submitted-disbursed.png, /assets/lending_assistant/kb_img/J1/J1-S1-09_loan-activity-status-history.png]
sources:
  - "sources/verification/walkthroughs/J1_walkthrough.md#stage-1"
  - "sources/verification/walkthroughs/J1_walkthrough.md#1.3"
  - "sources/verification/walkthroughs/J1_walkthrough.md#5.2"
related: [howto.loan.create, howto.loan_disbursement.view, journey.J1]
version: 1
status: approved
approved_by: Owner
---
**In short:** Submitting the draft loan disburses it: Frappe Lending creates the disbursement and the repayment schedule in the same action.

## Before you start

⚠ You need permission to **Submit** a **Loan**. The Loan Manager role has it. The loan must be saved as a draft first (`howto.loan.create`). Names you see in the screenshots, such as customer and loan names, are test records on the dev site.

## Steps

1. Open the draft loan.
2. Click **Submit**, then **Yes** to confirm.

## What you should see

The status changes to **Disbursed**, the **Disbursement Date** shows the posting date and **Disbursed Amount** shows the loan amount. Behind the scenes the loan went Draft, then Sanctioned, then Disbursed, and the system created the Loan Disbursement and the repayment schedule (BR-LMS-102).

![Loan submitted, status Disbursed](/assets/lending_assistant/kb_img/J1/J1-S1-06_loan-submitted-disbursed.png)

## If it looks wrong

The activity log shows only the change from Draft to Sanctioned. Later statuses are written without a version entry, so the loan has no full status history (ND-3, supports D2).

![Activity log showing only the first status change](/assets/lending_assistant/kb_img/J1/J1-S1-09_loan-activity-status-history.png)

To check the disbursement, see `howto.loan_disbursement.view`.
