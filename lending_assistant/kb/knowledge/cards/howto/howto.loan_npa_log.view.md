---
id: howto.loan_npa_log.view
type: howto
title: How to see when a loan became NPA and where its interest went
summary: "When days past due reach 90, the NPA run grades the loan Sub-Standard, flags it NPA, logs the event and moves the unpaid normal interest to a suspense account."
br_ids: [BR-LMS-144, BR-LMS-194]
brd_section: 7.9
doctypes: [Loan, Loan NPA Log, Journal Entry]
dev_items: []
journeys: [J4]
actions: ["Loan NPA Log:view"]
fields: [Loan.Is NPA, Loan.Days Past Due, Loan.Classification Code, Loan NPA Log.NPA Date, Loan NPA Log.Manual NPA]
options: []
menus: [Lending > Loan Management > Loan]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J4/J4-S4-05_loan-grade-ss.png, /assets/lending_assistant/kb_img/J4/J4-S4-06_loan-is-npa.png, /assets/lending_assistant/kb_img/J4/J4-S4-07_npa-log-list.png, /assets/lending_assistant/kb_img/J4/J4-S4-08_npa-log-record.png, /assets/lending_assistant/kb_img/J4/J4-S4-10_suspense-je-accounts.png]
sources:
  - "sources/verification/walkthroughs/J4_walkthrough.md#stage-4"
  - "sources/verification/walkthroughs/J4_walkthrough.md#4.1"
  - "sources/verification/walkthroughs/J4_walkthrough.md#4.2"
  - "sources/verification/walkthroughs/J4_walkthrough.md#4.3"
  - "sources/verification/walkthroughs/J4_walkthrough.md#4.4"
  - "sources/verification/walkthroughs/J4_walkthrough.md#4.5"
related: [howto.process_loan_interest_accrual.run, howto.process_loan_classification.run, bridge.BR-LMS-144, bridge.BR-LMS-194, journey.J4, screen.loan, screen.loan_npa_log]
version: 1
status: approved
approved_by: Owner
---
**In short:** When days past due reach 90, the NPA run grades the loan Sub-Standard, flags it NPA, logs the event and moves the unpaid normal interest to a suspense account.

## Before you start

⚠ You need read permission on **Loan**, **Loan NPA Log** and Journal Entry. The Loan NPA Log is opened by searching its name in the search bar. The walkthrough first accrued interest up to yesterday (`howto.process_loan_interest_accrual.run`) and then ran classification dated today with Force Update DPD in Loan ticked (`howto.process_loan_classification.run`). Names in the screenshots are test records on the dev site.

## Steps

1. Open the loan and read Days Past Due, Classification Code and **Is NPA** under Loan Classification Details and the Totals tab.
2. Search for Loan NPA Log, open the list and filter by loan.
3. Open the Journal Entry for the loan's interest in suspense, from the General Ledger report on the suspense account or by its loan reference.

![The loan at Sub-Standard](/assets/lending_assistant/kb_img/J4/J4-S4-05_loan-grade-ss.png)

## What you should see

The loan shows 91 days past due, code SS (Sub-Standard) and Is NPA ticked, and the customer is flagged NPA as well.

![The loan flagged NPA](/assets/lending_assistant/kb_img/J4/J4-S4-06_loan-is-npa.png)

The Loan NPA Log has one record: NPA ticked, Manual NPA off, event Background Job and the NPA date. Only "NPA in" is logged, not grade moves.

![NPA log list](/assets/lending_assistant/kb_img/J4/J4-S4-07_npa-log-list.png)

![NPA log record](/assets/lending_assistant/kb_img/J4/J4-S4-08_npa-log-record.png)

The Journal Entry debits Interest Income on Loans and credits Interest in Suspense for the same amount, both lines referring to the loan. In the walkthrough that was all the normal interest: billed unpaid 3,255.80 plus accrued not yet billed 848.86, less 0.03 of rounding. Income stops and the unpaid interest waits in suspense.

![Suspense entry lines](/assets/lending_assistant/kb_img/J4/J4-S4-10_suspense-je-accounts.png)

## If it looks wrong

No penalty or Additional Interest went to suspense in this run (DEF-10; configuration note CF-2 in `howto.loan_demand.view_penalty`). A payment reverses the suspense to income at the next classification run (verification L4-1), which this walkthrough did not show because nothing was paid. See `bridge.BR-LMS-144` and `bridge.BR-LMS-194`.
