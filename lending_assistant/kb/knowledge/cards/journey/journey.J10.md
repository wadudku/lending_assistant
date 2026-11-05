---
id: journey.J10
type: journey
title: "Journey J10: a co-lending partner shares loans"
summary: "Each partner's share of loans, collections and losses is right and reconciled; Frappe Lending 16.5.1 books the partner's share, but has no FLDG engine, closure share, settlement or partner report."
br_ids: []
brd_section: 7.12
doctypes: [Loan Partner, Loan, Loan Repayment Schedule, Loan Demand, Loan Repayment]
dev_items: []
journeys: [J10]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/verification/journeys_verified.json#J10"
  - "sources/verification/walkthroughs/J10_walkthrough.md#stage-1"
  - "sources/verification/walkthroughs/J10_walkthrough.md#stage-2"
  - "sources/verification/walkthroughs/J10_walkthrough.md#stage-3"
  - "sources/verification/walkthroughs/J10_walkthrough.md#stage-4"
  - "sources/verification/walkthroughs/J10_walkthrough.md#stage-5"
related: [howto.loan_partner.create, howto.loan_product.duplicate, howto.loan.choose_co_lender, howto.general_ledger.view_partner_position, howto.report.check_partner_report, screen.loan_partner, screen.loan, screen.loan_repayment_schedule, screen.loan_demand, screen.loan_repayment]
version: 1
status: approved
approved_by: Owner
---
**In short:** Each partner's share of loans, collections and losses is right and reconciled; Frappe Lending 16.5.1 books the partner's share, but has no FLDG engine, closure share, settlement or partner report.

## The process in plain words

A partner, for example an 80% funder of a product, joins a product. The goal in the BRD is that each partner's share of loans, collections and losses is right and reconciled. A partnership manager sets up the partner and the share, the system shares each loan, finance settles and reconciles, and the partnership manager reports back to the partner.

## Stages

| Stage | Who | What happens | System side | BR ids |
|---|---|---|---|---|
| 1 Set up the partner | Partnership manager | Partner master with FLDG or risk-sharing terms, linked to the product | Loan Partner and the Loan Product's Co Lending tab. `howto.loan_partner.create`, `howto.loan_product.duplicate`, `howto.loan.choose_co_lender` | 210, 116 |
| 2 Agree the share | Partnership manager | A share per product | One share figure on the Loan Partner. `howto.loan.choose_co_lender` | 211 |
| 3 Share each loan | System | Partner schedule beside the borrower's; charges shared | Co Lending tab of the schedule, demand and repayment. `howto.loan.choose_co_lender` | 212, 123 |
| 4 Settle and reconcile | Finance | Partner credit notes processed; position reconciled | None: the General Ledger on the partner accounts only. `howto.general_ledger.view_partner_position` | 213 |
| 5 Report to the partner | Partnership manager | Disbursed, collected, outstanding share, delinquency, guarantee used | None today. `howto.report.check_partner_report` | 214 |

## Gaps met on the way

- Stage 1: FLDG terms are stored but never evaluated (ND-41).
- Stage 2: the share is one figure per partner, not per product (ND-42).
- Stage 3: a Loan Closure posts nothing to the partner (DEF-44), and a credit note for a waived charge does not reverse the partner's share (DEF-45).
- Stage 4: no partner settlement, receipt or scheduled reconciliation (ND-40).
- Stage 5: no partner report; only an API without a screen.

## Outcome

A loan is shared with a partner and its first instalment splits correctly, but the loan then closes with nothing posted to the partner. The journey's verified requirement results are: covered for 116, 123, 210 and 211; partly covered for 212 and 213; gap for 214.
