---
id: brd_section.5.2
type: brd_section
title: BRD 5.2 Origination lifecycle states
summary: "Section 5.2 lists 23 origination statuses and five rules: only allowed changes, both amounts kept, only the origination system sanctions, idle applications expire, and every change is logged."
br_ids: [BR-LOS-001, BR-LOS-002, BR-LOS-002a, BR-LOS-003, BR-LOS-004]
brd_section: 5.2
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#5.2"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p25"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p26"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p27"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-001"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-002"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-002a"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-003"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-004"
related: [bridge.BR-LOS-001, bridge.BR-LOS-002, bridge.BR-LOS-002a, bridge.BR-LOS-003, bridge.BR-LOS-004]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 5.2 lists 23 origination statuses and five rules: only allowed changes, both amounts kept, only the origination system sanctions, idle applications expire, and every change is logged.

## What this section says

BRD 5.2 (PDF pages 25 to 27) says the LOS keeps exactly one current status for every application, and that this model drives what each user sees, what actions are available, what reporting counts and what reconciliation compares. A table lists 23 statuses, from DRAFT to HANDED_OFF, each with who sets it and what it means; HANDED_OFF is the confirmed funded loan accepted into servicing and is terminal for origination. Five requirements follow: BR-LOS-001 only allowed status changes go through and others are refused and logged; BR-LOS-002 when less is sanctioned than asked, both amounts are kept and shown; BR-LOS-002a only the origination system sanctions; BR-LOS-003 idle applications expire automatically; BR-LOS-004 every status change leaves a permanent audit record.

## Why the bank wants it

The BRD gives the reason in the section introduction: one status per application drives what each user sees, what actions are available, what reporting counts and what reconciliation compares (PDF page 25).

## How it meets Frappe Lending

The section holds 5 requirements (BR-LOS-001, BR-LOS-002, BR-LOS-002a, BR-LOS-003, BR-LOS-004). The team has not analysed them: the analysis covered the 103 servicing requirements of BRD section 7, so this card gives no verdict. Each row has a concept card with the rule and a not-analysed bridge card with pointers only.

## Related cards

Requirement cards: `concept.BR-LOS-001`, `concept.BR-LOS-002`, `concept.BR-LOS-002a`, `concept.BR-LOS-003` and `concept.BR-LOS-004` with matching bridge cards. Related: `brd_section.5.3`, `brd_section.5.4`.
