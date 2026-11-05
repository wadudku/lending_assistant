---
id: howto.loan_refund.create
type: howto
title: How to refund a security deposit or an excess amount
summary: "A Loan Refund returns a security deposit or an excess payment; it has a bank reference and blocks refunding more than the excess on Submit, but has no approver or workflow."
br_ids: [BR-LMS-233, BR-LMS-186, BR-LMS-187]
brd_section: 7.14
doctypes: [Loan Refund, Loan Security Deposit]
dev_items: []
journeys: [J9]
actions: ["Loan Refund:create"]
fields: [Loan Refund.Loan, Loan Refund.Is Security Amount Refund, Loan Refund.Is Excess Amount Refund, Loan Refund.Value Date, Loan Refund.Refund Amount, Loan Refund.Refund Account, Loan Refund.Reference Number, Loan Security Deposit.Available Amount]
options: []
menus: []
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J9/J9-S5-01_deposit-after-closure.png, /assets/lending_assistant/kb_img/J9/J9-S5-02_deposit-refund-filled.png, /assets/lending_assistant/kb_img/J9/J9-S5-04_deposit-after-refund.png, /assets/lending_assistant/kb_img/J9/J9-S5-12b_refund-5000-blocked.png, /assets/lending_assistant/kb_img/J9/J9-S5-14_gap-loan-refund-no-approver.png]
sources:
  - "sources/verification/walkthroughs/J9_walkthrough.md#stage-5"
  - "sources/verification/walkthroughs/J9_walkthrough.md#5.1"
  - "sources/verification/walkthroughs/J9_walkthrough.md#5.3"
related: [howto.loan_repayment.close_loan, howto.loan_security_release.request, bridge.BR-LMS-233, bridge.BR-LMS-186, journey.J9]
version: 1
status: approved
approved_by: Owner
---
**In short:** A Loan Refund returns a security deposit or an excess payment; it has a bank reference and blocks refunding more than the excess on Submit, but has no approver or workflow.

## Before you start

⚠ You need permission to create and submit a **Loan Refund**. A refund sends money out, so use a test loan. Names in the screenshots are test records on the dev site.

## Steps

1. For a deposit, type Loan Security Deposit in the search bar and open the deposit of the closed loan. Check **Available Amount**.

![The deposit after the closure](/assets/lending_assistant/kb_img/J9/J9-S5-01_deposit-after-closure.png)

2. Type Loan Refund in the search bar and click Add.
3. Choose the **Loan**. Tick **Is Security Amount Refund** for a deposit, or **Is Excess Amount Refund** for an excess payment.
4. Enter **Value Date**, **Refund Amount**, **Refund Account** and **Reference Number**.

![The deposit refund entered](/assets/lending_assistant/kb_img/J9/J9-S5-02_deposit-refund-filled.png)

5. Click **Save**, then **Submit**.

## What you should see

The refund is submitted and the deposit shows an **Available Amount** of zero. The closure itself did not apply or release the deposit, so the refund is a separate step. An excess refund lowers the loan's excess paid, and the loan can then close.

![The deposit after the refund](/assets/lending_assistant/kb_img/J9/J9-S5-04_deposit-after-refund.png)

## If it looks wrong

Refunding more than the excess is blocked, but only on Submit: a draft saves without error, and Submit says "Excess amount refund cannot be more than excess amount paid."

![An over-refund blocked on Submit](/assets/lending_assistant/kb_img/J9/J9-S5-12b_refund-5000-blocked.png)

The BRD wants an overpayment refund approved before the money goes out (BR-LMS-186, partly covered). A Loan Refund has a bank reference (BR-LMS-233, covered) and a correct ledger entry, but no approver, approval date or workflow, so the same user creates and submits it. A second check in the code is commented out.

![No approver on the refund](/assets/lending_assistant/kb_img/J9/J9-S5-14_gap-loan-refund-no-approver.png)

The workaround is a Frappe Workflow on Loan Refund and a bank-side approval outside the system. The fix is ND-37, an approval by a named person before Submit. See `bridge.BR-LMS-186`.
