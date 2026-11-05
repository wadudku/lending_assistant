---
id: journey.J8
type: journey
title: "Journey J8: a problem loan is settled or written off"
summary: "The bank recovers what it can from a problem loan under approval limits and keeps the full story; Frappe Lending 16.5.1 settles, writes off and recovers, but has no offer record, approval step or CBS posting."
br_ids: []
brd_section: 7.11
doctypes: [Loan, Loan Repayment, Loan Write Off]
dev_items: []
journeys: [J8]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/verification/journeys_verified.json#J8"
  - "sources/verification/walkthroughs/J8_walkthrough.md#stage-1"
  - "sources/verification/walkthroughs/J8_walkthrough.md#stage-2"
  - "sources/verification/walkthroughs/J8_walkthrough.md#stage-3"
  - "sources/verification/walkthroughs/J8_walkthrough.md#stage-4"
  - "sources/verification/walkthroughs/J8_walkthrough.md#stage-5"
related: [howto.loan_repayment.get_payoff_figure, howto.workflow.check_approval_limits, howto.loan_repayment.settle, howto.loan_write_off.create, howto.loan_repayment.check_cbs_reference, howto.loan_repayment.recover_write_off, screen.loan, screen.loan_repayment, screen.loan_write_off]
version: 1
status: approved
approved_by: Owner
---
**In short:** The bank recovers what it can from a problem loan under approval limits and keeps the full story; Frappe Lending 16.5.1 settles, writes off and recovers, but has no offer record, approval step or CBS posting.

## The process in plain words

A loan is deep in NPA, or the borrower offers a settlement, or recovery has stalled. The goal in the BRD is that the bank recovers what it can, under approval limits, and keeps the full story. A recovery officer works out the offer, approvers sign it off by amount and role, the system settles or writes off, the effects go to the core banking system, and money collected later is booked against the original loan.

## Stages

| Stage | Who | What happens | System side | BR ids |
|---|---|---|---|---|
| 1 Work out the offer | Recovery officer | Payoff figure on demand; settlement make-up shown before approval | The unsaved Loan Repayment form; no Get Dues screen. `howto.loan_repayment.get_payoff_figure` | 168, 200 |
| 2 Approve within limits | Approvers | Maker-checker within amount and role limits; full before and after record | None: no Workflow or limit on Loan Repayment or Loan Write Off. `howto.workflow.check_approval_limits` | 201, 205 |
| 3 Settle or write off | System | Settlement order used; write-off on its own DPD threshold; history kept | Loan Repayment of a settlement type creates its own waivers and a settlement Loan Write Off; automatic write-off at 1,080 DPD. `howto.loan_repayment.settle`, `howto.loan_write_off.create` | 114, 195, 202 |
| 4 Post to CBS | RPA | Settlement and write-off effects sent to the CBS; journal reference kept | None today. `howto.loan_repayment.check_cbs_reference` | 204 |
| 5 Recover later | Recovery officer | Money collected later is booked against the original loan | Loan Repayment of type Write Off Recovery or Write Off Settlement. `howto.loan_repayment.recover_write_off` | 203 |

## Gaps met on the way

- Stage 1: no settlement offer record, and the payoff figure leaves out interest accrued but not yet billed (DEF-34).
- Stage 2: settlements, waivers and write-offs post with no approver or limit.
- Stage 3: collected interest can land in Interest Waiver (DEF-34); a loan with nothing due can be written off by hand (DEF-35); a written-off loan keeps accruing (DEF-36).
- Stage 4: nothing is sent to the CBS.
- Stage 5: a partial Write Off Settlement marks the loan Settled (DEF-36).

## Outcome

One loan is settled, one is written off and partly recovered, and one is written off automatically by a classification run and then settled. The journey's verified requirement results are: covered for 195, 202 and 203; partly covered for 114, 168, 200, 201 and 205; gap needing the CBS link for 204.
