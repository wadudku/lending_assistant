---
id: howto.loan_security_type.create
type: howto
title: How to create a loan security type (haircut and LTV)
summary: "A security type carries two percentages: the haircut, which sets the lendable value of a pledge, and the loan-to-value ratio, which drives the shortfall check and releases; any number is accepted."
br_ids: [BR-LMS-170]
brd_section: 7.8
doctypes: [Loan Security Type]
dev_items: []
journeys: [J7]
actions: ["Loan Security Type:create"]
fields: [Loan Security Type.Loan Security Type, Loan Security Type.Haircut %, Loan Security Type.Loan To Value Ratio]
options: []
menus: [Lending > Security Management > Loan Security Type]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J7/J7-S1-01_security-type_filled.png, /assets/lending_assistant/kb_img/J7/J7-S1-01_security-type_saved.png, /assets/lending_assistant/kb_img/J7/J7-S1-07_type-150-250_saved.png]
sources:
  - "sources/verification/walkthroughs/J7_walkthrough.md#stage-1"
  - "sources/verification/walkthroughs/J7_walkthrough.md#1.1"
  - "sources/verification/walkthroughs/J7_walkthrough.md#1.5"
related: [howto.loan_security.create, bridge.BR-LMS-170c, journey.J7]
version: 1
status: approved
approved_by: Owner
---
**In short:** A security type carries two percentages: the haircut, which sets the lendable value of a pledge, and the loan-to-value ratio, which drives the shortfall check and releases; any number is accepted.

## Before you start

⚠ You need permission to create a **Loan Security Type**. Names in the screenshots, such as the type name, are test records on the dev site.

## Steps

1. Open Lending > Security Management > Loan Security Type and click + Add.
2. Enter **Loan Security Type** (the name, for example a fixed-deposit receipt), **Haircut %** (the walkthrough used 20) and **Loan To Value Ratio** (70).
3. Click **Save**.

![Type entered](/assets/lending_assistant/kb_img/J7/J7-S1-01_security-type_filled.png)

## What you should see

The type is saved. There are two percentages and they do different jobs. The haircut drives the maximum loan value of a pledge and what may be disbursed. The loan-to-value ratio drives the shortfall check and the releases (configuration note CF-3, and question Q7 for NRB in the walkthrough).

![Type saved](/assets/lending_assistant/kb_img/J7/J7-S1-01_security-type_saved.png)

## If it looks wrong

The BRD wants eligible values to be controlled (BR-LMS-170, partly covered). A test type with a haircut of 150 and a loan-to-value ratio of 250 was saved: there is no 0 to 100 check on either field (DEF-29, ND-29). The verification's fix is a validation of both fields. Until then, check the two numbers by eye. See `bridge.BR-LMS-170c`.

![A haircut of 150 and an LTV of 250 are saved](/assets/lending_assistant/kb_img/J7/J7-S1-07_type-150-250_saved.png)
