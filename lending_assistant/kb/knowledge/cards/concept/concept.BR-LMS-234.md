---
id: concept.BR-LMS-234
type: concept
title: Closure needs approval
summary: "Closure follows an authorised path from closure requested to closed, and keeps who authorised it and when."
br_ids: [BR-LMS-234]
brd_section: 7.14
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-234"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p56"
  - "sources/verification/reqs.json#BR-LMS-234"
  - "sources/verification/verification_report.md#BR-LMS-234"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-234"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-234"
related: [bridge.BR-LMS-234, brd_section.7.14, glossary.maker-checker, lifecycle.CLOSURE_REQUESTED, lifecycle.CLOSED]
version: 1
status: approved
approved_by: Owner
---
**In short:** Closure follows an authorised path from closure requested to closed, and keeps who authorised it and when.

## What the rule says

BR-LMS-234 in section 7.14 (Must, BRD PDF page 56) says closure shall follow an authorised workflow from closure requested to closed, with the authorising user and timestamp retained.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that closing a loan ends the bank's claim and releases its security, so a second person should agree and the record should show who and when.

## Example

Closure requested 5 June 2027 at 10:00 by Officer A; approved and closed at 10:30 by Manager B. An auditor reading the loan's record later can see both names and both times, and can tell that two different people were involved.

## Terms to know

- **Workflow:** the fixed steps a record passes through, with a named person approving each. See `glossary.maker-checker`.
- **Authorising user and timestamp:** who approved and when, kept on the record.
