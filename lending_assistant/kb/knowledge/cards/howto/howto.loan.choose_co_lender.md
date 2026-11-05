---
id: howto.loan.choose_co_lender
type: howto
title: How to book a co-lent loan and see the partner's share
summary: "Choosing a Loan Partner on the loan books the partner's share on disbursement, on its own schedule and on each demand and first repayment; a Loan Closure posts nothing to the partner."
br_ids: [BR-LMS-212, BR-LMS-211, BR-LMS-210, BR-LMS-123]
brd_section: 7.12
doctypes: [Loan, Loan Disbursement, Loan Repayment Schedule, Loan Demand, Loan Repayment, Loan Product]
dev_items: []
journeys: [J10]
actions: ["Loan:choose_co_lender"]
fields: [Loan.Loan Partner, Loan.FLDG Triggered, Loan Demand.Partner Share, Loan Repayment.Total Partner Principal Share, Loan Repayment.Total Partner Interest Share]
options: []
menus: [Lending > Loan Management > Loan, Lending > Loan Management > Loan Repayment Schedule, Lending > Loan Management > Loan Demand]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J10/J10-S3-01_loan-filled.png, /assets/lending_assistant/kb_img/J10/J10-S3-07_schedule-colender.png, /assets/lending_assistant/kb_img/J10/J10-S3-12_demand-interest.png, /assets/lending_assistant/kb_img/J10/J10-S3-15_repayment-colending.png, /assets/lending_assistant/kb_img/J10/J10-S3-20_closure-colending-zero.png]
sources:
  - "sources/verification/walkthroughs/J10_walkthrough.md#stage-1"
  - "sources/verification/walkthroughs/J10_walkthrough.md#stage-2"
  - "sources/verification/walkthroughs/J10_walkthrough.md#stage-3"
  - "sources/verification/walkthroughs/J10_walkthrough.md#3.1"
  - "sources/verification/walkthroughs/J10_walkthrough.md#3.3"
  - "sources/verification/walkthroughs/J10_walkthrough.md#3.5"
  - "sources/verification/walkthroughs/J10_walkthrough.md#3.7"
related: [howto.loan_partner.create, howto.loan_product.duplicate, howto.loan_disbursement.create, howto.loan_repayment.close_loan, bridge.BR-LMS-212, bridge.BR-LMS-211, bridge.BR-LMS-210, journey.J10, screen.loan, screen.loan_disbursement, screen.loan_repayment_schedule, screen.loan_demand, screen.loan_repayment]
version: 1
status: approved
approved_by: Owner
---
**In short:** Choosing a Loan Partner on the loan books the partner's share on disbursement, on its own schedule and on each demand and first repayment; a Loan Closure posts nothing to the partner.

## Before you start

⚠ You need a **Loan Partner** (`howto.loan_partner.create`). In the walkthrough it was also added to the product as a single tag in **Loan Partners** on the **Co Lending** tab. Names in the screenshots are test records on the dev site.

## Steps

1. Click Add Loan and fill the usual fields. Set **Loan Partner** to the partner.
2. Click **Save**, then **Submit** and **Yes**. Disburse from the loan as usual (`howto.loan_disbursement.create`).

![The loan with a partner chosen](/assets/lending_assistant/kb_img/J10/J10-S3-01_loan-filled.png)

3. Open the loan's repayment schedule and read its Co Lending tab: the partner's share, rate and the Co Lender Schedule rows.

![The Co Lender Schedule](/assets/lending_assistant/kb_img/J10/J10-S3-07_schedule-colender.png)

4. After the demands are billed, open a **Loan Demand** and read **Partner Share** on its Co Lending tab.

![The partner share on a demand](/assets/lending_assistant/kb_img/J10/J10-S3-12_demand-interest.png)

## What you should see

On disbursement the bank pays the whole amount and the partner's share is booked as a receivable against the partner's clearing account. The partner's plan is its own instalment calculation over the partner's share and rate, not a fixed percentage of the borrower's plan. A first repayment shows **Total Partner Principal Share** and **Total Partner Interest Share**, and the bank keeps the cash and owes the partner a payable.

![The first repayment's partner shares](/assets/lending_assistant/kb_img/J10/J10-S3-15_repayment-colending.png)

## If it looks wrong

The partner's data is covered (BR-LMS-123 and BR-LMS-116), with gaps:

- FLDG terms are recorded but never evaluated: the loan's **FLDG Triggered** box is never ticked by any process (BR-LMS-210, ND-41). The workaround is a person who watches the days past due and posts a Journal Entry by hand.
- The share is one figure per partner, not per product (BR-LMS-211, ND-42). The workaround is one Loan Partner record per share, each linked to its own product.
- A Loan Closure shows both partner shares as zero and posts nothing to the partner (BR-LMS-212, DEF-44). Before closing, a Finance officer reads the partner's remaining principal off the Co Lender Schedule and posts a Journal Entry by hand.

![The closure with zero partner shares](/assets/lending_assistant/kb_img/J10/J10-S3-20_closure-colending-zero.png)

- A credit note for a waived charge does not reverse the partner's charge share (DEF-45, read from code, not tested live). Reverse it by Journal Entry.

The fix for the last three is ND-40 or ND-42. See `bridge.BR-LMS-212`.
