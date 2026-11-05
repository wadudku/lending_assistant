---
id: howto.loan_repayment.check_cbs_reference
type: howto
title: How to check for a core banking reference on a posting
summary: "No Loan, Loan Repayment or Loan Write Off field holds a CBS balance or journal reference; the officer re-keys the posting into the CBS and notes its number by hand."
br_ids: [BR-LMS-204, BR-LMS-231]
brd_section: 7.11
doctypes: [Loan Write Off, Loan Repayment, Loan]
dev_items: [D13]
journeys: [J8, J9]
actions: ["Loan Repayment:check_cbs_reference"]
fields: [Loan Repayment.Reference Number, Loan Repayment.Reference Date, Loan Repayment.Manual Remarks]
options: []
menus: []
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J8/J8-S4-1a_gap-no-cbs-reference-write-off.png, /assets/lending_assistant/kb_img/J8/J8-S4-1b_gap-no-cbs-reference-repayment.png, /assets/lending_assistant/kb_img/J9/J9-S2-01_gap-loan-form-no-cbs-field.png, /assets/lending_assistant/kb_img/J9/J9-S2-02_gap-repayment-reference-fields-only.png]
sources:
  - "sources/verification/walkthroughs/J8_walkthrough.md#stage-4"
  - "sources/verification/walkthroughs/J9_walkthrough.md#stage-2"
related: [howto.loan_repayment.settle, howto.loan_write_off.create, bridge.BR-LMS-204, bridge.BR-LMS-231, journey.J8, journey.J9, screen.loan_write_off, screen.loan_repayment, screen.loan]
version: 1
status: approved
approved_by: Owner
---
**In short:** No Loan, Loan Repayment or Loan Write Off field holds a CBS balance or journal reference; the officer re-keys the posting into the CBS and notes its number by hand.

## Before you start

⚠ This is a read-only look at three forms. You need permission to read **Loan**, **Loan Repayment** and **Loan Write Off**. Names in the screenshots are test records on the dev site.

## Steps

1. Open a **Loan Write Off** and read its fields.
2. Open a **Loan Repayment** and read its reference fields.
3. Open a **Loan** and look for a field for a core banking balance or reference.

![Loan Write Off with no CBS reference](/assets/lending_assistant/kb_img/J8/J8-S4-1a_gap-no-cbs-reference-write-off.png)

![Loan Repayment with a reference number and date only](/assets/lending_assistant/kb_img/J8/J8-S4-1b_gap-no-cbs-reference-repayment.png)

## What you should see

A Loan Write Off has the loan, disbursement, applicant, product, company, dates, **Is NPA**, **Is Settlement Write Off**, cost center, write-off account and amount, and no CBS or journal reference. A Loan Repayment has only **Reference Number** and **Reference Date**, which the officer types. The Loan form has no CBS field either.

![The Loan form with no CBS field](/assets/lending_assistant/kb_img/J9/J9-S2-01_gap-loan-form-no-cbs-field.png)

![The repayment reference fields only](/assets/lending_assistant/kb_img/J9/J9-S2-02_gap-repayment-reference-fields-only.png)

## If it looks wrong

This is a gap that needs the CBS link, not a setting you can change (BR-LMS-204 and BR-LMS-231, both K). The BRD wants every settlement and write-off sent to the core banking system with its journal reference kept, and the CBS account and ledger checked before a closure is confirmed. Nothing in the closure or settlement path calls a core-banking service.

The workaround is that the officer checks the CBS by hand, re-keys each posting into it, and writes the CBS journal number or the check result in **Manual Remarks**. The fix is an RPA step that posts the journal or checks the balance and writes the result back. See `bridge.BR-LMS-204`.
