---
id: howto.process_loan_demand.rerun_failed
type: howto
title: How to re-run a batch that failed for some loans
summary: "A Process Loan Demand run only ever shows Submitted; a failed night is found in the Error Log, and re-running after the fix bills each loan once, with no duplicates."
br_ids: [BR-LMS-223, BR-LMS-135]
brd_section: 7.13
doctypes: [Process Loan Demand, Process Loan Interest Accrual, Loan Product]
dev_items: []
journeys: [J11]
actions: ["Process Loan Demand:rerun"]
fields: [Process Loan Demand.Posting Date, Process Loan Demand.Loan Product, Process Loan Demand.Loan, Process Loan Demand.Loan Disbursement]
options: []
menus: [Lending > Setup > Loan Product]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J11/J11-S1-03_process-demand-form-no-status.png, /assets/lending_assistant/kb_img/J11/J11-S1-07_process-demand-still-submitted.png, /assets/lending_assistant/kb_img/J11/J11-S1-08_process-demand-rerun-submitted.png, /assets/lending_assistant/kb_img/J11/J11-S1-09_loan-B-demands-after-rerun.png]
sources:
  - "sources/verification/walkthroughs/J11_walkthrough.md#stage-1"
  - "sources/verification/walkthroughs/J11_walkthrough.md#1.2"
  - "sources/verification/walkthroughs/J11_walkthrough.md#1.3"
  - "sources/verification/walkthroughs/J11_walkthrough.md#1.4"
related: [howto.process_loan_demand.run, howto.error_log.view_and_assign, howto.loan_product.duplicate, bridge.BR-LMS-223, bridge.BR-LMS-135, journey.J11, screen.loan_product]
version: 1
status: approved
approved_by: Owner
---
**In short:** A Process Loan Demand run only ever shows Submitted; a failed night is found in the Error Log, and re-running after the fix bills each loan once, with no duplicates.

## Before you start

⚠ You need permission to submit a **Process Loan Demand**. Names in the screenshots are test records on the dev site.

## Steps

1. Open Lending > Process Loan Demand and click Add. The form has **Posting Date**, **Loan Product**, **Loan** and **Loan Disbursement**, and no status or count.

![The Process Loan Demand form](/assets/lending_assistant/kb_img/J11/J11-S1-03_process-demand-form-no-status.png)

2. After a night when bills are missing, open the Error Log (`howto.error_log.view_and_assign`) and fix the cause named there, for example a blank account on the Loan Product.

![The run is still Submitted](/assets/lending_assistant/kb_img/J11/J11-S1-07_process-demand-still-submitted.png)

3. Add a new Process Loan Demand with the same **Posting Date** and the **Loan Product**, then click **Save** and **Submit**.

![The re-run](/assets/lending_assistant/kb_img/J11/J11-S1-08_process-demand-rerun-submitted.png)

## What you should see

After a few seconds each loan has one interest bill and one principal bill, with no duplicates and no half bill from the failed run. Each loan is tried in its own transaction: a failure is logged and rolled back, and the next loan is still tried. A run scoped to a single loan behaves differently, because the error shows on screen and nothing is logged.

![The bills after the re-run](/assets/lending_assistant/kb_img/J11/J11-S1-09_loan-B-demands-after-rerun.png)

## If it looks wrong

The BRD wants every batch to show a status and a per-loan result (BR-LMS-223, partly covered). Of the 11 runner doctypes only Loan Repayment Repost has a status; the others show Submitted and nothing else. Restart after a failure works (BR-LMS-135). The workaround is to open the Error Log each morning and compare the Loan Demand list with the open-loan list by eye. The fix is ND-43, a status, loan counts and a per-loan result table on every Process doctype. See `bridge.BR-LMS-223`.
