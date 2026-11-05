---
id: concept.BR-LOS-185
type: concept
title: Suspending an officer cuts off the app at once and returns their assignments
summary: "When an officer is suspended or deactivated, access on their bound device stops immediately and their open assignments go back to the queue."
br_ids: [BR-LOS-185]
brd_section: 6.7.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-185"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p42"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.7.4"
related: [bridge.BR-LOS-185, concept.BR-LOS-184, glossary.field-officer]
version: 1
status: approved
approved_by: Owner
---
**In short:** When an officer is suspended or deactivated, access on their bound device stops immediately and their open assignments go back to the queue.

## What the rule says

BR-LOS-185 (Must, BRD 6.7.4, PDF page 42) says suspending or deactivating an officer "shall immediately revoke application access on the bound device and shall return that officer's open assignments to the queue". Both effects follow from one action.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that an officer who has left or is under investigation should not keep access to applicant data, and their unfinished applicants must not be left stranded.

## Example

A bank user deactivates a field officer's profile. The officer's device can no longer use the app. The officer's open assignments return to the queue to be assigned again.

## Terms to know

- **Revoke:** withdraw access.
- **Open assignments:** assignments the officer has not completed.
