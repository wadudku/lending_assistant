---
id: screen.loan_security
type: screen
title: "Screen: Loan Security"
summary: "The Loan Security screen is the master record of one piece of collateral, such as a fixed deposit, with its type, haircut and loan-to-value ratio."
br_ids: [BR-LMS-170]
brd_section: 7.8
doctypes: [Loan Security]
dev_items: []
fields: [Loan Security.Loan Security Code, Loan Security.Loan Security Name, Loan Security.Loan Security Type, Loan Security.Haircut %, Loan Security.Loan To Value Ratio, Loan Security.Disabled]
options: []
menus: [Lending > Security Management > Loan Security]
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_security/loan_security.json]
images: [/assets/lending_assistant/kb_img/J7/J7-S1-02_security_saved.png]
sources:
  - "sources/verification/walkthroughs/J7_walkthrough.md#stage-1"
  - "sources/verification/walkthroughs/J7_walkthrough.md#1.2"
  - "sources/verification/walkthroughs/J7_walkthrough.md#1.3"
  - "sources/verification/verification_report.md#BR-LMS-170c"
  - "sources/verification/reqs.json#BR-LMS-170c"
related: [screen.loan, brd_section.7.8, bridge.BR-LMS-170c, concept.BR-LMS-170c]
version: 1
status: approved
approved_by: Owner
---
**In short:** The Loan Security screen is the master record of one piece of collateral, such as a fixed deposit, with its type, haircut and loan-to-value ratio.

## What this screen is for

**Loan Security** is the master record for one item that can be pledged against a loan (menu: Lending > Security Management > Loan Security). It is set up once, before any pledge: in the J7 walkthrough the officer first made a Loan Security Type with a haircut and a loan-to-value ratio, then this record, then a price for it. A pledge later names it with a quantity (see `screen.loan_security_assignment`).

## Before and after

Before: its Loan Security Type exists and carries the haircut and the **Loan To Value Ratio**; the new record inherits both (20% and 70% in the example). After: a Loan Security Price, which has its own validity dates, and then a pledge. The price is kept on its own record, not on this screen.

## Key fields

**Loan Security Code**, **Loan Security Name**, **Loan Security Type**, **Haircut %**, **Loan To Value Ratio**, **Disabled**, and the read-only **Utilized Security Value** and **Available Security Value**. The haircut drives the maximum loan value of a pledge; the loan-to-value ratio drives the shortfall check.

![A saved loan security with the haircut and loan-to-value ratio from its type](/assets/lending_assistant/kb_img/J7/J7-S1-02_security_saved.png)

The installed doctype gives System Manager and Loan Manager read, write, create and delete, and Loan Reporter read only.

## BRD needs it serves

BR-LMS-170c in BRD 7.8 (see `brd_section.7.8`): a record of the collateral with its haircut, loan-to-value ratio and price history. The bridge holds the verdict. Weak points shown: a price row that starts inside an older one is saved with no overlap error, and a haircut of 150% and a loan-to-value ratio of 250% were accepted (DEF-29, ND-29).
