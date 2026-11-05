---
id: howto.loan_security_assignment.pledge
type: howto
title: How to book a secured loan and pledge collateral to it
summary: "Booking the loan with Is Secured Loan ticked comes first, then a Loan Security Assignment pledges the units; submitting it sets Pledged at once, and the pledge is added on top of the typed Maximum Loan Amount."
br_ids: [BR-LMS-171, BR-LMS-170]
brd_section: 7.8
doctypes: [Loan Security Assignment, Loan]
dev_items: []
journeys: [J7]
actions: ["Loan Security Assignment:pledge"]
fields: [Loan.Is Secured Loan, Loan.Maximum Loan Amount, Loan Security Assignment.Loan, Loan Security Assignment.Applicant, Loan Security Assignment.Status]
options: [Loan Security Assignment.Status=Pledge Requested, Loan Security Assignment.Status=Pledged]
menus: [Lending > Security Management > Loan Security Assignment]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J7/J7-S2-03_loan-filled-secured.png, /assets/lending_assistant/kb_img/J7/J7-S2-06_pledge-filled-rows.png, /assets/lending_assistant/kb_img/J7/J7-S2-07_pledge-saved-requested.png, /assets/lending_assistant/kb_img/J7/J7-S2-08_pledge-submitted-pledged.png, /assets/lending_assistant/kb_img/J7/J7-S2-09_pledge-toolbar-no-release.png, /assets/lending_assistant/kb_img/J7/J7-S2-10_gap-max-loan-320000.png]
sources:
  - "sources/verification/walkthroughs/J7_walkthrough.md#stage-2"
  - "sources/verification/walkthroughs/J7_walkthrough.md#2.1"
  - "sources/verification/walkthroughs/J7_walkthrough.md#2.2"
  - "sources/verification/walkthroughs/J7_walkthrough.md#2.3"
  - "sources/verification/walkthroughs/J7_walkthrough.md#2.4"
related: [howto.loan.create, howto.loan_security_price.create, howto.loan_disbursement.create, bridge.BR-LMS-171c, journey.J7, screen.loan_security_assignment, screen.loan]
version: 1
status: approved
approved_by: Owner
---
**In short:** Booking the loan with Is Secured Loan ticked comes first, then a Loan Security Assignment pledges the units; submitting it sets Pledged at once, and the pledge is added on top of the typed Maximum Loan Amount.

## Before you start

⚠ You need permission to create a **Loan** and a **Loan Security Assignment**. The security and its price must exist (`howto.loan_security.create`, `howto.loan_security_price.create`). A product has no "secured" setting: security is set on the loan. Names in the screenshots are test records on the dev site.

## Steps

1. Book the loan as in `howto.loan.create`, but leave Auto create disbursement on loan booking off, because the pledge comes first. Tick **Is Secured Loan** and enter **Maximum Loan Amount**, which is mandatory for a secured loan with no Loan Application. Save and Submit: the loan is Sanctioned and nothing is disbursed.
2. Open Lending > Security Management > Loan Security Assignment and click + Add. Pick the **Loan**; the **Applicant** fills in. In Securities, add a row with the security and the quantity (200 units in the walkthrough).
3. Click **Save**. The status is Pledge Requested.
4. Click **Submit**, then **Yes**.

![The loan's secured fields](/assets/lending_assistant/kb_img/J7/J7-S2-03_loan-filled-secured.png)

![Securities row](/assets/lending_assistant/kb_img/J7/J7-S2-06_pledge-filled-rows.png)

## What you should see

The row fills the haircut, the price, the amount (200,000) and the post-haircut amount (160,000). After Submit the assignment is Pledged with no approval step, and a Sanctioned Loan Amount record is created as a side effect. Release is a separate screen (`howto.loan_security_release.request`).

![Pledge Requested after Save](/assets/lending_assistant/kb_img/J7/J7-S2-07_pledge-saved-requested.png)

![Pledged after Submit](/assets/lending_assistant/kb_img/J7/J7-S2-08_pledge-submitted-pledged.png)

## If it looks wrong

Statuses. The status list has seven values, which the verification report says match the BRD. The app sets Pledged on submit and Cancelled on cancel, and only the release API sets Released; the toolbar shows a Release button only for Release Requested, which no code sets (BR-LMS-171, partly covered; ND-30).

![No Release button on a Pledged assignment](/assets/lending_assistant/kb_img/J7/J7-S2-09_pledge-toolbar-no-release.png)

Limit. The loan's Maximum Loan Amount rose from the typed 160,000 to 320,000: the pledge's post-haircut value is added to what was typed (DEF-31, ND-31). The workaround is to type 0 where the form allows, or to read the Maximum Loan Value on the assignment. See `bridge.BR-LMS-171c`.

![Maximum Loan Amount after the pledge](/assets/lending_assistant/kb_img/J7/J7-S2-10_gap-max-loan-320000.png)
