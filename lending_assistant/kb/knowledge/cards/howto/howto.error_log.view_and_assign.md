---
id: howto.error_log.view_and_assign
type: howto
title: How to find a failed batch in the Error Log and assign it
summary: "A failed batch shows as Error Log rows naming the loan; a row can be assigned to a person as a ToDo, but there is no work queue, closing note or escalation."
br_ids: [BR-LMS-225, BR-LMS-224]
brd_section: 7.13
doctypes: [Error Log, ToDo]
dev_items: []
journeys: [J11]
actions: ["Error Log:assign"]
fields: []
options: []
menus: []
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J11/J11-S2-01_error-log-list.png, /assets/lending_assistant/kb_img/J11/J11-S2-02_error-log-detail.png, /assets/lending_assistant/kb_img/J11/J11-S2-06_assign-dialog-filled.png, /assets/lending_assistant/kb_img/J11/J11-S2-08_todo-list.png]
sources:
  - "sources/verification/walkthroughs/J11_walkthrough.md#stage-2"
  - "sources/verification/walkthroughs/J11_walkthrough.md#2.1"
  - "sources/verification/walkthroughs/J11_walkthrough.md#2.3"
related: [howto.process_loan_demand.rerun_failed, howto.notification.check_failure_alert, bridge.BR-LMS-224, bridge.BR-LMS-225, journey.J11]
version: 1
status: approved
approved_by: Owner
---
**In short:** A failed batch shows as Error Log rows naming the loan; a row can be assigned to a person as a ToDo, but there is no work queue, closing note or escalation.

## Before you start

⚠ You need read permission on the **Error Log** and permission to create a **ToDo**. Type Error Log in the search bar, because it is not in the Lending menu. Names in the screenshots are test records on the dev site.

## Steps

1. Open the Error Log list. Failed demand batches appear as rows titled "Term Loan Demand Generation Error", with reference doctype Loan and the loan as the reference name.

![The Error Log list](/assets/lending_assistant/kb_img/J11/J11-S2-01_error-log-list.png)

2. Open a row and read the message. The page also shows occurrences, first seen and last seen for identical errors.

![An Error Log row](/assets/lending_assistant/kb_img/J11/J11-S2-02_error-log-detail.png)

3. In the sidebar click Assign, choose the person and add a comment, then click Add to ToDo.

![The assign dialog](/assets/lending_assistant/kb_img/J11/J11-S2-06_assign-dialog-filled.png)

## What you should see

A **ToDo** is created, Open and assigned to that person. Opening a row marks it Seen, and first seen gives the age.

![The ToDo list](/assets/lending_assistant/kb_img/J11/J11-S2-08_todo-list.png)

## If it looks wrong

The BRD wants a work queue for things that went wrong, each with an owner, an age, a closing note and escalation (BR-LMS-224, not covered; BR-LMS-225, partly covered). The Error Log is a technical log, not a business work queue. There is no closing note or status, no queue per kind of exception, no counts with the oldest age, no automatic assignment and no escalation.

The workaround is to assign each row by hand and keep a spreadsheet. The fix is ND-44, an Exceptions queue fed by the batches, with owner, status, note and ageing. See `bridge.BR-LMS-224`.
