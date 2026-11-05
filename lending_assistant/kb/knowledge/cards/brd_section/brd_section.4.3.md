---
id: brd_section.4.3
type: brd_section
title: BRD 4.3 Access control and segregation of duties
summary: "Section 4.3 holds nine access-control rules: roles, partner data separation, no self-approval, sampling-reviewer independence, a second login factor, protected personal data, idle-account shutdown, logging and approval limits."
br_ids: [BR-GOV-020, BR-GOV-021, BR-GOV-022, BR-GOV-023, BR-GOV-024, BR-GOV-025, BR-GOV-026, BR-GOV-027, BR-GOV-028]
brd_section: 4.3
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#4.3"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p22"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p23"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-020"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-021"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-022"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-023"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-024"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-025"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-026"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-027"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-028"
related: [bridge.BR-GOV-020, bridge.BR-GOV-021, bridge.BR-GOV-022, bridge.BR-GOV-023, bridge.BR-GOV-024, bridge.BR-GOV-025, bridge.BR-GOV-026, bridge.BR-GOV-027, bridge.BR-GOV-028]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 4.3 holds nine access-control rules: roles, partner data separation, no self-approval, sampling-reviewer independence, a second login factor, protected personal data, idle-account shutdown, logging and approval limits.

## What this section says

BRD 4.3 (PDF pages 22 and 23) holds nine requirements, BR-GOV-020 to BR-GOV-028. In short: access follows roles and a person can hold several (020); a partner's users see only their own partner's data (021); nobody approves their own work (022); a sampling reviewer cannot review their own organisation's or their own earlier cases (023); every Bank and partner account needs a second login factor (024); sensitive personal data is permissioned apart and every look is logged (025); idle accounts switch off, and so do accounts the HR process ends (026, a Should); sign-ins, permission changes and sensitive views are logged with source and outcome (027); and approval limits are set by role and amount, with a case over the limit escalating (028).

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a lending system holds money and personal data, so who may see and approve what has to be enforced by the system, not left to habit.

## How it meets Frappe Lending

The section holds 9 requirements (BR-GOV-020 to BR-GOV-028). The team has not analysed them: the analysis covered the 103 servicing requirements of BRD section 7, so this card gives no verdict. Each row has a concept card with the rule and a not-analysed bridge card with pointers only.

## Related cards

Requirement cards: `concept.BR-GOV-020` to `concept.BR-GOV-028` with matching bridge cards.
