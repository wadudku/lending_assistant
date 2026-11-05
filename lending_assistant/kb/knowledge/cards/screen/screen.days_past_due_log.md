---
id: screen.days_past_due_log
type: screen
title: "Screen: Days Past Due Log"
summary: The Days Past Due Log screen holds one row per loan per day with the number of days the loan was past due.
br_ids: [BR-LMS-163, BR-LMS-190, BR-LMS-192]
brd_section: 7.10
doctypes: [Days Past Due Log]
dev_items: []
fields: [Days Past Due Log.Loan, Days Past Due Log.Posting Date, Days Past Due Log.Days Past Due, Days Past Due Log.Process Loan Classification, Days Past Due Log.Loan Disbursement]
options: []
menus: [Lending > Loan Management > DPD Log]
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/days_past_due_log/days_past_due_log.json]
images: [/assets/lending_assistant/kb_img/J3/J3-S4-06_dpd-log-07-05-zero.png, /assets/lending_assistant/kb_img/J3/J3-S4-07_dpd-log-all-rows.png]
sources:
  - "sources/verification/walkthroughs/J3_walkthrough.md#stage-4"
  - "sources/verification/walkthroughs/J3_walkthrough.md#4.2"
  - "sources/verification/walkthroughs/J3_walkthrough.md#4.3"
  - "sources/verification/walkthroughs/J4_walkthrough.md#stage-5"
  - "sources/verification/verification_report.md#BR-LMS-163"
related: [screen.loan, screen.loan_npa_log, brd_section.7.10, glossary.dpd, bridge.BR-LMS-163, bridge.BR-LMS-190]
version: 1
status: approved
approved_by: Owner
---
**In short:** The Days Past Due Log screen holds one row per loan per day with the number of days the loan was past due.

## What this screen is for

**Days Past Due Log** (menu label: Lending > Loan Management > DPD Log) is the daily history of how many days a loan was past due. The classification run writes it; all fields are read-only. In the J3 example a loan paid on the due date had a row for that date with **Days Past Due** 0, and 122 rows up to today, all 0. A run for a past date rewrites the existing rows, linking them to the new **Process Loan Classification**, rather than adding duplicates.

## Before and after

Before: the classification run for a day (`screen.loan` shows the current **Days Past Due**). After: later runs can change old rows. In the J4 freeze example the row for the day was rewritten from 91 to 0 while the loan still showed 91 (DEF-16).

## Key fields

**Loan**, **Posting Date**, **Days Past Due**, **Process Loan Classification** and **Loan Disbursement**. The installed doctype gives System Manager and Loan Manager read, write, create and delete, and Loan Reporter read only.

![The DPD log row for the due date, days past due 0](/assets/lending_assistant/kb_img/J3/J3-S4-06_dpd-log-07-05-zero.png)

![All DPD log rows for the loan](/assets/lending_assistant/kb_img/J3/J3-S4-07_dpd-log-all-rows.png)

## BRD needs it serves

BR-LMS-163 in BRD 7.7 and BR-LMS-190 and 192 in BRD 7.10 (see `brd_section.7.10`); the bridges hold the verdicts.
