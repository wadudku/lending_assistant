---
id: screen.loan_security_shortfall
type: screen
title: "Screen: Loan Security Shortfall"
summary: The Loan Security Shortfall screen is the alert the system raises when the pledged value no longer covers a loan; the app also closes it when security is added.
br_ids: [BR-LMS-172, BR-LMS-173]
brd_section: 7.8
doctypes: [Loan Security Shortfall]
dev_items: [D20]
fields: [Loan Security Shortfall.Loan, Loan Security Shortfall.Loan Amount, Loan Security Shortfall.Security Value, Loan Security Shortfall.Shortfall Amount, Loan Security Shortfall.Shortfall Percentage, Loan Security Shortfall.Status, Loan Security Shortfall.Shortfall Time]
options: [Loan Security Shortfall.Status=Pending, Loan Security Shortfall.Status=Completed]
menus: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_security_shortfall/loan_security_shortfall.json]
images: [/assets/lending_assistant/kb_img/J7/J7-S3-07_shortfall-list-two-records.png, /assets/lending_assistant/kb_img/J7/J7-S3-08_shortfall-loanwise-record.png]
sources:
  - "sources/verification/walkthroughs/J7_walkthrough.md#stage-3"
  - "sources/verification/walkthroughs/J7_walkthrough.md#3.4"
  - "sources/verification/walkthroughs/J7_walkthrough.md#stage-4"
  - "sources/verification/walkthroughs/J7_walkthrough.md#4.1"
  - "sources/verification/walkthroughs/J7_walkthrough.md#4.3"
  - "sources/verification/verification_report.md#BR-LMS-173"
  - "sources/verification/reqs.json#BR-LMS-172"
related: [screen.loan, screen.loan_security, screen.loan_security_assignment, brd_section.7.8, bridge.BR-LMS-172, bridge.BR-LMS-173, devitem.D20]
version: 1
status: approved
approved_by: Owner
---
**In short:** The Loan Security Shortfall screen is the alert the system raises when the pledged value no longer covers a loan; the app also closes it when security is added.

## What this screen is for

**Loan Security Shortfall** records that the collateral value, after the loan-to-value ratio, no longer covers a loan. The nightly shortfall check creates it, and most of its fields are read-only. In the J7 example a pledge of 200 units fell from 1,000 to 600 a unit, and the check created a loan-wise record of 16,000 (100,000 less 120,000 x 70%), Pending. The walkthrough opened the list from `/desk/loan-security-shortfall`.

## Before and after

Before: a pledge and a price that has fallen (`screen.loan_security_assignment`, `screen.loan_security`). After: the Add Loan Security button on the form opens a new Loan Security Assignment with the loan and applicant filled in. The app reduced the record by itself after each top-up, and set **Status** to Completed when the pledge covered the loan. In verification the app reduced it by the pledge's full value, not after the ratio, so a record closed with 3,400 still short (DEF-28).

## Key fields

**Loan**, **Loan Amount**, **Security Value**, **Shortfall Amount**, **Shortfall Percentage**, **Status** (Pending or Completed) and **Shortfall Time**. The check also made a second, applicant-wise record with no loan, which stayed Pending after the loan was covered. The record has ten fields and none for a remedy, an owner, a due date or notes.

![Two shortfall records for one customer](/assets/lending_assistant/kb_img/J7/J7-S3-07_shortfall-list-two-records.png)

![The loan-wise record](/assets/lending_assistant/kb_img/J7/J7-S3-08_shortfall-loanwise-record.png)

The installed doctype gives System Manager and Loan Manager read, write, create and delete, and Loan Reporter read only.

## BRD needs it serves

BR-LMS-172 and BR-LMS-173 in BRD 7.8 (see `brd_section.7.8`); the bridges hold the verdicts. Weak points shown: the **Process Loan Security Shortfall** run ignores its own Loan and Applicant fields when submitted and covers every loan and customer (DEF-27), and the nightly pass can flag borrowers with no collateral (DEF-32).
