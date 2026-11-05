---
id: screen.loan_disbursement
type: screen
title: "Screen: Loan Disbursement"
summary: "The Loan Disbursement screen records the money paid out on a loan, in one or more draws, and posts the accounting entries when submitted."
br_ids: [BR-LMS-100, BR-LMS-134, BR-LMS-204, BR-LMS-211]
brd_section: 7.1
doctypes: [Loan Disbursement]
dev_items: [D1]
fields: [Loan Disbursement.Against Loan, Loan Disbursement.Disbursement Date, Loan Disbursement.Disbursed Amount, Loan Disbursement.Posting Date, Loan Disbursement.Reference Date, Loan Disbursement.Reference Number, Loan Disbursement.Monthly Repayment Amount, Loan Disbursement.Repayment Start Date, Loan Disbursement.Broken Period Interest, Loan Disbursement.Status]
options: [Loan Disbursement.Status=Submitted]
menus: [Lending > Loan Management > Loan Disbursement]
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_disbursement/loan_disbursement.json]
images: [/assets/lending_assistant/kb_img/J1/J1-S1-07_disbursement-auto-created.png, /assets/lending_assistant/kb_img/J1/J1-S1-08_gap-no-disbursement-reference.png]
sources:
  - "sources/verification/walkthroughs/J1_walkthrough.md#stage-1"
  - "sources/verification/walkthroughs/J1_walkthrough.md#1.4"
  - "sources/verification/walkthroughs/J1_walkthrough.md#1.5"
  - "sources/verification/walkthroughs/J1_walkthrough.md#4.2"
  - "sources/verification/verification_report.md#BR-LMS-100"
  - "sources/verification/reqs.json#BR-LMS-100"
related: [howto.loan_disbursement.view, howto.loan_disbursement.view_ledger, howto.loan.submit, screen.loan, brd_section.7.1, bridge.BR-LMS-100, devitem.D1, lifecycle.PARTIALLY_DISBURSED]
version: 1
status: approved
approved_by: Owner
---
**In short:** The Loan Disbursement screen records the money paid out on a loan, in one or more draws, and posts the accounting entries when submitted.

## What this screen is for

**Loan Disbursement** records money paid out against a loan (menu: Lending > Loan Management > Loan Disbursement). It is a submittable document; on submit it posts the accounting entries. A loan can have several disbursements, one per draw. When the loan was booked with Auto create disbursement on loan booking ticked, the system creates and submits the disbursement itself, and the repayment schedule in the same action (see `howto.loan.submit`).

## Before and after

Before: the loan exists (`screen.loan`). After: the schedule, the daily interest and the demands run from the disbursement (`howto.loan_repayment_schedule.view`, `howto.loan_demand.view`). To check the ledger entries, see `howto.loan_disbursement.view_ledger`.

## Key fields

**Against Loan**, **Disbursement Date**, **Disbursed Amount**, **Reference Date**, **Reference Number**, and on a submitted record **Monthly Repayment Amount**, **Repayment Start Date**, **Broken Period Interest** and **Status**. In the J1 walkthrough the auto-created disbursement showed Submitted, 100,000 disbursed and a monthly repayment of 8,979. The disbursement's own **Posting Date**, and its ledger entries, were the day of the run, not the loan's back-dated date (DEF-5). The **Against Loan** picker lists only Sanctioned, Active or Partially Disbursed loans.

![An auto-created disbursement](/assets/lending_assistant/kb_img/J1/J1-S1-07_disbursement-auto-created.png)

**Reference Date** and **Reference Number** are optional: the walkthrough saved and submitted a disbursement with both empty.

![Reference Date and Reference Number are empty and optional](/assets/lending_assistant/kb_img/J1/J1-S1-08_gap-no-disbursement-reference.png)

## BRD needs it serves

BR-LMS-100 in BRD 7.1 (see `brd_section.7.1`), plus BR-LMS-134, 204 and 211; the bridges hold the verdicts. The weak point shown is that nothing rejects a handoff without a disbursement reference, and there is no exception queue (`bridge.BR-LMS-100`, D1). The installed doctype gives System Manager and Loan Manager read, write, create, submit, cancel and delete, and Loan Reporter read only.
