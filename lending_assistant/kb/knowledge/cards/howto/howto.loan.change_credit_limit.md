---
id: howto.loan.change_credit_limit
type: howto
title: How to change a credit line's limit and read the log
summary: "The maximum limit can be raised or cut on the Loan and every change leaves a Loan Limit Change Log row, but there is no reason or approver and a large cut needs no approval."
br_ids: [BR-LMS-221]
brd_section: 7.13
doctypes: [Loan, Loan Limit Change Log]
dev_items: []
journeys: [J11]
actions: ["Loan:change_credit_limit"]
fields: [Loan.Maximum Limit Amount, Loan.Utilized Limit Amount, Loan.Available Limit Amount, Loan.Limit Applicable End]
options: []
menus: [Lending > Loan Management > Loan]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J11/J11-S4-05_loc-limit-raised-150000.png, /assets/lending_assistant/kb_img/J11/J11-S4-06_loc-limit-cut-below-utilised-refused.png, /assets/lending_assistant/kb_img/J11/J11-S4-07_loc-limit-cut-to-60000.png]
sources:
  - "sources/verification/walkthroughs/J11_walkthrough.md#4.2"
related: [howto.loan_transfer.create, howto.loan.auto_close_credit_line, bridge.BR-LMS-221, journey.J11, screen.loan]
version: 1
status: approved
approved_by: Owner
---
**In short:** The maximum limit can be raised or cut on the Loan and every change leaves a Loan Limit Change Log row, but there is no reason or approver and a large cut needs no approval.

## Before you start

⚠ Changing a limit alters how much the borrower can draw. Use a test credit line. Names in the screenshots are test records on the dev site.

## Steps

1. Open the line-of-credit loan and read the Loan Credit Limits on the Details tab: **Maximum Limit Amount**, **Utilized Limit Amount** and **Available Limit Amount**.
2. Enter a higher **Maximum Limit Amount** and click Update. Available rises by the same amount.

![The limit raised](/assets/lending_assistant/kb_img/J11/J11-S4-05_loc-limit-raised-150000.png)

3. Enter a lower **Maximum Limit Amount** and click Update. A cut below the utilised amount is refused with "New maximum limit amount cannot be lesser than the utilized limit amount".

![A cut below the utilised amount refused](/assets/lending_assistant/kb_img/J11/J11-S4-06_loc-limit-cut-below-utilised-refused.png)

4. A cut that stays above the utilised amount is accepted.

![A cut accepted](/assets/lending_assistant/kb_img/J11/J11-S4-07_loc-limit-cut-to-60000.png)

5. Type Loan Limit Change Log in the search bar and read the rows: loan, event, value type and value change. A refused change leaves no row.

## What you should see

Booking, disbursement and each limit change leave a row in the **Loan Limit Change Log**, so the limit history can be read.

## If it looks wrong

The BRD wants limit changes logged with who approved them and why (BR-LMS-221, partly covered). The figures and the log work, but there is no reason and no approver, and a large cut needed no approval. Start and end date changes are not logged as such, and System Manager can edit or delete the rows. The Disbursement row counts Utilized while the Repayment row counts Available, so the rows do not add up to one figure (DEF-48).

The workaround is a written approval outside the system. The fix is ND-47, reason and approver fields, read-only rows, a row for date changes and one value type per figure. See `bridge.BR-LMS-221`.
