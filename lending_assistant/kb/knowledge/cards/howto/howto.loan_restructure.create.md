---
id: howto.loan_restructure.create
type: howto
title: How to start a restructure and compare two options
summary: "A Draft Loan Restructure is the what-if for one loan: save one draft per option, compare the plans they build, and delete the draft you do not choose."
br_ids: [BR-LMS-154, BR-LMS-124, BR-LMS-182]
brd_section: 7.6
doctypes: [Loan Restructure, Loan Repayment Schedule, Loan Product]
dev_items: [D11, D16]
journeys: [J5, J6]
actions: ["Loan Restructure:create"]
fields: [Loan Restructure.Loan, Loan Restructure.Restructure Date, Loan Restructure.Reason for Restructure, Loan Restructure.New Rate Of Interest, Loan Restructure.New Repayment Start Date, Loan Restructure.New Repayment Method, Loan Restructure.New Repayment Period in Months, Loan Restructure.New Monthly Repayment Amount, Loan Restructure.Interest Treatment, Loan Restructure.Penal Treatment]
options: [Loan Restructure.New Repayment Method=Repay Over Number of Periods, Loan Restructure.New Repayment Method=Repay Fixed Amount per Period]
menus: [Lending > Loan Management > Loan Restructure]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J5/J5-S3-02_trap-default-tenure.png, /assets/lending_assistant/kb_img/J5/J5-S3-04_draft-a-filled-terms.png, /assets/lending_assistant/kb_img/J5/J5-S3-06_draft-a-saved-terms.png, /assets/lending_assistant/kb_img/J5/J5-S3-08_draft-b-filled-terms.png, /assets/lending_assistant/kb_img/J5/J5-S3-12_two-drafts-list.png, /assets/lending_assistant/kb_img/J5/J5-S3-13_draft-b-deleted-list.png, /assets/lending_assistant/kb_img/J6/J6-S3-02_restructure-filled-treatment.png]
sources:
  - "sources/verification/walkthroughs/J5_walkthrough.md#stage-3"
  - "sources/verification/walkthroughs/J5_walkthrough.md#3.1"
  - "sources/verification/walkthroughs/J5_walkthrough.md#3.2"
  - "sources/verification/walkthroughs/J5_walkthrough.md#3.3"
  - "sources/verification/walkthroughs/J5_walkthrough.md#3.5"
  - "sources/verification/walkthroughs/J6_walkthrough.md#stage-3"
  - "sources/verification/walkthroughs/J6_walkthrough.md#3.1"
related: [howto.loan_repayment_schedule.compare_plans, howto.loan_restructure.approve, howto.loan_product.set_rates, bridge.BR-LMS-154, bridge.BR-LMS-124, bridge.BR-LMS-182, journey.J5, screen.loan_restructure, screen.loan_repayment_schedule]
version: 1
status: approved
approved_by: Owner
---
**In short:** A Draft Loan Restructure is the what-if for one loan: save one draft per option, compare the plans they build, and delete the draft you do not choose.

## Before you start

⚠ You need permission to create a **Loan Restructure**. Saving a draft changes nothing on the loan, but it builds a draft restructure and a draft repayment plan that someone must delete. A Normal Restructure fails on a product whose **BPI Recovery Method** is Add to First EMI or Amortized Over Tenure (DEF-17); the walkthrough used a copy of the product set to Upfront Deduction. Names in the screenshots are test records on the dev site.

## Steps

1. Open Lending > Loan Management > Loan Restructure and click + Add.
2. Pick the **Loan** and enter **Restructure Date**. A harmless message box about a missing form field may appear: close it.
3. Enter **Reason for Restructure**, the **New Rate Of Interest** (it starts empty and must be typed), **New Repayment Start Date**, and for option A **New Repayment Method** Repay Over Number of Periods with **New Repayment Period in Months** set to the months left. For option B choose Repay Fixed Amount per Period and enter **New Monthly Repayment Amount**.
4. When the loan has overdue amounts, choose **Interest Treatment** and **Penal Treatment** (the J6 walkthrough capitalized both).
5. Click **Save**. Do not submit.
6. Make a second draft for the other option the same way.

![Option A terms entered](/assets/lending_assistant/kb_img/J5/J5-S3-04_draft-a-filled-terms.png)

## What you should see

Each draft saves with its new monthly amount and a draft plan. In the J5 example the 7-month option gave an EMI of 9,013 and the fixed-EMI option kept 8,979 and needed one extra month. The loan does not change.

![Option A saved: EMI 9,013](/assets/lending_assistant/kb_img/J5/J5-S3-06_draft-a-saved-terms.png)

![Option B: fixed amount 8,979](/assets/lending_assistant/kb_img/J5/J5-S3-08_draft-b-filled-terms.png)

To delete the option you do not choose, delete its plan first (the plan links to the restructure), then the restructure. The list then shows only the chosen draft.

![Two drafts](/assets/lending_assistant/kb_img/J5/J5-S3-12_two-drafts-list.png)

![One draft left](/assets/lending_assistant/kb_img/J5/J5-S3-13_draft-b-deleted-list.png)

## If it looks wrong

Tenure trap. After you pick the method, the period shows 0. If you change only the rate and leave it at 0, the code falls back to the loan's original term and silently extends the loan. Always type the remaining months.

![The period shows 0 after choosing the method](/assets/lending_assistant/kb_img/J5/J5-S3-02_trap-default-tenure.png)

The BRD wants a dry run of a whole repricing batch with a preview per loan (BR-LMS-154, not covered; ND-18, D11). Today it is one draft per loan and per option, and each leaves two drafts to delete (BR-LMS-124, partly covered). The BRD also wants the type and treatment of a restructure recorded (BR-LMS-182, partly covered): the only type a user chooses is Normal Restructure (Pre Payment and Advance Payment restructures are created by the system), and there is no field for the regulatory treatment (ND-22, D16). The workaround is to write the category and approval memo reference in Reason for Restructure. See `bridge.BR-LMS-154`.

![Overdue and capitalize treatments](/assets/lending_assistant/kb_img/J6/J6-S3-02_restructure-filled-treatment.png)
