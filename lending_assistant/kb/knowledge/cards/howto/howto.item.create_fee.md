---
id: howto.item.create_fee
type: howto
title: How to create a fee item for a loan charge
summary: "Loan charge types are ordinary ERPNext Items, so a processing fee starts as a non-stock service Item."
br_ids: [BR-LMS-113]
brd_section: 7.2
doctypes: [Item]
dev_items: []
journeys: [J2]
actions: ["Item:create"]
fields: [Item.Item Code, Item.Item Group, Item.Maintain Stock, Item.Default Unit of Measure]
options: []
menus: [Stock > Item]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J2/J2-S3-01_item-fee-filled.png, /assets/lending_assistant/kb_img/J2/J2-S3-02_item-fee-saved.png]
sources:
  - "sources/verification/walkthroughs/J2_walkthrough.md#stage-3"
  - "sources/verification/walkthroughs/J2_walkthrough.md#3.1"
related: [howto.loan_product.add_charge, bridge.BR-LMS-113, journey.J2]
version: 1
status: approved
approved_by: Owner
---
**In short:** Loan charge types are ordinary ERPNext Items, so a processing fee starts as a non-stock service Item.

## Before you start

⚠ You need permission to create an **Item**. This is an ERPNext screen, not a Lending screen. Names in the screenshots are test records on the dev site.

## Steps

1. Open Stock > Item and click **+ Add Item**.
2. Enter **Item Code** (for example a processing-fee code), set **Item Group** to Services, untick **Maintain Stock** and set **Default Unit of Measure** to Nos.
3. Click **Save**.

![Fee item filled](/assets/lending_assistant/kb_img/J2/J2-S3-01_item-fee-filled.png)

## What you should see

The Item is saved and Enabled. It can now be picked as the Charge Type of a product's charge row (`howto.loan_product.add_charge`).

![Fee item saved](/assets/lending_assistant/kb_img/J2/J2-S3-02_item-fee-saved.png)

## If it looks wrong

Creating the Item is only the first step. The BRD wants the product's fee rules to raise the fee on each loan automatically (BR-LMS-113, partly covered). Putting the Item on a product does not do that: see `howto.loan_product.add_charge` and `bridge.BR-LMS-113`.
