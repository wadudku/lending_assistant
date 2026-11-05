---
id: screen.loan_classification
type: screen
title: "Screen: Loan Classification"
summary: "The Loan Classification screen is the short list of grade codes and names, such as STD and SMA, that a loan carries after the classification run."
br_ids: [BR-LMS-191]
brd_section: 7.10
doctypes: [Loan Classification]
dev_items: [D14]
fields: [Loan Classification.Classification Code, Loan Classification.Classification Name]
options: []
menus: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_classification/loan_classification.json]
images: []
sources:
  - "sources/verification/walkthroughs/J4_walkthrough.md#stage-2"
  - "sources/verification/walkthroughs/J4_walkthrough.md#stage-4"
  - "sources/verification/walkthroughs/J2_walkthrough.md#stage-5"
  - "sources/verification/walkthroughs/J2_walkthrough.md#5.4"
  - "sources/verification/verification_report.md#BR-LMS-191"
related: [screen.loan, screen.days_past_due_log, screen.loan_npa_log, brd_section.7.10, glossary.asset-classification, bridge.BR-LMS-190, bridge.BR-LMS-191]
version: 1
status: approved
approved_by: Owner
---
**In short:** The Loan Classification screen is the short list of grade codes and names, such as STD and SMA, that a loan carries after the classification run.

## What this screen is for

**Loan Classification** holds the grade codes and their names. A loan points to one through its read-only **Classification Code** (and **Classification Name**) in the Loan Classification Details section. The J4 walkthrough showed three of them in use: STD, SMA (Special Mention Account) and SS (Sub-Standard).

## Before and after

Before: the grade bands, in days past due, are set on the Company's Lending tab (Loan Classification Ranges), as plain editable tables with no version, effective date or approval. The classification run reads the loan's days past due, picks the band and writes the code on the loan. After: the loan shows the code, and the NPA flag follows in the same run; see `screen.loan` and `screen.loan_npa_log`. The walkthroughs show this screen only through the loan and the Company tables, so this card has no screenshot of its own.

## Key fields

**Classification Code** (the record's name) and **Classification Name**; nothing else. The grade bands in the walkthrough were STD 0 to 59, SMA 60 to 89, SS 90 to 179, DF 180 to 364, BL 365 to 1079 and WO 1080 to 99999 days past due. The installed doctype gives System Manager and Loan Manager read, write, create and delete, and Loan Reporter read only.

## BRD needs it serves

BR-LMS-191 in BRD 7.10 (see `brd_section.7.10`), the health grade; the bridges hold the verdicts. BR-LMS-191 names the Company's Loan Classification Ranges, whose codes are records of this screen. The only manual override the verification found is the Manual NPA tick on the loan, which is an NPA yes or no, not a grade, with no reason or approver (`bridge.BR-LMS-191`). The provision rates are only stored, and no provision is posted from the grade (D14).
