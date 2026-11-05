---
id: howto.loan_security_shortfall.top_up
type: howto
title: How to top up the pledge from a shortfall record
summary: "The shortfall record's Add Loan Security button opens a new pledge for the loan, and the app reduces the record itself, but the record has no remedy, owner or due date."
br_ids: [BR-LMS-173]
brd_section: 7.8
doctypes: [Loan Security Shortfall, Loan Security Assignment]
dev_items: []
journeys: [J7]
actions: ["Loan Security Shortfall:top_up"]
fields: []
options: []
menus: [Lending > Security Management > Loan Security Assignment]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J7/J7-S4-01_shortfall-add-security-button.png, /assets/lending_assistant/kb_img/J7/J7-S4-02a_topup-filled.png, /assets/lending_assistant/kb_img/J7/J7-S4-02b_topup-pledged.png, /assets/lending_assistant/kb_img/J7/J7-S4-02c_shortfall-after-topup.png, /assets/lending_assistant/kb_img/J7/J7-S4-05_gap-applicant-record-stays-pending.png, /assets/lending_assistant/kb_img/J7/J7-S4-06_gap-record-timeline-no-audit.png]
sources:
  - "sources/verification/walkthroughs/J7_walkthrough.md#stage-4"
  - "sources/verification/walkthroughs/J7_walkthrough.md#4.1"
  - "sources/verification/walkthroughs/J7_walkthrough.md#4.2"
  - "sources/verification/walkthroughs/J7_walkthrough.md#4.3"
  - "sources/verification/walkthroughs/J7_walkthrough.md#4.4"
related: [howto.process_loan_security_shortfall.run, howto.loan_security_assignment.pledge, bridge.BR-LMS-173, journey.J7, screen.loan_security_shortfall, screen.loan_security_assignment]
version: 1
status: approved
approved_by: Owner
---
**In short:** The shortfall record's Add Loan Security button opens a new pledge for the loan, and the app reduces the record itself, but the record has no remedy, owner or due date.

## Before you start

⚠ You need permission to create a **Loan Security Assignment**. The shortfall record comes from `howto.process_loan_security_shortfall.run`. Names in the screenshots are test records on the dev site.

## Steps

1. Open the Pending loan-wise Loan Security Shortfall record and click Add Loan Security.
2. The new assignment opens with the loan and the applicant filled in. Add a row in Securities with the security and a quantity (20 units in the walkthrough, at a price of 600).
3. Click **Save**, then **Submit** and **Yes**.
4. Repeat until the loan is covered, running the check again between top-ups.

![The Add Loan Security button](/assets/lending_assistant/kb_img/J7/J7-S4-01_shortfall-add-security-button.png)

![First top-up entered](/assets/lending_assistant/kb_img/J7/J7-S4-02a_topup-filled.png)

## What you should see

The new assignment is Pledged and the app reduces the shortfall record by itself within seconds, with no run: 16,000 became 4,000. Re-running the check corrects the same record to 7,600 and overwrites its figures in place. After the second top-up the record is Completed, set by the app and not by a person.

![The top-up pledged](/assets/lending_assistant/kb_img/J7/J7-S4-02b_topup-pledged.png)

![The record after the top-up](/assets/lending_assistant/kb_img/J7/J7-S4-02c_shortfall-after-topup.png)

## If it looks wrong

The BRD wants a shortfall fixed with more security, a repayment or an approved exception, with an owner and a due date (BR-LMS-173, partly covered). The loan-wise record has ten fields and none for a remedy, owner, due date, exception or notes. The app deducts the pledge's full value, not its value after the LTV, so the figure after the first top-up (4,000) was lower than the real gap (7,600). A Completed record is never reopened, and the applicant-wise record stays Pending even when the loan is covered (DEF-28, ND-28). The history keeps one line for the overwrite, so earlier figures are lost.

![The applicant-wise record stays Pending](/assets/lending_assistant/kb_img/J7/J7-S4-05_gap-applicant-record-stays-pending.png)

![The record's timeline](/assets/lending_assistant/kb_img/J7/J7-S4-06_gap-record-timeline-no-audit.png)

Paying the shortfall down is the BRD's second remedy, and the verification found that a repayment made while a loan-wise record is Pending posts the principal and the bank debit twice (DEF-26, ND-26). The walkthrough therefore made no payment on the loan. See `bridge.BR-LMS-173`.
