---
id: screen.loan_product
type: screen
title: "Screen: Loan Product"
summary: "The Loan Product screen holds the rate, schedule type, accounts and rules that every loan of that product copies at booking."
br_ids: [BR-LMS-103, BR-LMS-106, BR-LMS-111, BR-LMS-112, BR-LMS-113, BR-LMS-114, BR-LMS-116, BR-LMS-117]
brd_section: 7.2
doctypes: [Loan Product]
dev_items: [D5]
fields: [Loan Product.Product Code, Loan Product.Product Name, Loan Product.Rate of Interest (%) Yearly, Loan Product.Penalty Interest Rate (%), Loan Product.Grace Period in Days, Loan Product.Repayment Schedule Type, Loan Product.Cyclic Day Of the Month, Loan Product.Loan Category, Loan Product.Days Past Due Threshold for NPA, Loan Product.Loan Charges, Loan Product.Loan Partners]
options: [Loan Product.Repayment Schedule Type=Monthly as per cycle date, Loan Product.Repayment Schedule Type=Line of Credit, Loan Product.Repayment Schedule Type=Flat Interest Rate, Loan Product.How to Handle Advance Payments=Reduce Tenure]
menus: [Lending > Setup > Loan Product]
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_product/loan_product.json]
images: [/assets/lending_assistant/kb_img/J1/J1-S2-01_product-pl-emi-rules.png, /assets/lending_assistant/kb_img/J1/J1-S2-02_product-pl-emi-accounts.png]
sources:
  - "sources/verification/walkthroughs/J1_walkthrough.md#stage-2"
  - "sources/verification/walkthroughs/J1_walkthrough.md#2.1"
  - "sources/verification/walkthroughs/J2_walkthrough.md#stage-1"
  - "sources/verification/walkthroughs/J2_walkthrough.md#1.2"
  - "sources/verification/verification_report.md#BR-LMS-112"
  - "sources/verification/verification_report.md#BR-LMS-117"
  - "sources/verification/reqs.json#BR-LMS-111"
related: [howto.loan_product.view, howto.loan.view, brd_section.7.2, bridge.BR-LMS-112, bridge.BR-LMS-117, devitem.D5]
version: 1
status: approved
approved_by: Owner
---
**In short:** The Loan Product screen holds the rate, schedule type, accounts and rules that every loan of that product copies at booking.

## What this screen is for

**Loan Product** is the template for a kind of loan. It holds the interest rate, the penalty rate, the repayment schedule type, the accounts the postings use and the collection rules. A loan copies these values when it is booked (menu: Lending > Setup > Loan Product). It is shared configuration: the walkthroughs looked at the shared product and made changes only on a copy.

## Before and after

After: a loan picks the product and copies the rate, penalty rate, category and accounts (see `screen.loan`, `howto.loan.view`). Some rules are read from the product at each repayment instead, such as the payment order (see `screen.loan_repayment`).

## Key fields

**Product Code** and **Product Name**, **Rate of Interest (%) Yearly**, **Penalty Interest Rate (%)**, **Grace Period in Days**, **Loan Category**, **Repayment Schedule Type** with its **Cyclic Day Of the Month**, and **Days Past Due Threshold for NPA**. The **Repayment Schedule Type** list has five options: Monthly as per repayment start date, Pro-rated calendar months, Monthly as per cycle date, Line of Credit and Flat Interest Rate (J2 walkthrough 1.2). Further sections hold the accounts, **Loan Charges** and **Loan Partners**. A product has no moratorium field: moratorium is set on the loan, which the report records as a gap (ND-2, `bridge.BR-LMS-112`).

![The product rules on the Details tab](/assets/lending_assistant/kb_img/J1/J1-S2-01_product-pl-emi-rules.png)

![The product's accounts on the Accounting tab](/assets/lending_assistant/kb_img/J1/J1-S2-02_product-pl-emi-accounts.png)

The installed doctype gives System Manager and Loan Manager read, write, create and delete, and Loan Reporter read only.

## BRD needs it serves

The main rows are BR-LMS-103, 106, 111, 112, 113, 114, 116 and 117 in BRD 7.2 (see `brd_section.7.2`); the bridges hold the verdicts. Weak points to remember: there is no product approval or versioning (`bridge.BR-LMS-117`, D5) and no moratorium default (`bridge.BR-LMS-112`).
