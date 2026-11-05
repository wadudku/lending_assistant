---
id: concept.BR-LOS-162
type: concept
title: Data left unsent too long is erased and the check is marked abandoned
summary: "If captures stay unsent past a set time they are deleted, the verification is marked abandoned, and the applicant can be assigned again."
br_ids: [BR-LOS-162]
brd_section: 6.7.2
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-162"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p40"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.7.2"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p26"
related: [bridge.BR-LOS-162, concept.BR-LOS-161, brd_section.5.2]
version: 1
status: approved
approved_by: Owner
---
**In short:** If captures stay unsent past a set time they are deleted, the verification is marked abandoned, and the applicant can be assigned again.

## What the rule says

BR-LOS-162 (Must, BRD 6.7.2, PDF page 40) says "unsynchronised data older than a configurable period shall be purged and the verification marked abandoned". The applicant "shall be re-assignable", meaning the applicant can be assigned again. The time limit is a setting, not a fixed number.

## Why the bank wants it

The BRD gives the operating context for section 6.7 (PDF page 39): officers often work in rural places with unreliable mobile data. Section 6.7.2 (PDF page 40) is the part that deals with that. The BRD doesn't say why; the usual reason is that old unsent data is both a risk on the device and probably out of date, so it is safer to start the verification again than to send something stale.

## Example

An officer captures a signature on Monday and has no signal for the rest of the period. The time limit passes. The capture is erased from the device, the verification is marked abandoned, and the applicant can be assigned again.

## Terms to know

- **Abandoned:** a verification status in the BRD's state list (BRD 5.2, PDF page 26: "Applicant absent, unwilling or unable to complete"); this row also marks a verification abandoned when its old unsent data is purged.
- **Re-assignable:** able to be assigned again.
