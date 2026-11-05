---
id: screen.loan_write_off
type: screen
title: "Screen: Loan Write Off"
summary: The Loan Write Off screen records the writing off of a loan's unpaid principal and posts the entry to the bad-debt account.
br_ids: [BR-LMS-134, BR-LMS-195, BR-LMS-200, BR-LMS-201, BR-LMS-202, BR-LMS-204, BR-LMS-205]
brd_section: 7.11
doctypes: [Loan Write Off]
dev_items: [D13]
fields: [Loan Write Off.Loan, Loan Write Off.Posting Date, Loan Write Off.Value Date, Loan Write Off.Write Off Account, Loan Write Off.Write Off Amount, Loan Write Off.Is NPA, Loan Write Off.Is Settlement Write Off]
options: []
menus: [Lending > Loan Management > Loan Write Off]
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_write_off/loan_write_off.json]
images: [/assets/lending_assistant/kb_img/J8/J8-S3-5e_write-off-submitted.png]
sources:
  - "sources/verification/walkthroughs/J8_walkthrough.md#stage-2"
  - "sources/verification/walkthroughs/J8_walkthrough.md#stage-3"
  - "sources/verification/walkthroughs/J8_walkthrough.md#3.5"
  - "sources/verification/walkthroughs/J8_walkthrough.md#3.6"
  - "sources/verification/walkthroughs/J8_walkthrough.md#3.8"
  - "sources/verification/verification_report.md#BR-LMS-201"
  - "sources/verification/verification_report.md#BR-LMS-195"
  - "sources/verification/reqs.json#BR-LMS-204"
related: [screen.loan, screen.loan_repayment, brd_section.7.11, decision.write-off, decision.waiver, lifecycle.WRITTEN_OFF, glossary.write-off, bridge.BR-LMS-195, bridge.BR-LMS-201, bridge.BR-LMS-205]
version: 1
status: approved
approved_by: Owner
---
**In short:** The Loan Write Off screen records the writing off of a loan's unpaid principal and posts the entry to the bad-debt account.

## What this screen is for

**Loan Write Off** writes off a loan's unpaid principal (menu: Lending > Loan Management > Loan Write Off). It is a submittable document. A person can create one, and the system also creates and submits one: in the J8 walkthrough a loan that passed the 1,080 days-past-due threshold was written off in the classification run, and a settlement creates a write-off for the unpaid principal with **Is Settlement Write Off** ticked. The rules for when and by whom are in `decision.write-off`.

## Before and after

Before: the loan is overdue (`screen.loan`); in the manual example it was already NPA. In that example the officer entered the loan, the **Value Date** and the amount, and the only check seen was that **Write Off Amount** equals the pending principal: 50,000 against 100,000 pending was refused. On submit the loan became Written Off, and the entry was a debit to Bad Debts Written Off and a credit to the portfolio account, for the principal only. After: within seconds the system created and submitted a Penalty Waiver and an Interest Waiver repayment of its own (see `screen.loan_repayment`).

## Key fields

**Loan**, **Posting Date**, **Value Date**, **Write Off Account**, **Write Off Amount**, **Is NPA** and **Is Settlement Write Off**. The form has no reference, reason or approver field, and the activity log of a system-created write-off shows only "You created this" (BR-LMS-205). The walkthrough found no workflow on Loan Write Off (BR-LMS-201).

![A submitted write-off of 100,000](/assets/lending_assistant/kb_img/J8/J8-S3-5e_write-off-submitted.png)

The installed doctype gives System Manager and Loan Manager read, write, create, submit, cancel and delete, and Loan Reporter read only.

## BRD needs it serves

BR-LMS-195 is in BRD 7.10; BR-LMS-200, 201, 202, 204 and 205 are in BRD 7.11 (see `brd_section.7.11`); the bridges hold the verdicts. Weak points shown: a system write-off is submitted with no approver, and a written-off loan kept accruing interest and lost its grade (BR-LMS-202, DEF-36, ND-34).
