---
id: brd_section.9.5
type: brd_section
title: BRD 9.5 Credit Information Bureau
summary: "Section 9.5 sets four rules for the bureau inquiry: where it runs, how it is monitored, how its credentials are kept apart and how it is logged."
br_ids: []
brd_section: 9.5
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#9.5"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p64"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-030"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-031"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-032"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-033"
related: [brd_section.9, brd_section.9.3, brd_section.7, glossary.rpa, glossary.cib]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 9.5 sets four rules for the bureau inquiry: where it runs, how it is monitored, how its credentials are kept apart and how it is logged.

## What this section says

BRD 9.5 (PDF page 64) has 4 requirements, all Must. BR-INT-030: the bureau inquiry runs from a designated host inside the bank's permitted network, through robotic process automation, under the same controls as Section 9.3. BR-INT-031: the automation is monitored for failure and interface change and alerts on consecutive failures. BR-INT-032: bureau credentials and session handling are isolated from the main application and from the core banking system automation. BR-INT-033: every inquiry is logged in accordance with BR-LOS-196 and retained for the full retention period.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the bureau, like the core banking system, is reached by driving its screens, so it needs the same safeguards.

## How it meets Frappe Lending

The team's analysis covered Section 7 only. This section holds 4 requirement rows and none was analysed, so the team makes no statement about them. For the Section 7 totals, see `brd_section.7`.

## Related cards

Parent: `brd_section.9`. Controls: `brd_section.9.3`. Term: `glossary.rpa`.
