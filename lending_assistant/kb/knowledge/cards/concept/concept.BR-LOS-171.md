---
id: concept.BR-LOS-171
type: concept
title: The officer confirms the applicant's KYC details or flags a difference
summary: "At the start the app shows the officer the applicant's KYC data, the national database result and the portrait, read-only, and the officer confirms or flags a discrepancy."
br_ids: [BR-LOS-171]
brd_section: 6.7.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-171"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p40"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p41"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.7.3"
related: [bridge.BR-LOS-171, concept.BR-LOS-160]
version: 1
status: approved
approved_by: Owner
---
**In short:** At the start the app shows the officer the applicant's KYC data, the national database result and the portrait, read-only, and the officer confirms or flags a discrepancy.

## What the rule says

BR-LOS-171 (Must, BRD 6.7.3, PDF pages 40 and 41) says that on initiation the application shall display the KYC data submitted at application, the national database verification outcome and the retained portrait, "read-only, for officer confirmation". The officer "shall confirm the data or flag a discrepancy". A flagged discrepancy routes the application back to the Bank for resolution and "shall not proceed to approval".

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the officer is the only person who can compare the applicant in front of them with the data, so the bank asks for that check and does not let a flagged case go on to approval.

## Example

An officer sees the portrait and the details held for an applicant, and the name on the screen is not the name the applicant gives. The officer flags a discrepancy. The application goes back to the Bank and cannot be approved until the Bank has resolved it.

## Terms to know

- **KYC data:** the identity details submitted at application, as the BRD calls them.
- **Retained portrait:** the portrait kept from the national database check.
- **Discrepancy:** a difference the officer flags between the data and the applicant.
