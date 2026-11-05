---
id: howto.general_ledger.view_partner_position
type: howto
title: How to see a co-lending partner's position
summary: "The General Ledger on the partner's accounts is the only partner position there is; the Loan Partner form has no linked loans, ledger or balance, and no settlement or reconciliation document exists."
br_ids: [BR-LMS-213]
brd_section: 7.12
doctypes: [Loan Partner]
dev_items: [D10]
journeys: [J10]
actions: ["Loan Partner:view_position"]
fields: []
options: []
menus: [Accounting > General Ledger]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J10/J10-S4-03_partner-sidebar-links.png]
sources:
  - "sources/verification/walkthroughs/J10_walkthrough.md#stage-4"
  - "sources/verification/walkthroughs/J10_walkthrough.md#4.1"
  - "sources/verification/walkthroughs/J10_walkthrough.md#4.2"
related: [howto.loan.choose_co_lender, howto.report.check_partner_report, bridge.BR-LMS-213, journey.J10, screen.loan_partner]
version: 1
status: approved
approved_by: Owner
---
**In short:** The General Ledger on the partner's accounts is the only partner position there is; the Loan Partner form has no linked loans, ledger or balance, and no settlement or reconciliation document exists.

## Before you start

⚠ This is a read-only check. You need permission to read the General Ledger. The partner's accounts are set on the **Loan Partner** form: receivable, clearing, payable, interest share and FLDG. Names in the screenshots are test records on the dev site.

## Steps

1. Open Accounting > General Ledger.
2. Enter the Company and a date range. In the Account filter choose the partner accounts.
3. Read the vouchers posted to them: the disbursement, and each repayment with a partner share.
4. Open the **Loan Partner** form and look at its sidebar for linked loans, a ledger or a balance.

![The Loan Partner sidebar](/assets/lending_assistant/kb_img/J10/J10-S4-03_partner-sidebar-links.png)

## What you should see

The ledger lists every voucher posted to those accounts, so you can add up what the partner funded, what is owed to it and the interest share. The totals include every loan of that partner. The Loan Partner form has no linked loans, ledger or balance.

The hourly credit-notes job is not a partner job: it only makes credit notes for submitted Charges Waiver repayments, and nothing in it reads a partner or a partner account.

## If it looks wrong

The BRD wants the partner's funding recorded when it arrives, what is owed paid and matched to the partner's schedule, and a check that what was passed on agrees with the plan (BR-LMS-213, partly covered). There is no partner payment, receipt, settlement or reconciliation document. The partner's funding and the payment of its payable are never posted, and nothing compares the Co Lender Schedule with what was passed on.

The workaround is Journal Entries by hand (funding received, payable paid) and a spreadsheet that compares the ledger with the Co Lender Schedule. The fix is ND-40, a Loan Partner Settlement document. See `bridge.BR-LMS-213`.
