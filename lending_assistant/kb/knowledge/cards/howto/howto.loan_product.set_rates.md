---
id: howto.loan_product.set_rates
type: howto
title: How to set a product's interest and penalty rate
summary: "Enter the yearly interest rate and the penalty rate on the product; there is one fixed rate, with no fixed/floating choice, benchmark or repricing field."
br_ids: [BR-LMS-111]
brd_section: 7.2
doctypes: [Loan Product]
dev_items: [D4]
journeys: [J2, J5]
actions: ["Loan Product:set_rates"]
fields: [Loan Product.Rate of Interest (%) Yearly, Loan Product.Penalty Interest Rate (%)]
options: []
menus: [Lending > Setup > Loan Product]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J2/J2-S2-01_rate-penalty-filled.png, /assets/lending_assistant/kb_img/J2/J2-S2-02_rate-penalty-saved-no-changes.png, /assets/lending_assistant/kb_img/J2/J2-S2-04_gap-no-fixed-floating.png]
sources:
  - "sources/verification/walkthroughs/J2_walkthrough.md#stage-2"
  - "sources/verification/walkthroughs/J2_walkthrough.md#2.1"
  - "sources/verification/walkthroughs/J2_walkthrough.md#2.3"
  - "sources/verification/walkthroughs/J5_walkthrough.md#stage-1"
related: [howto.loan_product.duplicate, bridge.BR-LMS-111, journey.J2, screen.loan_product]
version: 1
status: approved
approved_by: Owner
---
**In short:** Enter the yearly interest rate and the penalty rate on the product; there is one fixed rate, with no fixed/floating choice, benchmark or repricing field.

## Before you start

⚠ You need permission to edit a **Loan Product**. Work on a copy (`howto.loan_product.duplicate`). Each loan copies the rate when it is booked, so a later change to the product does not reach loans that already exist. Names in the screenshots are test records on the dev site.

## Steps

1. Open the product and stay on the Details tab.
2. Enter **Rate of Interest (%) Yearly** (the walkthrough used 14) and **Penalty Interest Rate (%)** (12).
3. Click **Save**.

![Rate and penalty entered](/assets/lending_assistant/kb_img/J2/J2-S2-01_rate-penalty-filled.png)

## What you should see

In the walkthrough the copy already held 14 and 12, so Save answered "No changes in document" and nothing new was stored.

![Save: no changes in document](/assets/lending_assistant/kb_img/J2/J2-S2-02_rate-penalty-saved-no-changes.png)

The day-count rule, such as Actual/365, is not on the product. It is a Company setting (`howto.company.view_loan_settings`).

## If it looks wrong

Looking for a fixed or floating choice, a benchmark, a spread or repricing dates finds none: the rate column holds only the yearly rate, and the Loan has no such field either. The BRD wants each product to say whether the rate is fixed or floating (BR-LMS-111, partly covered). The verification names the fix as D4: rate type, benchmark, spread and reset frequency on the product, plus a repricing job for floating loans. See `bridge.BR-LMS-111`.

![No fixed/floating, benchmark or repricing field](/assets/lending_assistant/kb_img/J2/J2-S2-04_gap-no-fixed-floating.png)

The floating-rate journey (J5) looked for the same set-up on the product and on the loan and found only the one rate on each.
