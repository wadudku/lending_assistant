---
id: howto.report.check_restructure_report
type: howto
title: How to look for a Bangladesh Bank report of restructures and waivers
summary: "None of the Lending reports lists restructures, reschedules or waivers with a treatment; compliance builds the return from the Loan Restructure and Loan Repayment lists."
br_ids: [BR-LMS-188]
brd_section: 7.6
doctypes: [Loan Restructure, Loan Repayment]
dev_items: [D16]
journeys: [J6]
actions: ["Loan Restructure:check_report"]
fields: [Loan Restructure.Status, Loan Restructure.Restructure Type, Loan Restructure.Reason for Restructure, Loan Repayment.Repayment Type]
options: [Loan Restructure.Status=Approved, Loan Repayment.Repayment Type=Penalty Waiver]
menus: [Lending > Reports > Loan Outstanding Report]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/verification/walkthroughs/J6_walkthrough.md#stage-6"
  - "sources/verification/walkthroughs/J6_walkthrough.md#6.1"
related: [howto.loan_restructure.approve, bridge.BR-LMS-188, journey.J6, screen.loan_restructure, screen.loan_repayment]
version: 1
status: approved
approved_by: Owner
---
**In short:** None of the Lending reports lists restructures, reschedules or waivers with a treatment; compliance builds the return from the Loan Restructure and Loan Repayment lists.

## Before you start

⚠ This card is view only. You need read permission on the Lending reports, **Loan Restructure** and **Loan Repayment**. No screenshot was taken for this step in the walkthrough, so the card has none.

## Steps

1. Open the Lending reports: Loan Outstanding Report, Loan Statement of Account, Future and Past Cashflow Report, ALM Audit Report, Disbursement Analysis Report, Loan Repayment and Closure, and the Loan Security reports.
2. Look for a column or a report that lists restructures, reschedules or waivers with the treatment used.
3. As the workaround, open the Loan Restructure list and filter **Status** to Approved, grouping by **Restructure Type**. Open the Loan Repayment list and filter **Repayment Type** to the waiver types (Interest Waiver, Penalty Waiver, Charges Waiver). Export both lists to a spreadsheet.

## What you should see

None of the reports lists them, and there is no treatment field.

## If it looks wrong

The BRD wants restructures, reschedules and waivers reported to Bangladesh Bank with the treatment used (BR-LMS-188, not covered). Today compliance builds the return from the two exported lists, plus the Bangladesh Bank category kept in **Reason for Restructure**, written there by the officer as the verification's workaround for BR-LMS-182 (see `howto.loan_restructure.create`). The fix is D16 (ND-22): a restructure, reschedule and waiver report driven by a treatment field. See `bridge.BR-LMS-188`.
