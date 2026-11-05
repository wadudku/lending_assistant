---
id: howto.loan_disbursement.view
type: howto
title: How to open a loan's disbursement and check its reference
summary: "From the loan, open the auto-created Loan Disbursement and check its amounts and its Disbursement References section."
br_ids: []
brd_section: 7.1
doctypes: [Loan Disbursement, Loan]
dev_items: [D1]
journeys: [J1]
actions: ["Loan Disbursement:view"]
fields: [Loan Disbursement.Reference Number, Loan Disbursement.Reference Date, Loan Disbursement.Monthly Repayment Amount, Loan Disbursement.Disbursement Date, Loan Disbursement.Disbursed Amount]
menus: [Lending > Loan Management > Loan Disbursement]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J1/J1-S1-07_disbursement-auto-created.png, /assets/lending_assistant/kb_img/J1/J1-S1-08_gap-no-disbursement-reference.png]
sources:
  - "sources/verification/walkthroughs/J1_walkthrough.md#stage-1"
  - "sources/verification/walkthroughs/J1_walkthrough.md#1.4"
  - "sources/verification/walkthroughs/J1_walkthrough.md#1.5"
  - "sources/verification/reqs.json#BR-LMS-100"
related: [howto.loan.submit, howto.loan_disbursement.view_ledger, journey.J1]
version: 1
status: approved
approved_by: Owner
---
**In short:** From the loan, open the auto-created Loan Disbursement and check its amounts and its Disbursement References section.

## Before you start

You only need read permission. Names you see in the screenshots, such as customer and loan names, are test records on the dev site.

## Steps

1. Open the loan, then the **Connections** tab.
2. Under **Loan Disbursement**, click the one disbursement to open it. You can also use **Lending > Loan Management > Loan Disbursement**.
3. Read the header fields. Then scroll to the section **Disbursement References**.

![Auto-created Loan Disbursement](/assets/lending_assistant/kb_img/J1/J1-S1-07_disbursement-auto-created.png)

## What you should see

Status Submitted, the **Disbursement Date**, **Disbursed Amount** (for example 100,000), **Monthly Repayment Amount** (for example 8,979.00) and **Broken Period Interest** 0.00. Broken-period interest is zero when the disbursement falls exactly on the cycle day. The disbursement's own posting date, and its accounting entry, are the day of entry, not the disbursement date (DEF-5).

⚠ The section **Disbursement References** is empty. **Reference Number** and **Reference Date** were not filled in, and a submitted form hides blank fields.

## If it looks wrong

This is the missing part of BR-LMS-100, which is partly covered (see D1): Frappe Lending accepts a disbursement with no CBS reference and has no exception queue. Reference Number is optional. To look at the empty fields, open a new unsaved Loan Disbursement and expand the section (do not save):

![Reference Date and Reference Number empty and optional](/assets/lending_assistant/kb_img/J1/J1-S1-08_gap-no-disbursement-reference.png)

Today the officer must check the CBS reference by eye and type it in.
