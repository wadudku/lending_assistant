---
id: howto.loan_repayment.submit
type: howto
title: How to submit a payment and read how it was applied
summary: "Submitting a Draft repayment applies it to the open demands in the order of the payment order and posts the ledger entries; the split, the ledger and the payment types can all be read afterwards."
br_ids: [BR-LMS-162, BR-LMS-163, BR-LMS-165, BR-LMS-166]
brd_section: 7.7
doctypes: [Loan Repayment, Loan Repayment Detail, Bulk Repayment Log]
dev_items: [D9, D12]
journeys: [J3]
actions: ["Loan Repayment:submit"]
fields: [Loan Repayment.Total Interest Paid, Loan Repayment.Principal Amount Paid, Loan Repayment.Reference Number, Loan Repayment.Repayment Type]
options: [Loan Repayment.Repayment Type=Normal Repayment, Loan Repayment.Repayment Type=Pre Payment, Loan Repayment.Repayment Type=Loan Closure]
menus: [Lending > Loan Management > Loan Repayment]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J3/J3-S4-01_repayment-submitted.png, /assets/lending_assistant/kb_img/J3/J3-S4-02_repayment-paid-split.png, /assets/lending_assistant/kb_img/J3/J3-S4-03_repayment-details-interest-then-principal.png, /assets/lending_assistant/kb_img/J3/J3-S4-09_gl-repayment.png, /assets/lending_assistant/kb_img/J3/J3-S4-10_repayment-types.png, /assets/lending_assistant/kb_img/J3/J3-S4-11_gap-reference-not-unique.png, /assets/lending_assistant/kb_img/J3/J3-S4-12_gap-bulk-repayment-log-list.png]
sources:
  - "sources/verification/walkthroughs/J3_walkthrough.md#stage-4"
  - "sources/verification/walkthroughs/J3_walkthrough.md#4.1"
  - "sources/verification/walkthroughs/J3_walkthrough.md#4.5"
  - "sources/verification/walkthroughs/J3_walkthrough.md#4.6"
  - "sources/verification/walkthroughs/J3_walkthrough.md#4.7"
  - "sources/verification/walkthroughs/J3_walkthrough.md#4.8"
  - "sources/verification/verification_report.md#BR-LMS-163"
related: [howto.loan_repayment.create, howto.process_loan_classification.run, bridge.BR-LMS-162, bridge.BR-LMS-163, bridge.BR-LMS-165, bridge.BR-LMS-166, journey.J3, screen.loan_repayment]
version: 1
status: approved
approved_by: Owner
---
**In short:** Submitting a Draft repayment applies it to the open demands in the order of the payment order and posts the ledger entries; the split, the ledger and the payment types can all be read afterwards.

## Before you start

⚠ You need permission to **Submit** a **Loan Repayment**. The Draft comes from `howto.loan_repayment.create`. Names in the screenshots are test records on the dev site.

## Steps

1. Open the Draft repayment.
2. Click **Submit**, then **Yes**.
3. Read **Total Interest Paid** and **Principal Amount Paid**, then open the Repayment Details table.
4. To see the accounting, open the General Ledger report (Accounting > General Ledger) and filter by the repayment's voucher number.
5. To see the payment types, open a new repayment and open the **Repayment Type** list.

![Repayment submitted](/assets/lending_assistant/kb_img/J3/J3-S4-01_repayment-submitted.png)

## What you should see

The status is Submitted. In the walkthrough's payment of 8,979, the split was interest 1,150.68 then principal 7,828.32, and both demands showed nothing outstanding. The rows follow the product's payment order (`howto.loan_demand_offset_order.create`).

![Paid: interest and principal](/assets/lending_assistant/kb_img/J3/J3-S4-02_repayment-paid-split.png)

![Repayment Details: interest first, then principal](/assets/lending_assistant/kb_img/J3/J3-S4-03_repayment-details-interest-then-principal.png)

The ledger shows a debit to the collection bank and credits to the loan portfolio and Interest Receivable, balanced. The entries are dated the day of posting, not the value date. The fix is ND-12.

![Ledger entries](/assets/lending_assistant/kb_img/J3/J3-S4-09_gl-repayment.png)

The Repayment Type list holds 20 types, including Normal Repayment, the waivers, Advance Payment, Pre Payment, Loan Closure, the settlements, write-off recovery and the capitalizations (BR-LMS-165, covered). Do not use Pre Payment on a loan you want to keep unchanged: it restructures the loan.

![The 20 repayment types](/assets/lending_assistant/kb_img/J3/J3-S4-10_repayment-types.png)

## If it looks wrong

Duplicate CBS reference. Reference Number is a plain text field with no uniqueness rule. The BRD wants each CBS payment applied once only (BR-LMS-162, not covered). In the verification a Normal and a Pre Payment with the same reference were both accepted and posted. The workaround is to search Loan Repayment by Reference Number before keying; the fix is ND-6. See `bridge.BR-LMS-162`.

![Reference Number is not unique](/assets/lending_assistant/kb_img/J3/J3-S4-11_gap-reference-not-unique.png)

Bulk payments. There is no upload screen: the Bulk Repayment Log lists runs of the payment API only, and only loan existence is checked first (BR-LMS-166, partly covered; ND-7, D9). See `bridge.BR-LMS-166`.

![Bulk Repayment Log list](/assets/lending_assistant/kb_img/J3/J3-S4-12_gap-bulk-repayment-log-list.png)
