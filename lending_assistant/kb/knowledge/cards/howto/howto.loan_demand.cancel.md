---
id: howto.loan_demand.cancel
type: howto
title: How to cancel a wrong bill
summary: "An unpaid Loan Demand is cancelled in one click with no reason or approver; a partly paid one is blocked by its link to the repayment, with a Cancel All shortcut."
br_ids: [BR-LMS-133]
brd_section: 7.4
doctypes: [Loan Demand, Loan Repayment, Loan]
dev_items: []
journeys: [J11]
actions: ["Loan Demand:cancel"]
fields: [Loan.Days Past Due]
options: []
menus: [Lending > Loan Management > Loan Demand]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J11/J11-S3-04_cancel-dialog.png, /assets/lending_assistant/kb_img/J11/J11-S3-05_demand-B-interest-cancelled.png, /assets/lending_assistant/kb_img/J11/J11-S3-08_loan-B-dpd-after-cancel.png, /assets/lending_assistant/kb_img/J11/J11-S3-14_cancel-partly-paid-demand-linked-dialog.png]
sources:
  - "sources/verification/walkthroughs/J11_walkthrough.md#stage-3"
  - "sources/verification/walkthroughs/J11_walkthrough.md#3.1"
  - "sources/verification/walkthroughs/J11_walkthrough.md#3.2"
related: [howto.loan_repayment_repost.create, howto.loan_accrual_repost.create, bridge.BR-LMS-133, journey.J11, screen.loan_demand, screen.loan_repayment, screen.loan]
version: 1
status: approved
approved_by: Owner
---
**In short:** An unpaid Loan Demand is cancelled in one click with no reason or approver; a partly paid one is blocked by its link to the repayment, with a Cancel All shortcut.

## Before you start

⚠ Cancel on a **Loan Demand** is allowed to System Manager only, and it changes the borrower's bill. Use a test loan. Names in the screenshots are test records on the dev site.

## Steps

1. Open Lending > Loan Demand and open the unpaid bill, for example an interest bill.
2. Click Cancel and confirm with Yes. Do the same for the principal bill of that instalment.

![The cancel confirmation](/assets/lending_assistant/kb_img/J11/J11-S3-04_cancel-dialog.png)

3. To see the protection, open a partly paid bill and click Cancel.

![A partly paid bill is linked to a repayment](/assets/lending_assistant/kb_img/J11/J11-S3-14_cancel-partly-paid-demand-linked-dialog.png)

## What you should see

The unpaid bill stays visible as Cancelled and its ledger entries are reversed. The loan's **Days Past Due** falls to 0 until the next bill run.

![The cancelled bill](/assets/lending_assistant/kb_img/J11/J11-S3-05_demand-B-interest-cancelled.png)

![Days Past Due after the cancel](/assets/lending_assistant/kb_img/J11/J11-S3-08_loan-B-dpd-after-cancel.png)

For a partly paid bill the screen does not cancel it: it says the bill is linked to the **Loan Repayment** and offers Cancel All. Through the API the same attempt fails with a message that the demand is linked with the repayment.

## If it looks wrong

The BRD wants a bill never deleted or quietly changed, with a reason and an approver for every cancel (BR-LMS-133, partly covered). The confirmation asks only whether to cancel permanently. Who cancelled and why is not recorded: no reason, approver, version row or comment. The protection of a partly paid bill is the link between two records, not an approval, and Cancel All would cancel the payment in the same click, again with no reason or approver (DEF-47).

The workaround is a written approval outside the system and a comment typed by hand. The fix is ND-45, a mandatory reason, a maker-checker workflow on cancel, change tracking and Cancel limited to a named role. See `bridge.BR-LMS-133`.
