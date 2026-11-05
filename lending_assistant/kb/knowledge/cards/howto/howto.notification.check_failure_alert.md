---
id: howto.notification.check_failure_alert
type: howto
title: How to check whether anyone is told when a job fails
summary: "Nobody is told: the stock Error Log notification is disabled, and a failed batch sends no email or notification, because the job that starts it still shows Complete."
br_ids: [BR-LMS-225]
brd_section: 7.13
doctypes: [Notification, Error Log, Scheduled Job Log]
dev_items: []
journeys: [J11]
actions: ["Notification:check_failure_alert"]
fields: []
options: []
menus: []
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J11/J11-S2-04_notification-list.png, /assets/lending_assistant/kb_img/J11/J11-S2-05_email-queue.png]
sources:
  - "sources/verification/walkthroughs/J11_walkthrough.md#2.2"
related: [howto.error_log.view_and_assign, howto.notification.check_borrower_notice, bridge.BR-LMS-225, journey.J11]
version: 1
status: approved
approved_by: Owner
---
**In short:** Nobody is told: the stock Error Log notification is disabled, and a failed batch sends no email or notification, because the job that starts it still shows Complete.

## Before you start

⚠ This card is view only. You need read permission on the **Scheduled Job Log**, **Notification** and Email Queue lists. Type each name in the search bar. Names in the screenshots are test records on the dev site.

## Steps

1. After a failed batch, open the Scheduled Job Log and read the status of the job that started it.
2. Open the Notification list and find the notification on **Error Log**.

![The Notification list](/assets/lending_assistant/kb_img/J11/J11-S2-04_notification-list.png)

3. Open the Email Queue and look for new mails.

![The Email Queue](/assets/lending_assistant/kb_img/J11/J11-S2-05_email-queue.png)

## What you should see

The Scheduled Job Log shows the job that starts the batch as Complete, because the work for each loan runs in the background and the failure is logged only in the Error Log. The stock notification on Error Log exists but is disabled. No new mail is queued and no notification log entry is created.

## If it looks wrong

The BRD wants an alert by email and SMS when a job fails, and a stronger one when it fails several times in a row, naming the loan (BR-LMS-225, partly covered). Nothing is sent today. Enabling the stock notification would mail every new Error Log, with only the method as the subject; there is no SMS, no repeat rule and no loan in the subject.

The workaround is that a person opens the Error Log every morning (`howto.error_log.view_and_assign`). The fix is ND-44, alert rules per job, with channel, escalation and the loan in the message. See `bridge.BR-LMS-225`.
