---
id: concept.BR-LOS-182
type: concept
title: "Assignment can be done in bulk, with workload shown and a capacity warning"
summary: "Assigning can be done in bulk, shows each officer's current workload and coverage area, and warns when an assignment would go over the officer's daily capacity."
br_ids: [BR-LOS-182]
brd_section: 6.7.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-182"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p41"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.7.4"
related: [bridge.BR-LOS-182, concept.BR-LOS-181]
version: 1
status: approved
approved_by: Owner
---
**In short:** Assigning can be done in bulk, shows each officer's current workload and coverage area, and warns when an assignment would go over the officer's daily capacity.

## What the rule says

BR-LOS-182 (Must, BRD 6.7.4, PDF page 41) says assignment "shall be bulk-capable". It shall display each officer's current open workload and coverage area, and "shall warn where an assignment would exceed a configurable per-officer daily capacity". The BRD says warn, not block.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that an assigner who can see who is already busy, and where each officer works, can spread the work and avoid sending one officer more applicants than a day allows.

## Example

A bank user selects 30 applications and assigns them to officers in one step. The screen shows each officer's open workload and coverage area. One assignment would take an officer over the daily capacity, so a warning appears.

## Terms to know

- **Open workload:** the verifications an officer has been assigned and not yet completed.
- **Coverage area:** the area the officer covers, held on the officer profile (BR-LOS-184).
- **Daily capacity:** the configurable number of assignments one officer can take per day.
