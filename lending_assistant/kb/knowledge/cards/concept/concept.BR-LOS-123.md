---
id: concept.BR-LOS-123
type: concept
title: An account check result expires after a set time
summary: "A validation result expires after a configurable period, seven days by default, and a stale result forces a new check before submission."
br_ids: [BR-LOS-123]
brd_section: 6.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-123"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p32"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-120"
related: [bridge.BR-LOS-123, concept.BR-LOS-120]
version: 1
status: approved
approved_by: Owner
---
**In short:** A validation result expires after a configurable period, seven days by default, and a stale result forces a new check before submission.

## What the rule says

BR-LOS-123 (Must, BRD 6.3, PDF page 32) says a validation result expires after a configurable period, default seven days. A stale result forces re-validation before submission is permitted. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that an account can become dormant or closed after it was checked, so an old result is not a safe guide.

## Example

An account is checked on the 1st. The partner submits on the 10th. The result is older than seven days, so the platform asks for a new check first.

## Terms to know

- **Validation result:** the outcome of the account check.
- **Stale:** older than the allowed period.
- **Re-validation:** running the check again.
- **Configurable:** set by the Bank, not fixed in the program.
