---
id: glossary.nid
type: glossary
title: NID (National Identity Document)
summary: "The national identity document, whose number identifies a person for duplicate checks and identity verification."
br_ids: []
brd_section: 1.5
doctypes: []
dev_items: []
terms: [nid, national identity document]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#1.5"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-116"
related: [glossary.ecdb, concept.BR-LOS-116, brd_section.6.2.2]
version: 1
status: approved
approved_by: Owner
---
**In short:** The national identity document, whose number identifies a person for duplicate checks and identity verification.

## Plain meaning

The BRD defines NID as the National Identity Document (BRD 1.5). In the application field list the NID number is 10, 13 or 17 digits (BRD 6.2.2).

## Example

Two rows in a file carry the same NID number. Duplicate detection flags both for the partner to resolve (BR-LOS-116).

## Why it matters here

The NID is a match field for duplicates (BR-LOS-116) and the key for identity verification against the ECDB. The team has analysed only the LMS requirements (Section 7). The LOS requirements have not been analysed.

## See also

`glossary.ecdb`, `concept.BR-LOS-116`, `brd_section.6.2.2`.
