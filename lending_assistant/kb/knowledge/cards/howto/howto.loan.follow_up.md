---
id: howto.loan.follow_up
type: howto
title: How to chase an overdue loan without a collections screen
summary: "The collections module of the BRD does not exist in 16.5.1; the workaround is a saved overdue list, an assignment with a follow-up date, and comments on the loan."
br_ids: [BR-LMS-198]
brd_section: 7.9
doctypes: [Loan, ToDo]
dev_items: [D17]
journeys: [J4]
actions: ["Loan:follow_up"]
fields: []
options: []
menus: [Lending > Loan Management > Loan]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J4/J4-S3-01_no-collection-case.png]
sources:
  - "sources/verification/walkthroughs/J4_walkthrough.md#stage-3"
  - "sources/verification/walkthroughs/J4_walkthrough.md#3.1"
  - "sources/verification/walkthroughs/J4_walkthrough.md#3.3"
  - "sources/verification/walkthroughs/J4_walkthrough.md#3.4"
  - "sources/verification/walkthroughs/J4_walkthrough.md#3.5"
related: [howto.loan.filter_list, bridge.BR-LMS-198, journey.J4, screen.loan]
version: 1
status: approved
approved_by: Owner
---
**In short:** The collections module of the BRD does not exist in 16.5.1; the workaround is a saved overdue list, an assignment with a follow-up date, and comments on the loan.

## Before you start

⚠ You need permission to assign and comment on a **Loan**. Assign only to yourself while testing. The screens for this workaround show the user's name, so the card has no screenshots of them. In the walkthrough the user was a loan officer working through a list of overdue loans.

## Steps

1. Build the overdue list as in `howto.loan.filter_list`.
2. Open a loan and use Assign + in the sidebar. Tick Assign to me, add a short comment about the case and click Add. A ToDo linked to the loan is created. A "complete by" date typed in this dialog was not taken in the walkthrough: the ToDo got today's date.
3. Open the ToDo from the sidebar, set its Complete By date to the follow-up date and click Save. It then appears in your ToDo list.
4. Back on the loan, type the call and the promise in the Comments box at the bottom and click Comment, for example "called the borrower, promised to pay two EMIs by the 10th".

## What you should see

The sidebar shows the loan as assigned to you, the ToDo is open with the follow-up date, and the comment sits on the loan's Activity timeline. This is free text. Nothing tracks whether the promise is kept, and nothing escalates when it is broken.

## If it looks wrong

The BRD wants a collection case per overdue loan, with calls, promises to pay, follow-ups, dunning and escalation to recovery or legal (BR-LMS-198, not covered). The walkthrough found that Collection Case, Collection Activity, Promise to Pay, Dunning Rule and Process Collection Dunning do not exist in 16.5.1: they exist in develop only, and opening the Collection Case page answers "not found". ERPNext's own Dunning works on Sales Invoices, not on loan demands. The verification names D17 as the fix: build a collections module, or back-port develop's. See `bridge.BR-LMS-198`.

![Collection Case: page not found](/assets/lending_assistant/kb_img/J4/J4-S3-01_no-collection-case.png)
