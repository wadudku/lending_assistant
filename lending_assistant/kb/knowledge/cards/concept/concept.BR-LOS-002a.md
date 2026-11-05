---
id: concept.BR-LOS-002a
type: concept
title: "Only the origination system sanctions, never the servicing system"
summary: "The servicing system never sets a sanction; the origination system is the sanctioning authority, either by a system decision within set limits or through a credit approver within delegated authority."
br_ids: [BR-LOS-002a]
brd_section: 5.2
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-002a"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p27"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-028"
related: [bridge.BR-LOS-002a, glossary.los, glossary.lms, concept.BR-GOV-028]
version: 1
status: approved
approved_by: Owner
---
**In short:** The servicing system never sets a sanction; the origination system is the sanctioning authority, either by a system decision within set limits or through a credit approver within delegated authority.

## What the rule says

BR-LOS-002a (Must, BRD 5.2, PDF page 27) says sanction is never set by the servicing system. The LOS is the sanctioning authority, acting either as a system decision within configured thresholds or through a credit approver within delegated authority, as specified in BRD Section 6.6.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that approval of credit is a separate control from looking after a loan, and keeping the two in different systems stops one person or system doing both.

## Example

A borrower asks for more money on a running loan. The servicing system does not approve it. The request goes back to the origination system, where either the system's rules (within the set thresholds) or a credit approver (within their limit) decides.

## Terms to know

- **Sanction:** the bank's decision to lend, with amount, tenor, rate and fees.
- **Sanctioning authority:** the system or person allowed to make that decision.
- **Credit approver:** a bank staff member who decides cases above the automatic thresholds.
- **Delegated authority:** the decision limit the bank gives a role.
