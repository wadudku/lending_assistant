---
id: howto.loan.view_grade
type: howto
title: How to read a loan's grade (SMA) and what can override it
summary: "The loan shows its days past due and grade from the company's bands; the only manual override is the NPA tick, and no history of grade changes is kept."
br_ids: [BR-LMS-191, BR-LMS-192]
brd_section: 7.9
doctypes: [Loan, Days Past Due Log]
dev_items: [D15]
journeys: [J4]
actions: ["Loan:view_grade"]
fields: [Loan.Days Past Due, Loan.Classification Code, Loan.Classification Name, Loan.Manual NPA]
options: []
menus: [Lending > Loan Management > Loan, Lending > Loan Management > DPD Log]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J4/J4-S2-03_dpd-log.png, /assets/lending_assistant/kb_img/J4/J4-S2-04_loan-grade-sma.png, /assets/lending_assistant/kb_img/J4/J4-S2-06_manual-npa-only-override.png, /assets/lending_assistant/kb_img/J4/J4-S2-07_no-grade-history-version.png, /assets/lending_assistant/kb_img/J4/J4-S1-11_accrual-0410-submitted.png, /assets/lending_assistant/kb_img/J4/J4-S1-12_demand-0510-submitted.png]
sources:
  - "sources/verification/walkthroughs/J4_walkthrough.md#stage-2"
  - "sources/verification/walkthroughs/J4_walkthrough.md#2.1"
  - "sources/verification/walkthroughs/J4_walkthrough.md#2.2"
  - "sources/verification/walkthroughs/J4_walkthrough.md#2.3"
  - "sources/verification/walkthroughs/J4_walkthrough.md#2.6"
related: [howto.process_loan_classification.run, howto.days_past_due_log.view, howto.company.view_loan_settings, bridge.BR-LMS-191, bridge.BR-LMS-192, journey.J4, screen.loan, screen.days_past_due_log]
version: 1
status: approved
approved_by: Owner
---
**In short:** The loan shows its days past due and grade from the company's bands; the only manual override is the NPA tick, and no history of grade changes is kept.

## Before you start

⚠ This card is view only. You need read permission on **Loan** and **Days Past Due Log**. The walkthrough first ran classification for day 60 with Force Update DPD in Loan ticked (`howto.process_loan_classification.run`). Names in the screenshots are test records on the dev site.

## Steps

1. Open the loan and read Days Past Due, Classification Code and Classification Name under Loan Classification Details. They are read-only.
2. Open Lending > Loan Management > DPD Log and filter by loan to see the dated rows.
3. For the bands behind the grade, see `howto.company.view_loan_settings`.
4. Open the Totals tab to see the manual controls.

![Days past due log rows](/assets/lending_assistant/kb_img/J4/J4-S2-03_dpd-log.png)

## What you should see

After day 60 the loan shows Days Past Due 60, code SMA and Special Mention Account, and is not marked NPA. The bands used were STD 0–59, SMA 60–89, SS 90–179, DF 180–364, BL 365–1079 and WO from 1080. The DPD log holds only the days that were run; the nightly job writes one row a day. Billing carries on meanwhile: the walkthrough billed the third EMI the same way as the first two.

![The loan at SMA](/assets/lending_assistant/kb_img/J4/J4-S2-04_loan-grade-sma.png)

## If it looks wrong

Override. The BRD wants a manual override of the grade with a reason and an approver (BR-LMS-191, partly covered). The only manual control is Manual NPA (and Unmark NPA) on the Totals tab: there is no field for a grade, a reason, an approver or an expiry, and the grade cannot be changed after submit. The walkthrough did not tick Manual NPA, because removing it later leaves its suspense in place (DEF-13). The workaround is to record the decision outside the system and, only if NPA is wanted, tick Manual NPA and add a comment on the loan; the fix is ND-15 (D15).

![Totals: Manual NPA is the only override](/assets/lending_assistant/kb_img/J4/J4-S2-06_manual-npa-only-override.png)

History. The move from STD to SMA left no trace: the loan's Version list has one row, because the grade is written without a version, and the Loan NPA Log holds NPA only (BR-LMS-192, partly covered). See `bridge.BR-LMS-191` and `bridge.BR-LMS-192`.

![Version list: no grade change](/assets/lending_assistant/kb_img/J4/J4-S2-07_no-grade-history-version.png)

![Accrual for EMI 3](/assets/lending_assistant/kb_img/J4/J4-S1-11_accrual-0410-submitted.png)

![Demand for EMI 3](/assets/lending_assistant/kb_img/J4/J4-S1-12_demand-0510-submitted.png)
