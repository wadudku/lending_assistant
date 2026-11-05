---
id: concept.BR-LOS-309
type: concept
title: "An authorised person can override a score decision, with a second approver and a reason"
summary: "A user with delegated authority can override a score-driven decision under maker-checker with a mandatory reason; overrides are recorded, reported separately and watched for volume and later performance."
br_ids: [BR-LOS-309]
brd_section: 6.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-309"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p34"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-028"
related: [bridge.BR-LOS-309, glossary.maker-checker, concept.BR-GOV-028]
version: 1
status: approved
approved_by: Owner
---
**In short:** A user with delegated authority can override a score-driven decision under maker-checker with a mandatory reason; overrides are recorded, reported separately and watched for volume and later performance.

## What the rule says

BR-LOS-309 (Must, BRD 6.4, PDF page 34) says an authorised user can override a score-driven decision under maker-checker, within their delegated authority, with a mandatory reason. Overrides are recorded against the application, reported as a distinct population, and monitored for volume and subsequent performance. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a person sometimes knows something the score cannot, but overrides must stay visible so they do not become a way around the policy. BR-GOV-028 lists score override among the actions that need delegated authority (PDF page 23).

## Example

A clerk proposes to turn a decline into an approval because a document arrived late. A second officer with enough authority approves, and the reason is saved. The case counts in the monthly override report.

## Terms to know

- **Override:** a person replaces the system's recommended decision.
- **Delegated authority:** the limit of what a person may approve. See BR-GOV-028.
- **Maker-checker:** one person proposes and another approves. See `glossary.maker-checker`.
- **Population:** a group of cases reported on its own.
