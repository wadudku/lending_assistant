---
id: howto.loan_security.create
type: howto
title: How to register a security (collateral)
summary: "A Loan Security takes its haircut and LTV from its type; its value fields stay 0, so use the exposure report for what is pledged."
br_ids: [BR-LMS-170]
brd_section: 7.8
doctypes: [Loan Security]
dev_items: []
journeys: [J7]
actions: ["Loan Security:create"]
fields: [Loan Security.Loan Security Code, Loan Security.Loan Security Name, Loan Security.Loan Security Type]
options: []
menus: [Lending > Security Management > Loan Security]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J7/J7-S1-02_security_filled.png, /assets/lending_assistant/kb_img/J7/J7-S1-02_security_saved.png, /assets/lending_assistant/kb_img/J7/J7-S1-08_gap-security-values-zero.png]
sources:
  - "sources/verification/walkthroughs/J7_walkthrough.md#stage-1"
  - "sources/verification/walkthroughs/J7_walkthrough.md#1.2"
  - "sources/verification/walkthroughs/J7_walkthrough.md#1.6"
related: [howto.loan_security_type.create, howto.loan_security_price.create, bridge.BR-LMS-170c, journey.J7, screen.loan_security]
version: 1
status: approved
approved_by: Owner
---
**In short:** A Loan Security takes its haircut and LTV from its type; its value fields stay 0, so use the exposure report for what is pledged.

## Before you start

⚠ You need permission to create a **Loan Security**, and the security type must exist (`howto.loan_security_type.create`). Names in the screenshots are test records on the dev site.

## Steps

1. Open Lending > Security Management > Loan Security and click + Add.
2. Enter **Loan Security Code**, **Loan Security Name** and **Loan Security Type**.
3. Click **Save**.

![Security entered](/assets/lending_assistant/kb_img/J7/J7-S1-02_security_filled.png)

## What you should see

The security is saved with the haircut and the LTV inherited from its type. A price comes next (`howto.loan_security_price.create`).

![Security saved](/assets/lending_assistant/kb_img/J7/J7-S1-02_security_saved.png)

## If it looks wrong

The BRD wants a master list that shows what is pledged and what is left (BR-LMS-170, partly covered). After a pledge and a disbursement, the three fields **Original Security Value**, **Utilized Security Value** and **Available Security Value** on the security still read 0: nothing writes **Original Security Value**, so **Utilized Security Value** and **Available Security Value**, which disbursements and repayments update against it, stay 0 (DEF-29, ND-29). Use the Loan Security Exposure report for quantity and value per security (`howto.loan_security_report.view`). The verification's fix is to maintain the three fields on pledge and release. See `bridge.BR-LMS-170c`.

![The three value fields read 0](/assets/lending_assistant/kb_img/J7/J7-S1-08_gap-security-values-zero.png)
