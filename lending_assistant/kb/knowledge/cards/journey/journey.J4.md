---
id: journey.J4
type: journey
title: "Journey J4: Rahim falls behind"
summary: "A missed EMI starts daily penalty bills and a days-past-due count; the loan is graded SMA at 60 days and NPA after 90 days, with its interest moved to suspense. Collections, provisioning and a controlled freeze are the gaps."
br_ids: []
brd_section: 7.9
doctypes: [Loan, Loan Demand, Days Past Due Log, Loan NPA Log, Loan Freeze Log]
dev_items: [D8, D14, D15, D17]
journeys: [J4]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/verification/journeys_verified.json#J4"
  - "sources/verification/walkthroughs/J4_walkthrough.md#stage-1"
  - "sources/verification/walkthroughs/J4_walkthrough.md#stage-2"
  - "sources/verification/walkthroughs/J4_walkthrough.md#stage-3"
  - "sources/verification/walkthroughs/J4_walkthrough.md#stage-4"
  - "sources/verification/walkthroughs/J4_walkthrough.md#stage-5"
  - "sources/verification/reqs.json#BR-LMS-190"
  - "sources/verification/reqs.json#BR-LMS-198"
related: [howto.loan_demand.view_penalty, howto.loan.view_grade, howto.loan.filter_list, howto.loan.follow_up, howto.loan_npa_log.view, howto.loan.freeze, howto.company.view_loan_settings, howto.process_loan_interest_accrual.run, howto.process_loan_demand.run, howto.process_loan_classification.run, howto.days_past_due_log.view, screen.loan, screen.loan_demand, screen.days_past_due_log, screen.loan_npa_log, screen.loan_freeze_log]
version: 1
status: approved
approved_by: Owner
---
**In short:** A missed EMI starts daily penalty bills and a days-past-due count; the loan is graded SMA at 60 days and NPA after 90 days, with its interest moved to suspense. Collections, provisioning and a controlled freeze are the gaps.

## The process in plain words

The EMI stays unpaid after the 5 grace days. The goal in the BRD is that late loans are graded, chased and accounted for under Bangladesh Bank rules. The walkthrough follows Rahim's loan from the first missed EMI to NPA, with the monthly accrual and demand runs (`howto.process_loan_interest_accrual.run`, `howto.process_loan_demand.run`) and classification runs back-dated to the days that matter (`howto.process_loan_classification.run`, `howto.days_past_due_log.view`).

## Stages

| Stage | Who | What happens | System side | BR ids |
|---|---|---|---|---|
| 1 EMI missed | System | Days past due are counted daily; penalty interest starts, kept separate | Process Loan Classification, Days Past Due Log, daily Additional Interest demands. `howto.loan_demand.view_penalty` | BR-LMS-141, 190 |
| 2 Early warning (SMA) | System, Credit Risk | The loan is graded by days-past-due bands; a manual override with a reason; every grade change logged | Grade on the Loan (read-only), bands on the Company; the only override is Manual NPA on the Loan. `howto.loan.view_grade`, `howto.company.view_loan_settings` | BR-LMS-191, 192 |
| 3 Chase the payment | Collections officer | Calls, promises to pay, follow-ups; escalation to recovery if promises break | None in 16.5.1: Collection Case and Promise to Pay exist in develop only. `howto.loan.filter_list`, `howto.loan.follow_up` | BR-LMS-198 |
| 4 Becomes NPA | System | Normal income stops; unpaid interest and charges move to suspense | Journal Entries against the loan and the Loan NPA Log. `howto.loan_npa_log.view` | BR-LMS-144, 194 |
| 5 Provision and special cases | Finance, approver | Money set aside by grade and security; freeze when needed | IRAC provisioning table on the Company (no calculation); Freeze Account on the Loan and the Loan Freeze Log. `howto.company.view_loan_settings`, `howto.loan.freeze` | BR-LMS-193, 196 |

## Gaps met on the way

- Stage 1: the penalty billed is contract-rate interest on overdue principal, not the product's penal rate (BR-LMS-141, DEF-10, ND-13).
- Stage 2: the override is NPA yes or no only (BR-LMS-191, D15); the move from STD to SMA is not logged (BR-LMS-192, ND-15).
- Stage 3: no collection case, promises or dunning (BR-LMS-198, D17); the workaround is a saved list, an assignment and comments.
- Stage 4: suspense can be released late or not at all on a partial recovery (DEF-7, DEF-9, DEF-15).
- Stage 5: provision rates are stored but nothing calculates or posts a provision (BR-LMS-193, D14); a freeze has no reason, approver or scope (BR-LMS-196, D8, ND-16).

## Outcome

Rahim's loan, with no payment since the first EMI, is Sub-Standard and flagged NPA at 91 days past due. Its unpaid normal interest sits in suspense. The journey's verified requirement results are: covered for 144 and 190; partly covered for 141, 191, 192, 194 and 196; gap for 193 and 198.
