---
id: howto.customer.create
type: howto
title: How to create a borrower (Customer)
summary: "Create the Customer record that a loan is booked against: name and type, then Save."
br_ids: []
brd_section: 7.1
doctypes: [Customer]
dev_items: []
journeys: [J1]
actions: ["Customer:create"]
fields: [Customer.Customer Name, Customer.Customer Type]
options: [Customer.Customer Type=Individual]
menus: [Lending > Loan Origination > Customer]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J1/J1-S1-01_customer-filled.png, /assets/lending_assistant/kb_img/J1/J1-S1-02_customer-saved.png]
sources:
  - "sources/verification/walkthroughs/J1_walkthrough.md#stage-1"
  - "sources/verification/walkthroughs/J1_walkthrough.md#stage-5"
  - "sources/verification/walkthroughs/J1_walkthrough.md#1.1"
  - "sources/verification/walkthroughs/J1_walkthrough.md#5.1"
related: [howto.loan.create, journey.J1]
version: 1
status: approved
approved_by: Owner
---
**In short:** Create the Customer record that a loan is booked against: name and type, then Save.

## Before you start

You need permission to create a **Customer**. Names you see in the screenshots, such as customer and loan names, are test records on the dev site. The same steps create the borrower for a migrated loan. The name you give is the one staff pick later in the loan's Applicant field.

## Steps

1. Open **Lending > Loan Origination > Customer**, then click **+ Add Customer** (address `/desk/customer/new`).
2. Fill **Customer Name** with the borrower's name, for example Rahim.
3. Set **Customer Type** to **Individual**.
4. Click **Save**.

![Customer form filled in with name and type](/assets/lending_assistant/kb_img/J1/J1-S1-01_customer-filled.png)

## What you should see

The customer is saved and shown as Enabled, with the name in the header.

![Customer saved](/assets/lending_assistant/kb_img/J1/J1-S1-02_customer-saved.png)

## If it looks wrong

If **Save** is refused with a permission message, ask for a role that can create a Customer. The Customer is only the party: the loan itself is booked next (`howto.loan.create`).
