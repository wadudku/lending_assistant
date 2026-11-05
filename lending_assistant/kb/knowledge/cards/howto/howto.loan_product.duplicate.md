---
id: howto.loan_product.duplicate
type: howto
title: How to copy a loan product
summary: "Duplicate an existing product to try a change safely; the copy needs its own Product Code before the first save and starts with no charges, partners or payment-order overrides if the source had none."
br_ids: []
brd_section: 7.1
doctypes: [Loan Product]
dev_items: []
journeys: [J2, J5]
actions: ["Loan Product:duplicate"]
fields: [Loan Product.Product Code, Loan Product.Product Name]
options: []
menus: [Lending > Setup > Loan Product]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J2/J2-S1-01_pl-emi-menu-duplicate.png, /assets/lending_assistant/kb_img/J2/J2-S1-02_duplicate-filled.png, /assets/lending_assistant/kb_img/J2/J2-S1-03_copy-saved.png, /assets/lending_assistant/kb_img/J2/J2-S1-04_copy-no-charges-no-offsets.png]
sources:
  - "sources/verification/walkthroughs/J2_walkthrough.md#stage-1"
  - "sources/verification/walkthroughs/J2_walkthrough.md#1.1"
related: [howto.loan_product.view, journey.J2, screen.loan_product]
version: 1
status: approved
approved_by: Owner
---
**In short:** Duplicate an existing product to try a change safely; the copy needs its own Product Code before the first save and starts with no charges, partners or payment-order overrides if the source had none.

## Before you start

⚠ You need permission to create a **Loan Product**. Do not edit a product that already has loans: copy it and work on the copy. Names you see in the screenshots, such as product codes, are test records on the dev site.

## Steps

1. Open Lending > Setup > Loan Product and open the product you want to copy, for example the standard personal-loan product.
2. Click the ⋯ menu at the top right, then Duplicate.
3. The form opens as a new, unsaved Loan Product with every value of the source, including its **Product Code**. Change **Product Code** and **Product Name**: the code is the record name, so it must be new before the first save.
4. Click **Save**.

![The ⋯ menu with Duplicate](/assets/lending_assistant/kb_img/J2/J2-S1-01_pl-emi-menu-duplicate.png)

![New code and name entered](/assets/lending_assistant/kb_img/J2/J2-S1-02_duplicate-filled.png)

## What you should see

The new product is saved and Enabled. The rate, penalty rate, repayment schedule type, cycle day, grace days and the loan, interest and penalty accounts are carried over from the source.

![The copy, saved](/assets/lending_assistant/kb_img/J2/J2-S1-03_copy-saved.png)

Duplicate copied the header fields and accounts. In the walkthrough the source had no Charges rows, no Loan Partners and no Collection Offset Sequence overrides, so the copy started with none of them either.

![Copy with empty offset overrides and empty Charges](/assets/lending_assistant/kb_img/J2/J2-S1-04_copy-no-charges-no-offsets.png)

## If it looks wrong

If the form still shows the source's Product Code, change it before you save. Saving it unchanged was not tried in the walkthrough. A copy only holds what the source holds, so add charges, partners and offset overrides afterwards (see howto.loan_product.add_charge, howto.loan_partner.create and howto.loan_demand_offset_order.create).
