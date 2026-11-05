---
id: howto.loan_repayment_repost.create
type: howto
title: How to repost a wrong payment safely
summary: "A Loan Repayment Repost reverses and re-posts a payment's ledger entries and goes from Draft to Completed; it has no reason or approval, and no role can cancel it."
br_ids: [BR-LMS-169]
brd_section: 7.7
doctypes: [Loan Repayment Repost, Loan Repayment]
dev_items: []
journeys: [J11]
actions: ["Loan Repayment Repost:create"]
fields: [Loan Repayment Repost.Loan, Loan Repayment Repost.Repost Date, Loan Repayment Repost.Entries To Repost, Loan Repayment Repost.Status]
options: [Loan Repayment Repost.Status=Completed]
menus: []
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J11/J11-S3-21_repayment-repost-filled.png, /assets/lending_assistant/kb_img/J11/J11-S3-22_repayment-repost-completed.png]
sources:
  - "sources/verification/walkthroughs/J11_walkthrough.md#3.4"
related: [howto.loan_repayment.submit, howto.loan_accrual_repost.create, bridge.BR-LMS-169, journey.J11, screen.loan_repayment]
version: 1
status: approved
approved_by: Owner
---
**In short:** A Loan Repayment Repost reverses and re-posts a payment's ledger entries and goes from Draft to Completed; it has no reason or approval, and no role can cancel it.

## Before you start

⚠ Loan Repayment Repost is open to System Manager only. Use a test loan. Names in the screenshots are test records on the dev site.

## Steps

1. Type Loan Repayment Repost in the search bar and click Add.
2. Choose the **Loan** and the **Repost Date**.
3. In **Entries To Repost** add a row for each repayment to repost.

![The repost entered](/assets/lending_assistant/kb_img/J11/J11-S3-21_repayment-repost-filled.png)

4. Click **Save**, then **Submit**.

## What you should see

The document goes from Draft to Completed, and the repayment keeps its name and figures. Its ledger now shows the original entries cancelled, a reversing set and a new live set. The post-actions also catch the loan up to today.

![The repost Completed](/assets/lending_assistant/kb_img/J11/J11-S3-22_repayment-repost-completed.png)

## If it looks wrong

The BRD wants a wrong posting fixed safely (BR-LMS-169, covered), with these caveats:

- The doctype has permissions for System Manager only (read, write, create, submit, delete), and no role has Cancel, so the screen shows no Cancel button. A completed repost can be cancelled only by Administrator.
- It has no reason field and no approval: the same person creates and submits it.

See `bridge.BR-LMS-169`.
