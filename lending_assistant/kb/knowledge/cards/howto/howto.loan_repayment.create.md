---
id: howto.loan_repayment.create
type: howto
title: How to key a payment as a Draft
summary: "Create the Loan Repayment from the loan and save it without submitting; a Draft changes no dues, which makes it a manual hold until the bank confirms."
br_ids: [BR-LMS-160, BR-LMS-161, BR-LMS-167]
brd_section: 7.7
doctypes: [Loan Repayment, Loan]
dev_items: [D12]
journeys: [J3]
actions: ["Loan Repayment:create"]
fields: [Loan Repayment.Repayment Type, Loan Repayment.Value Date, Loan Repayment.Amount Paid, Loan Repayment.Reference Number]
options: [Loan Repayment.Repayment Type=Normal Repayment]
menus: [Lending > Loan Management > Loan Repayment]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J3/J3-S3-01_loan-create-repayment-menu.png, /assets/lending_assistant/kb_img/J3/J3-S3-02_repayment-filled-top.png, /assets/lending_assistant/kb_img/J3/J3-S3-03_repayment-filled-amounts.png, /assets/lending_assistant/kb_img/J3/J3-S3-04_repayment-draft-saved.png, /assets/lending_assistant/kb_img/J3/J3-S3-05_gap-draft-dues-unchanged.png, /assets/lending_assistant/kb_img/J3/J3-S3-06_gap-repayment-list-draft-only.png, /assets/lending_assistant/kb_img/J3/J3-S3-07_gap-bank-transaction-no-loan.png]
sources:
  - "sources/verification/walkthroughs/J3_walkthrough.md#stage-3"
  - "sources/verification/walkthroughs/J3_walkthrough.md#3.1"
  - "sources/verification/walkthroughs/J3_walkthrough.md#3.2"
  - "sources/verification/walkthroughs/J3_walkthrough.md#3.3"
related: [howto.loan_repayment.submit, bridge.BR-LMS-160, bridge.BR-LMS-161, bridge.BR-LMS-167, journey.J3, screen.loan_repayment, screen.loan]
version: 1
status: approved
approved_by: Owner
---
**In short:** Create the Loan Repayment from the loan and save it without submitting; a Draft changes no dues, which makes it a manual hold until the bank confirms.

## Before you start

⚠ You need permission to create a **Loan Repayment**. The loan must be Disbursed. In the walkthrough the customer paid at the branch and the officer keyed the payment later, with the value date of the payment. Names in the screenshots, such as the reference, are test records on the dev site.

## Steps

1. Open the loan, click Create at the top right and choose Loan Repayment. The form opens pre-filled with the loan, the applicant and **Repayment Type** Normal Repayment.
2. Enter **Value Date**. It is a date and time field: type the time too (for example 00:00:00) or the value is dropped.
3. Enter **Amount Paid** (e.g. 8,979 for Rahim's first EMI).
4. Under Payment References, enter **Reference Number**, the bank or CBS transaction id.
5. Click **Save**. Do not click Submit yet.

![Loan > Create > Loan Repayment](/assets/lending_assistant/kb_img/J3/J3-S3-01_loan-create-repayment-menu.png)

![Value date entered](/assets/lending_assistant/kb_img/J3/J3-S3-02_repayment-filled-top.png)

![Amount and reference entered](/assets/lending_assistant/kb_img/J3/J3-S3-03_repayment-filled-amounts.png)

## What you should see

The repayment is saved as Draft and its Repayment Details already show the planned allocation to the open demands. The Posting Date cannot be set: the code sets it to the time of saving.

![Saved as Draft](/assets/lending_assistant/kb_img/J3/J3-S3-04_repayment-draft-saved.png)

## If it looks wrong

Draft is the only "pending" state. While the repayment is a Draft the demands still show nothing paid and no ledger entry exists. Loan Repayment has no status field and no workflow, so nothing marks it as waiting for the CBS. The BRD wants a payment to count only after the CBS confirms it (BR-LMS-161, partly covered). The workaround in the verification is to save as Draft with the CBS reference and submit after the confirmation is seen; the fix is D12. See `bridge.BR-LMS-161`.

![Dues unchanged while Draft](/assets/lending_assistant/kb_img/J3/J3-S3-05_gap-draft-dues-unchanged.png)

![Draft is the only waiting state](/assets/lending_assistant/kb_img/J3/J3-S3-06_gap-repayment-list-draft-only.png)

No payment from a bank line. A Bank Transaction has no loan field and no action that creates a repayment (BR-LMS-167, partly covered): the officer keys the repayment by hand and then matches it in Bank Reconciliation. See `bridge.BR-LMS-167`.

![Bank Transaction: no loan field](/assets/lending_assistant/kb_img/J3/J3-S3-07_gap-bank-transaction-no-loan.png)
