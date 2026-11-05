---
id: howto.loan_demand_offset_order.create
type: howto
title: "How to see, create and assign a payment order"
summary: "A payment order says in which sequence a payment settles penalty, charges, interest and principal; the Company holds four, and a product can name its own."
br_ids: [BR-LMS-114]
brd_section: 7.2
doctypes: [Loan Demand Offset Order, Loan Demand Offset Detail, Loan Product, Company]
dev_items: []
journeys: [J2]
actions: ["Loan Demand Offset Order:create"]
fields: [Loan Demand Offset Order.Title, Loan Demand Offset Detail.Demand Type, Loan Product.Collection Offset Sequence for Standard Asset]
options: []
menus: []
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J2/J2-S3-05_company-offset-sequences.png, /assets/lending_assistant/kb_img/J2/J2-S3-06_offset-order-list.png, /assets/lending_assistant/kb_img/J2/J2-S3-07_pt-std-order-rows.png, /assets/lending_assistant/kb_img/J2/J2-S3-08_ver-wt-order-filled.png, /assets/lending_assistant/kb_img/J2/J2-S3-09_ver-wt-order-saved.png, /assets/lending_assistant/kb_img/J2/J2-S3-10_override-filled.png, /assets/lending_assistant/kb_img/J2/J2-S3-11_override-saved.png]
sources:
  - "sources/verification/walkthroughs/J2_walkthrough.md#stage-3"
  - "sources/verification/walkthroughs/J2_walkthrough.md#3.4"
  - "sources/verification/walkthroughs/J2_walkthrough.md#3.5"
  - "sources/verification/walkthroughs/J2_walkthrough.md#3.6"
  - "sources/verification/walkthroughs/J2_walkthrough.md#6.2"
related: [bridge.BR-LMS-114, journey.J2, screen.loan_product]
version: 1
status: approved
approved_by: Owner
---
**In short:** A payment order says in which sequence a payment settles penalty, charges, interest and principal; the Company holds four, and a product can name its own.

## Before you start

⚠ You need permission to create a **Loan Demand Offset Order** and to edit a **Loan Product**. Do not edit the Company's orders, which are shared. Names in the screenshots are test records on the dev site.

## Steps

1. Look first at what exists. The Company form shows four orders, one each for Standard, Sub Standard, Written Off and Settlement, chosen by the NPA flag. Type Loan Demand Offset Order in the search bar to open the list, and open one order to see its rows.
2. To make your own, click + Add, enter a **Title** and add rows in this order, each with a **Demand Type**: Penalty, Additional Interest, Charges, EMI (Principal + Interest). Click **Save**.
3. Open the product and set **Collection Offset Sequence for Standard Asset** to your order. Leave the other three empty so they use the Company's orders. Click **Save**.

![The Company's four orders](/assets/lending_assistant/kb_img/J2/J2-S3-05_company-offset-sequences.png)

![The orders in the list](/assets/lending_assistant/kb_img/J2/J2-S3-06_offset-order-list.png)

![The standard order's rows](/assets/lending_assistant/kb_img/J2/J2-S3-07_pt-std-order-rows.png)

![Own order filled](/assets/lending_assistant/kb_img/J2/J2-S3-08_ver-wt-order-filled.png)

## What you should see

The new order is saved with four rows in the sequence you set, and the product field holds its name. The activity log shows the change from empty to your order.

![Override filled on the product](/assets/lending_assistant/kb_img/J2/J2-S3-10_override-filled.png)

![Order saved](/assets/lending_assistant/kb_img/J2/J2-S3-09_ver-wt-order-saved.png)

![Override saved on the product](/assets/lending_assistant/kb_img/J2/J2-S3-11_override-saved.png)

## If it looks wrong

The order is not stored on the loan. It is read from the product each time a payment is posted, and falls back to the Company when the product field is empty. Changing a product's order therefore changes how its existing loans are paid from the next payment, with no version kept (this adds to the BR-LMS-117 gap).

The walkthrough used an order with no plain Interest row, because in 16.5.1 a payment never goes to an Interest component, so the whole EMI goes to principal and interest stays overdue (DEF-3). See `bridge.BR-LMS-114`.
