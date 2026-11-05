---
id: journey.J6
type: journey
title: "Journey J6: Rahim asks to change his loan"
summary: "Rahim wants to pay extra, or cannot keep up with the EMI; prepayments, restructures and waivers are shown, approved and recorded. Frappe Lending 16.5.1 has the screens, with no approval step, no regulator category and no Bangladesh Bank report."
br_ids: []
brd_section: 7.6
doctypes: [Loan Repayment, Loan Restructure, Loan Balance Adjustment, Loan Repayment Schedule]
dev_items: [D6, D8, D16, D20]
journeys: [J6]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/verification/journeys_verified.json#J6"
  - "sources/verification/walkthroughs/J6_walkthrough.md#stage-1"
  - "sources/verification/walkthroughs/J6_walkthrough.md#stage-2"
  - "sources/verification/walkthroughs/J6_walkthrough.md#stage-3"
  - "sources/verification/walkthroughs/J6_walkthrough.md#stage-4"
  - "sources/verification/walkthroughs/J6_walkthrough.md#stage-5"
  - "sources/verification/walkthroughs/J6_walkthrough.md#stage-6"
  - "sources/verification/reqs.json#BR-LMS-180"
  - "sources/verification/reqs.json#BR-LMS-188"
related: [howto.loan_repayment.preview_effect, howto.loan_repayment.pay_ahead, howto.loan_restructure.create, howto.loan_restructure.approve, howto.loan_repayment.waive_penalty, howto.loan_balance_adjustment.create, howto.loan_repayment_schedule.compare_plans, howto.report.check_restructure_report, screen.loan_repayment, screen.loan_restructure, screen.loan_repayment_schedule]
version: 1
status: approved
approved_by: Owner
---
**In short:** Rahim wants to pay extra, or cannot keep up with the EMI; prepayments, restructures and waivers are shown, approved and recorded. Frappe Lending 16.5.1 has the screens, with no approval step, no regulator category and no Bangladesh Bank report.

## The process in plain words

Rahim wants to pay extra, or he cannot keep up with the EMI. The goal in the BRD is that prepayments, restructures and waivers are shown first, approved, and fully recorded. The branch officer and an approver handle two loans in the walkthrough: one on time, for prepayments, and one with two missed EMIs, for corrections and a restructure. The walkthrough shows Stage 4 before Stage 3, because the restructure capitalizes all overdue amounts.

## Stages

| Stage | Who | What happens | System side | BR ids |
|---|---|---|---|---|
| 1 Show the effect first | Branch officer | What-if view of the new EMI or tenor, nothing posted | A Draft Pre Payment builds a draft restructure and plan. `howto.loan_repayment.preview_effect` | BR-LMS-124 |
| 2 Pay ahead or prepay | Rahim | An advance covers future EMIs; a prepayment cuts principal, with a fee | Loan Repayment of type Advance Payment or Pre Payment, which creates and approves a Loan Restructure. `howto.loan_repayment.pay_ahead` | BR-LMS-180, 181, 131 |
| 3 Restructure terms | Branch officer | New rate, tenor or EMI; type recorded; branch limits enforced | Loan Restructure; approval is a status edit; the Restructure Limit Log is never filled. `howto.loan_restructure.create`, `howto.loan_restructure.approve` | BR-LMS-182, 184 |
| 4 Approve corrections | Approver | Waivers and balance fixes under maker-checker, with before and after | Loan Repayment of waiver types and Loan Balance Adjustment, with no approval step. `howto.loan_repayment.waive_penalty`, `howto.loan_balance_adjustment.create` | BR-LMS-185 |
| 5 New schedule version | System | A new plan; the old one is kept as superseded | Loan Repayment Schedule, old plan Restructured or Rescheduled. `howto.loan_repayment_schedule.compare_plans` | BR-LMS-183, 125, 126 |
| 6 Report to Bangladesh Bank | Compliance | Restructures, reschedules and waivers reported with the treatment | None today. `howto.report.check_restructure_report` | BR-LMS-188 |

## Gaps met on the way

- Stage 1: a what-if leaves three records to delete by hand (D6).
- Stage 2: Rahim cannot choose a lower EMI against a shorter loan, and Reduce EMI is ignored (DEF-21, D20); the prepayment fee is typed by hand (BR-LMS-131, ND-1).
- Stage 3: no regulator category (D16); restructuring an NPA loan moves suspense to income (DEF-22).
- Stage 4: no workflow, limit or reason (BR-LMS-185, D8).
- Stage 6: no report (BR-LMS-188, D16).

## Outcome

One loan is two months shorter after a prepayment with the same EMI; the other is restructured over 12 months with its arrears capitalized. The journey's verified requirement results are: covered for 183; partly covered for 124, 125, 131, 180, 181, 182 and 185; gap for 126, 184 and 188.
