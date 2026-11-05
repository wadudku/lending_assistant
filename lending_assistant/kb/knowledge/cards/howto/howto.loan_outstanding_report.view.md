---
id: howto.loan_outstanding_report.view
type: howto
title: How to see what a borrower owes (Loan Outstanding Report)
summary: "The report shows paid and outstanding principal for a loan as on a date, but has no penalty or charges columns, and no report reconciles interest or matches a payment end to end."
br_ids: [BR-LMS-132, BR-LMS-145]
brd_section: 7.5
doctypes: [Loan]
dev_items: [D7, D10, D13]
journeys: [J3]
actions: ["Loan:view_outstanding"]
fields: []
options: []
menus: [Lending > Reports > Loan Outstanding Report]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J3/J3-S5-01_outstanding-07-05-left.png, /assets/lending_assistant/kb_img/J3/J3-S5-02_outstanding-07-05-paid.png, /assets/lending_assistant/kb_img/J3/J3-S5-03_outstanding-07-05-right.png, /assets/lending_assistant/kb_img/J3/J3-S5-06_gap-no-interest-reconciliation-report.png]
sources:
  - "sources/verification/walkthroughs/J3_walkthrough.md#stage-5"
  - "sources/verification/walkthroughs/J3_walkthrough.md#5.1"
  - "sources/verification/walkthroughs/J3_walkthrough.md#5.2"
  - "sources/verification/walkthroughs/J3_walkthrough.md#5.3"
related: [howto.days_past_due_log.view, bridge.BR-LMS-132, bridge.BR-LMS-145, journey.J3, screen.loan]
version: 1
status: approved
approved_by: Owner
---
**In short:** The report shows paid and outstanding principal for a loan as on a date, but has no penalty or charges columns, and no report reconciles interest or matches a payment end to end.

## Before you start

⚠ This card is view only. You need read permission on the Loan Outstanding Report. The report is a script report, so the entries below are filters and columns of the report, not fields of a doctype. Names in the screenshots are test records on the dev site.

## Steps

1. Open Lending > Reports > Loan Outstanding Report.
2. Leave the company as it is. Set the As On Date and the Applicant Type, and pick the Loan.
3. Read the row, left to right.

![Loan and disbursement, as on the due date](/assets/lending_assistant/kb_img/J3/J3-S5-01_outstanding-07-05-left.png)

## What you should see

For e.g. Rahim's loan of 100,000 after the first EMI of 8,979: total principal paid 7,828.32, interest paid 1,150.68, principal outstanding 92,171.68, nothing overdue, 1 EMI raised and 1 paid, 12 months tenure, 14% rate.

![Paid and outstanding](/assets/lending_assistant/kb_img/J3/J3-S5-02_outstanding-07-05-paid.png)

![Overdue amounts and days past due](/assets/lending_assistant/kb_img/J3/J3-S5-03_outstanding-07-05-right.png)

The report counts billed demands only, and days past due and the instalment counts are the loan's current values, not values as on the date.

## If it looks wrong

Missing columns. There is no penalty column and no charges column. The BRD wants what is owed on a date in full, with the days past due as at that date (BR-LMS-132, partly covered). The verification names D7 (ND-8) as the fix, reading as-at-date values from the Days Past Due Log.

No reconciliation. The Lending reports list holds 11 reports, and none reconciles interest accrued, billed, paid and posted (BR-LMS-145, not covered; D10). In the walkthrough, 1,150.80 accrued against 1,150.68 billed, and nothing reports the 0.12 difference. See `bridge.BR-LMS-145`.

![The 11 lending reports: no interest reconciliation](/assets/lending_assistant/kb_img/J3/J3-S5-06_gap-no-interest-reconciliation-report.png)

No CBS feed. Payments made directly in the CBS do not flow in, and no report matches a CBS transaction to a repayment and the ledger (BR-LMS-170 and BR-LMS-171, both gaps needing the CBS link; D13). Each CBS payment is keyed by hand (`howto.loan_repayment.create`).
