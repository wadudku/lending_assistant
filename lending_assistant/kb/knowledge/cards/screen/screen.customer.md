---
id: screen.customer
type: screen
title: "Screen: Customer"
summary: The Customer screen is ERPNext's standard record for a borrower; Frappe Lending adds a Loan Details tab and an Is NPA tick to it.
br_ids: []
brd_section: 7.1
doctypes: [Customer]
dev_items: []
fields: [Customer.Customer Name, Customer.Customer Type, Customer.Customer Group, Customer.Territory, Customer.Is NPA]
options: [Customer.Customer Type=Individual]
menus: [Lending > Loan Origination > Customer]
lending_version: 16.5.1
code_refs: [lending/install.py]
images: [/assets/lending_assistant/kb_img/J1/J1-S1-01_customer-filled.png, /assets/lending_assistant/kb_img/J1/J1-S1-02_customer-saved.png]
sources:
  - "sources/verification/walkthroughs/J1_walkthrough.md#stage-1"
  - "sources/verification/walkthroughs/J1_walkthrough.md#1.1"
  - "sources/verification/verification_report.md#BR-LMS-100"
related: [howto.customer.create, howto.loan.create, brd_section.7.1, lifecycle.BOOKED]
version: 1
status: approved
approved_by: Owner
---
**In short:** The Customer screen is ERPNext's standard record for a borrower; Frappe Lending adds a Loan Details tab and an Is NPA tick to it.

## What this screen is for

**Customer** is the standard ERPNext record for the borrower. A loan points to it through its Applicant Type (Customer) and Applicant fields. In the walkthroughs the officer creates the customer first, then books the loan against it (menu: Lending > Loan Origination > Customer). The screen is part of ERPNext, not of Frappe Lending, so its permissions come from ERPNext's sales, stock and accounts roles.

## Before and after

Before: nothing. A borrower who is not yet a customer needs one before a loan can be booked in the walkthrough (see `howto.customer.create`). After: the loan is booked with this customer as the applicant (see `screen.loan`).

## Key fields

**Customer Name** and **Customer Type** are required; the walkthrough used the type Individual. Other fields on the Details tab include **Customer Group**, **Territory** and **Gender**. Frappe Lending adds a **Loan Details** tab, shown on the saved customer in the screenshots, and an **Is NPA** tick. The installed `lending/install.py` creates both as custom fields on Customer, and the loan code sets the tick when it classifies the borrower's loans.

![A new customer, filled in](/assets/lending_assistant/kb_img/J1/J1-S1-01_customer-filled.png)

![The saved customer, with the Loan Details tab](/assets/lending_assistant/kb_img/J1/J1-S1-02_customer-saved.png)

## BRD needs it serves

No BR-LMS row in the verified requirements data names the Customer screen, so this card links none. Names in the screenshots are test records on the dev site.
