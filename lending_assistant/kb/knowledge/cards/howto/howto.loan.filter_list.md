---
id: howto.loan.filter_list
type: howto
title: How to build a working list of loans with a filter
summary: "The Loan list can be filtered and the filter saved, which is the workaround for an overdue work list and for a repricing selection; the list has no arrears column."
br_ids: [BR-LMS-198, BR-LMS-150, BR-LMS-158]
brd_section: 7.9
doctypes: [Loan]
dev_items: [D11, D17]
journeys: [J4, J5]
actions: ["Loan:filter_list"]
fields: [Loan.Days Past Due, Loan.Loan Product, Loan.Status, Loan.Company]
options: [Loan.Status=Disbursed]
menus: [Lending > Loan Management > Loan]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J4/J4-S3-02_loan-list-filter-dpd.png, /assets/lending_assistant/kb_img/J4/J4-S3-03_save-filter-filled.png, /assets/lending_assistant/kb_img/J4/J4-S3-04_saved-filter-list.png, /assets/lending_assistant/kb_img/J5/J5-S2-01_loan-list-by-product.png]
sources:
  - "sources/verification/walkthroughs/J4_walkthrough.md#stage-3"
  - "sources/verification/walkthroughs/J4_walkthrough.md#3.2"
  - "sources/verification/walkthroughs/J5_walkthrough.md#stage-2"
  - "sources/verification/walkthroughs/J5_walkthrough.md#2.1"
related: [howto.loan.follow_up, bridge.BR-LMS-198, bridge.BR-LMS-150, bridge.BR-LMS-158, journey.J4, screen.loan]
version: 1
status: approved
approved_by: Owner
---
**In short:** The Loan list can be filtered and the filter saved, which is the workaround for an overdue work list and for a repricing selection; the list has no arrears column.

## Before you start

⚠ You need read permission on **Loan**. A saved filter is private to you unless you make it global. This is a workaround for two BRD needs that 16.5.1 has no screen for, described below. Names in the screenshots are test records on the dev site.

## Steps

1. Open Lending > Loan Management > Loan and set the Company quick filter.
2. For an overdue list: click Filters, add a filter on **Days Past Due**, choose Greater Than, enter 0 and apply it.
3. For a selection by product, filter on **Loan Product**, **Status** (Disbursed) and **Company**.
4. To keep the filter, open Saved Filters, choose Save Current Filter, enter a filter name, leave Is Global off and click Create.
5. To hand the list on, the list can be exported with the ⋯ menu.

![Filter: days past due above 0](/assets/lending_assistant/kb_img/J4/J4-S3-02_loan-list-filter-dpd.png)

![Saving the filter](/assets/lending_assistant/kb_img/J4/J4-S3-03_save-filter-filled.png)

## What you should see

Saved Filters now lists your filter. The list shows the loans that match, with no days past due or arrears column, so the officer opens each loan to see the numbers. The product filter showed the single loan on the product.

![The saved filter in the menu](/assets/lending_assistant/kb_img/J4/J4-S3-04_saved-filter-list.png)

![Loan list filtered by product](/assets/lending_assistant/kb_img/J5/J5-S2-01_loan-list-by-product.png)

## If it looks wrong

The BRD wants a collection case per overdue loan (BR-LMS-198, not covered; D17), and a repricing run that picks loans by product, segment, branch or list and skips fixed, closed, written-off and frozen loans (BR-LMS-150 and BR-LMS-158, both not covered; D11). The filter does neither: you must check Freeze Account and status loan by loan, and keep a list of skipped loans and why. See `bridge.BR-LMS-198`, `bridge.BR-LMS-150` and `bridge.BR-LMS-158`. For the collections workaround see `howto.loan.follow_up`.
