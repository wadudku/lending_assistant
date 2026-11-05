---
id: brd_section.10.2
type: brd_section
title: BRD 10.2 Servicing entities
summary: "Section 10.2 is a table of 16 servicing entities, from Loan and Demand to ReconciliationRun, each with its purpose and notable attributes."
br_ids: []
brd_section: 10.2
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#10.2"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p66"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p67"
related: [brd_section.10, brd_section.10.1, brd_section.10.3, glossary.dpd, glossary.cbs]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 10.2 is a table of 16 servicing entities, from Loan and Demand to ReconciliationRun, each with its purpose and notable attributes.

## What this section says

BRD 10.2 (PDF page 67) is a table of 16 entities used by servicing: Loan, RepaymentSchedule, Demand, InterestAccrual, Repayment, Charge, LoanSecurity, Restructure, DPDLog, Classification, Provision, WriteOff, LoanPartner, CBSTransaction, AutomationRun and ReconciliationRun. For example, Loan is the servicing system of record, with borrower, product, terms, balances, status and classification. CBSTransaction is an instruction executed in the Core Banking System, with its type, unique platform reference, values entered, values read back, resolved state and voucher or journal reference.

## Why the bank wants it

The BRD gives the reason for all of Section 10 in its opening (PDF page 66): the table “establishes the shared vocabulary in which the two systems and the business describe the same things”.

## How it meets Frappe Lending

This section holds no requirement row, so there is nothing in it to compare with Frappe Lending, and the team has made no statement about it.

## Related cards

Parent: `brd_section.10`. Terms: `glossary.dpd`, `glossary.cbs`.
