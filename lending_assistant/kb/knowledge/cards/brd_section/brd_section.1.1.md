---
id: brd_section.1.1
type: brd_section
title: BRD 1.1 Purpose
summary: "Section 1.1 says the document specifies two connected systems for NRB Bank, the Loan Origination System and the Loan Management System, and that it is one document because the handoff between them is itself a control."
br_ids: []
brd_section: 1.1
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#1.1"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p9"
related: []
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 1.1 says the document specifies two connected systems for NRB Bank, the Loan Origination System and the Loan Management System, and that it is one document because the handoff between them is itself a control.

## What this section says

BRD 1.1 (PDF page 9) says the document specifies the business requirements for two connected systems for NRB Bank Limited. The Loan Origination System (LOS) carries a prospective loan from submission, by an aggregator partner or the Bank's own channel, through validation, sampling, identity and credit verification, approval, loan account opening and confirmed disbursement. The Loan Management System (LMS) takes the confirmed funded loan from that point and services it through schedule generation, demand raising, interest accrual, repayment allocation, collateral management, restructuring, delinquency management, classification, provisioning, recovery and closure. The document is meant as the basis for solution design, development estimation, user acceptance test design, and NRB's internal governance and vendor approval processes.

## Why the bank wants it

The BRD gives the reason for one document in the section itself: the boundary between the two systems, the handoff of a confirmed funded loan, is itself a business control that must be agreed once and honoured by both (PDF page 9).

## How it meets Frappe Lending

This section holds no requirement row, so there is nothing in it to compare with Frappe Lending, and the team has made no statement about it. Frappe Lending is the servicing side; the team's analysis covers the LMS requirements of BRD section 7, and the team has not analysed the LOS.

## Related cards

Boundary: `brd_section.3.2`, `brd_section.5.4`. Terms: `glossary.los`, `glossary.lms`.
