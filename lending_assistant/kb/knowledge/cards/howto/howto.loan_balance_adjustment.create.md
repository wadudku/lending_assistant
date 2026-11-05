---
id: howto.loan_balance_adjustment.create
type: howto
title: How to correct a loan balance with a Loan Balance Adjustment
summary: "A credit or debit adjustment moves the pending principal against an account the user picks, with no approval step; its reason and reference are optional."
br_ids: [BR-LMS-185]
brd_section: 7.7
doctypes: [Loan Balance Adjustment]
dev_items: [D8]
journeys: [J6]
actions: ["Loan Balance Adjustment:create"]
fields: [Loan Balance Adjustment.Loan, Loan Balance Adjustment.Posting Date, Loan Balance Adjustment.Adjustment Type, Loan Balance Adjustment.Amount, Loan Balance Adjustment.Adjustment Account]
options: [Loan Balance Adjustment.Adjustment Type=Credit Adjustment]
menus: []
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J6/J6-S4-05_balance-adjustment-filled.png, /assets/lending_assistant/kb_img/J6/J6-S4-06_balance-adjustment-submitted.png]
sources:
  - "sources/verification/walkthroughs/J6_walkthrough.md#stage-4"
  - "sources/verification/walkthroughs/J6_walkthrough.md#4.2"
related: [howto.loan_repayment.waive_penalty, bridge.BR-LMS-185, journey.J6]
version: 1
status: approved
approved_by: Owner
---
**In short:** A credit or debit adjustment moves the pending principal against an account the user picks, with no approval step; its reason and reference are optional.

## Before you start

⚠ You need permission to **Submit** a **Loan Balance Adjustment**. It changes a loan's principal and posts to the ledger, so use a test loan. Names in the screenshots are test records on the dev site.

## Steps

1. Type Loan Balance Adjustment in the search bar and click + Add.
2. Pick the **Loan**, enter **Posting Date**, set **Adjustment Type** (Credit Adjustment in the walkthrough), enter **Amount** (20) and pick the **Adjustment Account** (an interest waiver account). Remarks and Reference Name are not required.
3. Click **Save**, then **Submit** and **Yes**. There is no approval step.

![The adjustment entered](/assets/lending_assistant/kb_img/J6/J6-S4-05_balance-adjustment-filled.png)

## What you should see

The adjustment is Submitted. The ledger shows a debit to Interest Waiver and a credit to the loan portfolio for 20, and the pending principal falls by 20.

![The adjustment submitted](/assets/lending_assistant/kb_img/J6/J6-S4-06_balance-adjustment-submitted.png)

## If it looks wrong

The BRD wants corrections under maker and checker, with limits and a full record (BR-LMS-185, partly covered). The same user keys and submits, and there is no workflow or approval limit by role or amount. The Adjustment Account is any account the user picks: the verification accepted a 10,000,000 draft against Cash. The reason and the reference are optional, and the record does not store the amounts before and after. The workaround is a Draft checked by a second officer against a signed request, with the reason, the approver and the amounts written in Remarks. The fix is ND-23 (D8). See `bridge.BR-LMS-185`.
