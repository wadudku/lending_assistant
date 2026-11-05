---
id: howto.loan.view
type: howto
title: "How to check a loan: rules, amounts and connections"
summary: "Open a loan to see which product rules it picked up, how much was drawn, and everything linked to it on the Connections tab."
br_ids: []
brd_section: 7.1
doctypes: [Loan]
dev_items: []
journeys: [J1]
actions: ["Loan:view"]
fields: [Loan.Rate of Interest (%) / Year, Loan.Penalty Charges Rate, Loan.Loan Category, Loan.Loan Amount, Loan.Disbursed Amount, Loan.Disbursement Date]
menus: [Lending > Loan Management > Loan]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J1/J1-S2-03_loan-rules-from-product.png, /assets/lending_assistant/kb_img/J1/J1-S2-05_loan-accounts-from-product.png, /assets/lending_assistant/kb_img/J1/J1-S2-04_loan-amount-vs-disbursed.png, /assets/lending_assistant/kb_img/J1/J1-S4-01_loan-dashboard-connections.png]
sources:
  - "sources/verification/walkthroughs/J1_walkthrough.md#stage-2"
  - "sources/verification/walkthroughs/J1_walkthrough.md#stage-4"
  - "sources/verification/walkthroughs/J1_walkthrough.md#2.2"
  - "sources/verification/walkthroughs/J1_walkthrough.md#2.3"
  - "sources/verification/walkthroughs/J1_walkthrough.md#4.1"
related: [howto.loan_product.view, howto.loan_repayment_schedule.view, journey.J1]
version: 1
status: approved
approved_by: Owner
---
**In short:** Open a loan to see which product rules it picked up, how much was drawn, and everything linked to it on the Connections tab.

## Before you start

Read permission on **Loan** is enough. Names you see in the screenshots, such as customer and loan names, are test records on the dev site.

## Steps

1. Open the loan from **Lending > Loan Management > Loan**.
2. On the **Details** tab, read **Loan Details**: **Rate of Interest (%) / Year**, **Penalty Charges Rate** and **Loan Category**.
3. Expand **Account Info** to see the accounts.
4. Compare **Loan Amount** with **Disbursed Amount**.
5. Open the **Connections** tab.

![Rate, penalty and category copied from the product](/assets/lending_assistant/kb_img/J1/J1-S2-03_loan-rules-from-product.png)

## What you should see

The rate, penalty and category match the product, and none was typed on the loan. **Account Info** shows the disbursement, payment, loan, interest income and penalty income accounts, also from the product.

![Accounts copied from the product](/assets/lending_assistant/kb_img/J1/J1-S2-05_loan-accounts-from-product.png)

A loan drawn in one go shows the same **Loan Amount** and **Disbursed Amount** and a **Disbursement Date**.

![Loan Amount and Disbursed Amount](/assets/lending_assistant/kb_img/J1/J1-S2-04_loan-amount-vs-disbursed.png)

The **Connections** tab shows **Stats** (Disbursed Amount, Pending Principal) and links grouped as Schedule and Disbursement, Repayment, Security, Adjustments, Logs and Accounting.

![Loan Connections tab](/assets/lending_assistant/kb_img/J1/J1-S4-01_loan-dashboard-connections.png)

## If it looks wrong

If the rate differs from the product, someone edited it on the draft, and nothing stopped that (ND-5). The accounting entries are not on this dashboard. Open them through the ledger (see `howto.loan_disbursement.view_ledger`). Migrated loans show **Is Imported** and **Migration Date** (see `howto.data_import.migrate_loan`).
