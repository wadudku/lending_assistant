---
id: concept.BR-LOS-175
type: concept
title: A liveness check compares the live face with the retained portrait
summary: "The app checks that the applicant is a live person by camera, returns pass or fail with limited retries, and compares the live image with the retained portrait."
br_ids: [BR-LOS-175]
brd_section: 6.7.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-175"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p41"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.7.3"
related: [bridge.BR-LOS-175, concept.BR-LOS-174]
version: 1
status: approved
approved_by: Owner
---
**In short:** The app checks that the applicant is a live person by camera, returns pass or fail with limited retries, and compares the live image with the retained portrait.

## What the rule says

BR-LOS-175 (Must, BRD 6.7.3, PDF page 41) says a liveness check "shall be performed by camera capture with on-screen alignment guidance, returning pass or fail, with retry up to a configured attempt limit". The live image "shall be face-matched against the retained national database portrait". The number of tries allowed is a setting.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a photo of a photo, or of someone else, should not pass; a live capture matched to the national database portrait ties the person at the meeting to the identity on file.

## Example

The applicant looks into the camera and follows the on-screen guide to line up the face. The first try fails and the officer retries. The second try returns pass, and the live image is matched to the portrait kept from the national database.

## Terms to know

- **Liveness check:** the camera check in this row that returns pass or fail.
- **Attempt limit:** the configured number of retries allowed.
- **Face-match:** comparing the live image with the retained portrait.
