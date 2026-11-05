---
id: concept.BR-LOS-326
type: concept
title: "Approvers cannot approve their own sampled cases or their own organisation's, and dual sanction needs two people"
summary: "An approver cannot sanction an application they reviewed at sampling or one from an organisation their account is linked to; where dual sanction is required, the second approver is a different user."
br_ids: [BR-LOS-326]
brd_section: 6.6
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-326"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p38"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-141"
related: [bridge.BR-LOS-326, concept.BR-LOS-141, concept.BR-LOS-325, glossary.sampling]
version: 1
status: approved
approved_by: Owner
---
**In short:** An approver cannot sanction an application they reviewed at sampling or one from an organisation their account is linked to; where dual sanction is required, the second approver is a different user.

## What the rule says

BR-LOS-326 (Must, BRD 6.6, PDF page 38) says an approver cannot sanction an application they reviewed at sampling, nor one submitted by an organisation to which their user account is linked. Where the Bank requires dual sanction above a configurable amount, the second approver is a different user from the first. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the same person should not both review and approve a case, or approve a case from their own organisation.

## Example

A reviewer rejected a case at sampling, and later it comes to them in the approval queue. The platform does not let them sanction it. For a 500,000 loan needing dual sanction, a second, different approver must also sanction.

## Terms to know

- **Segregation of duties:** different people do conflicting steps.
- **Dual sanction:** two approvers must sanction above a stated amount.
- **Linked organisation:** the partner the account holder belongs to.
- **Sampling review:** the manual check of a sampled application. See BR-LOS-141.
