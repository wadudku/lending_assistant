---
id: brd_section.6.2.3
type: brd_section
title: BRD 6.2.3 Borrower consent
summary: "Section 6.2.3 holds one rule: no application is accepted without a recorded borrower consent, and the BRD flags a legal question about what the consent must be."
br_ids: [BR-LOS-117]
brd_section: 6.2.3
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.2.3"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p31"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p32"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-117"
related: [bridge.BR-LOS-117]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 6.2.3 holds one rule: no application is accepted without a recorded borrower consent, and the BRD flags a legal question about what the consent must be.

## What this section says

BRD 6.2.3 (PDF pages 31 and 32) holds one requirement, BR-LOS-117: the platform accepts no application without a recorded borrower consent covering the partner's sharing of the individual's personal data with the Bank, the Bank's inquiry to the credit bureau, and identity verification against the national database. The partner keeps the underlying evidence; the platform records the consent reference, the method of capture and the timestamp, and makes them available to Bank compliance. A boxed note, “Legal confirmation required”, says it is a legal question for NRB whether a consent reference supplied in a file is enough authority for a credit bureau inquiry, or whether a signed instrument must exist first. If one is needed, bureau checking cannot happen before the field officer captures the signature, and the platform must enforce that order.

## Why the bank wants it

The BRD gives the reason for the boxed note in the section: the answer to the legal question materially affects the flow, because a required signed instrument would put bureau checking after the field officer's visit (PDF pages 31 and 32).

## How it meets Frappe Lending

The section holds 1 requirement (BR-LOS-117). The team has not analysed it: the analysis covered the 103 servicing requirements of BRD section 7, so this card gives no verdict. Each row has a concept card with the rule and a not-analysed bridge card with pointers only.

## Related cards

Requirement cards: `concept.BR-LOS-117` with matching bridge cards. Related: `brd_section.6.2`, `brd_section.6.2.2`.
