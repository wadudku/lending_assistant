---
id: howto.loan_product.change_penalty_rate
type: howto
title: How to change a product's penalty rate and read the change history
summary: "A product change saves at once with no approval, version or effective date; the Version log records who changed which value and when."
br_ids: [BR-LMS-117]
brd_section: 7.2
doctypes: [Loan Product, Version]
dev_items: [D5]
journeys: [J2]
actions: ["Loan Product:change_penalty_rate"]
fields: [Loan Product.Penalty Interest Rate (%)]
options: []
menus: [Lending > Setup > Loan Product]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J2/J2-S5-01_penalty-18-filled.png, /assets/lending_assistant/kb_img/J2/J2-S5-02_penalty-18-saved-no-approval.png, /assets/lending_assistant/kb_img/J2/J2-S5-03_version-log-12-to-18.png, /assets/lending_assistant/kb_img/J2/J2-S5-05_activity-12-18-12.png]
sources:
  - "sources/verification/walkthroughs/J2_walkthrough.md#stage-5"
  - "sources/verification/walkthroughs/J2_walkthrough.md#5.1"
  - "sources/verification/walkthroughs/J2_walkthrough.md#5.2"
  - "sources/verification/walkthroughs/J2_walkthrough.md#5.3"
related: [howto.loan_product.set_rates, bridge.BR-LMS-117, journey.J2, screen.loan_product]
version: 1
status: approved
approved_by: Owner
---
**In short:** A product change saves at once with no approval, version or effective date; the Version log records who changed which value and when.

## Before you start

⚠ Any user with write access to **Loan Product** can do this on the live product. Try it only on a copy (`howto.loan_product.duplicate`), and put the value back. Names in the screenshots are test records on the dev site.

## Steps

1. Open the product and stay on the Details tab.
2. Change **Penalty Interest Rate (%)**, for example from 12 to 18.
3. Click **Save**.
4. To see the history, scroll to the Activity section of the product, or open the product's Version record.
5. To undo, enter the old value and save again.

![Penalty 18 entered](/assets/lending_assistant/kb_img/J2/J2-S5-01_penalty-18-filled.png)

## What you should see

The product saves at once. There is no "send for approval", no checker, no effective date and no warning, and Save is the only button because Loan Product is not submittable.

![Saved at once, no approval](/assets/lending_assistant/kb_img/J2/J2-S5-02_penalty-18-saved-no-approval.png)

The Version record shows the document, the field and the old and new value (12.0% to 18.0%) and who changed it. It holds no reason, approver or effective date. Putting the value back adds a second Version entry.

![Version: 12.0% to 18.0%](/assets/lending_assistant/kb_img/J2/J2-S5-03_version-log-12-to-18.png)

![Activity after the rate went back to 12](/assets/lending_assistant/kb_img/J2/J2-S5-05_activity-12-18-12.png)

## If it looks wrong

The BRD wants each product change to be a new version with an effective date, approved by a checker, and each loan to record the version it was booked under (BR-LMS-117, not covered). Today new loans pick up the new value from that moment, and no version number is kept on the product or the loan. Existing loans keep their old rate, since the rate is copied onto each loan at booking.

The workaround in the verification is to keep product changes with a few product admins by role permission, record approval outside the system and use the Version log as the audit trail. The fix is D5. See `bridge.BR-LMS-117`.
