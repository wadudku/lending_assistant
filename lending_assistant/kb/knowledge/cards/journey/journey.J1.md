---
id: journey.J1
type: journey
title: "Journey J1: a funded loan arrives from the LOS"
summary: "From the moment the LOS confirms that the money has reached the borrower, the loan system must take over the loan once, complete and correct: book it, apply product rules, build the schedule, go live and load old loans."
br_ids: []
brd_section: 7.1
doctypes: [Loan, Loan Disbursement, Loan Repayment Schedule]
dev_items: [D1, D2, D3]
journeys: [J1]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/verification/journeys_verified.json#J1"
  - "sources/verification/walkthroughs/J1_walkthrough.md#stage-1"
  - "sources/verification/walkthroughs/J1_walkthrough.md#stage-2"
  - "sources/verification/walkthroughs/J1_walkthrough.md#stage-3"
  - "sources/verification/walkthroughs/J1_walkthrough.md#stage-4"
  - "sources/verification/walkthroughs/J1_walkthrough.md#stage-5"
  - "sources/verification/reqs.json#BR-LMS-100"
  - "sources/verification/reqs.json#BR-LMS-105"
related: [howto.customer.create, howto.loan.create, howto.loan.submit, howto.loan_disbursement.view, howto.loan_product.view, howto.loan.view, howto.loan_repayment_schedule.view, howto.loan_disbursement.view_ledger, howto.data_import.migrate_loan, howto.loan_demand.view]
version: 1
status: approved
approved_by: Owner
---
**In short:** From the moment the LOS confirms that the money has reached the borrower, the loan system must take over the loan once, complete and correct: book it, apply product rules, build the schedule, go live and load old loans.

## The process in plain words

The origination system (LOS) approves a loan and the bank pays the money out. The trigger for this journey is the LOS confirming that the money has reached the borrower's account. From then on the loan belongs to the servicing system (LMS), and the officer's goal is that every funded loan lands in the LMS once, complete and correct. The loan officer books the loan, the product supplies the rate and accounts, the system builds the repayment plan, the loan goes live on one record, and at go-live the old book is brought over from the previous system. Rahim's 100,000 loan over 12 months at 14% is the running example.

## Stages

| Stage | Who | What happens | System side | BR ids |
|---|---|---|---|---|
| 1 Receive handoff | LOS to LMS | The funded package arrives: terms, disbursement reference, approval trail | Loan, then Loan Disbursement; no booking API in 16.5.1 | BR-LMS-100, 102 |
| 2 Apply product rules | System | Rate, schedule method, charges and accounts come from the product | Loan Product, Loan | BR-LMS-103, 104, 106 |
| 3 Build the schedule | System | Twelve EMI rows of principal and interest | Loan Repayment Schedule | BR-LMS-120, 121, 122, 123 |
| 4 Loan goes live | Operations officer | One record shows terms, plan, bills, payments, postings | Loan dashboard | BR-LMS-101 |
| 5 Bring the old book over | Migration team | Old loans come in with opening balances | Loan with Is Imported, loaded by Data Import | BR-LMS-105 |

How-to cards for each screen: `howto.customer.create`, `howto.loan.create`, `howto.loan.submit`, `howto.loan_disbursement.view`, `howto.loan_product.view`, `howto.loan.view`, `howto.loan_repayment_schedule.view`, `howto.loan_disbursement.view_ledger`, `howto.data_import.migrate_loan` and `howto.loan_demand.view`.

## Gaps met on the way

- Stage 1: a handoff with no disbursement reference is accepted, and there is no exception queue (BR-LMS-100, D1). The booking is a plain Loan insert, since there is no booking API.
- Stage 2: the interest rate can still be edited on a draft loan unless it is locked by permission (ND-5).
- Stage 3: a Flat Interest Rate schedule adds a 13th instalment for rounding (DEF-1). Rahim's loan is not on that method and has 12 rows.
- Stage 5: migration has no control totals or sign-off, and the opening principal is billed as one bill (demand) on day one (BR-LMS-105, DEF-6). The verification judged that migration cannot go live as it is.

## Outcome

A loan of 100,000 over 12 months is Disbursed, with an active schedule of 12 rows (EMI 8,979, total interest 7,757.22) and the accounting entry Dr loan portfolio / Cr disbursement bank. The journey's verified requirement results are: covered for 101, 102, 103, 104, 106, 120, 121, 122 and 123, and partly covered for 100 and 105.
