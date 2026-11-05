---
id: howto.report.check_partner_report
type: howto
title: How to check for a partner-wise report
summary: "There is no partner-wise report; the Lending reports are none of them split by partner, and only an API without a screen returns raw payout figures."
br_ids: [BR-LMS-214]
brd_section: 7.12
doctypes: [Loan Partner]
dev_items: [D19]
journeys: [J10]
actions: ["Loan Partner:check_report"]
fields: []
options: []
menus: []
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J10/J10-S5-01_lending-reports-list.png]
sources:
  - "sources/verification/walkthroughs/J10_walkthrough.md#stage-5"
related: [howto.general_ledger.view_partner_position, howto.loan.choose_co_lender, bridge.BR-LMS-214, journey.J10, screen.loan_partner]
version: 1
status: approved
approved_by: Owner
---
**In short:** There is no partner-wise report; the Lending reports are none of them split by partner, and only an API without a screen returns raw payout figures.

## Before you start

⚠ This is a read-only check. You need permission to read the Lending reports. Names in the screenshots are test records on the dev site.

## Steps

1. Open the Lending workspace and look at the Reports list.
2. Read the report names and look for one that groups by partner.

![The Lending reports list](/assets/lending_assistant/kb_img/J10/J10-S5-01_lending-reports-list.png)

## What you should see

The list shows 11 reports: Loan Repayment and Closure, Loan Security Status, Applicant-Wise Loan Security Exposure, Loan Security Exposure, ALM Audit, Loan Outstanding, Past Cashflow, Future Cashflow, Loan Security Ledger, Loan Statement of Account and Disbursement Analysis. None is partner-wise.

## If it looks wrong

The BRD wants, for each partner, what was disbursed, what was collected, the outstanding share, the overdue amount and how much of the guarantee has been used (BR-LMS-214, not covered). A method `get_colender_payout_details` exists in the code, with a posting date, and returns raw payable figures, but it has no screen.

The workaround is a General Ledger export (`howto.general_ledger.view_partner_position`) plus the Co Lender Schedule, joined in a spreadsheet. The fix is ND-40, a partner-wise report built on top of that method. See `bridge.BR-LMS-214`.
