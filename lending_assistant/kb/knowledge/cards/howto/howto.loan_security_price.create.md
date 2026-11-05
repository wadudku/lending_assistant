---
id: howto.loan_security_price.create
type: howto
title: How to set and change a security's price
summary: "A price has a validity period; to change it, end the old row first and then add the new one, because a row that starts inside an older one is accepted and two functions then read different prices."
br_ids: [BR-LMS-170, BR-LMS-172]
brd_section: 7.8
doctypes: [Loan Security Price]
dev_items: []
journeys: [J7]
actions: ["Loan Security Price:create"]
fields: [Loan Security Price.Loan Security, Loan Security Price.Loan Security Price, Loan Security Price.Valid From, Loan Security Price.Valid Upto]
options: []
menus: [Lending > Security Management > Loan Security Price]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J7/J7-S1-03_price-1000_filled.png, /assets/lending_assistant/kb_img/J7/J7-S3-03_price-old-row-end-filled.png, /assets/lending_assistant/kb_img/J7/J7-S3-05_price-600-filled.png, /assets/lending_assistant/kb_img/J7/J7-S3-06_price-600-saved.png, /assets/lending_assistant/kb_img/J7/J7-S1-06_price-nested_saved.png]
sources:
  - "sources/verification/walkthroughs/J7_walkthrough.md#stage-1"
  - "sources/verification/walkthroughs/J7_walkthrough.md#1.3"
  - "sources/verification/walkthroughs/J7_walkthrough.md#1.4"
  - "sources/verification/walkthroughs/J7_walkthrough.md#3.3"
  - "sources/verification/walkthroughs/J7_walkthrough.md#5.1"
related: [howto.loan_security.create, bridge.BR-LMS-170c, bridge.BR-LMS-172, journey.J7]
version: 1
status: approved
approved_by: Owner
---
**In short:** A price has a validity period; to change it, end the old row first and then add the new one, because a row that starts inside an older one is accepted and two functions then read different prices.

## Before you start

⚠ You need permission to create and edit a **Loan Security Price**. A price change can create a collateral shortfall, so test on a test security. Names in the screenshots are test records on the dev site.

## Steps

1. Open Lending > Security Management > Loan Security Price and click + Add.
2. Pick the **Loan Security**, enter **Loan Security Price** (the walkthrough used 1,000 a unit), **Valid From** and **Valid Upto** (a year later) and click **Save**.
3. To change the price, first open the current row and set **Valid Upto** to the moment before the change. Click Save.
4. Add a new row with the new price (e.g. 600), a **Valid From** one second after, and a **Valid Upto** far enough ahead. Click Save.
5. To restore the price later, end the 600 row the same way and add a new row at 1,000.

![Price entered](/assets/lending_assistant/kb_img/J7/J7-S1-03_price-1000_filled.png)

![The old row ended first](/assets/lending_assistant/kb_img/J7/J7-S3-03_price-old-row-end-filled.png)

## What you should see

Each price is its own row, so a price history is kept. After the change the pledged value follows the new price: 200 units at 600 are worth 120,000.

![The new price entered](/assets/lending_assistant/kb_img/J7/J7-S3-05_price-600-filled.png)

![The new price saved](/assets/lending_assistant/kb_img/J7/J7-S3-06_price-600-saved.png)

## If it looks wrong

The BRD wants one valid price at any time (BR-LMS-170, partly covered). A row that starts inside an older row and ends after it is refused, but a row nested inside an older one is saved with no overlap error. Both rows are then valid, and pledges and disbursements use the newest price while the shortfall check uses the last in the list, so a real price fall can go undetected (DEF-29, ND-29). The workaround is the order in the steps: end the old row before adding a new one. The verification's fix is a proper range-overlap test and one price lookup. See `bridge.BR-LMS-170c`.

![A nested row is saved](/assets/lending_assistant/kb_img/J7/J7-S1-06_price-nested_saved.png)
