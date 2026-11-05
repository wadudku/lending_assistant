---
id: concept.BR-LMS-252
type: concept
title: Every regulatory extract is kept so a return can be reproduced
summary: "The platform keeps every regulatory extract it generates, with its parameters and the generating user, for the full retention period, so a submitted return can be reproduced exactly."
br_ids: [BR-LMS-252]
brd_section: 8.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-252"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p58"
related: [bridge.BR-LMS-252]
version: 1
status: approved
approved_by: Owner
---
**In short:** The platform keeps every regulatory extract it generates, with its parameters and the generating user, for the full retention period, so a submitted return can be reproduced exactly.

## What the rule says

BR-LMS-252 (Must, BRD 8.3, PDF page 58) says the platform retains every generated regulatory extract. It also keeps the parameters used and the generating user, for the full retention period. The aim stated in the BRD is that a submitted return can be reproduced exactly. The id carries the LMS prefix, but the row sits in Section 8.3, outside the 103 requirements of Section 7.

## Why the bank wants it

The BRD states the aim in the row itself: “so that a submitted return can be reproduced exactly” (PDF page 58). It doesn't say who will ask for a reproduction; the usual reason is an inspection or audit asking the bank to show exactly what it filed.

## Example

A year after filing, the regulator asks about one figure in a return. The bank opens the stored copy of that extract, sees who generated it, on what date and with which settings, and shows the figure as filed.

## Terms to know

- **Retention period:** how long the bank must keep a record.
- **Reproduce exactly:** produce the same figures again from the stored extract and settings.
