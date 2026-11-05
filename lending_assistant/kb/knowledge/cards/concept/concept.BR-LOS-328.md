---
id: concept.BR-LOS-328
type: concept
title: Every sanction is recorded as a system or user decision with the rules relied on
summary: "Each sanction records whether the system or a user decided, the rule or authority relied on, scorecard and configuration versions, proposed and final terms, reason codes and time; a system sanction is never recorded against a user."
br_ids: [BR-LOS-328]
brd_section: 6.6
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-328"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p38"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-321"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-304"
related: [bridge.BR-LOS-328, concept.BR-LOS-321, concept.BR-LOS-325, concept.BR-LOS-304, glossary.scorecard]
version: 1
status: approved
approved_by: Owner
---
**In short:** Each sanction records whether the system or a user decided, the rule or authority relied on, scorecard and configuration versions, proposed and final terms, reason codes and time; a system sanction is never recorded against a user.

## What the rule says

BR-LOS-328 (Must, BRD 6.6, PDF page 38) says every sanction records: whether it was a system decision or a person's decision; the threshold rule and version relied on, or the approver identity and the delegated limit relied on; the scorecard version and grade; the configuration version in force; the proposed and final terms; the reason codes; and the timestamp. A system sanction is recorded as a system decision naming the threshold applied, never against a user. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a sanction must later be explainable: which rule or person approved it, on what basis. The 6.6.1 table shows how each case is recorded: as a system decision, a user decision, or an escalation naming both approvers (PDF page 39).

## Example

An auto-sanction is recorded as “System decision, threshold rule T4, version 3, scorecard version 4, grade B”. A manual one is recorded as “Approver, limit 150,000, reason code …”. Both show the proposed and final terms and the time.

## Terms to know

- **System decision:** a decision taken by the platform under a threshold rule.
- **Person's decision:** a decision taken by a named approver.
- **Configuration version:** the numbered edition of the settings in force.
- **Timestamp:** the date and time of the decision.
