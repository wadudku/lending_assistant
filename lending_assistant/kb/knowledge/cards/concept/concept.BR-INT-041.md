---
id: concept.BR-INT-041
type: concept
title: Check that the applicant is physically present
summary: "At field verification the platform checks that the applicant is physically present, using liveness detection."
br_ids: [BR-INT-041]
brd_section: 9.6
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-041"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p64"
related: [bridge.BR-INT-041]
version: 1
status: approved
approved_by: Owner
---
**In short:** At field verification the platform checks that the applicant is physically present, using liveness detection.

## What the rule says

BR-INT-041 (Must, BRD 9.6, PDF page 64) says the platform verifies that the applicant is physically present through liveness detection at field verification. The live capture taken during this check is then compared with the retained portrait under BR-INT-042. Both rows are part of the identity checks in 9.6.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a photo or recording of the applicant could be shown to the camera, so the check must show a live person.

## Example

At the visit the field officer app guides the applicant to line up their face with the on-screen frame, and the check returns pass or fail. The check confirms a live person is present before the face is compared with the stored portrait.

## Terms to know

- **Liveness detection:** a check that the face in front of the camera belongs to a live person, not a picture.
- **Field verification:** the visit to the applicant.
