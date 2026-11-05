---
id: screen.loan_partner
type: screen
title: "Screen: Loan Partner"
summary: "The Loan Partner screen is the master record of a co-lending partner: its share, base rate, schedule type, guarantee terms and accounts."
br_ids: [BR-LMS-111, BR-LMS-116, BR-LMS-123, BR-LMS-210, BR-LMS-211, BR-LMS-212, BR-LMS-214]
brd_section: 7.12
doctypes: [Loan Partner]
dev_items: [D19]
fields: [Loan Partner.Partner Code, Loan Partner.Partner Name, Loan Partner.Effective Date, Loan Partner.Partner Loan Share Percentage, Loan Partner.Partner Base Interest Rate, Loan Partner.Repayment Schedule Type, Loan Partner.Enable Partner Accounting, Loan Partner.FLDG Trigger DPD, Loan Partner.Type of FLDG Applicable, Loan Partner.Receivable Account, Loan Partner.Payable Account, Loan Partner.Credit Account]
options: [Loan Partner.Repayment Schedule Type=EMI (PMT) based, Loan Partner.Organization Type=Centralized, Loan Partner.Type of FLDG Applicable=Both Fixed Deposit and Corporate Guarantee]
menus: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_partner/loan_partner.json]
images: [/assets/lending_assistant/kb_img/J10/J10-S0-03_partner-list.png, /assets/lending_assistant/kb_img/J10/J10-S1-02_partner-saved.png]
sources:
  - "sources/verification/walkthroughs/J10_walkthrough.md#stage-1"
  - "sources/verification/walkthroughs/J10_walkthrough.md#1.1"
  - "sources/verification/walkthroughs/J10_walkthrough.md#0.2"
  - "sources/verification/verification_report.md#BR-LMS-210"
  - "sources/verification/verification_report.md#BR-LMS-211"
  - "sources/verification/verification_report.md#BR-LMS-212"
  - "sources/verification/verification_report.md#BR-LMS-214"
related: [screen.loan, screen.loan_product, screen.loan_repayment_schedule, brd_section.7.12, glossary.partner, glossary.fldg, bridge.BR-LMS-210, bridge.BR-LMS-211, bridge.BR-LMS-212, bridge.BR-LMS-214, devitem.D19]
version: 1
status: approved
approved_by: Owner
---
**In short:** The Loan Partner screen is the master record of a co-lending partner: its share, base rate, schedule type, guarantee terms and accounts.

## What this screen is for

**Loan Partner** holds the terms of a co-lending partner (the J10 walkthrough opened it at `/desk/loan-partner`). A product lists the partners that may join its loans (see `screen.loan_product`), and a loan names one partner. The J10 walkthrough created a partner with a 20% share, a 10% base rate, the schedule type **EMI (PMT) based** and an effective date, then set the accounts the postings use.

## Before and after

Before: the partner's accounts exist. After: on disbursement the ledger books the partner's share, and the loan's repayment schedule gets a Co Lender Schedule (`screen.loan_repayment_schedule`). Demands and repayments carry the partner's share.

## Key fields

**Partner Code**, **Partner Name**, **Effective Date**, **Partner Loan Share Percentage**, **Partner Base Interest Rate**, **Repayment Schedule Type** (EMI (PMT) based, Collection at partner's percentage, or POS reduction plus interest at partner ROI), **Organization Type**, the FLDG fields (**FLDG Trigger DPD**, **Type of FLDG Applicable**, the limit component and the two percentages) and the accounts (**Receivable Account**, **Payable Account**, **Credit Account**, **FLDG Account**, **Partner Interest Share**). The master validates the percentages between 1 and 99 and, at disbursement, that the partner's accounts are set. The list shows no status, exposure or outstanding column.

![The partner list](/assets/lending_assistant/kb_img/J10/J10-S0-03_partner-list.png)

![A saved partner](/assets/lending_assistant/kb_img/J10/J10-S1-02_partner-saved.png)

The installed doctype gives System Manager and Loan Manager read, write, create and delete, and Loan Reporter read only.

## BRD needs it serves

The main rows are BR-LMS-210, 211, 212 and 214 in BRD 7.12 (see `brd_section.7.12`), with BR-LMS-111, 116 and 123 where they name the partner; the bridges hold the verdicts. Weak points shown: the FLDG fields are recorded but nothing evaluates them (ND-41), the share is one figure on the partner so a different share per product needs a separate partner, and a loan closure on a co-lent loan posted nothing to the partner (DEF-44).
