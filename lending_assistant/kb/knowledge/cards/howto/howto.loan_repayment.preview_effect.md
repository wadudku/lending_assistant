---
id: howto.loan_repayment.preview_effect
type: howto
title: How to show a borrower the effect of a prepayment before it is made
summary: "A Draft Pre Payment builds a draft restructure and a draft plan that show the shorter loan, and posts nothing; the three drafts must be deleted by hand."
br_ids: [BR-LMS-124]
brd_section: 7.6
doctypes: [Loan Repayment, Loan Restructure, Loan Repayment Schedule]
dev_items: [D6]
journeys: [J6]
actions: ["Loan Repayment:preview_effect"]
fields: [Loan Repayment.Repayment Type, Loan Repayment.Value Date, Loan Repayment.Amount Paid, Loan Repayment.Reference Number]
options: [Loan Repayment.Repayment Type=Pre Payment]
menus: [Lending > Loan Management > Loan Repayment]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J6/J6-S1-01_whatif-prepay-filled-top.png, /assets/lending_assistant/kb_img/J6/J6-S1-03_whatif-prepay-draft-saved.png, /assets/lending_assistant/kb_img/J6/J6-S1-04_whatif-draft-restructure.png, /assets/lending_assistant/kb_img/J6/J6-S1-05_whatif-draft-schedule.png, /assets/lending_assistant/kb_img/J6/J6-S1-07_whatif-deleted-repayment-list.png]
sources:
  - "sources/verification/walkthroughs/J6_walkthrough.md#stage-1"
  - "sources/verification/walkthroughs/J6_walkthrough.md#1.1"
  - "sources/verification/walkthroughs/J6_walkthrough.md#1.2"
  - "sources/verification/walkthroughs/J6_walkthrough.md#1.3"
related: [howto.loan_repayment.pay_ahead, howto.loan_restructure.create, bridge.BR-LMS-124, journey.J6, screen.loan_repayment, screen.loan_restructure, screen.loan_repayment_schedule]
version: 1
status: approved
approved_by: Owner
---
**In short:** A Draft Pre Payment builds a draft restructure and a draft plan that show the shorter loan, and posts nothing; the three drafts must be deleted by hand.

## Before you start

⚠ You need permission to create and delete a **Loan Repayment**. Save it as a Draft only and never submit it: submitting makes the prepayment real (`howto.loan_repayment.pay_ahead`). Names in the screenshots are test records on the dev site.

## Steps

1. Open the loan, click Create and choose Loan Repayment.
2. Set **Repayment Type** to Pre Payment, enter **Value Date** (with a time), **Amount Paid** (for example Rahim's 20,000 extra) and **Reference Number**.
3. Click **Save**. Do not submit.
4. Open the loan's Loan Restructure list and open the Draft of type Pre Payment, then its draft plan.
5. To throw the what-if away, delete in this order: the plan, the restructure, then the repayment.

![The what-if entered](/assets/lending_assistant/kb_img/J6/J6-S1-01_whatif-prepay-filled-top.png)

![Saved as a Draft](/assets/lending_assistant/kb_img/J6/J6-S1-03_whatif-prepay-draft-saved.png)

## What you should see

A draft restructure and a draft plan. The EMI stays the same and the plan shrinks: in the walkthrough it had 10 rows, ending two months earlier. The loan itself is unchanged and nothing is posted to the ledger.

![The draft restructure](/assets/lending_assistant/kb_img/J6/J6-S1-04_whatif-draft-restructure.png)

![The draft plan](/assets/lending_assistant/kb_img/J6/J6-S1-05_whatif-draft-schedule.png)

After the deletes the repayment list shows only the real EMIs.

![The what-if deleted](/assets/lending_assistant/kb_img/J6/J6-S1-07_whatif-deleted-repayment-list.png)

## If it looks wrong

The BRD wants a what-if with nothing saved, where Rahim can compare a lower EMI with a shorter loan (BR-LMS-124, partly covered). A draft payment works, but it saves three records that must be deleted by hand, and it shows only one option, the shorter loan. A draft restructure works the same way for one option at a time (`howto.loan_restructure.create`). The verification's fix is a preview screen with both options side by side and nothing saved (ND-21, D6). See `bridge.BR-LMS-124`.
