---
id: concept.BR-GOV-050
type: concept
title: A daily comparison of the platform and the core banking system
summary: "Every day the platform compares its own application and loan status with the core banking system for each record after approval, and produces an exception report of all differences."
br_ids: [BR-GOV-050]
brd_section: 8.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-050"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p59"
related: [bridge.BR-GOV-050, glossary.cbs]
version: 1
status: approved
approved_by: Owner
---
**In short:** Every day the platform compares its own application and loan status with the core banking system for each record after approval, and produces an exception report of all differences.

## What the rule says

BR-GOV-050 (Must, BRD 8.4, PDF page 59) says the platform runs a daily reconciliation. It compares its own application and loan status with the Core Banking System and servicing position, for every record in a post-approval status. It produces an exception report of all differences.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the platform and the core banking system each hold part of the story, so a daily comparison finds a difference while it is small. BRD 3.4 sets the same idea as a principle (BR-GOV-004, PDF page 19).

## Example

At night the platform compares 3,000 loans with the core banking system. It finds two where the platform shows a loan as active but the core banking system shows the account as closed. Both are listed in the morning exception report.

## Terms to know

- **Reconciliation:** comparing two records of the same thing and explaining any difference.
- **Post-approval status:** any status after the application has been approved.
- **CBS:** the bank's main system. See `glossary.cbs`.
- **Exception report:** a list of the differences found.
