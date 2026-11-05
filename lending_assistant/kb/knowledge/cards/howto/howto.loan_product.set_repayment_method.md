---
id: howto.loan_product.set_repayment_method
type: howto
title: How to pick a product's repayment method (and where the moratorium lives)
summary: The product's Repayment Schedule Type offers five options; the moratorium is not a product setting and is keyed on each loan.
br_ids: [BR-LMS-110, BR-LMS-112]
brd_section: 7.2
doctypes: [Loan Product, Loan]
dev_items: []
journeys: [J2]
actions: ["Loan Product:set_repayment_method"]
fields: [Loan Product.Repayment Schedule Type, Loan Product.Cyclic Day Of the Month, Loan.Moratorium Type]
options: [Loan Product.Repayment Schedule Type=Monthly as per repayment start date, Loan Product.Repayment Schedule Type=Pro-rated calendar months, Loan Product.Repayment Schedule Type=Monthly as per cycle date, Loan Product.Repayment Schedule Type=Line of Credit, Loan Product.Repayment Schedule Type=Flat Interest Rate]
menus: [Lending > Setup > Loan Product]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J2/J2-S1-05_schedule-type-5-options.png, /assets/lending_assistant/kb_img/J2/J2-S1-06_gap-no-moratorium-on-product.png]
sources:
  - "sources/verification/walkthroughs/J2_walkthrough.md#stage-1"
  - "sources/verification/walkthroughs/J2_walkthrough.md#1.2"
  - "sources/verification/walkthroughs/J2_walkthrough.md#1.3"
related: [howto.loan_product.duplicate, bridge.BR-LMS-110, bridge.BR-LMS-112, journey.J2, screen.loan_product, screen.loan]
version: 1
status: approved
approved_by: Owner
---
**In short:** The product's Repayment Schedule Type offers five options; the moratorium is not a product setting and is keyed on each loan.

## Before you start

⚠ You need permission to edit a **Loan Product**. Change a copy of the product, never one that already has loans (`howto.loan_product.duplicate`). Names in the screenshots are test records on the dev site.

## Steps

1. Open the product and stay on the Details tab.
2. Open the **Repayment Schedule Type** list. These are the five choices: *Monthly as per repayment start date*, *Pro-rated calendar months*, *Monthly as per cycle date*, *Line of Credit* and *Flat Interest Rate*.
3. For a monthly loan on a fixed day, keep *Monthly as per cycle date* and set **Cyclic Day Of the Month** (the walkthrough kept day 5). Nothing changed there, so nothing was saved.
4. To look for a moratorium rule, scan the Details tab, including the collapsed Limits section.

![The five Repayment Schedule Type options](/assets/lending_assistant/kb_img/J2/J2-S1-05_schedule-type-5-options.png)

## What you should see

The list shows exactly the five options above. The verification report lists BR-LMS-110 as covered and BR-LMS-112 as partly covered.

The product has no moratorium field: no type, no length and no interest treatment. The Grace Period in Days sits in the Limits section.

![No moratorium field on the product](/assets/lending_assistant/kb_img/J2/J2-S1-06_gap-no-moratorium-on-product.png)

## If it looks wrong

The BRD wants the product to set the moratorium rule for every loan of that product (BR-LMS-112). Today **Moratorium Type** and its related fields exist only on the **Loan**, with no default from the product, so ops must key them on every loan and loans of the same product can differ. The verification names the fix as ND-2: moratorium default fields on the product, fetched onto the loan. See `bridge.BR-LMS-112`.

The walkthrough also notes that *Flat Interest Rate* has a known rounding fault (DEF-1); it is not shown here.
