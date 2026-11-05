---
id: screen.loan_application
type: screen
title: "Screen: Loan Application"
summary: "The Loan Application screen is Frappe Lending's origination form: a request for a loan that can become a Loan. The team has not analysed the LOS side."
br_ids: [BR-LMS-171, BR-LMS-201]
brd_section: 7.1
doctypes: [Loan Application]
dev_items: []
fields: [Loan Application.Applicant Type, Loan Application.Applicant, Loan Application.Application Date, Loan Application.Status, Loan Application.Loan Product, Loan Application.Loan Amount, Loan Application.Repayment Method, Loan Application.Repayment Period in Months, Loan Application.Is Secured Loan, Loan Application.Proposed Pledges, Loan Application.Maximum Loan Amount]
options: [Loan Application.Status=Open, Loan Application.Status=Approved, Loan Application.Status=Rejected]
menus: [Lending > Loan Origination > Loan Application]
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_application/loan_application.json, lending/loan_management/doctype/loan_application/loan_application.py, lending/loan_management/doctype/loan/loan.py]
images: []
sources:
  - "sources/verification/verification_report.md#BR-LMS-171c"
  - "sources/verification/verification_report.md#BR-LMS-201"
  - "sources/verification/verification_report.md#BR-LMS-100"
  - "sources/verification/reqs.json#BR-LMS-171c"
  - "sources/verification/reqs.json#BR-LMS-201"
related: [screen.loan, screen.loan_security_assignment, brd_section.7.1, glossary.los, glossary.application, bridge.BR-LMS-171c, bridge.BR-LMS-201]
version: 1
status: approved
approved_by: Owner
---
**In short:** The Loan Application screen is Frappe Lending's origination form: a request for a loan that can become a Loan. The team has not analysed the LOS side.

## What this screen is for

**Loan Application** is the origination form in Frappe Lending: the request for a loan, before any Loan exists (menu: Lending > Loan Origination > Loan Application). The team has not analysed the loan origination system (LOS) yet, so this card only describes the screen. It gives no verdict on how well it fits the bank's LOS needs, and no walkthrough shows it, so there is no screenshot. It is built from the doctype definition, the code and the verification report.

## Before and after

Before: the applicant exists (`screen.customer`) and the product exists (`screen.loan_product`). After: the installed code can create a Loan from an application (`create_loan` in `loan_application.py`), and a Loan has a read-only **Loan Application** link. When a Loan has an application, the loan amount is read from it. A secured loan with no application must have **Maximum Loan Amount** typed on the loan (the code message says it is mandatory). The code can also create a pledge from the application's **Proposed Pledges** (`create_loan_security_assignment`; see `screen.loan_security_assignment`).

## Key fields

**Applicant Type**, **Applicant**, **Application Date**, **Status** (Open, Approved or Rejected), **Loan Product**, **Loan Amount**, **Repayment Method**, **Repayment Period in Months**, **Is Secured Loan**, **Proposed Pledges** and **Maximum Loan Amount**. The form also has tables for **Documents** and co-applicants. The installed doctype names the roles Loan Manager, Loan Reporter, Employee and Loan LOS User in its permissions.

## BRD needs it serves

Only the BR-LMS rows where the verified text cites it: BR-LMS-171c, in BRD 7.8 (the life of a pledge; the report notes what the code does when there is no application) and BR-LMS-201, in BRD 7.11 (approval limits); the bridges hold the verdicts. For approval limits, the verification report notes that the site has Loan Application and Loan Lead workflows, both inactive. The BR-LOS rows (see `glossary.los`) are not analysed.
