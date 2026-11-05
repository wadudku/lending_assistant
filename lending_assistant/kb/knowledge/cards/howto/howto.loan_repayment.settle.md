---
id: howto.loan_repayment.settle
type: howto
title: How to settle a loan with a Partial or Full Settlement
summary: "A settlement is a Loan Repayment of type Partial Settlement or Full Settlement; a Full Settlement creates and submits its own Loan Write Off with nobody asked, and no offer record exists."
br_ids: [BR-LMS-114, BR-LMS-200, BR-LMS-201]
brd_section: 7.11
doctypes: [Loan Repayment, Loan Write Off, Loan Product]
dev_items: [D18, D8]
journeys: [J8]
actions: ["Loan Repayment:settle"]
fields: [Loan Repayment.Repayment Type, Loan Repayment.Value Date, Loan Repayment.Amount Paid, Loan Repayment.Reference Number, Loan Write Off.Is Settlement Write Off, Loan Write Off.Write Off Amount]
options: [Loan Repayment.Repayment Type=Partial Settlement, Loan Repayment.Repayment Type=Full Settlement]
menus: [Lending > Loan Management > Loan, Lending > Loan Management > Loan Write Off]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J8/J8-S1-3a_gap-no-doctype-settlement.png, /assets/lending_assistant/kb_img/J8/J8-S1-3b_gap-no-doctype-offer.png, /assets/lending_assistant/kb_img/J8/J8-S3-1a_partial-filled-top.png, /assets/lending_assistant/kb_img/J8/J8-S3-2a_full-filled-top.png, /assets/lending_assistant/kb_img/J8/J8-S3-3a_auto-write-off-list.png, /assets/lending_assistant/kb_img/J8/J8-S3-3b_auto-write-off-form.png]
sources:
  - "sources/verification/walkthroughs/J8_walkthrough.md#stage-3"
  - "sources/verification/walkthroughs/J8_walkthrough.md#3.1"
  - "sources/verification/walkthroughs/J8_walkthrough.md#3.2"
  - "sources/verification/walkthroughs/J8_walkthrough.md#3.3"
  - "sources/verification/walkthroughs/J8_walkthrough.md#3.4"
  - "sources/verification/walkthroughs/J8_walkthrough.md#1.2"
related: [howto.loan_repayment.get_payoff_figure, howto.workflow.check_approval_limits, howto.loan_write_off.create, bridge.BR-LMS-200, bridge.BR-LMS-114, journey.J8, screen.loan_repayment, screen.loan_write_off]
version: 1
status: approved
approved_by: Owner
---
**In short:** A settlement is a Loan Repayment of type Partial Settlement or Full Settlement; a Full Settlement creates and submits its own Loan Write Off with nobody asked, and no offer record exists.

## Before you start

⚠ You need permission to **Submit** a **Loan Repayment**. A settlement posts money and a write-off, so use a test loan. Names in the screenshots are test records on the dev site.

## Steps

1. Read the payoff figure first (`howto.loan_repayment.get_payoff_figure`). Write the offer outside the system, because no settlement or offer record exists.

![No document with Settlement in its name](/assets/lending_assistant/kb_img/J8/J8-S1-3a_gap-no-doctype-settlement.png)

![No document with Offer in its name](/assets/lending_assistant/kb_img/J8/J8-S1-3b_gap-no-doctype-offer.png)

2. On the loan click Create and choose Loan Repayment. Set **Repayment Type** to Partial Settlement, **Value Date**, **Amount Paid** and **Reference Number**.

![Partial Settlement entered](/assets/lending_assistant/kb_img/J8/J8-S3-1a_partial-filled-top.png)

3. Click **Save**, then **Submit** and **Yes**. The loan stays Disbursed.
4. For a Full Settlement repeat with **Repayment Type** Full Settlement and the agreed **Amount Paid**.

![Full Settlement entered](/assets/lending_assistant/kb_img/J8/J8-S3-2a_full-filled-top.png)

## What you should see

The Full Settlement is allocated by the settlement payment order (**Collection Offset Sequence for Settlement Collection**, from the product or else the Company), and the loan becomes Settled. On Submit the system creates and submits a **Loan Write Off** for the unpaid principal, with **Is Settlement Write Off** ticked.

![The write-off list for the loan](/assets/lending_assistant/kb_img/J8/J8-S3-3a_auto-write-off-list.png)

![The write-off the system created](/assets/lending_assistant/kb_img/J8/J8-S3-3b_auto-write-off-form.png)

## If it looks wrong

The BRD wants a settlement offer record, approval limits and held waivers (BR-LMS-200 and BR-LMS-201, partly covered). Here there is no offer record, and the write-off appears with no approver. Interest that was accrued but not yet billed is billed by the settlement itself (DEF-34). The suspense for interest that was collected in cash was released to Interest Waiver, an expense line, so Interest Income is understated by the same amount (DEF-34, ND-33). The fix is ND-32, a Loan Settlement record approved before the repayment. See `bridge.BR-LMS-200`.
