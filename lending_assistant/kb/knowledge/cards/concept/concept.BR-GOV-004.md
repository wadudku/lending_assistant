---
id: concept.BR-GOV-004
type: concept
title: The platform's status is checked against the bank's core system every day
summary: The platform keeps its own status for every application and loan and compares it with the bank's core system daily; where they differ the core system is right and the difference is an exception to close.
br_ids: [BR-GOV-004]
brd_section: 3.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-004"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-001"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
related: [bridge.BR-GOV-004, glossary.cbs, concept.BR-GOV-001]
version: 1
status: approved
approved_by: Owner
---
**In short:** The platform keeps its own status for every application and loan and compares it with the bank's core system daily; where they differ the core system is right and the difference is an exception to close.

## What the rule says

BR-GOV-004 (Must, BRD 3.4, PDF page 19) says the platform keeps its own status for every application and every loan, and reconciles that status against the CBS daily. Where the two differ, the CBS is authoritative for all post-booking facts, and the difference is raised as an exception that needs documented closure.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that two systems each holding a status will drift apart over time, and a daily comparison finds the drift while it is small. The rule fits the principle that the platform never holds the official books (BR-GOV-001, PDF page 19).

## Example

The platform shows a loan as active, but the CBS shows its account as closed. The daily comparison raises an exception. A named person reviews it, records why the two differed, and closes the exception. The platform takes the CBS value for the facts after booking.

## Terms to know

- **Reconcile:** compare two records of the same thing and explain any difference.
- **Authoritative:** the system whose value wins when two differ.
- **Post-booking facts:** facts that arise after a loan is booked, such as balances and repayments.
- **Exception:** a flagged difference that someone must review and close with a written reason.
