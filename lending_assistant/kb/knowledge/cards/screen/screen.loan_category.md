---
id: screen.loan_category
type: screen
title: "Screen: Loan Category"
summary: "The Loan Category screen is a short master list of categories, a code and a name, used to label products and loans; the BRD wants it for reports (BR-LMS-106)."
br_ids: [BR-LMS-106]
brd_section: 7.1
doctypes: [Loan Category]
dev_items: []
fields: [Loan Category.Loan Category Code, Loan Category.Loan Category Name, Loan Category.Disabled]
options: []
menus: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_category/loan_category.json, lending/loan_management/doctype/loan_product/loan_product.json]
images: []
sources:
  - "sources/verification/walkthroughs/J1_walkthrough.md#stage-2"
  - "sources/verification/reqs.json#BR-LMS-106"
  - "sources/verification/verification_report.md#BR-LMS-106"
related: [screen.loan_product, screen.loan, brd_section.7.1, bridge.BR-LMS-106]
version: 1
status: approved
approved_by: Owner
---
**In short:** The Loan Category screen is a short master list of categories, a code and a name, used to label products and loans; the BRD wants it for reports (BR-LMS-106).

## What this screen is for

**Loan Category** is a list of category labels, each with a **Loan Category Code** and a **Loan Category Name**, and a **Disabled** tick. A Loan Product carries a **Loan Category** (see `screen.loan_product`) and the loan copies it when it is booked (see `screen.loan`); in the J1 example the loan showed the category Retail, copied from its product. The walkthroughs show the category on the product and the loan, not this screen, so this card has no screenshot. It is built from the doctype definition and the verification report.

## Before and after

Before: the category exists as a record. After: a Loan Product points to it, and each loan booked on that product copies it (`screen.loan_product`, `screen.loan`).

## Key fields

**Loan Category Code** (the record's name), **Loan Category Name** and **Disabled**. The installed doctype gives System Manager and Loan Manager read, write, create and delete, and Loan Reporter read only.

## BRD needs it serves

BR-LMS-106 in BRD 7.1 (see `brd_section.7.1`), each loan has a category for reports; the bridge holds the verdict.
