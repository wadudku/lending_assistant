---
id: howto.loan_disbursement.view_ledger
type: howto
title: How to see the accounting entries of a disbursement
summary: "From a Loan Disbursement, use View and Accounting Ledger to open the General Ledger filtered to that document."
br_ids: []
brd_section: 7.1
doctypes: [Loan Disbursement]
dev_items: []
journeys: [J1]
actions: ["Loan Disbursement:view_ledger"]
menus: [Accounting > General Ledger]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J1/J1-S4-02_disbursement-view-accounting-ledger.png, /assets/lending_assistant/kb_img/J1/J1-S4-03_general-ledger-disbursement.png]
sources:
  - "sources/verification/walkthroughs/J1_walkthrough.md#stage-4"
  - "sources/verification/walkthroughs/J1_walkthrough.md#4.2"
related: [howto.loan_disbursement.view, howto.loan_demand.view, journey.J1]
version: 1
status: approved
approved_by: Owner
---
**In short:** From a Loan Disbursement, use View and Accounting Ledger to open the General Ledger filtered to that document.

## Before you start

You need read permission on the Loan Disbursement and on the General Ledger report. Names you see in the screenshots, such as customer and loan names, are test records on the dev site.

## Steps

1. Open the Loan Disbursement (`howto.loan_disbursement.view`).
2. Click **View**, then **Accounting Ledger**.

   The same report by hand: **Accounting > General Ledger**, with **Voucher No** set to the disbursement's name. Loan is not an accounting dimension here, so there is no Loan filter.

![View menu with Accounting Ledger](/assets/lending_assistant/kb_img/J1/J1-S4-02_disbursement-view-accounting-ledger.png)

## What you should see

The General Ledger for the company and voucher: a debit to the loan portfolio account and a credit to the disbursement bank account, both for the disbursed amount.

![General Ledger for the disbursement](/assets/lending_assistant/kb_img/J1/J1-S4-03_general-ledger-disbursement.png)

## If it looks wrong

The posting date on these rows is the day the document was entered, not the disbursement date, because the code always sets it to today (DEF-5). For a back-dated loan the entry can land in a later month than the payout. GL Entry is not a link on the Loan dashboard, so use this route.
