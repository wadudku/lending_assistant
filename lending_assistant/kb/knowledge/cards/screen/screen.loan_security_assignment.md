---
id: screen.loan_security_assignment
type: screen
title: "Screen: Loan Security Assignment"
summary: "The Loan Security Assignment screen records a pledge: which securities, in what quantity, are pledged to a borrower or a loan."
br_ids: [BR-LMS-171, BR-LMS-174]
brd_section: 7.8
doctypes: [Loan Security Assignment]
dev_items: []
fields: [Loan Security Assignment.Applicant, Loan Security Assignment.Loan, Loan Security Assignment.Status, Loan Security Assignment.Total Security Value, Loan Security Assignment.Maximum Loan Value, Loan Security Assignment.Securities, Loan Security Assignment.Pledge Time, Loan Security Assignment.Release Time]
options: [Loan Security Assignment.Status=Pledge Requested, Loan Security Assignment.Status=Pledged, Loan Security Assignment.Status=Release Requested, Loan Security Assignment.Status=Released, Loan Security Assignment.Status=Unpledged, Loan Security Assignment.Status=Repossessed, Loan Security Assignment.Status=Cancelled]
menus: [Lending > Security Management > Loan Security Assignment]
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_security_assignment/loan_security_assignment.json, lending/loan_management/doctype/loan_security_assignment/loan_security_assignment.py]
images: [/assets/lending_assistant/kb_img/J7/J7-S2-08_pledge-submitted-pledged.png, /assets/lending_assistant/kb_img/J7/J7-S2-09_pledge-toolbar-no-release.png]
sources:
  - "sources/verification/walkthroughs/J7_walkthrough.md#stage-2"
  - "sources/verification/walkthroughs/J7_walkthrough.md#2.2"
  - "sources/verification/walkthroughs/J7_walkthrough.md#2.3"
  - "sources/verification/walkthroughs/J7_walkthrough.md#2.4"
  - "sources/verification/verification_report.md#BR-LMS-171c"
  - "sources/verification/verification_report.md#BR-LMS-174"
related: [screen.loan, screen.loan_security, screen.loan_disbursement, brd_section.7.8, bridge.BR-LMS-171c, bridge.BR-LMS-174]
version: 1
status: approved
approved_by: Owner
---
**In short:** The Loan Security Assignment screen records a pledge: which securities, in what quantity, are pledged to a borrower or a loan.

## What this screen is for

**Loan Security Assignment** records a pledge (menu: Lending > Security Management > Loan Security Assignment). The officer picks the applicant and the loan and adds rows in the **Securities** table, each with a Loan Security and a quantity. The row fills in the haircut, the price, the amount and the amount after the haircut. In the J7 walkthrough, 200 units priced at 1,000 gave an amount of 200,000 and a post-haircut value of 160,000. It is a submittable document.

## Before and after

Before: the securities and their prices exist (`screen.loan_security`), and the loan is booked (`screen.loan`). In the J7 example the loan was booked without auto-disbursement so that the pledge came first, and was disbursed after (`screen.loan_disbursement`). After: the shortfall check compares the pledged value with the loan (`screen.loan_security_shortfall`).

## Key fields

**Applicant**, **Loan**, **Securities**, **Total Security Value**, **Maximum Loan Value** and **Status**. The status list has seven values, which the verification report says match the BRD: Pledge Requested, Pledged, Release Requested, Released, Unpledged, Repossessed and Cancelled. In the verification a saved draft was Pledge Requested and Submit set Pledged at once, with no approval; Release Requested, Unpledged and Repossessed were never set by any code, and the status field is read-only on the form (BR-LMS-171c, ND-30). A release is a separate Loan Security Release record, and after an approved release the assignment still read Pledged.

![A submitted pledge, status Pledged](/assets/lending_assistant/kb_img/J7/J7-S2-08_pledge-submitted-pledged.png)

![The toolbar of a pledged assignment, with no Release button](/assets/lending_assistant/kb_img/J7/J7-S2-09_pledge-toolbar-no-release.png)

The installed doctype gives System Manager and Loan Manager read, write, create, submit, cancel and delete, and Loan Reporter read only.

## BRD needs it serves

BR-LMS-171c and BR-LMS-174 in BRD 7.8 (see `brd_section.7.8`), cited from the verification report; the bridges hold the verdicts. Weak points shown: the pledge's post-haircut value was added on top of the Maximum Loan Amount typed on the loan (160,000 and 160,000 gave 320,000, DEF-31), and a secured loan was disbursed with no pledge at all.
