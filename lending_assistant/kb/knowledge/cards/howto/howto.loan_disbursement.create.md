---
id: howto.loan_disbursement.create
type: howto
title: "How to disburse a sanctioned loan, and why a secured loan can go out with no pledge"
summary: "Disbursement uses the pledged value as its limit if there is one, otherwise the typed amount; a secured loan can therefore be disbursed before any collateral is pledged."
br_ids: [BR-LMS-171, BR-LMS-170, BR-LMS-212]
brd_section: 7.8
doctypes: [Loan Disbursement, Loan]
dev_items: []
journeys: [J7, J10]
actions: ["Loan Disbursement:create"]
fields: [Loan Disbursement.Disbursement Date, Loan Disbursement.Disbursed Amount, Loan Disbursement.Repayment Start Date, Loan Disbursement.Disbursement Account]
options: []
menus: [Lending > Loan Management > Loan Disbursement]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J7/J7-S2-11_disbursement-filled.png, /assets/lending_assistant/kb_img/J7/J7-S2-12_disbursement-submitted.png, /assets/lending_assistant/kb_img/J7/J7-S2-13_loan-disbursed.png, /assets/lending_assistant/kb_img/J7/J7-S2-14_gap-L7-3-disbursement.png, /assets/lending_assistant/kb_img/J7/J7-S2-15_gap-L7-3-pledge-after.png]
sources:
  - "sources/verification/walkthroughs/J7_walkthrough.md#stage-2"
  - "sources/verification/walkthroughs/J7_walkthrough.md#2.5"
  - "sources/verification/walkthroughs/J7_walkthrough.md#2.6"
related: [howto.loan_security_assignment.pledge, howto.loan_disbursement.view, bridge.BR-LMS-171c, journey.J7, screen.loan_disbursement, screen.loan]
version: 1
status: approved
approved_by: Owner
---
**In short:** Disbursement uses the pledged value as its limit if there is one, otherwise the typed amount; a secured loan can therefore be disbursed before any collateral is pledged.

## Before you start

⚠ You need permission to create and submit a **Loan Disbursement**. The loan must be Sanctioned. This card covers a loan booked without auto-disbursement; for an auto-disbursed loan see the J1 card `howto.loan_disbursement.view`. Names in the screenshots are test records on the dev site.

## Steps

1. Open the loan and click Create, then Loan Disbursement.
2. Check **Disbursement Date**, **Disbursed Amount** and **Repayment Start Date**: all three fill in from the loan.
3. Pick the **Disbursement Account**.
4. Click **Save**, then **Submit** and **Yes**.

![Disbursement entered](/assets/lending_assistant/kb_img/J7/J7-S2-11_disbursement-filled.png)

## What you should see

The disbursement is Submitted and the loan is Disbursed for 100,000. In the walkthrough the disbursement used the pledged value (160,000) as its limit.

![Disbursement submitted](/assets/lending_assistant/kb_img/J7/J7-S2-12_disbursement-submitted.png)

![Loan Disbursed](/assets/lending_assistant/kb_img/J7/J7-S2-13_loan-disbursed.png)

## If it looks wrong

The BRD wants no disbursement against a secured loan until the security is in place (BR-LMS-171, partly covered). Today the disbursement amount check uses the pledged value if any, otherwise the typed amount: the secured flag is a label unless the origination side always pledges first. An earlier verification loan was disbursed with no collateral, and its first pledge was created 0.09 seconds after the disbursement (DEF-31, ND-31). The workaround is to pledge first and disburse after (`howto.loan_security_assignment.pledge`), and to check by eye. See `bridge.BR-LMS-171c`.

![A secured loan disbursed with no collateral](/assets/lending_assistant/kb_img/J7/J7-S2-14_gap-L7-3-disbursement.png)

![Its pledge created afterwards](/assets/lending_assistant/kb_img/J7/J7-S2-15_gap-L7-3-pledge-after.png)
