---
id: howto.loan_demand.view
type: howto
title: How to see what a migration billed and posted
summary: "After a migration import, open the Loan Demand (the bill the import raised) and the opening ledger entry to see what the import really created."
br_ids: []
brd_section: 7.1
doctypes: [Loan Demand, Loan Repayment Schedule]
dev_items: [D3]
journeys: [J1]
actions: ["Loan Demand:view"]
fields: [Loan Demand.Demand Type, Loan Demand.Demand Subtype, Loan Demand.Demand Amount, Loan Demand.Outstanding Amount, Loan Demand.Demand Date]
options: [Loan Demand.Demand Type=EMI]
menus: [Lending > Loan Management > Loan Demand, Accounting > General Ledger]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J1/J1-S5-12_migrated-loan-demand-list.png, /assets/lending_assistant/kb_img/J1/J1-S5-13_opening-principal-demand.png, /assets/lending_assistant/kb_img/J1/J1-S5-14_opening-gl-entry.png, /assets/lending_assistant/kb_img/J1/J1-S5-15_migrated-schedule-billed-rows.png]
sources:
  - "sources/verification/walkthroughs/J1_walkthrough.md#stage-5"
  - "sources/verification/walkthroughs/J1_walkthrough.md#5.5"
  - "sources/verification/verification_report.md#BR-LMS-105"
  - "sources/verification/FINAL_REPORT.md#D3"
related: [howto.data_import.migrate_loan, howto.loan_disbursement.view_ledger, journey.J1]
version: 1
status: approved
approved_by: Owner
---
**In short:** After a migration import, open the Loan Demand (the bill the import raised) and the opening ledger entry to see what the import really created.

## Before you start

Read permission on Loan Demand and on the General Ledger. Names you see in the screenshots, such as customer and loan names, are test records on the dev site.

## Steps

1. Open **Lending > Loan Management > Loan Demand** and filter **Loan** to the migrated loan.
2. Open the demand and read **Demand Type**, **Demand Subtype**, **Demand Amount** and **Outstanding Amount**.
3. For the accounting, open **Accounting > General Ledger**, set the company, the dates and **Voucher No** to the loan, and **tick Show Opening Entries**. Without that tick the report shows nothing, because the entries are opening entries.
4. Open the loan's repayment schedule and look at the balance column on the last billed row.

![Loan Demand list for the migrated loan](/assets/lending_assistant/kb_img/J1/J1-S5-12_migrated-loan-demand-list.png)

## What you should see

One demand: Demand Type EMI, Demand Subtype Principal, with the Demand Amount and Outstanding Amount both equal to the opening principal, dated on the migration date. No interest demand exists when the opening interest was 0.

![The opening principal as one demand](/assets/lending_assistant/kb_img/J1/J1-S5-13_opening-principal-demand.png)

The ledger shows one opening entry on the migration date, and the imported disbursement posted no entry.

![Opening entry in the General Ledger](/assets/lending_assistant/kb_img/J1/J1-S5-14_opening-gl-entry.png)

In the schedule, the rows billed in the old system carry a tick, and the later rows still carry the remaining principal.

![Schedule with billed rows ticked](/assets/lending_assistant/kb_img/J1/J1-S5-15_migrated-schedule-billed-rows.png)

## If it looks wrong

For a loan that was up to date in the old system, this bills the whole opening principal on day one, while the schedule also still carries the remaining principal. The opening entry also runs debit to the collection bank and credit to the portfolio, the opposite of what a loan asset would show. The walkthrough first only flagged the direction; the verification report then made it part of defect DEF-6, together with the one-demand billing and the old interest accrued again, and the final report says migration cannot go live on the standard code. See `howto.data_import.migrate_loan` and D3.
