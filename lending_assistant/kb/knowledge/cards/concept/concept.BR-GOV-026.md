---
id: concept.BR-GOV-026
type: concept
title: "Idle accounts switch off, and so do accounts the HR process ends"
summary: "User accounts are disabled automatically after a set time without use, and immediately when the bank's HR process says so."
br_ids: [BR-GOV-026]
brd_section: 4.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-026"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p23"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p23"
related: [bridge.BR-GOV-026]
version: 1
status: approved
approved_by: Owner
---
**In short:** User accounts are disabled automatically after a set time without use, and immediately when the bank's HR process says so.

## What the rule says

BR-GOV-026 (Should, BRD 4.3, PDF page 23) says user accounts are automatically disabled after a configurable period of inactivity, and immediately on instruction from the Bank's HR processes. This is a Should requirement, not a Must.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that an unused account, or one for a person who has left, is an open door that nobody is watching.

## Example

An officer does not sign in for 90 days (the period is a setting). The account is switched off. When HR reports that another officer has resigned, that account is switched off the same day.

## Terms to know

- **Inactivity period:** how long an account may go unused before it is switched off; a setting.
- **Disabled:** the account cannot sign in until it is switched on again.
- **HR process:** the bank's staff joining, moving and leaving procedures.
