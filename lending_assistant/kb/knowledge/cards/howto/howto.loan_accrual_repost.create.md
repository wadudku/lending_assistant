---
id: howto.loan_accrual_repost.create
type: howto
title: How to repost interest for a period
summary: "A Loan Accrual Repost only repairs missing ledger entries of accruals that are still submitted; a cancelled day is never booked again, so it cannot redo interest for a period."
br_ids: [BR-LMS-143]
brd_section: 7.5
doctypes: [Loan Accrual Repost, Loan Interest Accrual, Process Loan Interest Accrual]
dev_items: []
journeys: [J11]
actions: ["Loan Accrual Repost:create"]
fields: [Loan Accrual Repost.From Date, Loan Accrual Repost.To Date]
options: []
menus: []
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J11/J11-S3-15_accrual-repost-nothing-wrong-submitted.png, /assets/lending_assistant/kb_img/J11/J11-S3-17_accrual-0915-cancelled.png, /assets/lending_assistant/kb_img/J11/J11-S3-19_accrual-day-still-empty.png]
sources:
  - "sources/verification/walkthroughs/J11_walkthrough.md#3.3"
related: [howto.loan_demand.cancel, howto.loan_repayment_repost.create, howto.loan_interest_accrual.view, bridge.BR-LMS-143, journey.J11, screen.loan_interest_accrual]
version: 1
status: approved
approved_by: Owner
---
**In short:** A Loan Accrual Repost only repairs missing ledger entries of accruals that are still submitted; a cancelled day is never booked again, so it cannot redo interest for a period.

## Before you start

⚠ Loan Accrual Repost is open to System Manager only. Use a test loan. Names in the screenshots are test records on the dev site.

## Steps

1. Type Loan Accrual Repost in the search bar and click Add.
2. Enter **From Date** and **To Date**, then add a row for each loan in the loans table.
3. Click **Save**, then **Submit**. It runs on submit; more than 10 loans go to the background.

![A repost with nothing to repair](/assets/lending_assistant/kb_img/J11/J11-S3-15_accrual-repost-nothing-wrong-submitted.png)

## What you should see

Nothing changes when nothing is wrong: the number of accruals and ledger rows is the same before and after. A repost only creates the ledger entries of accruals that are still submitted, and only for normal interest.

If you cancel one day's accrual and then run a Process Loan Interest Accrual for that date and a second repost, the day stays empty and the loan is left one accrual short.

![One accrual cancelled](/assets/lending_assistant/kb_img/J11/J11-S3-17_accrual-0915-cancelled.png)

![The day is still empty](/assets/lending_assistant/kb_img/J11/J11-S3-19_accrual-day-still-empty.png)

## If it looks wrong

The BRD wants interest to be undone and redone for a period, for example after a wrong rate, with approval (BR-LMS-143, partly covered). A cancelled day is never booked again by the nightly run or by the repost, so the borrower is undercharged by that day and nothing says so (DEF-46). The form has no reason, status or approval.

The workaround is to cancel each wrong accrual by hand and enter the corrected interest by a Journal Entry. The fix is ND-46, a repair that reverses and re-posts a date range with a corrected rate, covers penalty accruals, and has a reason and approval. See `bridge.BR-LMS-143`.
