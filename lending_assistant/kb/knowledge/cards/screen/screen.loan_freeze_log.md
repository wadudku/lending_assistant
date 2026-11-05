---
id: screen.loan_freeze_log
type: screen
title: "Screen: Loan Freeze Log"
summary: "The Loan Freeze Log screen is the record the system writes when an account is frozen or unfrozen, with the date and a reason field."
br_ids: [BR-LMS-196]
brd_section: 7.10
doctypes: [Loan Freeze Log]
dev_items: [D8]
fields: [Loan Freeze Log.Loan, Loan Freeze Log.Freeze Date, Loan Freeze Log.Reason For Freezing, Loan Freeze Log.Unfreeze Date]
options: []
menus: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_freeze_log/loan_freeze_log.json]
images: [/assets/lending_assistant/kb_img/J4/J4-S5-06_freeze-log-list.png, /assets/lending_assistant/kb_img/J4/J4-S5-07_freeze-log-no-reason.png]
sources:
  - "sources/verification/walkthroughs/J4_walkthrough.md#stage-5"
  - "sources/verification/walkthroughs/J4_walkthrough.md#5.2"
  - "sources/verification/walkthroughs/J4_walkthrough.md#5.3"
  - "sources/verification/walkthroughs/J4_walkthrough.md#5.5"
  - "sources/verification/verification_report.md#BR-LMS-196"
related: [screen.loan, brd_section.7.10, decision.freeze, lifecycle.FROZEN, bridge.BR-LMS-196, devitem.D8]
version: 1
status: approved
approved_by: Owner
---
**In short:** The Loan Freeze Log screen is the record the system writes when an account is frozen or unfrozen, with the date and a reason field.

## What this screen is for

**Loan Freeze Log** records that a loan was frozen or unfrozen. In the walkthrough the log was written by the loan's **Freeze Account** tick on the Totals tab, not created by hand: ticking **Freeze Account** and entering a **Freeze Date** on the loan produced a log row with that date, and unticking it produced a separate row with an **Unfreeze Date**. The rules for freezing are in `decision.freeze`.

## Before and after

Before: the officer sets the freeze on the loan (`screen.loan`). After: the log holds the dates. The unfreeze row has no link to the freeze row, so the two are paired only by loan and date.

## Key fields

**Loan**, **Freeze Date**, **Reason For Freezing** and **Unfreeze Date**. In the example **Reason For Freezing** was empty, because the loan form has no field to fill it from, and nothing asked for an approver. The walkthrough opened it by searching for its name as a System Manager. The installed doctype lists only System Manager, with read, write, create and delete.

![The freeze log list for one loan](/assets/lending_assistant/kb_img/J4/J4-S5-06_freeze-log-list.png)

![A freeze log row with no reason](/assets/lending_assistant/kb_img/J4/J4-S5-07_freeze-log-no-reason.png)

## BRD needs it serves

BR-LMS-196 in BRD 7.10 (see `brd_section.7.10`); the bridge holds the verdict. The weak point shown is that a freeze has no reason, no approver and no record of what is suspended, and on an NPA loan the freeze also changed the suspense and the DPD log (ND-16, D8, DEF-16).
