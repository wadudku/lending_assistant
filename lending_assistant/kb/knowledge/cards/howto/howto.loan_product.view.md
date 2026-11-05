---
id: howto.loan_product.view
type: howto
title: How to look at a loan product's rules (view only)
summary: "Open a Loan Product to see the rate, schedule type and accounts that every loan of that product copies. Look, do not edit."
br_ids: []
brd_section: 7.1
doctypes: [Loan Product]
dev_items: [D5]
journeys: [J1]
actions: ["Loan Product:view"]
fields: [Loan Product.Rate of Interest (%) Yearly, Loan Product.Penalty Interest Rate (%), Loan Product.Loan Category, Loan Product.Repayment Schedule Type, Loan Product.Cyclic Day Of the Month]
menus: [Lending > Setup > Loan Product]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J1/J1-S2-01_product-pl-emi-rules.png, /assets/lending_assistant/kb_img/J1/J1-S2-02_product-pl-emi-accounts.png]
sources:
  - "sources/verification/walkthroughs/J1_walkthrough.md#stage-2"
  - "sources/verification/walkthroughs/J1_walkthrough.md#2.1"
  - "sources/verification/walkthroughs/J1_walkthrough.md#2.2"
  - "sources/verification/reqs.json#BR-LMS-117"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-117"
  - "sources/verification/FINAL_REPORT.md#D4"
  - "sources/verification/FINAL_REPORT.md#D5"
related: [howto.loan.view, journey.J1]
version: 1
status: approved
approved_by: Owner
---
**In short:** Open a Loan Product to see the rate, schedule type and accounts that every loan of that product copies. Look, do not edit.

## Before you start

Read permission is enough. ⚠ A Loan Product is shared configuration: do not edit it. Names you see in the screenshots, such as customer and loan names, are test records on the dev site.

## Steps

1. Open **Lending > Setup > Loan Product** and open the product, for example a monthly-EMI personal loan.
2. On the **Details** tab, read the rate, penalty, category and schedule type.
3. Open the **Accounting** tab to see the account groups.

![Loan Product rules on the Details tab](/assets/lending_assistant/kb_img/J1/J1-S2-01_product-pl-emi-rules.png)

## What you should see

**Rate of Interest (%) Yearly** (for example 14), **Penalty Interest Rate (%)** (for example 12), **Loan Category** (Retail), **Repayment Schedule Type** (for example Monthly as per cycle date) and **Cyclic Day Of the Month** (for example 5). The **Accounting** tab lists Loan Accounts, Interest Accounts, Additional Interest Accounts, Penalty Charges Accounts and Write Off Accounts.

![Loan Product Accounting tab](/assets/lending_assistant/kb_img/J1/J1-S2-02_product-pl-emi-accounts.png)

## If it looks wrong

The rate, penalty rate and category are copied onto each loan when it is booked, so a later edit of those does not change loans already booked; to check a loan picked them up, see `howto.loan.view`. Not everything is copied: the final report notes that the payment order is read from the product at each repayment, so editing it changes existing loans. The BRD wants product changes approved and versioned, which Frappe Lending does not provide (BR-LMS-117 is a gap; D5).
