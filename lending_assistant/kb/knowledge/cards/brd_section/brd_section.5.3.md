---
id: brd_section.5.3
type: brd_section
title: BRD 5.3 Servicing lifecycle states
summary: "Section 5.3 lists twelve states a loan can be in while it is serviced, and requires that every loan has exactly one current state with a full history."
br_ids: []
brd_section: 5.3
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan/loan.json]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#5.3"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p27"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p28"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-001"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-002"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-003"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#5.1-the-two-lifecycles-side-by-side"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#5.2-the-main-difference"
related: [lifecycle.OVERDUE, lifecycle.NPA, glossary.dpd]
version: 3
status: approved
approved_by: Owner
---
**In short:** Section 5.3 lists twelve states a loan can be in while it is serviced, and requires that every loan has exactly one current state with a full history.

## What this section says

BRD 5.3 (PDF pages 27 and 28) defines twelve servicing states: BOOKED, ACTIVE, PARTIALLY_DISBURSED, OVERDUE, SMA, NPA, RESTRUCTURED, FROZEN, CLOSURE_REQUESTED, CLOSED, SETTLED and WRITTEN_OFF. Three requirements follow. BR-LMS-001: every loan has exactly one current servicing status, with the full history of earlier statuses, each with date and reason. BR-LMS-002: a status change never deletes or overwrites an earlier classification, schedule version or posting. BR-LMS-003: the status names must be aligned with the bank's own vocabulary and with Bangladesh Bank terms before the configuration is fixed.

The BRD adds a note: the names are the supplier's proposal, and where NRB's systems or Bangladesh Bank reporting use different words for the same state, the bank's words win.

## Why the bank wants it

The BRD gives one reason, for BR-LMS-003: the bank's own terms should be adopted "so that two vocabularies do not describe the same loan" (PDF page 28). The BRD doesn't say why one status with a full history is needed; the usual reason is that collections, finance, risk and the regulator all ask what state a loan is in and how it got there. If each team infers the state from different fields, they disagree, and one status with its history gives a single answer and a trail for audit.

## How it meets Frappe Lending

Frappe Lending's Loan Status field has 9 options, Draft included, 8 besides Draft (`lending/loan_management/doctype/loan/loan.json:176`), plus separate flags and fields. Six BRD states match a status directly. OVERDUE, SMA, NPA, RESTRUCTURED and FROZEN exist only as flags or fields, and BOOKED differs in timing. BR-LMS-001 to 003 are not among the 103 requirements the team verified, so they carry no verdict here. The team's lifecycle comparison is in section 5 of the coverage analysis, and the proposed answer is the servicing status field in D2.

## Related cards

State cards: `lifecycle.OVERDUE` and `lifecycle.NPA`. Term: `glossary.dpd`.
