---
id: concept.BR-LOS-325
type: concept
title: Delegated authority is enforced at the moment of decision
summary: An approver cannot sanction above their limit; the application escalates to the next authority level and the escalation is recorded.
br_ids: [BR-LOS-325]
brd_section: 6.6
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-325"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p38"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-028"
related: [bridge.BR-LOS-325, concept.BR-GOV-028, concept.BR-LOS-324]
version: 1
status: approved
approved_by: Owner
---
**In short:** An approver cannot sanction above their limit; the application escalates to the next authority level and the escalation is recorded.

## What the rule says

BR-LOS-325 (Must, BRD 6.6, PDF page 38) says delegated authority is enforced at the point of decision. An application above the acting approver's limit cannot be sanctioned by that approver and escalates to the next authority level, with the escalation recorded. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that approval limits are only a control if the system refuses an approval above them. BR-GOV-028 lists sanction among the actions that need delegated authority (PDF page 23).

## Example

An approver has a limit of 150,000. A case for 220,000 is in their queue. They cannot sanction it; the system sends it to the next level, and the history shows the escalation and both approvers.

## Terms to know

- **Delegated authority:** the amount a person is allowed to approve. See BR-GOV-028.
- **Escalate:** pass a case to the next level of authority.
- **Acting approver:** the person trying to decide the case.
- **Limit:** the highest amount that person may approve.
