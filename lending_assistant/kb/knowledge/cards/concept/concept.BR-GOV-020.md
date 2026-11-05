---
id: concept.BR-GOV-020
type: concept
title: "Access follows roles, and a person can hold several"
summary: "Access is given through roles, one person can hold more than one role, and permissions can be set per function and not only per role."
br_ids: [BR-GOV-020]
brd_section: 4.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-020"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p22"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p22"
related: [bridge.BR-GOV-020, concept.BR-GOV-022, concept.BR-GOV-028]
version: 1
status: approved
approved_by: Owner
---
**In short:** Access is given through roles, one person can hold more than one role, and permissions can be set per function and not only per role.

## What the rule says

BR-GOV-020 (Must, BRD 4.3, PDF page 22) says access is role-based and a user may hold more than one role. Permissions can be assigned at function level, not only at role level.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that real staff do mixed jobs, and a role alone is too coarse when two people with the same role must not be able to do the same thing.

## Example

An officer holds both the “loan processor” and the “reports” roles. A separate switch lets the bank stop that officer from running one specific function, such as bulk upload, without removing either role.

## Terms to know

- **Role-based access:** permissions are given to a named role, and people receive the role.
- **Function level:** a permission for one action, such as “approve a waiver”, rather than a whole role.
- **Multiple roles:** one person holding several roles at once.
