---
id: concept.BR-LMS-173
type: concept
title: Track how a shortfall is fixed
summary: "When there is a shortfall, the platform tracks the remedy (more security, a repayment or an approved exception), each with an owner and a due date."
br_ids: [BR-LMS-173]
brd_section: 7.8
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-173"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p52"
  - "sources/verification/reqs.json#BR-LMS-173"
  - "sources/verification/verification_report.md#BR-LMS-173"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-173"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-173"
related: [bridge.BR-LMS-173, brd_section.7.8, concept.BR-LMS-172]
version: 1
status: approved
approved_by: Owner
---
**In short:** When there is a shortfall, the platform tracks the remedy (more security, a repayment or an approved exception), each with an owner and a due date.

## What the rule says

BR-LMS-173 in section 7.8 (Must, BRD PDF page 52) says that where a shortfall arises, the platform tracks the remediation: additional security offered, repayment received, or an approved exception. Each remedy has an owner and a due date.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a shortfall is a risk the bank has to close, so someone must be named and a date set, or it stays open and is forgotten.

## Example

Rahim must add a 10,000 fixed deposit by 15 November. The owner is the branch credit officer.

## Terms to know

- **Remediation:** the action that closes a shortfall.
- **Approved exception:** the bank agrees to leave the shortfall open for a stated reason.
- **Owner:** the person responsible for the fix.
- **Shortfall:** see `concept.BR-LMS-172`.
