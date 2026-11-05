---
id: concept.BR-INT-040
type: concept
title: Verify each applicant's identity against the Election Commission Database
summary: "The platform verifies each applicant against the Election Commission Database, returning a demographic agreement, a portrait and a verification reference, and keeps the portrait for face comparison."
br_ids: [BR-INT-040]
brd_section: 9.6
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-040"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p64"
related: [bridge.BR-INT-040, glossary.ecdb, glossary.nid]
version: 1
status: approved
approved_by: Owner
---
**In short:** The platform verifies each applicant against the Election Commission Database, returning a demographic agreement, a portrait and a verification reference, and keeps the portrait for face comparison.

## What the rule says

BR-INT-040 (Must, BRD 9.6, PDF page 64) says the platform verifies applicant identity against the Election Commission Database for every submitted application. It returns a demographic match, a portrait and a verification reference. The returned portrait is retained for face matching at field verification.

## Why the bank wants it

The BRD gives the reason for keeping the portrait in the row: it is “retained for face matching at field verification” (PDF page 64). It doesn't say why every application is checked; the usual reason is that the bank must know the applicant is the person named.

## Example

An application arrives with a national identity number. The platform asks the Election Commission Database, which returns that the name and date of birth agree, a photo and a reference number. The photo is kept so that, at the field visit, it can be compared with the person present.

## Terms to know

- **Demographic match:** the personal details given agree with the database's.
- **Portrait:** the photo returned for the person.
- **Verification reference:** the number identifying this check.
- **Field verification:** the visit to the applicant.
