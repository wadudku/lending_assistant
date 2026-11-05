---
id: screen.loan_demand
type: screen
title: "Screen: Loan Demand"
summary: "The Loan Demand screen is the bill raised for a loan on a due date: the EMI's interest and principal, penalty or a charge, with its outstanding amount."
br_ids: [BR-LMS-130, BR-LMS-131, BR-LMS-133, BR-LMS-134, BR-LMS-135, BR-LMS-224, BR-LMS-230]
brd_section: 7.4
doctypes: [Loan Demand]
dev_items: [D9, D13]
fields: [Loan Demand.Demand Date, Loan Demand.Demand Type, Loan Demand.Demand Subtype, Loan Demand.Demand Amount, Loan Demand.Paid Amount, Loan Demand.Waived Amount, Loan Demand.Outstanding Amount, Loan Demand.Loan, Loan Demand.Loan Repayment Schedule, Loan Demand.Posting Date]
options: [Loan Demand.Demand Type=EMI, Loan Demand.Demand Type=Penalty, Loan Demand.Demand Type=Charges, Loan Demand.Demand Type=BPI]
menus: [Lending > Loan Management > Loan Demand]
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_demand/loan_demand.json]
images: [/assets/lending_assistant/kb_img/J3/J3-S2-03_demand-list.png, /assets/lending_assistant/kb_img/J3/J3-S2-04_demand-emi-interest.png]
sources:
  - "sources/verification/walkthroughs/J3_walkthrough.md#stage-2"
  - "sources/verification/walkthroughs/J3_walkthrough.md#2.1"
  - "sources/verification/walkthroughs/J3_walkthrough.md#2.2"
  - "sources/verification/walkthroughs/J3_walkthrough.md#2.3"
  - "sources/verification/walkthroughs/J3_walkthrough.md#2.4"
  - "sources/verification/walkthroughs/J3_walkthrough.md#2.5"
  - "sources/verification/reqs.json#BR-LMS-130"
related: [howto.loan_demand.view, screen.loan, screen.loan_repayment, screen.loan_repayment_schedule, brd_section.7.4, bridge.BR-LMS-130, bridge.BR-LMS-131, bridge.BR-LMS-134, bridge.BR-LMS-135, glossary.demand, devitem.D9, devitem.D13]
version: 1
status: approved
approved_by: Owner
---
**In short:** The Loan Demand screen is the bill raised for a loan on a due date: the EMI's interest and principal, penalty or a charge, with its outstanding amount.

## What this screen is for

**Loan Demand** is a bill: the amount a borrower owes on one date (menu: Lending > Loan Management > Loan Demand). The daily job raises demands from the repayment schedule on the due date; a Sales Invoice for a charge is turned into a Charges demand. A repayment is split across the open demands. The **Demand Type** options are EMI, Penalty, Normal, Charges, BPI and Additional Interest.

## Before and after

Before: the schedule row is due (`screen.loan_repayment_schedule`) and the interest has built up (`screen.loan_interest_accrual`). After: the borrower pays and the repayment settles the **Outstanding Amount** (`screen.loan_repayment`).

## Key fields

**Demand Date**, **Demand Type**, **Demand Subtype**, **Demand Amount**, **Paid Amount**, **Waived Amount**, **Outstanding Amount**, **Loan** and **Loan Repayment Schedule**. In the J3 example the due-date run produced two EMI demands for 05-07-2026: an Interest demand of 1,150.68 and a Principal demand of 7,828.32. The demand's own **Posting Date** is the day of the run, not the due date.

![The demand list for one loan](/assets/lending_assistant/kb_img/J3/J3-S2-03_demand-list.png)

![An EMI Interest demand](/assets/lending_assistant/kb_img/J3/J3-S2-04_demand-emi-interest.png)

## BRD needs it serves

The main rows are BR-LMS-130, 131 and 133 to 135 in BRD 7.4 (BR-LMS-224 is in the work queues of BRD 7.13, BR-LMS-230 in the closure rows of BRD 7.14) (see `brd_section.7.4`); the bridges hold the verdicts. Weak points shown in the J3 walkthrough: an instalment charge is not billed with the EMI (ND-11, DEF-4, `bridge.BR-LMS-131`), there is no field for the CBS journal reference on the bill (`bridge.BR-LMS-134`, D13), and the demand run keeps no per-loan result list and no resume (`bridge.BR-LMS-135`, D9). The installed doctype gives System Manager and Loan Manager read, write, create, submit and delete, and Loan Reporter read only.
