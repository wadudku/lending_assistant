---
id: howto.notification.check_borrower_notice
type: howto
title: How to check whether a borrower is told about a change
summary: "No notification is set up on Loan, Loan Restructure or Loan Repayment Schedule, so a borrower hears about a new rate or plan only if the branch sends a letter."
br_ids: [BR-LMS-159, BR-LMS-235]
brd_section: 7.6
doctypes: [Loan Restructure]
dev_items: [D11]
journeys: [J5, J9]
actions: ["Loan Restructure:check_notice"]
fields: []
options: []
menus: []
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J5/J5-S6-01_gap-no-notification.png]
sources:
  - "sources/verification/walkthroughs/J5_walkthrough.md#stage-6"
  - "sources/verification/walkthroughs/J5_walkthrough.md#6.1"
  - "sources/verification/walkthroughs/J9_walkthrough.md#6.1"
related: [howto.loan_restructure.approve, bridge.BR-LMS-159, journey.J5, screen.loan_restructure]
version: 1
status: approved
approved_by: Owner
---
**In short:** No notification is set up on Loan, Loan Restructure or Loan Repayment Schedule, so a borrower hears about a new rate or plan only if the branch sends a letter.

## Before you start

⚠ This card is view only. You need read permission on the Notification list in the Settings area. The check was done on the dev site after a restructure was approved (`howto.loan_restructure.approve`). Names in the screenshots are test records.

## Steps

1. Open Settings > Notification.
2. Filter the list by Document Type, first Loan Restructure, then Loan and Loan Repayment Schedule.

![The Notification list, filtered on Loan Restructure](/assets/lending_assistant/kb_img/J5/J5-S6-01_gap-no-notification.png)

## What you should see

No records. There are no Notifications on Loan, Loan Restructure or Loan Repayment Schedule.

## If it looks wrong

The BRD wants the affected borrowers told after a repricing is approved (BR-LMS-159, not covered; D11 in the verification). Today there is no repricing event and no notice.

The same holds for a loan closure: no Notification exists for Loan, so no closure message is sent (BR-LMS-235; see `howto.loan_statement_of_account.view`).

The workaround in the verification is that the branch prints a letter from the new plan (old rate, new rate, effective date, new EMI and new last date) and sends it outside the system. A Frappe Notification on Loan Restructure that fires when the Status changes to Approved could email the borrower if an email is on file, but none is set up and none was created in the walkthrough. See `bridge.BR-LMS-159`.
