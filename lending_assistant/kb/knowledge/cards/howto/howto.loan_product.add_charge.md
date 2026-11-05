---
id: howto.loan_product.add_charge
type: howto
title: "How to add a fee to a product, and why it does not apply itself"
summary: "A product's Charges row names the fee and its accounts, but Frappe Lending 16.5.1 does not raise the fee on a loan from it; the officer types the fee on each loan."
br_ids: [BR-LMS-113]
brd_section: 7.2
doctypes: [Loan Product, Loan Charges, Loan]
dev_items: [D5]
journeys: [J2]
actions: ["Loan Product:add_charge"]
fields: [Loan Charges.Charge Type, Loan Charges.Charge Based On, Loan Charges.Percentage, Loan Charges.Income Account, Loan Charges.Receivable Account, Loan Charges.Waiver Account, Loan Charges.Write Off Account, Loan Charges.Suspense Account]
options: [Loan Charges.Charge Based On=Percentage]
menus: [Lending > Setup > Loan Product]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J2/J2-S3-03_charge-row-filled.png, /assets/lending_assistant/kb_img/J2/J2-S3-04_charge-row-saved.png]
sources:
  - "sources/verification/walkthroughs/J2_walkthrough.md#stage-3"
  - "sources/verification/walkthroughs/J2_walkthrough.md#stage-6"
  - "sources/verification/walkthroughs/J2_walkthrough.md#3.2"
  - "sources/verification/walkthroughs/J2_walkthrough.md#3.3"
  - "sources/verification/walkthroughs/J2_walkthrough.md#6.1"
related: [howto.item.create_fee, bridge.BR-LMS-113, journey.J2, screen.loan_product, screen.loan]
version: 1
status: approved
approved_by: Owner
---
**In short:** A product's Charges row names the fee and its accounts, but Frappe Lending 16.5.1 does not raise the fee on a loan from it; the officer types the fee on each loan.

## Before you start

⚠ You need permission to edit a **Loan Product**, and the fee Item must exist (`howto.item.create_fee`). Edit a copy of the product. Names in the screenshots are test records on the dev site.

## Steps

1. Open the product, expand the Charges section and add a row in Loan Charges.
2. Pick the **Charge Type** (the fee Item), set **Charge Based On** to Percentage and enter the **Percentage** (the walkthrough used 1).
3. Fill the accounts: **Income Account**, **Receivable Account**, **Waiver Account**, **Write Off Account** and **Suspense Account**. The walkthrough used existing accounts of the test company.
4. Collapse the row and click **Save**.

![Charge row, reopened after save](/assets/lending_assistant/kb_img/J2/J2-S3-03_charge-row-filled.png)

## What you should see

Loan Charges shows one row with the fee, Percentage, 1% and an amount of 0.00. The activity log reads "You added 1 row to Loan Charges".

![Charge row saved](/assets/lending_assistant/kb_img/J2/J2-S3-04_charge-row-saved.png)

## If it looks wrong

The BRD wants the product's fee rules to raise the fee on each loan (BR-LMS-113, partly covered). The verification found the row is a label with accounts: the percentage and amount are not read anywhere in the 16.5.1 code (ND-1). A loan booked on a product with such a row got no fee, no invoice and no demand. A draft loan saved on the walkthrough's product also shows an empty Loan Booking Charges table.

The workaround in the verification is to add the fee on each loan: Loan > Loan Booking Charges > Add row with the charge and the amount. The fee was then invoiced. Do not use the `apply_charge` API with loan accounting on (DEF-2). See `bridge.BR-LMS-113`.
