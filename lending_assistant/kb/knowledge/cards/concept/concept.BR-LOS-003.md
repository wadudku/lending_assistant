---
id: concept.BR-LOS-003
type: concept
title: Idle applications expire automatically
summary: "An application that stays too long in any status that is not final moves to EXPIRED by itself, after a period the bank sets."
br_ids: [BR-LOS-003]
brd_section: 5.2
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-003"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p27"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-001"
related: [bridge.BR-LOS-003, concept.BR-GOV-005]
version: 1
status: approved
approved_by: Owner
---
**In short:** An application that stays too long in any status that is not final moves to EXPIRED by itself, after a period the bank sets.

## What the rule says

BR-LOS-003 (Must, BRD 5.2, PDF page 27) says applications automatically move to EXPIRED after a configurable period in any non-terminal status. The default periods are to be confirmed by the Bank. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that unfinished applications left open for months clutter the queues, hold exposure and become out of date.

## Example

An application sits in SUBMITTED for longer than the configured period and nobody acts on it. The system moves it to EXPIRED on its own. The BRD has not yet fixed the default period for each status; the Bank has to confirm them.

## Terms to know

- **Non-terminal status:** a status that is not an end point, so more steps can still follow.
- **EXPIRED:** the status for an application that lapsed without progress.
- **Configurable:** set by the bank, not fixed in the program.
