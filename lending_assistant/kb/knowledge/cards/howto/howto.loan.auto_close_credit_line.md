---
id: howto.loan.auto_close_credit_line
type: howto
title: How a line-of-credit loan is closed automatically
summary: "A scheduled job closes an Active line-of-credit loan once its limit end date has passed and nothing is drawn; it has no screen, no loan filter, no approval and no notification."
br_ids: [BR-LMS-222]
brd_section: 7.13
doctypes: [Loan, Loan Product, Loan Repayment]
dev_items: []
journeys: [J9]
actions: ["Loan:auto_close_credit_line"]
fields: [Loan Product.Repayment Schedule Type, Loan.Limit Applicable End, Loan.Utilized Limit Amount, Loan.Closure Date, Loan Repayment.Repayment Type]
options: [Loan Repayment.Repayment Type=Pre Payment, Loan Repayment.Repayment Type=Normal Repayment]
menus: [Lending > Setup > Loan Product, Lending > Loan Management > Loan]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J9/J9-S7-01_loc-product-setting.png, /assets/lending_assistant/kb_img/J9/J9-S7-02a_prepayment-filled.png, /assets/lending_assistant/kb_img/J9/J9-S7-03_loc-still-active-utilised-0.png, /assets/lending_assistant/kb_img/J9/J9-S7-04_loc-loan-closed-by-job.png]
sources:
  - "sources/verification/walkthroughs/J9_walkthrough.md#stage-7"
  - "sources/verification/walkthroughs/J9_walkthrough.md#7.1"
  - "sources/verification/walkthroughs/J9_walkthrough.md#7.2"
  - "sources/verification/walkthroughs/J9_walkthrough.md#7.3"
related: [howto.loan_repayment.close_loan, howto.loan_product.set_repayment_method, bridge.BR-LMS-222, journey.J9, screen.loan, screen.loan_product, screen.loan_repayment]
version: 1
status: approved
approved_by: Owner
---
**In short:** A scheduled job closes an Active line-of-credit loan once its limit end date has passed and nothing is drawn; it has no screen, no loan filter, no approval and no notification.

## Before you start

⚠ The job runs for the whole site from the scheduler, so do not run it by hand on a live site. Everything below is what you set up and what to expect. Names in the screenshots are test records on the dev site.

## Steps

1. Open the **Loan Product** and check that **Repayment Schedule Type** is Line of Credit.

![Part of the line-of-credit product with Is Term Loan unticked](/assets/lending_assistant/kb_img/J9/J9-S7-01_loc-product-setting.png)

2. On the loan, check **Limit Applicable End** is in the past.
3. Repay the drawn amount. A line-of-credit loan has no Create button for a repayment, so use the Loan Repayment list and click Add Loan Repayment. Set **Repayment Type** to Pre Payment, because a Normal Repayment is refused when nothing was demanded.

![The repayment entered](/assets/lending_assistant/kb_img/J9/J9-S7-02a_prepayment-filled.png)

4. Click **Save**, then **Submit** and **Yes**. The loan shows **Utilized Limit Amount** 0 and stays Active.

![The loan still Active with a Disbursed Amount of 20,000](/assets/lending_assistant/kb_img/J9/J9-S7-03_loc-still-active-utilised-0.png)

## What you should see

When the daily job `auto_close_loc_loans` runs, the loan becomes Closed and **Closure Date** is the date passed to the job. The job matches Active, Line of Credit loans whose limit end date has passed and whose utilised limit is 0.

![Closed by the job](/assets/lending_assistant/kb_img/J9/J9-S7-04_loc-loan-closed-by-job.png)

## If it looks wrong

This requirement is covered (BR-LMS-222), with these limits:

- There is no screen for the job, and `auto_close_loc_loans` takes no loan filter, so it works on the whole site.
- It has no approval or notification step.
- It runs only after the limit end date, so a line repaid in full before that date stays open.

See `bridge.BR-LMS-222`.
