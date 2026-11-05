---
id: brd_section.1.2.1
type: brd_section
title: BRD 1.2.1 In scope
summary: "Section 1.2.1 lists what is in scope for the origination system, the servicing system and what both share."
br_ids: []
brd_section: 1.2.1
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#1.2.1"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p9"
related: []
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 1.2.1 lists what is in scope for the origination system, the servicing system and what both share.

## What this section says

BRD 1.2.1 (PDF page 9) has a table with three rows. For the Loan Origination System: a Partner Portal (web) for bulk application submission, correction and status visibility; a Bank Admin Console (web) for random sampling, configuration, assignment, oversight and reporting; a Field Officer App (Android) for in-person verification, evidence capture, credit bureau check and final approval; electronic KYC covering liveness, face matching and national database verification; and the integration layer to core banking, loan management, credit bureau and SMS. For the Loan Management System: funded-loan handoff and booking through to closure, including schedule generation and versioning, demand and charges, interest and penal accrual, repricing, repayment allocation, collateral, prepayment, restructuring, days-past-due tracking, classification and provisioning, settlement, write-off and recovery, co-lending and partner economics, portfolio operations, and statements, reporting and reconciliation. Shared by both: role-based access control, maker-checker governance, immutable audit trail, configuration versioning, reporting and the integration adapters to the Core Banking System and external providers.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a supplier and the Bank need one agreed list of what will be built before design and estimation begin.

## How it meets Frappe Lending

This section holds no requirement row, so there is nothing in it to compare with Frappe Lending, and the team has made no statement about it. Its LMS row is the servicing scope the team's analysis follows; its LOS row describes the origination system, which the team has not analysed.

## Related cards

Terms: `glossary.los`, `glossary.lms`, `glossary.cbs`.
