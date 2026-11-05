---
id: howto.loan_repayment.close_loan
type: howto
title: How to close a loan with a Loan Closure repayment
summary: "A Loan Closure is a Loan Repayment of that type; it can be accepted a little short, the interest gap is posted to Interest Waiver inside the closure with no separate record (DEF-38), and no approval step exists."
br_ids: [BR-LMS-234, BR-LMS-230, BR-LMS-201]
brd_section: 7.14
doctypes: [Loan Repayment, Loan Product, Loan Demand, Workflow]
dev_items: [D8]
journeys: [J9]
actions: ["Loan Repayment:close_loan"]
fields: [Loan Repayment.Repayment Type, Loan Repayment.Value Date, Loan Repayment.Amount Paid, Loan Repayment.Reference Number, Loan Product.Auto Write Off Amount, Loan Demand.Outstanding Amount]
options: [Loan Repayment.Repayment Type=Loan Closure, Loan Repayment.Repayment Type=Normal Repayment]
menus: [Lending > Loan Management > Loan]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J9/J9-S3-20_product-auto-write-off-amount-help.png, /assets/lending_assistant/kb_img/J9/J9-S3-23_B-closed-by-repayment.png, /assets/lending_assistant/kb_img/J9/J9-S3-05_loanA-principal-demand-overpaid.png, /assets/lending_assistant/kb_img/J9/J9-S3-30_gap-no-workflow-list.png]
sources:
  - "sources/verification/walkthroughs/J9_walkthrough.md#stage-3"
  - "sources/verification/walkthroughs/J9_walkthrough.md#3.1"
  - "sources/verification/walkthroughs/J9_walkthrough.md#3.2"
  - "sources/verification/walkthroughs/J9_walkthrough.md#3.3"
  - "sources/verification/walkthroughs/J9_walkthrough.md#3.4"
  - "sources/verification/walkthroughs/J9_walkthrough.md#3.5"
related: [howto.loan_repayment.get_payoff_figure, howto.loan_repayment.check_cbs_reference, bridge.BR-LMS-234, bridge.BR-LMS-201, journey.J9, screen.loan_repayment, screen.loan_product, screen.loan_demand]
version: 1
status: approved
approved_by: Owner
---
**In short:** A Loan Closure is a Loan Repayment of that type; it can be accepted a little short, the interest gap is posted to Interest Waiver inside the closure with no separate record (DEF-38), and no approval step exists.

## Before you start

⚠ You need permission to **Submit** a **Loan Repayment**. A closure ends the loan, so use a test loan. Names in the screenshots are test records on the dev site.

## Steps

1. Read the payoff figure (`howto.loan_repayment.get_payoff_figure`).
2. On the loan click Create and choose Loan Repayment. Set **Repayment Type** to Loan Closure, enter **Value Date**, **Amount Paid** and **Reference Number**.
3. Click **Save**, then **Submit** and **Yes**.

## What you should see

The repayment is submitted and the loan becomes Closed with a closure date. The loan's **Auto Write Off Amount** (a product setting, applied to every loan of the product) is the tolerance for a shortfall.

![The Auto Write Off Amount help text on the product](/assets/lending_assistant/kb_img/J9/J9-S3-20_product-auto-write-off-amount-help.png)

## If it looks wrong

The BRD wants a closure to be requested and approved (BR-LMS-234, partly covered), with any waiver approved and recorded as a waiver (BR-LMS-201).

- The loan's Status menu has Request Loan Closure, which sets the status Loan Closure Requested; it writes off a balance below the product's **Auto Write Off Amount** and refuses when more is outstanding (BR-LMS-234).
- A closure paid slightly short is accepted, and the gap is posted to Interest Waiver inside the closure itself. There is no waiver record, approver or reason (DEF-38, ND-35).
- The product help text says the write-off happens on a "loan closure request", but the code acts on any repayment that leaves a shortfall within the tolerance. A Normal Repayment can therefore close a loan with no request, no approver and no collateral check (DEF-39).

![A Normal Repayment closed the loan](/assets/lending_assistant/kb_img/J9/J9-S3-23_B-closed-by-repayment.png)

- The closure parks the whole pending principal on the one principal demand, so that demand's **Outstanding Amount** goes negative and the repayment detail line cannot be reconciled with it. A report that sums outstanding is wrong on a closed loan (DEF-41).

![The principal demand form with its loan, schedule and disbursement links](/assets/lending_assistant/kb_img/J9/J9-S3-05_loanA-principal-demand-overpaid.png)

- There is no Workflow for Loan Repayment, Loan Refund, Loan Security Release or the loan, and no Loan Closure Request document.

![No workflow list entry for closure](/assets/lending_assistant/kb_img/J9/J9-S3-30_gap-no-workflow-list.png)

The workaround is a Frappe Workflow on Loan Repayment, with conditions that exempt the repayments the system creates itself. The fix is ND-35, closure as a request that passes checks and is approved. See `bridge.BR-LMS-234`.
