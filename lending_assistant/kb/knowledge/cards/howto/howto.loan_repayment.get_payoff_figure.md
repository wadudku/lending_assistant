---
id: howto.loan_repayment.get_payoff_figure
type: howto
title: How to read the payoff figure for a loan
summary: "There is no Get Dues screen: the payoff figure is the unsaved Loan Repayment form, and it changes with the Repayment Type you pick."
br_ids: [BR-LMS-168, BR-LMS-230]
brd_section: 7.7
doctypes: [Loan Repayment]
dev_items: []
journeys: [J8, J9]
actions: ["Loan Repayment:payoff_figure"]
fields: [Loan Repayment.Repayment Type, Loan Repayment.Value Date, Loan Repayment.Pending Principal Amount, Loan Repayment.Interest Payable, Loan Repayment.Penalty Amount, Loan Repayment.Payable Amount, Loan Repayment.Amount Paid]
options: [Loan Repayment.Repayment Type=Normal Repayment, Loan Repayment.Repayment Type=Partial Settlement, Loan Repayment.Repayment Type=Full Settlement, Loan Repayment.Repayment Type=Loan Closure]
menus: [Lending > Loan Management > Loan]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/verification/walkthroughs/J8_walkthrough.md#stage-1"
  - "sources/verification/walkthroughs/J8_walkthrough.md#1.1"
  - "sources/verification/walkthroughs/J8_walkthrough.md#1.2"
  - "sources/verification/walkthroughs/J9_walkthrough.md#stage-1"
  - "sources/verification/walkthroughs/J9_walkthrough.md#1.1"
  - "sources/verification/walkthroughs/J9_walkthrough.md#1.2"
  - "sources/verification/walkthroughs/J9_walkthrough.md#1.3"
related: [howto.loan_repayment.settle, howto.loan_repayment.close_loan, bridge.BR-LMS-168, bridge.BR-LMS-230, journey.J8, journey.J9, screen.loan_repayment]
version: 1
status: approved
approved_by: Owner
---
**In short:** There is no Get Dues screen: the payoff figure is the unsaved Loan Repayment form, and it changes with the Repayment Type you pick.

## Before you start

⚠ You need permission to create a **Loan Repayment**. Nothing is saved while you only read the figure, so no record is created. Names in the screenshots are test records on the dev site.

## Steps

1. Open the loan, click Create and choose Loan Repayment.
2. Set **Value Date** to the day the borrower would pay.
3. Pick **Repayment Type** Normal Repayment and read **Payable Amount**. This is the current instalment only.
4. Change **Repayment Type** to Partial Settlement, Full Settlement or Loan Closure and read the figure again. Each type shows its own **Pending Principal Amount**, **Interest Payable**, **Penalty Amount** and **Payable Amount**.
5. Close the form without saving.

## What you should see

The figure depends on the type: a Normal Repayment asks for the instalment, a Full Settlement adds the principal not yet due, and a Loan Closure adds the interest accrued but not yet billed. On Partial Settlement, Full Settlement and Loan Closure, **Amount Paid** stayed at 0 in the walkthrough, so the officer types the amount. The same figure is also available through the `calculate_amounts` method of the Loan Repayment code.

## If it looks wrong

The BRD wants one exact payoff figure that the closure then enforces (BR-LMS-168 and BR-LMS-230, partly covered). Here the figure differs by repayment type, and a Loan Closure checks only the amount against the saved payable, less up to the product's tolerance. It does not check open demands, charges, pledged collateral or a CBS balance.

The workaround is to read the payable from the form and re-check demands, collateral and the CBS balance by hand. The fix is ND-36, one calculation for the form, the check and the posting. See `bridge.BR-LMS-168`.
