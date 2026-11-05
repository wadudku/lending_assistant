---
id: howto.process_loan_security_shortfall.run
type: howto
title: How to check collateral cover and read the shortfall records
summary: "The shortfall check compares each loan with its collateral at the loan-to-value ratio; the form must be saved as a draft only, because submitting it covers every loan and customer."
br_ids: [BR-LMS-172]
brd_section: 7.8
doctypes: [Process Loan Security Shortfall, Loan Security Shortfall]
dev_items: []
journeys: [J7]
actions: ["Process Loan Security Shortfall:run"]
fields: []
options: []
menus: []
lending_version: 16.5.1
code_refs: []
images: [/assets/lending_assistant/kb_img/J7/J7-S3-01_process-form-filled.png, /assets/lending_assistant/kb_img/J7/J7-S3-02_process-form-saved-draft.png, /assets/lending_assistant/kb_img/J7/J7-S3-07_shortfall-list-two-records.png, /assets/lending_assistant/kb_img/J7/J7-S3-08_shortfall-loanwise-record.png, /assets/lending_assistant/kb_img/J7/J7-S3-09_shortfall-applicant-record.png]
sources:
  - "sources/verification/walkthroughs/J7_walkthrough.md#stage-3"
  - "sources/verification/walkthroughs/J7_walkthrough.md#3.1"
  - "sources/verification/walkthroughs/J7_walkthrough.md#3.2"
  - "sources/verification/walkthroughs/J7_walkthrough.md#3.4"
  - "sources/verification/walkthroughs/J7_walkthrough.md#3.5"
related: [howto.loan_security_price.create, howto.loan_security_shortfall.top_up, bridge.BR-LMS-172, journey.J7, screen.loan_security_shortfall]
version: 1
status: approved
approved_by: Owner
---
**In short:** The shortfall check compares each loan with its collateral at the loan-to-value ratio; the form must be saved as a draft only, because submitting it covers every loan and customer.

## Before you start

⚠ Do not submit a **Process Loan Security Shortfall** on a shared site. The walkthrough found that Submit ignores the Loan and Applicant fields and covers every loan and every customer, like the nightly job (DEF-27, DEF-32). The scheduler is paused on the dev site, and the walkthrough used the form only to save a draft and then called the check for one loan from the command line, which needs bench access. Names in the screenshots are test records.

## Steps

1. Type Process Loan Security Shortfall in the search bar and click + Add. The update time fills in. Pick the loan and the borrower.
2. Click **Save** and stop: do not submit.
3. Run the check for the one loan and borrower with the `check_for_ltv_shortfall` function (a bench command, as Administrator). While the collateral covers the loan, it makes no record.
4. After a price fall (`howto.loan_security_price.create`) run it again, then open the Loan Security Shortfall list and filter by the customer.

![The form, filled](/assets/lending_assistant/kb_img/J7/J7-S3-01_process-form-filled.png)

![Saved as a draft](/assets/lending_assistant/kb_img/J7/J7-S3-02_process-form-saved-draft.png)

## What you should see

After the price fell from 1,000 to 600, two Pending records appeared for the borrower's 100,000 loan: a loan-wise record and an applicant-wise record, both with a shortfall of 16,000. A hand check agrees: 100,000 less 120,000 × 70% is 16,000. The two records state different "security value" figures, because the applicant-wise one is already multiplied by 70%.

![The two records](/assets/lending_assistant/kb_img/J7/J7-S3-07_shortfall-list-two-records.png)

![The loan-wise record](/assets/lending_assistant/kb_img/J7/J7-S3-08_shortfall-loanwise-record.png)

![The applicant-wise record](/assets/lending_assistant/kb_img/J7/J7-S3-09_shortfall-applicant-record.png)

## If it looks wrong

The BRD wants an alert for a collateral shortfall (BR-LMS-172, partly covered). The Process form ignores its scope on Submit (ND-27); the workaround is the draft plus a scoped call. The nightly job also runs an applicant-wise pass that subtracts the pending principal of all a customer's loans from the customer's collateral without checking whether a loan is secured, so it would flag borrowers with no collateral (DEF-32, ND-27). See `bridge.BR-LMS-172`.
