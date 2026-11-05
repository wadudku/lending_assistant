---
id: howto.process_loan_demand.run
type: howto
title: How to bill the EMI on the due date
summary: "The demand run turns the due schedule row into bills (demands) for interest and principal; the run form holds a date and optional filters, and shows no per-loan result."
br_ids: [BR-LMS-130, BR-LMS-135]
brd_section: 7.4
doctypes: [Process Loan Demand]
dev_items: [D9]
journeys: [J3, J4, J8, J11]
actions: ["Process Loan Demand:run"]
fields: [Process Loan Demand.Posting Date, Process Loan Demand.Loan]
options: []
menus: []
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J3/J3-S2-01_demand-run-filled.png, /assets/lending_assistant/kb_img/J3/J3-S2-02_demand-run-submitted.png, /assets/lending_assistant/kb_img/J3/J3-S2-07_gap-no-batch-result.png]
sources:
  - "sources/verification/walkthroughs/J3_walkthrough.md#stage-2"
  - "sources/verification/walkthroughs/J3_walkthrough.md#2.1"
  - "sources/verification/walkthroughs/J3_walkthrough.md#2.5"
related: [howto.loan_demand.view_emi_bill, howto.process_loan_interest_accrual.run, bridge.BR-LMS-130, bridge.BR-LMS-135, journey.J3]
version: 1
status: approved
approved_by: Owner
---
**In short:** The demand run turns the due schedule row into bills (demands) for interest and principal; the run form holds a date and optional filters, and shows no per-loan result.

## Before you start

⚠ You need permission to create and submit a **Process Loan Demand**. In production the daily scheduled job bills today's dues for all loans. The scheduler is paused on the dev site, so the walkthrough ran it from the form. Run the interest accrual first (`howto.process_loan_interest_accrual.run`). Names in the screenshots are test records.

## Steps

1. Type Process Loan Demand in the search bar and click + Add.
2. Enter **Posting Date**: the due date (for example the first EMI date).
3. Pick the **Loan**. Always set it, so the run touches only this loan.
4. Click **Save**, then **Submit** and **Yes**.

![The run, filled](/assets/lending_assistant/kb_img/J3/J3-S2-01_demand-run-filled.png)

## What you should see

The run is Submitted, with a link at the top to the demands it created (two in the walkthrough: interest and principal). This doctype has no naming series, so its name is a random string. The schedule row is now marked as having generated its demand (`howto.loan_demand.view_emi_bill`).

![The run, submitted, with its demand link](/assets/lending_assistant/kb_img/J3/J3-S2-02_demand-run-submitted.png)

## If it looks wrong

The form holds the date and optional Loan Product, Loan and Loan Disbursement filters, and links to the demands. There is no result per loan (succeeded, failed or skipped), no error column and no resume or retry action. The BRD wants the billing batch to report each loan's result and restart from where it stopped (BR-LMS-135, partly covered). A rerun for the same date is safe, and failures are found only in the Error Log. The verification names the fix as D9: a batch result table and a resume action. See `bridge.BR-LMS-135`.

![The run form: no result list, no resume](/assets/lending_assistant/kb_img/J3/J3-S2-07_gap-no-batch-result.png)
