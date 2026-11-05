---
id: howto.loan_repayment.recover_write_off
type: howto
title: How to recover money on a written-off loan
summary: "A written-off loan takes only Write Off Recovery or Write Off Settlement; recovery goes to Bad Debt Recovery, and a Write Off Settlement of any size closes the loan as Settled."
br_ids: [BR-LMS-203, BR-LMS-200]
brd_section: 7.11
doctypes: [Loan Repayment, Loan]
dev_items: []
journeys: [J8]
actions: ["Loan Repayment:recover_write_off"]
fields: [Loan Repayment.Against Loan, Loan Repayment.Repayment Type, Loan Repayment.Value Date, Loan Repayment.Amount Paid, Loan Repayment.Reference Number]
options: [Loan Repayment.Repayment Type=Normal Repayment, Loan Repayment.Repayment Type=Write Off Recovery, Loan Repayment.Repayment Type=Write Off Settlement]
menus: [Lending > Loan Management > Loan Repayment]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J8/J8-S5-1a_normal-repayment-filled.png, /assets/lending_assistant/kb_img/J8/J8-S5-1b_normal-repayment-refused.png, /assets/lending_assistant/kb_img/J8/J8-S5-2a_recovery-filled-top.png, /assets/lending_assistant/kb_img/J8/J8-S5-3a_wo-settlement-filled-top.png]
sources:
  - "sources/verification/walkthroughs/J8_walkthrough.md#stage-5"
  - "sources/verification/walkthroughs/J8_walkthrough.md#5.1"
  - "sources/verification/walkthroughs/J8_walkthrough.md#5.2"
  - "sources/verification/walkthroughs/J8_walkthrough.md#5.3"
related: [howto.loan_write_off.create, howto.loan_repayment.settle, bridge.BR-LMS-203, journey.J8, screen.loan_repayment, screen.loan]
version: 1
status: approved
approved_by: Owner
---
**In short:** A written-off loan takes only Write Off Recovery or Write Off Settlement; recovery goes to Bad Debt Recovery, and a Write Off Settlement of any size closes the loan as Settled.

## Before you start

⚠ You need permission to **Submit** a **Loan Repayment**. A Written Off loan has no Create button, so start from the Loan Repayment list. Names in the screenshots are test records on the dev site.

## Steps

1. Click Add Loan Repayment and choose the written-off loan in **Against Loan**.
2. Try **Repayment Type** Normal Repayment first if you want to see the block, then change it.

![A Normal Repayment entered](/assets/lending_assistant/kb_img/J8/J8-S5-1a_normal-repayment-filled.png)

![The Normal Repayment refused](/assets/lending_assistant/kb_img/J8/J8-S5-1b_normal-repayment-refused.png)

3. For a recovery set **Repayment Type** to Write Off Recovery, enter **Value Date**, **Amount Paid** and **Reference Number**, then click **Save**, **Submit** and **Yes**.

![A recovery entered](/assets/lending_assistant/kb_img/J8/J8-S5-2a_recovery-filled-top.png)

4. To close the written-off loan use Write Off Settlement instead.

![A Write Off Settlement entered](/assets/lending_assistant/kb_img/J8/J8-S5-3a_wo-settlement-filled-top.png)

## What you should see

A Normal Repayment is refused with "Repayment type can only be Write Off Recovery or Write Off Settlement". A recovery posts the bank amount to Bad Debt Recovery, nothing goes back to the portfolio, and the loan stays Written Off with its written-off amount unchanged. A Write Off Settlement moves the loan from Written Off straight to Settled.

## If it looks wrong

The BRD wants recovery posted to its own income account and the loan history kept (BR-LMS-203, covered), and a settlement of a written-off loan to be a controlled decision (BR-LMS-200, partly covered). A settlement for a small part of the written-off amount is accepted and closes the loan in one submit. There is no minimum-recovery or proportionality check and no record of why the amount was accepted (DEF-36). The fix is ND-34, a recovery rule and an approved reason before the status changes. See `bridge.BR-LMS-203`.
