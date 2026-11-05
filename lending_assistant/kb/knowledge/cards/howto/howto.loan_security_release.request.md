---
id: howto.loan_security_release.request
type: howto
title: How to request and approve the release of collateral
summary: "A release is requested on its own screen and approved by editing its Status; the request is checked alone against the pledged quantity, and the same user can request and approve."
br_ids: [BR-LMS-174, BR-LMS-232]
brd_section: 7.8
doctypes: [Loan Security Release]
dev_items: []
journeys: [J7, J9]
actions: ["Loan Security Release:request"]
fields: [Loan Security Release.Loan, Loan Security Release.Status]
options: [Loan Security Release.Status=Approved, Loan Security Release.Status=Requested]
menus: [Lending > Security Management > Loan Security Release]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J9/J9-S4-06_loanA-closure-date-after-approval.png, /assets/lending_assistant/kb_img/J7/J7-S5-06b_release-filled-rows.png, /assets/lending_assistant/kb_img/J7/J7-S5-06d_release-requested.png, /assets/lending_assistant/kb_img/J7/J7-S5-07a_release-approve-filled.png, /assets/lending_assistant/kb_img/J7/J7-S5-07b_release-approved.png, /assets/lending_assistant/kb_img/J7/J7-S5-08_gap-same-user-requested-and-approved.png]
sources:
  - "sources/verification/walkthroughs/J7_walkthrough.md#stage-5"
  - "sources/verification/walkthroughs/J7_walkthrough.md#5.2"
  - "sources/verification/walkthroughs/J7_walkthrough.md#5.3"
  - "sources/verification/walkthroughs/J7_walkthrough.md#5.4"
  - "sources/verification/walkthroughs/J7_walkthrough.md#5.5"
  - "sources/verification/walkthroughs/J7_walkthrough.md#5.6"
  - "sources/verification/walkthroughs/J9_walkthrough.md#stage-4"
  - "sources/verification/walkthroughs/J9_walkthrough.md#4.1"
related: [howto.loan_security_assignment.pledge, howto.loan_repayment.close_loan, howto.loan_security_report.view, bridge.BR-LMS-174, journey.J7]
version: 1
status: approved
approved_by: Owner
---
**In short:** A release is requested on its own screen and approved by editing its Status; the request is checked alone against the pledged quantity, and the same user can request and approve.

## Before you start

⚠ You need permission to create and submit a **Loan Security Release**. Release only on a test loan. Names in the screenshots are test records on the dev site.

## Steps

1. Open Lending > Security Management > Loan Security Release and click + Add.
2. Pick the **Loan**. The applicant fills in. In Securities, remove the empty second row that the form adds, then enter the security and the quantity to release.
3. Click **Save**, then **Submit** and **Yes**. The status is Requested and the pledged quantity has not changed.
4. To approve, open the record, set **Status** to Approved and click Save. The pledged quantity then falls.

![The release rows](/assets/lending_assistant/kb_img/J7/J7-S5-06b_release-filled-rows.png)

![Requested](/assets/lending_assistant/kb_img/J7/J7-S5-06d_release-requested.png)

## What you should see

A request that would leave the loan above the loan-to-value limit is refused at the request, with a Loan To Value ratio breach message, and nothing is saved. A release within the excess is accepted as Requested and, once Approved, reduces the pledged quantity (the Loan Security Ledger report shows it, see `howto.loan_security_report.view`).

![Status set to Approved](/assets/lending_assistant/kb_img/J7/J7-S5-07a_release-approve-filled.png)

![Approved](/assets/lending_assistant/kb_img/J7/J7-S5-07b_release-approved.png)

## If it looks wrong

Maker and checker. The BRD wants a release only after approval by someone other than the requester (BR-LMS-174, partly covered). Approval is a status edit on the same document by anyone with write permission: the form has no approver, approval-date or reason field and no workflow (DEF-30, ND-30). The verification used one user for both steps, so it shows the missing control and not what a narrow role could do.

![The form: no approver or reason field](/assets/lending_assistant/kb_img/J7/J7-S5-08_gap-same-user-requested-and-approved.png)

Two requests together. Each request is checked against the quantity currently pledged and ignores other open requests, and approval re-runs no check. Two requests of 30 units, each valid alone, left the loan at 76.9% loan to value against a limit of 70%. The workaround is to approve one request at a time and read the Loan Security Exposure report between approvals.

API. The whitelisted method that releases a whole assignment needs only write permission and does no exposure check; the form's Release button calls it only when the status is Release Requested, which no code sets. An earlier verification loan had a 200-unit assignment released while 83,231 of principal was outstanding. After an approved **Loan Security Release**, the assignment still shows Pledged. See `bridge.BR-LMS-174`.

Closed loans. A loan can close while its collateral is still pledged, and approving a release on an already closed loan overwrites its closure date with the day of approval (BR-LMS-232, DEF-37, ND-35). Interest cut-off and any report by closure date then change after the fact.

![The closure date after approval](/assets/lending_assistant/kb_img/J9/J9-S4-06_loanA-closure-date-after-approval.png)
