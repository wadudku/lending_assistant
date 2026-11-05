---
id: howto.loan_statement_of_account.view
type: howto
title: How to produce the final statement and what a closure letter needs
summary: The Loan Statement of Account report gives the final statement of a closed loan; there is no closure letter print format and no notification on closure.
br_ids: [BR-LMS-235]
brd_section: 7.14
doctypes: [Loan, Print Format, Notification, Process Loan Statement of Accounts]
dev_items: [D20]
journeys: [J9]
actions: ["Loan:view_statement"]
fields: []
options: []
menus: []
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J9/J9-S6-02_gap-no-print-format-for-loan.png, /assets/lending_assistant/kb_img/J9/J9-S6-03_gap-no-notification-for-loan.png]
sources:
  - "sources/verification/walkthroughs/J9_walkthrough.md#stage-6"
  - "sources/verification/walkthroughs/J9_walkthrough.md#6.1"
related: [howto.notification.check_borrower_notice, howto.loan_refund.create, bridge.BR-LMS-235, journey.J9, screen.loan]
version: 1
status: approved
approved_by: Owner
---
**In short:** The Loan Statement of Account report gives the final statement of a closed loan; there is no closure letter print format and no notification on closure.

## Before you start

⚠ This is a read-only check. You need permission to read the **Loan** and its reports. Names in the screenshots are test records on the dev site.

## Steps

1. Type Loan Statement of Account in the search bar and open the report.
2. Choose the Company and the loan. The From Date and To Date filters are filled in.
3. Read the lines: disbursement, demands, accruals and the Loan Closure repayment.
4. To look for a closure letter, type Print Format in the search bar and filter on Document Type Loan.
5. To look for a closure message, type Notification in the search bar and filter on Document Type Loan.

## What you should see

A detailed statement with a running balance, ending with the Loan Closure line. This covers the final statement half of the requirement. The Process Loan Statement of Accounts doctype can also send the report by email on a schedule.

![No print format for Loan](/assets/lending_assistant/kb_img/J9/J9-S6-02_gap-no-print-format-for-loan.png)

![No notification for Loan](/assets/lending_assistant/kb_img/J9/J9-S6-03_gap-no-notification-for-loan.png)

## If it looks wrong

The BRD wants a closure letter, a final statement and a message to the borrower (BR-LMS-235, partly covered). Only the statement exists. There is no closure or payoff letter, because no Print Format exists for Loan, and no closure message on any channel, because no Notification exists for Loan. The scheduled email covers the statement only.

The workaround is that the officer prints the statement, writes the letter outside the system and sends the message by hand. The fix is ND-37, a Loan Closure Letter print format and a notification on closure. See `bridge.BR-LMS-235`.
