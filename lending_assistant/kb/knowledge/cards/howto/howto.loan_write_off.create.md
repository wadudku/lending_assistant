---
id: howto.loan_write_off.create
type: howto
title: How to write off a loan
summary: "A manual Loan Write Off must equal the whole pending principal and ignores the write-off threshold; the system also writes off by itself from the classification run, with no approver."
br_ids: [BR-LMS-195, BR-LMS-202, BR-LMS-201]
brd_section: 7.11
doctypes: [Loan Write Off, Loan Repayment, Process Loan Classification, Loan]
dev_items: [D8]
journeys: [J8]
actions: ["Loan Write Off:create"]
fields: [Loan Write Off.Loan, Loan Write Off.Value Date, Loan Write Off.Write Off Amount, Loan Write Off.Is NPA, Process Loan Classification.Posting Date, Process Loan Classification.Loan, Process Loan Classification.Force Update DPD in Loan]
options: [Loan Repayment.Repayment Type=Interest Waiver, Loan Repayment.Repayment Type=Penalty Waiver]
menus: [Lending > Loan Management > Loan Write Off]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J8/J8-S3-5b_write-off-50000-filled.png, /assets/lending_assistant/kb_img/J8/J8-S3-5c_write-off-50000-refused.png, /assets/lending_assistant/kb_img/J8/J8-S3-5e_write-off-submitted.png, /assets/lending_assistant/kb_img/J8/J8-S3-6a_system-waivers-list.png, /assets/lending_assistant/kb_img/J8/J8-S3-6c_gap-waiver-no-reason-or-approver.png, /assets/lending_assistant/kb_img/J8/J8-S3-7a_process-form-cannot-pick-written-off-loan.png, /assets/lending_assistant/kb_img/J8/J8-S3-8c_classification-filled.png, /assets/lending_assistant/kb_img/J8/J8-S3-9f_company-threshold-view-only.png, /assets/lending_assistant/kb_img/J8/J8-S4-2a_def35-performing-loan-write-off-cancelled.png]
sources:
  - "sources/verification/walkthroughs/J8_walkthrough.md#stage-3"
  - "sources/verification/walkthroughs/J8_walkthrough.md#3.5"
  - "sources/verification/walkthroughs/J8_walkthrough.md#3.6"
  - "sources/verification/walkthroughs/J8_walkthrough.md#3.7"
  - "sources/verification/walkthroughs/J8_walkthrough.md#3.8"
  - "sources/verification/walkthroughs/J8_walkthrough.md#3.9"
related: [howto.workflow.check_approval_limits, howto.loan_repayment.settle, howto.process_loan_classification.run, bridge.BR-LMS-195, bridge.BR-LMS-202, journey.J8, screen.loan_write_off, screen.loan_repayment, screen.loan]
version: 1
status: approved
approved_by: Owner
---
**In short:** A manual Loan Write Off must equal the whole pending principal and ignores the write-off threshold; the system also writes off by itself from the classification run, with no approver.

## Before you start

⚠ You need permission to **Submit** a **Loan Write Off**. A write-off is hard to undo, so use a test loan. Names in the screenshots are test records on the dev site.

## Steps

1. Type Loan Write Off in the search bar and click Add.
2. Choose the **Loan**, enter **Value Date** (required) and **Write Off Amount**. A part amount is refused, as the next picture shows.

![A part write-off entered](/assets/lending_assistant/kb_img/J8/J8-S3-5b_write-off-50000-filled.png)

![The part write-off refused](/assets/lending_assistant/kb_img/J8/J8-S3-5c_write-off-50000-refused.png)

3. Enter the full pending principal in **Write Off Amount**, click **Save**, then **Submit** and **Yes**.

![The write-off submitted](/assets/lending_assistant/kb_img/J8/J8-S3-5e_write-off-submitted.png)

The automatic path needs no form. A Process Loan Classification run with **Force Update DPD in Loan** ticked writes off a loan whose days past due pass the Company threshold.

![The classification run entered](/assets/lending_assistant/kb_img/J8/J8-S3-8c_classification-filled.png)

## What you should see

The loan becomes Written Off, and the principal is posted to Bad Debts Written Off. Within seconds the system also creates and submits an Interest Waiver and a Penalty Waiver repayment of its own.

![The waivers the system created](/assets/lending_assistant/kb_img/J8/J8-S3-6a_system-waivers-list.png)

The loan keeps its history: demands, accruals, the DPD log, the NPA log and the ledger.

## If it looks wrong

The BRD wants a write-off with its own trigger, an approver and a record that keeps the loan visible (BR-LMS-195, BR-LMS-201, BR-LMS-202; covered for BR-LMS-195 and BR-LMS-202, partly covered for BR-LMS-201).

- The only manual check is that the amount equals the pending principal. A loan with nothing due was accepted for write-off once, then cancelled (DEF-35).

![A write-off on a loan with nothing due, cancelled](/assets/lending_assistant/kb_img/J8/J8-S4-2a_def35-performing-loan-write-off-cancelled.png)

- The automatic write-off is created and submitted inside the classification job, with no approver. The threshold is one Company setting, checked only by the classification run (nightly, or started by hand with **Force Update DPD in Loan**).

![The Company threshold, view only](/assets/lending_assistant/kb_img/J8/J8-S3-9f_company-threshold-view-only.png)

- The waivers have no reason, approver or link to the write-off.

![A waiver with no reason or approver](/assets/lending_assistant/kb_img/J8/J8-S3-6c_gap-waiver-no-reason-or-approver.png)

- The Process forms cannot pick a written-off loan, so accruals that still run on it cannot be started or checked from the form (DEF-36).

![The Process form cannot pick a written-off loan](/assets/lending_assistant/kb_img/J8/J8-S3-7a_process-form-cannot-pick-written-off-loan.png)

The fix is ND-34. See `bridge.BR-LMS-195`.
