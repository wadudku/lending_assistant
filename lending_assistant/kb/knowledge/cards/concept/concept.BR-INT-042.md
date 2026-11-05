---
id: concept.BR-INT-042
type: concept
title: Compare the live face with the stored portrait and keep the score
summary: The platform compares the live capture with the retained portrait by face matching and keeps the confidence score against the application.
br_ids: [BR-INT-042]
brd_section: 9.6
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-042"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p64"
related: [bridge.BR-INT-042]
version: 1
status: approved
approved_by: Owner
---
**In short:** The platform compares the live capture with the retained portrait by face matching and keeps the confidence score against the application.

## What the rule says

BR-INT-042 (Must, BRD 9.6, PDF page 64) says the platform verifies applicant identity by face-matching the live capture against the retained portrait. It returns a confidence score, which is retained against the application.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the portrait from the election database is the trusted reference, and a score records how closely the person in front of the officer agrees with it.

## Example

The live photo is compared with the stored portrait and gets a score of 93 out of 100. The score is saved with the application, so a reviewer can see how close the match was.

## Terms to know

- **Face matching:** comparing two face images.
- **Confidence score:** a number saying how sure the comparison is.
