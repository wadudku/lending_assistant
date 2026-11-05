---
id: journey.J5
type: journey
title: "Journey J5: the floating rate changes for many loans"
summary: "When a benchmark moves, treasury wants thousands of floating loans repriced safely from the right date; Frappe Lending 16.5.1 can restructure one loan at a time, with no floating-rate set-up, selection, dry run, maker-checker or notice."
br_ids: []
brd_section: 7.6
doctypes: [Loan Restructure, Loan Repayment Schedule, Loan]
dev_items: [D4, D6, D11]
journeys: [J5]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/verification/journeys_verified.json#J5"
  - "sources/verification/walkthroughs/J5_walkthrough.md#stage-1"
  - "sources/verification/walkthroughs/J5_walkthrough.md#stage-2"
  - "sources/verification/walkthroughs/J5_walkthrough.md#stage-3"
  - "sources/verification/walkthroughs/J5_walkthrough.md#stage-4"
  - "sources/verification/walkthroughs/J5_walkthrough.md#stage-5"
  - "sources/verification/walkthroughs/J5_walkthrough.md#stage-6"
  - "sources/verification/reqs.json#BR-LMS-111"
  - "sources/verification/reqs.json#BR-LMS-154"
related: [howto.loan_product.duplicate, howto.loan_product.set_rates, howto.loan.filter_list, howto.loan_restructure.create, howto.loan_repayment_schedule.compare_plans, howto.loan_restructure.approve, howto.notification.check_borrower_notice, screen.loan_restructure, screen.loan_repayment_schedule, screen.loan]
version: 1
status: approved
approved_by: Owner
---
**In short:** When a benchmark moves, treasury wants thousands of floating loans repriced safely from the right date; Frappe Lending 16.5.1 can restructure one loan at a time, with no floating-rate set-up, selection, dry run, maker-checker or notice.

## The process in plain words

The benchmark rate moves, for example from 9% to 10%. The goal in the BRD is that thousands of floating loans move to the new rate safely and from the right date. Treasury is the maker and Credit Operations the checker. The walkthrough shows what 16.5.1 offers for one loan: a Rahim loan of 100,000 over 12 months, with five on-time EMIs, restructured from 14% to 15%. It works on a copy of the product (`howto.loan_product.duplicate`) that can be restructured.

## Stages

| Stage | Who | What happens | System side | BR ids |
|---|---|---|---|---|
| 1 Benchmark moves | Treasury | Floating loans carry a benchmark, a spread and a review date | None today: one fixed rate on the product and the loan. `howto.loan_product.set_rates` | BR-LMS-111 |
| 2 Pick the loans | Maker | Select by product, segment, branch or ids; skip fixed, closed and frozen loans with a reason | None today; a filtered Loan list is the workaround. `howto.loan.filter_list` | BR-LMS-150, 158 |
| 3 Practice run | Maker | A dry run shows old and new rate, EMI, tenor and total interest | One loan only, through a Draft Loan Restructure. `howto.loan_restructure.create`, `howto.loan_repayment_schedule.compare_plans` | BR-LMS-154, 124 |
| 4 Approve the run | Checker | A different person approves | Loan Restructure: approval is a status edit. `howto.loan_restructure.approve` | BR-LMS-155 |
| 5 Apply safely | System | New rate from the effective date; paid history untouched; new plan versions; rerun-safe | Loan Restructure (Normal Restructure), one loan at a time; the old plan becomes Restructured. `howto.loan_repayment_schedule.compare_plans` | BR-LMS-151, 152, 153, 156, 157, 125, 126 |
| 6 Tell borrowers | System | Affected borrowers are notified after approval | None today. `howto.notification.check_borrower_notice` | BR-LMS-159 |

## Gaps met on the way

- Stage 1: nothing tells fixed from floating loans (BR-LMS-111, D4).
- Stages 2 to 4: no repricing run, dry run or maker-checker; the workaround is a filtered list and one draft per loan and option (D11, ND-18).
- Stage 5: the restructure fails on products whose first-instalment interest is added to the first EMI (DEF-17); using Loan Restructure counts every loan as restructured for Bangladesh Bank (Q5); the interest carried into the first row is also added to principal (DEF-18); a stale draft can be applied twice (DEF-19).
- Stage 6: no borrower notice (BR-LMS-159).

## Outcome

One loan is at 15%, with its paid instalments untouched under an old plan marked Restructured and a new Active plan. The journey's verified requirement results are: partly covered for 111, 124, 125, 152, 153 and 156; gap for 126, 150, 151, 154, 155, 157, 158 and 159.
