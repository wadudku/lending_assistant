---
id: howto.loan_repayment.pay_ahead
type: howto
title: How to take an advance payment or a prepayment
summary: "An Advance Payment pays the next EMI early and a Pre Payment cuts principal with the EMI kept; each creates and approves its own restructure and a new plan, and Rahim cannot choose a lower EMI."
br_ids: [BR-LMS-180, BR-LMS-181, BR-LMS-131]
brd_section: 7.7
doctypes: [Loan Repayment, Loan Restructure, Prepayment Charges]
dev_items: [D20]
journeys: [J6]
actions: ["Loan Repayment:pay_ahead"]
fields: [Loan Repayment.Repayment Type, Loan Repayment.Value Date, Loan Repayment.Amount Paid, Loan Repayment.Reference Number, Prepayment Charges.Charge Code, Prepayment Charges.Charge Amount]
options: [Loan Repayment.Repayment Type=Advance Payment, Loan Repayment.Repayment Type=Pre Payment]
menus: [Lending > Loan Management > Loan Repayment]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J6/J6-S2-01_advance-filled-top.png, /assets/lending_assistant/kb_img/J6/J6-S2-03_advance-submitted.png, /assets/lending_assistant/kb_img/J6/J6-S2-04_advance-auto-restructure-approved.png, /assets/lending_assistant/kb_img/J6/J6-S2-05_advance-plans-rescheduled-active.png, /assets/lending_assistant/kb_img/J6/J6-S2-08_demands-list-0925-no-0510.png, /assets/lending_assistant/kb_img/J6/J6-S2-09_prepay-filled-top.png, /assets/lending_assistant/kb_img/J6/J6-S2-11_prepay-fee-row-filled.png, /assets/lending_assistant/kb_img/J6/J6-S2-13_prepay-split-fee-interest-principal.png, /assets/lending_assistant/kb_img/J6/J6-S2-15_prepay-plans-list.png, /assets/lending_assistant/kb_img/J6/J6-S2-16_prepay-new-plan-header.png, /assets/lending_assistant/kb_img/J6/J6-S2-18_prepay-restructure-fixed-amount-only.png]
sources:
  - "sources/verification/walkthroughs/J6_walkthrough.md#stage-2"
  - "sources/verification/walkthroughs/J6_walkthrough.md#2.1"
  - "sources/verification/walkthroughs/J6_walkthrough.md#2.2"
  - "sources/verification/walkthroughs/J6_walkthrough.md#2.3"
  - "sources/verification/walkthroughs/J6_walkthrough.md#2.4"
related: [howto.loan_repayment.preview_effect, howto.loan_repayment.submit, howto.loan_repayment_schedule.compare_plans, bridge.BR-LMS-180, bridge.BR-LMS-181, bridge.BR-LMS-131, journey.J6, screen.loan_repayment, screen.loan_restructure]
version: 1
status: approved
approved_by: Owner
---
**In short:** An Advance Payment pays the next EMI early and a Pre Payment cuts principal with the EMI kept; each creates and approves its own restructure and a new plan, and Rahim cannot choose a lower EMI.

## Before you start

⚠ You need permission to **Submit** a **Loan Repayment**. Submitting changes the loan's plan for good, so test on a test loan. Names in the screenshots are test records on the dev site.

## Steps

1. Open the loan, click Create and choose Loan Repayment.
2. For an early EMI, set **Repayment Type** to Advance Payment, enter **Value Date** (with a time) and **Amount Paid** (the EMI, 8,979 in the walkthrough) and **Reference Number**. Click **Save**, then **Submit** and **Yes**.
3. For a prepayment, set the type to Pre Payment and enter the amount (20,000 in the walkthrough, fee included). Expand Prepayment Charges, add a row and enter **Charge Code** and **Charge Amount** (the fee, typed by hand: 1% of 20,000 was 200). Click Save, then Submit and Yes.

![Advance Payment entered](/assets/lending_assistant/kb_img/J6/J6-S2-01_advance-filled-top.png)

![Pre Payment entered](/assets/lending_assistant/kb_img/J6/J6-S2-09_prepay-filled-top.png)

![The fee row, typed by hand](/assets/lending_assistant/kb_img/J6/J6-S2-11_prepay-fee-row-filled.png)

## What you should see

The advance splits into interest up to the payment date and principal. It creates and approves a Loan Restructure by itself, the old plan becomes Rescheduled and a new plan is Active. The demand run for the original due date then bills nothing, because the EMI is already covered.

![Advance submitted](/assets/lending_assistant/kb_img/J6/J6-S2-03_advance-submitted.png)

![The auto-approved restructure](/assets/lending_assistant/kb_img/J6/J6-S2-04_advance-auto-restructure-approved.png)

![Rescheduled and Active plans](/assets/lending_assistant/kb_img/J6/J6-S2-05_advance-plans-rescheduled-active.png)

![No demand on the original due date](/assets/lending_assistant/kb_img/J6/J6-S2-08_demands-list-0925-no-0510.png)

The prepayment splits into the fee (200), interest and principal. The fee becomes a Sales Invoice and a charges demand, both paid from the 20,000. The EMI stays 8,979 and the loan ends two months earlier.

![Fee, interest and principal](/assets/lending_assistant/kb_img/J6/J6-S2-13_prepay-split-fee-interest-principal.png)

![Rescheduled plans and the new Active plan](/assets/lending_assistant/kb_img/J6/J6-S2-15_prepay-plans-list.png)

![The new plan](/assets/lending_assistant/kb_img/J6/J6-S2-16_prepay-new-plan-header.png)

## If it looks wrong

Advance. The BRD wants an advance to cover the next EMIs (BR-LMS-180, partly covered). More than one EMI ahead does not cover the following EMIs: in the verification the extra only shrank the last row, and a product set to Reduce EMI got the same plan as Reduce Tenure (DEF-21). The workaround is to take one EMI at a time as an Advance Payment and larger amounts as a Pre Payment.

Fee. The product's fee row has no "on prepayment" event, so the officer types the code and the amount and nothing checks them (BR-LMS-131, ND-1).

Choice. Loan Repayment has no choice between lower EMI and shorter loan: a Pre Payment always uses Repay Fixed Amount per Period, whatever the product says (BR-LMS-181, partly covered). The workaround is a normal restructure with the remaining term, which counts as a restructure and meets DEF-18. The fix is ND-21 (D20). See `bridge.BR-LMS-180` and `bridge.BR-LMS-181`.

![A Pre Payment restructure always uses a fixed amount](/assets/lending_assistant/kb_img/J6/J6-S2-18_prepay-restructure-fixed-amount-only.png)
