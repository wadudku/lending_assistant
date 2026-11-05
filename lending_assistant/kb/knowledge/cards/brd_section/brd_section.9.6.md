---
id: brd_section.9.6
type: brd_section
title: BRD 9.6 Electronic KYC and identity
summary: "Section 9.6 sets five rules for checking applicant identity: the election database check, liveness, face comparison, protection of images and behaviour when verification is down."
br_ids: []
brd_section: 9.6
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#9.6"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p64"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p65"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-040"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-041"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-042"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-043"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-044"
related: [brd_section.9, brd_section.9.1, brd_section.7, glossary.ecdb, glossary.ekyc]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 9.6 sets five rules for checking applicant identity: the election database check, liveness, face comparison, protection of images and behaviour when verification is down.

## What this section says

BRD 9.6 (PDF pages 64 and 65) has 5 requirements, all Must. BR-INT-040: identity is verified against the Election Commission Database for every submitted application, returning a demographic match, a portrait and a verification reference; the portrait is kept for face matching at field verification. BR-INT-041: liveness detection shows the applicant is physically present at field verification. BR-INT-042: the live capture is face-matched against the retained portrait, and the confidence score is retained. BR-INT-043: identity images and portraits are encrypted at rest, access-logged and retained under bank policy. BR-INT-044 (PDF page 65): where verification is unavailable, the application holds rather than fails, with automatic retry.

## Why the bank wants it

The BRD doesn't say why in this section as a whole; the usual reason is that the bank must be sure the applicant is who they say they are. Row 040 states a reason for keeping the portrait: face matching at field verification (PDF page 64).

## How it meets Frappe Lending

The team's analysis covered Section 7 only. This section holds 5 requirement rows and none was analysed, so the team makes no statement about them. For the Section 7 totals, see `brd_section.7`.

## Related cards

Parent: `brd_section.9`. The inventory that lists the Election Commission Database: `brd_section.9.1`.
