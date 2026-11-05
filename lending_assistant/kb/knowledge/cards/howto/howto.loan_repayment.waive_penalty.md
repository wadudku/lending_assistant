---
id: howto.loan_repayment.waive_penalty
type: howto
title: How to waive part of a penalty
summary: "A Penalty Waiver is a Loan Repayment of that type, submitted with no approval step, no reason and no approver; the before and after amounts are not stored on it."
br_ids: [BR-LMS-185]
brd_section: 7.7
doctypes: [Loan Repayment]
dev_items: [D8]
journeys: [J6]
actions: ["Loan Repayment:waive_penalty"]
fields: [Loan Repayment.Repayment Type, Loan Repayment.Value Date, Loan Repayment.Amount Paid, Loan Repayment.Reference Number, Loan Repayment.Manual Remarks]
options: [Loan Repayment.Repayment Type=Penalty Waiver]
menus: [Lending > Loan Management > Loan Repayment]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J6/J6-S4-01_penalty-waiver-filled-top.png, /assets/lending_assistant/kb_img/J6/J6-S4-03_penalty-waiver-submitted.png, /assets/lending_assistant/kb_img/J6/J6-S4-04_penalty-waiver-no-approver-no-reason.png]
sources:
  - "sources/verification/walkthroughs/J6_walkthrough.md#stage-4"
  - "sources/verification/walkthroughs/J6_walkthrough.md#4.1"
related: [howto.loan_balance_adjustment.create, howto.loan_repayment.submit, bridge.BR-LMS-185, journey.J6, screen.loan_repayment]
version: 1
status: approved
approved_by: Owner
---
**In short:** A Penalty Waiver is a Loan Repayment of that type, submitted with no approval step, no reason and no approver; the before and after amounts are not stored on it.

## Before you start

⚠ You need permission to **Submit** a **Loan Repayment**. A waiver changes what a borrower owes, so use a test loan. Names in the screenshots are test records on the dev site.

## Steps

1. Open the loan, click Create and choose Loan Repayment.
2. Set **Repayment Type** to Penalty Waiver, enter **Value Date**, **Amount Paid** (the part to waive, 50 in the walkthrough) and **Reference Number**. **Manual Remarks** is not required.
3. Click **Save**, then **Submit** and **Yes**. There is no approval step.

![The waiver entered](/assets/lending_assistant/kb_img/J6/J6-S4-01_penalty-waiver-filled-top.png)

## What you should see

The repayment is Submitted and Total Penalty Paid shows the waived amount. The penalty overdue on the loan falls by that amount: here from 273.96 to 223.96. The 50 is posted to the ledger as a debit and a credit in the same income account and nets to zero, because the product's Additional Interest accounts all point to one account (configuration note CF-2).

![The waiver submitted](/assets/lending_assistant/kb_img/J6/J6-S4-03_penalty-waiver-submitted.png)

## If it looks wrong

The BRD wants waivers under maker and checker, with limits by role and amount and a full record with before and after amounts (BR-LMS-185, partly covered). The same user keys and submits, there is no workflow, and the only check is that a waiver is not more than what is overdue. The reason and the reference are optional, and the record does not store the amounts before and after; they show only by comparing the loan before and after.

![No approver and no reason](/assets/lending_assistant/kb_img/J6/J6-S4-04_penalty-waiver-no-approver-no-reason.png)

The workaround is to save the repayment as a Draft, have a second officer check it against a signed request, submit only then, and write the reason, the approver and the amounts in Manual Remarks. The fix is ND-23 (D8). See `bridge.BR-LMS-185`.
