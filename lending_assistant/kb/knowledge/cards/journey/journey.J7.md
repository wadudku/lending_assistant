---
id: journey.J7
type: journey
title: "Journey J7: collateral is pledged, watched and released"
summary: "A secured loan stays covered by its collateral, and security is released only when safe; Frappe Lending 16.5.1 has the screens, but its price, shortfall and release controls have gaps."
br_ids: []
brd_section: 7.8
doctypes: [Loan Security Type, Loan Security, Loan Security Price, Loan Security Assignment, Loan Security Shortfall, Loan Security Release]
dev_items: []
journeys: [J7]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/verification/journeys_verified.json#J7"
  - "sources/verification/walkthroughs/J7_walkthrough.md#stage-1"
  - "sources/verification/walkthroughs/J7_walkthrough.md#stage-2"
  - "sources/verification/walkthroughs/J7_walkthrough.md#stage-3"
  - "sources/verification/walkthroughs/J7_walkthrough.md#stage-4"
  - "sources/verification/walkthroughs/J7_walkthrough.md#stage-5"
  - "sources/verification/reqs.json#BR-LMS-172"
  - "sources/verification/reqs.json#BR-LMS-175"
related: [howto.loan_security_type.create, howto.loan_security.create, howto.loan_security_price.create, howto.loan_security_assignment.pledge, howto.loan_disbursement.create, howto.process_loan_security_shortfall.run, howto.loan_security_shortfall.top_up, howto.loan_security_release.request, howto.loan_security_report.view, screen.loan_security, screen.loan_security_assignment, screen.loan_security_shortfall]
version: 1
status: approved
approved_by: Owner
---
**In short:** A secured loan stays covered by its collateral, and security is released only when safe; Frappe Lending 16.5.1 has the screens, but its price, shortfall and release controls have gaps.

## The process in plain words

A secured loan is booked, for example with a fixed-deposit receipt pledged. The goal in the BRD is that every loan stays covered by its collateral and that security is released only when safe. Credit Administration's security officer registers the security, pledges it, watches its value, fixes a shortfall and releases part of it. The running story is Rahim's 100,000 loan at 14% over 12 months, secured by a fixed-deposit receipt whose price falls and then recovers.

## Stages

| Stage | Who | What happens | System side | BR ids |
|---|---|---|---|---|
| 1 Register the security | Security officer | Type, value, price history, haircut and eligible value | Loan Security Type, Loan Security, Loan Security Price; the secured flag and maximum amount are on the Loan. `howto.loan_security_type.create`, `howto.loan_security.create`, `howto.loan_security_price.create` | BR-LMS-170 |
| 2 Pledge it | Security officer | Pledge requested, then pledged; later release requested, then released | Loan Security Assignment (submit sets Pledged); release is a separate screen. `howto.loan_security_assignment.pledge`, `howto.loan_disbursement.create` | BR-LMS-171 |
| 3 Watch the value | System | A daily check of collateral value against what is owed | Process Loan Security Shortfall, whose Loan and Applicant fields are ignored. `howto.process_loan_security_shortfall.run` | BR-LMS-172 |
| 4 Fix a shortfall | Security officer | More security, a repayment or an approved exception, with an owner and due date | Loan Security Shortfall, with its Add Loan Security button. `howto.loan_security_shortfall.top_up` | BR-LMS-173 |
| 5 Release and report | Approver | Release only after an exposure check and approval; exposure reports | Loan Security Release (Requested, then Approved) and the collateral reports. `howto.loan_security_release.request`, `howto.loan_security_report.view` | BR-LMS-174, 175 |

## Gaps met on the way

- Stage 1: nested price rows and a haircut over 100% are accepted (DEF-29).
- Stage 2: a secured loan can be disbursed with no pledge, and the pledge is added on top of the typed limit (DEF-31).
- Stage 3: the nightly run flags every borrower with no collateral (DEF-32).
- Stage 4: a shortfall has no remedy, owner or due date (DEF-28), and a repayment made while it is Pending is booked twice (DEF-26).
- Stage 5: approval re-checks nothing, and the requester can approve (DEF-30).

## Outcome

Rahim's loan is disbursed and secured, with part of the collateral released after a price fall and recovery. The journey's verified requirement results are: covered for 175; partly covered for 170, 171, 172, 173 and 174.
