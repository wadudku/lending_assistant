---
id: concept.BR-LOS-172
type: concept
title: Only the supplementary fields an application needs are shown
summary: "The app asks only for the extra fields that a given application requires, and the bank can change those fields without a software release."
br_ids: [BR-LOS-172]
brd_section: 6.7.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-172"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p41"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.7.3"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-234"
related: [bridge.BR-LOS-172]
version: 1
status: approved
approved_by: Owner
---
**In short:** The app asks only for the extra fields that a given application requires, and the bank can change those fields without a software release.

## What the rule says

BR-LOS-172 (Must, BRD 6.7.3, PDF page 41) says that "where the individual application requires supplementary fields, only those fields shall be presented". The definitions of the fields "shall be maintainable as reference data without a software release". So the list of extra fields is data the bank can edit, and an application does not show fields it does not need.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a short screen is quicker to complete at a busy meeting, and being able to change field definitions without a release avoids waiting for a new version of the app.

## Example

A product needs one extra field that another product does not. An officer working on the first application sees that field. On the second application the field does not appear. The bank adds a new field by editing reference data, and no new version of the app is issued.

## Terms to know

- **Supplementary fields:** the additional fields an individual application requires beyond the standard ones.
- **Reference data:** lists and definitions kept as data that can be changed without a software release.
