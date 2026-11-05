---
id: glossary.schedule-version
type: glossary
title: Schedule version
summary: "One saved generation of a loan's repayment plan. When later terms produce a new plan, the old version is kept, not overwritten."
br_ids: [BR-LMS-125, BR-LMS-183]
brd_section: 7.3
doctypes: [Loan Repayment Schedule]
dev_items: []
terms: [schedule version, plan version, superseded schedule]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#1.5"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-125"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-183"
related: [devitem.D6]
version: 1
status: approved
approved_by: Owner
---
**In short:** One saved generation of a loan's repayment plan. When later terms produce a new plan, the old version is kept, not overwritten.

## Plain meaning

The BRD defines a schedule version as an immutable generation of a repayment schedule, retained when later terms produce a replacement schedule (BRD 1.5).

## Example

Rahim's loan starts with schedule version 1. After a restructure, version 2 becomes the live plan, and version 1 is kept and marked as replaced, so anyone can see what was agreed before.

## Why it matters here

BR-LMS-125 asks that an old plan is never overwritten; the verified result is partly covered because there is no direct link from a plan to its replacement. BR-LMS-183 asks the same for a restructure and is covered.

## See also

`devitem.D6`, `glossary.restructuring`.
