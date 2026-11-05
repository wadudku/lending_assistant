---
id: journey.J3
type: journey
title: "Journey J3: Rahim pays his EMI on time"
summary: "Interest accrues daily, the EMI is billed on the due date, Rahim's payment is keyed and applied once, and operations checks the numbers; the CBS legs and the duplicate-payment check are the gaps."
br_ids: []
brd_section: 7.4
doctypes: [Process Loan Interest Accrual, Loan Interest Accrual, Process Loan Demand, Loan Demand, Loan Repayment]
dev_items: [D7, D9, D10, D12, D13]
journeys: [J3]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/verification/journeys_verified.json#J3"
  - "sources/verification/walkthroughs/J3_walkthrough.md#stage-1"
  - "sources/verification/walkthroughs/J3_walkthrough.md#stage-2"
  - "sources/verification/walkthroughs/J3_walkthrough.md#stage-3"
  - "sources/verification/walkthroughs/J3_walkthrough.md#stage-4"
  - "sources/verification/walkthroughs/J3_walkthrough.md#stage-5"
  - "sources/verification/reqs.json#BR-LMS-140"
  - "sources/verification/reqs.json#BR-LMS-162"
related: [howto.process_loan_interest_accrual.run, howto.loan_interest_accrual.view, howto.process_loan_demand.run, howto.loan_demand.view_emi_bill, howto.loan_repayment.create, howto.loan_repayment.submit, howto.process_loan_classification.run, howto.days_past_due_log.view, howto.loan_outstanding_report.view, howto.customer.create, howto.loan.create, howto.loan.submit, howto.loan_repayment_schedule.view, screen.loan_interest_accrual, screen.loan_demand, screen.loan_repayment]
version: 1
status: approved
approved_by: Owner
---
**In short:** Interest accrues daily, the EMI is billed on the due date, Rahim's payment is keyed and applied once, and operations checks the numbers; the CBS legs and the duplicate-payment check are the gaps.

## The process in plain words

On the 5th of the month Rahim's EMI is due. The BRD goal: Rahim is billed correctly, his payment counts once, and the loan system and the core banking system (CBS) agree. The example is Rahim's 100,000 loan over 12 months at 14%: EMI 8,979, daily interest 38.36. Rahim pays at the branch and the officer keys the payment. The loan is first set up with the J1 how-tos (`howto.customer.create`, `howto.loan.create`, `howto.loan.submit`, `howto.loan_repayment_schedule.view`).

## Stages

| Stage | Who | What happens | System side | BR ids |
|---|---|---|---|---|
| 1 Interest builds daily | System | 38.36 accrues every day; odd-day interest is handled | Process Loan Interest Accrual, Loan Interest Accrual. `howto.process_loan_interest_accrual.run`, `howto.loan_interest_accrual.view` | BR-LMS-140, 142 |
| 2 Bill on the due date | System | The night batch raises the 8,979 bill and any fees | Process Loan Demand, Loan Demand. `howto.process_loan_demand.run`, `howto.loan_demand.view_emi_bill` | BR-LMS-130, 131, 134, 135 |
| 3 Rahim pays | Rahim, CBS | The CBS records the money; the loan system records channel, reference and value date and waits for confirmation | Loan Repayment as a Draft; a Bank Transaction is only matched through the Bank Reconciliation Tool. `howto.loan_repayment.create` | BR-LMS-160, 161, 167 |
| 4 Apply the payment | Operations officer | The payment is split in the set order as at its value date | Loan Repayment; bulk entry is API only, with Bulk Repayment Log as its result. `howto.loan_repayment.submit`, `howto.process_loan_classification.run`, `howto.days_past_due_log.view` | BR-LMS-162, 163, 164, 165, 166 |
| 5 Check the numbers | Operations, Finance | A dues view on any date; interest and payments reconciled with the CBS | Loan Outstanding Report with its As On Date filter, and the Days Past Due Log. `howto.loan_outstanding_report.view` | BR-LMS-132, 145, 170r, 171r |

## Gaps met on the way

- Stage 2: instalment charges are not billed with the EMI (BR-LMS-131, ND-11, DEF-4); the bill has no CBS journal reference (BR-LMS-134, D13); the demand run has no per-loan result and no resume (BR-LMS-135, D9).
- Stage 3: a Draft is the only "pending" state and nothing marks it as waiting for the CBS (BR-LMS-161, D12), and no repayment from a Bank Transaction (BR-LMS-167).
- Stage 4: the same CBS reference can be applied twice (BR-LMS-162, ND-6); an Interest row in the payment order sends the EMI to principal (DEF-3); bulk entry has no upload screen (BR-LMS-166, ND-7).
- Stage 5: no penalty or charges columns and no as-at-date days past due (BR-LMS-132, ND-8); no interest reconciliation (BR-LMS-145, D10); no CBS feed and no end-to-end match (BR-LMS-170r, 171r, D13).

## Outcome

Rahim's loan is Disbursed with 0 days past due, the first EMI is billed and paid on time as interest first and then principal. The journey's verified requirement results are: covered for 130, 140, 142, 160, 163 and 165; partly covered for 131, 132, 135, 161, 164, 166 and 167; gap for 145 and 162; gap needing the CBS link for 134, 170r and 171r.
