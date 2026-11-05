---
id: concept.BR-LOS-001
type: concept
title: Only allowed status changes go through; others are refused and logged
summary: "A status change that the lifecycle model does not allow is rejected, logged as an exception, and leaves the application unchanged."
br_ids: [BR-LOS-001]
brd_section: 5.2
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-001"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p27"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-004"
related: [bridge.BR-LOS-001, glossary.los, brd_section.5.3]
version: 1
status: approved
approved_by: Owner
---
**In short:** A status change that the lifecycle model does not allow is rejected, logged as an exception, and leaves the application unchanged.

## What the rule says

BR-LOS-001 (Must, BRD 5.2, PDF page 27) says status transitions are validated against the lifecycle model in BRD 5.2. An attempted transition that the model does not permit is rejected, logged as an exception, and does not alter the application. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD gives the context in the introduction to 5.2: the status model drives what each user sees, what actions are available, what reporting counts and what reconciliation compares (PDF page 24). If any change were allowed, those four things would stop agreeing.

## Example

An application is in the status DRAFT. Someone tries to move it straight to DISBURSED. Suppose the model does not allow that jump; then the system refuses, writes the refused attempt to an exception log, and the application stays in DRAFT.

## Terms to know

- **Status transition:** a move from one status to the next.
- **Lifecycle model:** the table in BRD 5.2 of statuses and who sets each.
- **Exception:** a flagged event that someone must review.
- **LOS:** the origination system. See `glossary.los`.
