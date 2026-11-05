---
id: howto.loan.freeze
type: howto
title: How to freeze a loan and read the Freeze Log
summary: "Ticking Freeze Account on the Totals tab freezes a loan with no reason, approver or confirmation, and the Loan Freeze Log records the date but no reason."
br_ids: [BR-LMS-196]
brd_section: 7.9
doctypes: [Loan, Loan Freeze Log]
dev_items: [D8]
journeys: [J4]
actions: ["Loan:freeze"]
fields: [Loan.Freeze Account, Loan.Freeze Date, Loan Freeze Log.Freeze Date, Loan Freeze Log.Unfreeze Date, Loan Freeze Log.Reason For Freezing]
options: []
menus: [Lending > Loan Management > Loan]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J4/J4-S5-03_freeze-filled.png, /assets/lending_assistant/kb_img/J4/J4-S5-06_freeze-log-list.png, /assets/lending_assistant/kb_img/J4/J4-S5-07_freeze-log-no-reason.png]
sources:
  - "sources/verification/walkthroughs/J4_walkthrough.md#stage-5"
  - "sources/verification/walkthroughs/J4_walkthrough.md#5.2"
  - "sources/verification/walkthroughs/J4_walkthrough.md#5.3"
related: [howto.company.view_loan_settings, bridge.BR-LMS-196, journey.J4, screen.loan, screen.loan_freeze_log]
version: 1
status: approved
approved_by: Owner
---
**In short:** Ticking Freeze Account on the Totals tab freezes a loan with no reason, approver or confirmation, and the Loan Freeze Log records the date but no reason.

## Before you start

⚠ You need permission to edit a **Loan**. Freezing changes accruals and demands, so do it only on a test loan. The Loan Freeze Log is opened by searching its name in the search bar and needs the System Manager role. Names in the screenshots are test records on the dev site.

## Steps

1. Open the loan and go to the Totals tab.
2. Tick **Freeze Account**. **Freeze Date** appears and is mandatory: enter the date.
3. Click **Save**. There is no confirmation and no approval.
4. Open the Loan Freeze Log list and filter by loan.

![Freeze Account ticked, date entered](/assets/lending_assistant/kb_img/J4/J4-S5-03_freeze-filled.png)

## What you should see

The loan holds Freeze Account ticked and the Freeze Date. The Loan Freeze Log has a new record with the freeze date, an empty **Unfreeze Date** and an empty **Reason For Freezing**: the Loan form has no reason field to fill it from, and there is no approver.

![Loan Freeze Log list](/assets/lending_assistant/kb_img/J4/J4-S5-06_freeze-log-list.png)

![Freeze Log record: reason empty](/assets/lending_assistant/kb_img/J4/J4-S5-07_freeze-log-no-reason.png)

## If it looks wrong

The BRD wants a freeze to carry a reason, an approver and the scope of what is suspended (BR-LMS-196, partly covered). Today none of these exists, and unfreezing gives the Log a separate row that is not linked to the freeze row. The verification found that unfreezing back-charges the whole frozen period in one go (DEF-12). The workaround is to record the reason and the approval outside the system, add a comment on the loan, and have Finance review the loan's entries around the freeze date. The fix is ND-16 (D8). See `bridge.BR-LMS-196`.
