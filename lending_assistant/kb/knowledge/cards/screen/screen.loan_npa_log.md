---
id: screen.loan_npa_log
type: screen
title: "Screen: Loan NPA Log"
summary: "The Loan NPA Log screen records each time a loan is marked NPA, with the date and what triggered it."
br_ids: [BR-LMS-192]
brd_section: 7.10
doctypes: [Loan NPA Log]
dev_items: []
fields: [Loan NPA Log.Loan, Loan NPA Log.NPA, Loan NPA Log.Manual NPA, Loan NPA Log.Event, Loan NPA Log.NPA Date, Loan NPA Log.Delinked]
options: []
menus: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_npa_log/loan_npa_log.json]
images: [/assets/lending_assistant/kb_img/J4/J4-S4-07_npa-log-list.png, /assets/lending_assistant/kb_img/J4/J4-S4-08_npa-log-record.png]
sources:
  - "sources/verification/walkthroughs/J4_walkthrough.md#stage-4"
  - "sources/verification/walkthroughs/J4_walkthrough.md#4.4"
  - "sources/verification/verification_report.md#BR-LMS-192"
related: [screen.loan, brd_section.7.10, lifecycle.NPA, glossary.npa, bridge.BR-LMS-192]
version: 1
status: approved
approved_by: Owner
---
**In short:** The Loan NPA Log screen records each time a loan is marked NPA, with the date and what triggered it.

## What this screen is for

**Loan NPA Log** records that a loan became NPA. The classification run writes it; in the J4 walkthrough the run that took a loan to 91 days past due created one row with **NPA** ticked, **Manual NPA** off, **Event** "Background Job" and the **NPA Date**.

## Before and after

Before: the classification run sets the loan to Sub-Standard and NPA (`screen.loan`, **Is NPA** and **Classification Code**). After: interest moves to suspense and the customer is flagged NPA. The log records moves into and out of NPA; grade moves such as STD to SMA are not logged.

## Key fields

**Loan**, **NPA**, **Manual NPA**, **Event**, **NPA Date** and **Delinked**. The walkthrough opened it from the System Manager list by searching for its name. The form shows a **Save** button, because it is not submittable and has no change tracking, so a System Manager can edit a row with no version history (an observation; not tested by editing). The installed doctype lists only System Manager, with read, write, create and delete.

![The NPA log list for one loan](/assets/lending_assistant/kb_img/J4/J4-S4-07_npa-log-list.png)

![One NPA log row](/assets/lending_assistant/kb_img/J4/J4-S4-08_npa-log-record.png)

## BRD needs it serves

BR-LMS-192 in BRD 7.10 (see `brd_section.7.10`); the bridge holds the verdict.
