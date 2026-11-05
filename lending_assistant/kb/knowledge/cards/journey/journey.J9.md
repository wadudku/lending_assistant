---
id: journey.J9
type: journey
title: "Journey J9: Rahim closes his loan"
summary: "A loan closes only when everything is cleared and Rahim gets his security, refund and letter; Frappe Lending 16.5.1 closes loans and refunds, but has no closure approval, CBS check or closure letter."
br_ids: []
brd_section: 7.14
doctypes: [Loan, Loan Repayment, Loan Security Release, Loan Refund, Loan Security Deposit]
dev_items: []
journeys: [J9]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/verification/journeys_verified.json#J9"
  - "sources/verification/walkthroughs/J9_walkthrough.md#stage-1"
  - "sources/verification/walkthroughs/J9_walkthrough.md#stage-2"
  - "sources/verification/walkthroughs/J9_walkthrough.md#stage-3"
  - "sources/verification/walkthroughs/J9_walkthrough.md#stage-4"
  - "sources/verification/walkthroughs/J9_walkthrough.md#stage-5"
  - "sources/verification/walkthroughs/J9_walkthrough.md#stage-6"
  - "sources/verification/walkthroughs/J9_walkthrough.md#stage-7"
related: [howto.loan_repayment.get_payoff_figure, howto.loan_repayment.check_cbs_reference, howto.loan_repayment.close_loan, howto.loan_security_release.request, howto.loan_refund.create, howto.loan_statement_of_account.view, howto.notification.check_borrower_notice, howto.loan.auto_close_credit_line, screen.loan, screen.loan_repayment]
version: 1
status: approved
approved_by: Owner
---
**In short:** A loan closes only when everything is cleared and Rahim gets his security, refund and letter; Frappe Lending 16.5.1 closes loans and refunds, but has no closure approval, CBS check or closure letter.

## The process in plain words

Rahim asks to pay off his loan, or pays his last instalment. The goal in the BRD is that the loan closes only when everything is cleared, and that Rahim gets his security back, any refund and a letter. Loan Operations gives the payoff figure, checks the core banking system, closes the loan through approval, releases the collateral, refunds what is left and closes the file. A repaid credit line should close by itself.

## Stages

The verified journey file lists five stages; the walkthrough splits them into seven, and the table follows the walkthrough.

| Stage | Who | What happens | System side | BR ids |
|---|---|---|---|---|
| 1 Work out what is left | Rahim, branch | The exact amount to close today | The unsaved Loan Repayment form of type Loan Closure. `howto.loan_repayment.get_payoff_figure` | 168, 230 |
| 2 Confirm with the core banking system | Ops officer | CBS account and ledger checked before closure | None today. `howto.loan_repayment.check_cbs_reference` | 231 |
| 3 Close the loan and approve it | Ops officer | Closure blocked until cleared, then approved | Loan Repayment of type Loan Closure, or Request Loan Closure on the loan (status Loan Closure Requested); no approval step. `howto.loan_repayment.close_loan` | 230, 234 |
| 4 Release the collateral | Ops officer | Collateral released | Loan Security Release. `howto.loan_security_release.request` | 232 |
| 5 Refund what is left | Ops officer | Deposit or excess refunded with a reference | Loan Refund, Loan Security Deposit. `howto.loan_refund.create` | 233, 186, 187 |
| 6 Close the file and tell Rahim | System | Closure letter, final statement, message | Loan Statement of Account report. `howto.loan_statement_of_account.view`, `howto.notification.check_borrower_notice` | 235 |
| 7 Close credit lines automatically | System | Repaid credit lines close by themselves | The daily job `auto_close_loc_loans`. `howto.loan.auto_close_credit_line` | 222 |

## Gaps met on the way

- Stage 1: the figure shown and the figure booked differ (DEF-42).
- Stage 3: a closure is accepted short and the gap waived with no approver (DEF-38); an ordinary repayment can close the loan (DEF-39); the closure leaves a negative outstanding on a demand (DEF-41).
- Stage 4: releasing collateral rewrites the closure date (DEF-37).
- Stages 2, 5 and 6: no CBS check, no refund approval, no closure letter or message.

## Outcome

Rahim's loans are closed, the collateral is released, the deposit and excess are refunded and a credit line closes by the job. The journey's verified requirement results are: covered for 187, 222 and 233; partly covered for 168, 186, 230, 232, 234 and 235; gap needing the CBS link for 231.
