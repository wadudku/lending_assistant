---
id: howto.loan.create
type: howto
title: How to book a loan with auto-disbursement
summary: "Create a Loan for a borrower with the product, amount and dates, tick Auto create disbursement, and Save as a draft."
br_ids: []
brd_section: 7.1
doctypes: [Loan]
dev_items: []
journeys: [J1]
actions: ["Loan:create"]
fields: [Loan.Applicant Type, Loan.Applicant, Loan.Posting Date, Loan.Auto create disbursement on loan booking, Loan.Loan Product, Loan.Loan Amount, Loan.Repayment Method, Loan.Tenure, Loan.Repayment Start Date, Loan.Cost Center, Loan.Rate of Interest (%) / Year]
options: [Loan.Repayment Method=Repay Over Number of Periods, Loan.Applicant Type=Customer]
menus: [Lending > Loan Management > Loan]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J1/J1-S1-03_loan-filled-applicant.png, /assets/lending_assistant/kb_img/J1/J1-S1-04_loan-filled-terms.png, /assets/lending_assistant/kb_img/J1/J1-S1-05_loan-saved-draft.png]
sources:
  - "sources/verification/walkthroughs/J1_walkthrough.md#stage-1"
  - "sources/verification/walkthroughs/J1_walkthrough.md#1.2"
  - "sources/verification/walkthroughs/J1_walkthrough.md#2.2"
  - "sources/verification/walkthroughs/J1_walkthrough.md#5.2"
related: [howto.customer.create, howto.loan.submit, journey.J1]
version: 1
status: approved
approved_by: Owner
---
**In short:** Create a Loan for a borrower with the product, amount and dates, tick Auto create disbursement, and Save as a draft.

## Before you start

You need create permission on **Loan** (the Loan Manager role has it). The Customer must exist (`howto.customer.create`). Names you see in the screenshots, such as customer and loan names, are test records on the dev site. In production the origination system creates the same record by a web call, because Frappe Lending 16.5.1 has no separate booking API.

## Steps

1. Open **Lending > Loan Management > Loan**, then **+ Add Loan** (`/desk/loan/new`).
2. Leave **Applicant Type** as **Customer** and pick the borrower in **Applicant**.
3. Set **Posting Date** to the day the money reached the borrower. Back-dating is allowed.
4. Tick **Auto create disbursement on loan booking**.
5. Choose the **Loan Product** (for example a personal loan with monthly EMI) and type **Loan Amount** (for example 100,000).
6. Set **Repayment Method** to **Repay Over Number of Periods**, **Tenure** to 12 and **Repayment Start Date** to the first due date.
7. Under **Accounting Dimensions**, set **Cost Center**.
8. Click **Save**.

![Loan form, applicant and booking section](/assets/lending_assistant/kb_img/J1/J1-S1-03_loan-filled-applicant.png)

![Loan form, product, amount and terms](/assets/lending_assistant/kb_img/J1/J1-S1-04_loan-filled-terms.png)

## What you should see

The loan is saved with status **Draft**. **Rate of Interest (%) / Year**, **Penalty Charges Rate** and **Loan Category** are already filled from the product.

![Loan saved as Draft](/assets/lending_assistant/kb_img/J1/J1-S1-05_loan-saved-draft.png)

## If it looks wrong

While the loan is a draft, **Rate of Interest (%) / Year** can still be edited, so one loan can differ from the product with no approval (ND-5 in the verification report). Locking it needs a permission-level setting that is not applied. Next step: `howto.loan.submit`.
