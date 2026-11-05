---
id: journey.J11
type: journey
title: "Journey J11: back office keeps the book healthy"
summary: "Batches finish, failures are owned and fixed, and corrections leave a trail; Frappe Lending 16.5.1 runs and repairs, but its batches show no result, failures have no queue and cancels need no reason."
br_ids: []
brd_section: 7.13
doctypes: [Process Loan Demand, Error Log, Loan Demand, Loan Accrual Repost, Loan Repayment Repost, Loan Transfer, Loan Limit Change Log]
dev_items: []
journeys: [J11]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/verification/journeys_verified.json#J11"
  - "sources/verification/walkthroughs/J11_walkthrough.md#stage-1"
  - "sources/verification/walkthroughs/J11_walkthrough.md#stage-2"
  - "sources/verification/walkthroughs/J11_walkthrough.md#stage-3"
  - "sources/verification/walkthroughs/J11_walkthrough.md#stage-4"
related: [howto.process_loan_demand.rerun_failed, howto.error_log.view_and_assign, howto.notification.check_failure_alert, howto.loan_demand.cancel, howto.loan_accrual_repost.create, howto.loan_repayment_repost.create, howto.loan_transfer.create, howto.loan.change_credit_limit, screen.loan_demand]
version: 1
status: approved
approved_by: Owner
---
**In short:** Batches finish, failures are owned and fixed, and corrections leave a trail; Frappe Lending 16.5.1 runs and repairs, but its batches show no result, failures have no queue and cancels need no reason.

## The process in plain words

Every night the batch runs for accrual, demand and classification, and errors can follow. The goal in the BRD is that batches finish, failures are owned and fixed, and corrections leave a trail. LMS Operations and IT support watch the runs, hear about failures, fix wrong entries with a maker and a checker, and handle portfolio moves such as branch transfers and credit-line limits.

## Stages

| Stage | Who | What happens | System side | BR ids |
|---|---|---|---|---|
| 1 Night batches run | System | Runs with a clear status and per-loan result | Process records that show only Submitted. `howto.process_loan_demand.rerun_failed` | 223, 135 |
| 2 Something fails | Ops, IT | Alert on failure; item lands in a work queue with owner and age | Error Log with Assign; the stock notification is disabled. `howto.error_log.view_and_assign`, `howto.notification.check_failure_alert` | 225, 224 |
| 3 Fix wrong entries | Ops (maker and checker) | Reverse bills with a reason; repost interest or payments; originals kept | Loan Demand Cancel, Loan Accrual Repost, Loan Repayment Repost. `howto.loan_demand.cancel`, `howto.loan_accrual_repost.create`, `howto.loan_repayment_repost.create` | 133, 143, 169 |
| 4 Portfolio moves | Ops officer | Loans move between branches in bulk; limit changes logged | Loan Transfer, which needs a Branch accounting dimension, and the Loan Limit Change Log. `howto.loan_transfer.create`, `howto.loan.change_credit_limit` | 220, 221 |

## Gaps met on the way

- Stage 1: only Loan Repayment Repost has proper run states (ND-43).
- Stage 2: failures sit in an Error Log nobody owns, and nobody is told (ND-44).
- Stage 3: cancelling a bill needs no reason or approver (DEF-47); a cancelled accrual day cannot be redone (DEF-46).
- Stage 4: the limit log has no reason or approver and its rows can be deleted (DEF-48); a transfer cannot run on this site without a Branch dimension.

## Outcome

A failed demand batch is found and re-run, wrong bills and payments are corrected, and credit-line limit changes are logged. The journey's verified requirement results are: covered for 169 and 220; partly covered for 133, 135, 143, 221, 223 and 225; gap for 224.
