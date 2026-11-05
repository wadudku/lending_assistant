---
id: concept.BR-LOS-333
type: concept
title: Sanction activity is reported
summary: "The platform reports sanction activity: auto against approver-sanctioned volume, declines and reasons, revisions and average reduction, approver throughput and queue ageing, and escalations by authority level."
br_ids: [BR-LOS-333]
brd_section: 6.6
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-333"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p39"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-321"
related: [bridge.BR-LOS-333, concept.BR-LOS-321, concept.BR-LOS-329, glossary.scorecard]
version: 1
status: approved
approved_by: Owner
---
**In short:** The platform reports sanction activity: auto against approver-sanctioned volume, declines and reasons, revisions and average reduction, approver throughput and queue ageing, and escalations by authority level.

## What the rule says

BR-LOS-333 (Must, BRD 6.6, PDF page 39) says the platform reports sanction activity: auto-sanctioned against approver-sanctioned volume, decline rate and reasons, revision rate and average reduction, approver throughput and queue ageing, and escalation volume by authority level. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the Bank decides how far to open or close the automatic line by looking at these figures. The 6.6 introduction says the threshold is configuration that the Bank can change as confidence in the scorecard develops (PDF page 37).

## Example

Each month the Bank sees that 70% of sanctions were automatic, 6% declined, and that cases above the 150,000 level waited four days on average. It uses these figures to move the automatic line.

## Terms to know

- **Throughput:** how many cases an approver finishes in a period.
- **Revision rate:** the share of sanctions at terms different from the proposal.
- **Average reduction:** how much lower the sanctioned amount is on revised cases.
- **Authority level:** a rung of delegated authority.
