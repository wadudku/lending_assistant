---
id: howto.loan_transfer.create
type: howto
title: How to move loans between branches
summary: "A Loan Transfer moves an applicant's loans from one branch to another, but it needs a Branch accounting dimension and a Branch field on the Loan, neither of which this site has."
br_ids: [BR-LMS-220]
brd_section: 7.13
doctypes: [Loan Transfer, Loan]
dev_items: []
journeys: [J11]
actions: ["Loan Transfer:create"]
fields: [Loan Transfer.Company, Loan Transfer.Transfer Date, Loan Transfer.Applicant, Loan Transfer.From Branch, Loan Transfer.To Branch]
options: []
menus: [Lending > Loan Management > Loan Transfer]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J11/J11-S4-02_loan-transfer-filled.png, /assets/lending_assistant/kb_img/J11/J11-S4-03_loan-transfer-save-error.png, /assets/lending_assistant/kb_img/J11/J11-S4-10_loan-form-no-branch-field.png]
sources:
  - "sources/verification/walkthroughs/J11_walkthrough.md#stage-4"
  - "sources/verification/walkthroughs/J11_walkthrough.md#4.1"
related: [howto.loan_demand.cancel, bridge.BR-LMS-220, journey.J11, screen.loan]
version: 1
status: approved
approved_by: Owner
---
**In short:** A Loan Transfer moves an applicant's loans from one branch to another, but it needs a Branch accounting dimension and a Branch field on the Loan, neither of which this site has.

## Before you start

⚠ You need permission to create a **Loan Transfer**. The From Branch and To Branch links need two Branch records. Adding Branch as an accounting dimension is a site-wide setting; do not change it on a shared site. Names in the screenshots are test records on the dev site.

## Steps

1. Open Lending > Loan Management > Loan Transfer and click Add.
2. Enter **Company**, **Transfer Date**, **Applicant**, **From Branch** and **To Branch**.

![The transfer entered](/assets/lending_assistant/kb_img/J11/J11-S4-02_loan-transfer-filled.png)

3. Click **Save**.

## What you should see

On this site the save is refused: "Please set up Branch as an Accounting Dimension before transferring loans between branches."

![The save refused](/assets/lending_assistant/kb_img/J11/J11-S4-03_loan-transfer-save-error.png)

Read from the code: with the dimension in place, the list is built from one branch, each loan keeps its record and number and gets the new branch value, and one Journal Entry per loan moves the branch's profit-and-loss balances. Cancelling puts the branch back.

## If it looks wrong

The BRD wants loans moved between branches in bulk, each keeping its record, number and history (BR-LMS-220). The Loan form has no Branch field, so nothing sets a branch on a loan today. The covered verdict comes from code and meta only; a live transfer was not run.

![The Loan form has no Branch field](/assets/lending_assistant/kb_img/J11/J11-S4-10_loan-form-no-branch-field.png)

The workaround is to configure the Branch dimension, a site-wide step outside the loan app, and then set a branch on every loan. The fix is the dimension and a Branch field on the Loan, set at booking. See `bridge.BR-LMS-220`.
