---
id: howto.loan_security_report.view
type: howto
title: How to read the four collateral reports
summary: "Four reports cover collateral: status, exposure, applicant-wise exposure and ledger; only the exposure reports net out releases, and none shows coverage or shortfalls."
br_ids: [BR-LMS-175]
brd_section: 7.8
doctypes: [Loan Security Assignment, Loan Security Release]
dev_items: []
journeys: [J7]
actions: ["Loan Security Assignment:view_reports"]
fields: []
options: []
menus: [Lending > Reports > Loan Security Status, Lending > Reports > Loan Security Exposure, Lending > Reports > Applicant-Wise Loan Security Exposure]
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J7/J7-S5-13_report-status.png, /assets/lending_assistant/kb_img/J7/J7-S5-14_report-exposure.png, /assets/lending_assistant/kb_img/J7/J7-S5-15_report-applicant-exposure.png, /assets/lending_assistant/kb_img/J7/J7-S5-16_report-ledger.png, /assets/lending_assistant/kb_img/J7/J7-S5-17_gap-report-list-security.png]
sources:
  - "sources/verification/walkthroughs/J7_walkthrough.md#5.7"
  - "sources/verification/walkthroughs/J7_walkthrough.md#5.8"
related: [howto.loan_security_release.request, bridge.BR-LMS-175, journey.J7, screen.loan_security_assignment]
version: 1
status: approved
approved_by: Owner
---
**In short:** Four reports cover collateral: status, exposure, applicant-wise exposure and ledger; only the exposure reports net out releases, and none shows coverage or shortfalls.

## Before you start

⚠ This card is view only. You need read permission on the reports. They are script reports, so their filters and columns are not doctype fields. Names in the screenshots are test records on the dev site.

## Steps

1. Open Lending > Reports and choose Loan Security Status, Loan Security Exposure or Applicant-Wise Loan Security Exposure, and set the company. The fourth, Loan Security Ledger, is opened by searching its name.
2. Filter by applicant for the status report and by loan for the ledger.
3. Read each report as in the table below.

## What you should see

For e.g. Rahim's pledged FDR after the releases:

| Report | What it shows |
|---|---|
| Loan Security Status | the three pledges, each still Pledged, 240 units in all. It is gross: released units are not netted, and each row is valued at the price on its pledge day |
| Loan Security Exposure | 130 units at 1,000, worth 130,000, net of releases, with the share of the portfolio |
| Applicant-Wise Loan Security Exposure | the borrower's 130 units and 130,000 |
| Loan Security Ledger | two rows, one for the pledges (240) and one for the releases (110), each dated at the first event of its kind: not a movement ledger |

![Status report](/assets/lending_assistant/kb_img/J7/J7-S5-13_report-status.png)

![Exposure report](/assets/lending_assistant/kb_img/J7/J7-S5-14_report-exposure.png)

![Applicant-wise exposure](/assets/lending_assistant/kb_img/J7/J7-S5-15_report-applicant-exposure.png)

![Ledger report](/assets/lending_assistant/kb_img/J7/J7-S5-16_report-ledger.png)

## If it looks wrong

The BRD's reports include coverage (loan outstanding against collateral value against the LTV) and the shortfall list with age and remedy (BR-LMS-175, covered in the verification). Searching the report list for "Security" finds the four reports, and none of them shows coverage. The only view of shortfalls is the Loan Security Shortfall list (`howto.process_loan_security_shortfall.run`), and nothing shows a loan above its limit until a shortfall check is run (ND-31). See `bridge.BR-LMS-175`.

![The report list filtered on Security](/assets/lending_assistant/kb_img/J7/J7-S5-17_gap-report-list-security.png)
