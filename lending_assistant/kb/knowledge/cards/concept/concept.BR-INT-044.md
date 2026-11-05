---
id: concept.BR-INT-044
type: concept
title: "If identity verification is down, the application waits and retries"
summary: "Where identity verification is unavailable, the application holds rather than fails, with automatic retry."
br_ids: [BR-INT-044]
brd_section: 9.6
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-044"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p65"
related: [bridge.BR-INT-044]
version: 1
status: approved
approved_by: Owner
---
**In short:** Where identity verification is unavailable, the application holds rather than fails, with automatic retry.

## What the rule says

BR-INT-044 (Must, BRD 9.6, PDF page 65) says that where verification is unavailable, the application holds rather than fails, with automatic retry. The inventory in 9.1 marks the Election Commission Database as “Blocking at verification” (PDF page 60), which is why a pause is needed when it cannot be reached.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that an outage of the election database is not the applicant's fault, so the application should wait, not be rejected.

## Example

The election database cannot be reached at 3 p.m. The application stays in a waiting state, and the system tries again every few minutes. When the database returns, the check completes and the application carries on.

## Terms to know

- **Hold:** keep the application waiting.
- **Automatic retry:** trying again without a person asking.
