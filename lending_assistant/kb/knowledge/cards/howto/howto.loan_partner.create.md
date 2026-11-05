---
id: howto.loan_partner.create
type: howto
title: How to create a co-lending partner and link it to a product
summary: "A partner holds its loan share and base rate on its own record; a product only links to it, so one partner has one share across all its products."
br_ids: [BR-LMS-116, BR-LMS-210, BR-LMS-211]
brd_section: 7.2
doctypes: [Loan Partner, Loan Product, Loan Product Loan Partner]
dev_items: []
journeys: [J2, J10]
actions: ["Loan Partner:create"]
fields: [Loan Partner.Partner Code, Loan Partner.Partner Name, Loan Partner.Partner Loan Share Percentage, Loan Partner.Partner Base Interest Rate, Loan Partner.Repayment Schedule Type, Loan Partner.Effective Date, Loan Partner.Organization Type]
options: []
menus: []
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J2/J2-S4-05_partner-filled-with-org-type.png, /assets/lending_assistant/kb_img/J2/J2-S4-06_partner-saved.png, /assets/lending_assistant/kb_img/J2/J2-S4-07_co-lending-partner-filled.png, /assets/lending_assistant/kb_img/J2/J2-S4-08_co-lending-partner-saved.png]
sources:
  - "sources/verification/walkthroughs/J2_walkthrough.md#stage-4"
  - "sources/verification/walkthroughs/J2_walkthrough.md#4.3"
  - "sources/verification/walkthroughs/J2_walkthrough.md#4.4"
  - "sources/verification/walkthroughs/J10_walkthrough.md#stage-1"
  - "sources/verification/walkthroughs/J10_walkthrough.md#stage-2"
  - "sources/verification/walkthroughs/J10_walkthrough.md#1.1"
  - "sources/verification/walkthroughs/J10_walkthrough.md#1.2"
related: [howto.loan_product.duplicate, bridge.BR-LMS-116, bridge.BR-LMS-210, bridge.BR-LMS-211, journey.J2, screen.loan_partner, screen.loan_product]
version: 1
status: approved
approved_by: Owner
---
**In short:** A partner holds its loan share and base rate on its own record; a product only links to it, so one partner has one share across all its products.

## Before you start

⚠ You need permission to create a **Loan Partner** (the doctype carries an "Experimental" badge) and to edit a **Loan Product**. Link the partner to a copy of a product, not to one that already has loans. Names in the screenshots are test records on the dev site.

## Steps

1. Type Loan Partner in the search bar to open the list, then click + Add.
2. Enter **Partner Code**, **Partner Name**, **Partner Loan Share Percentage** (the walkthrough used 20) and **Partner Base Interest Rate** (10).
3. Set **Repayment Schedule Type** and **Effective Date**, and fill **Organization Type**, which sits in the collapsed Address Details section. The form tells you what is missing when you save.
4. Click **Save**. No partner accounts were needed in the walkthrough.
5. Open the product, go to the Co Lending tab, pick the partner in Loan Partners and click **Save**.

![Partner filled, with Organization Type](/assets/lending_assistant/kb_img/J2/J2-S4-05_partner-filled-with-org-type.png)

![Partner saved](/assets/lending_assistant/kb_img/J2/J2-S4-06_partner-saved.png)

![Partner picked on the product](/assets/lending_assistant/kb_img/J2/J2-S4-07_co-lending-partner-filled.png)

## What you should see

The partner shows its share, base rate and effective date. The product shows a partner chip in Loan Partners, and the activity log says a row was added.

![Partner linked to the product](/assets/lending_assistant/kb_img/J2/J2-S4-08_co-lending-partner-saved.png)

## If it looks wrong

The BRD wants each partner to join chosen products with a share for each (BR-LMS-211). Today the share is one figure on the partner, not per product: the Loan form shows the partner but no share, and the same partner cannot take 20% of one product and 30% of another. The verification's workaround is one Loan Partner record per share, each linked to its own product; the fix is ND-42 in the verification. See `bridge.BR-LMS-211`.
