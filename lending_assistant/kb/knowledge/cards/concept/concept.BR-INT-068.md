---
id: concept.BR-INT-068
type: concept
title: More automation sessions add throughput without changing the engine
summary: "Automation capacity scales sideways: extra concurrent sessions raise throughput without change to the origination or servicing engine, within the core banking system's own limits."
br_ids: [BR-INT-068]
brd_section: 9.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-068"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p63"
related: [bridge.BR-INT-068, glossary.rpa, glossary.cbs]
version: 1
status: approved
approved_by: Owner
---
**In short:** Automation capacity scales sideways: extra concurrent sessions raise throughput without change to the origination or servicing engine, within the core banking system's own limits.

## What the rule says

BR-INT-068 (Must, BRD 9.3, PDF page 63) says automation capacity is horizontally scalable. Additional concurrent sessions increase throughput without change to the origination or servicing engine, subject to the core banking system's own concurrency limits.

## Why the bank wants it

The BRD gives the reason in section 9.2: concurrent sessions, their machines and the system's login ceiling “together set the platform's ceiling. Increasing volume means increasing that capacity” (PDF page 61).

## Example

Volume doubles. The bank adds a second automation machine with its own sessions, and the queue clears twice as fast. The platform itself is not changed. It stops gaining speed once the core banking system's limit on logins is reached.

## Terms to know

- **Horizontally scalable:** capacity grows by adding more of the same unit.
- **Concurrent session:** one sign-in working at the same time as others.
- **Concurrency limit:** the most logins the core banking system allows at once.
