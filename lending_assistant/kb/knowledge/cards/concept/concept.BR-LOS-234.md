---
id: concept.BR-LOS-234
type: concept
title: Reference data can be changed without a software release
summary: "Reference data such as districts, upazilas, loan purposes, rejection reason codes and supplementary field definitions can be maintained without a software release."
br_ids: [BR-LOS-234]
brd_section: 6.11
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-234"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p45"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.11"
related: [bridge.BR-LOS-234, concept.BR-LOS-172]
version: 1
status: approved
approved_by: Owner
---
**In short:** Reference data such as districts, upazilas, loan purposes, rejection reason codes and supplementary field definitions can be maintained without a software release.

## What the rule says

BR-LOS-234 (Must, BRD 6.11, PDF page 45) says reference data "shall be maintainable without a software release". The BRD names five kinds: districts, upazilas, loan purposes, rejection reason codes and supplementary field definitions.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that these lists change from time to time, and the bank should not have to wait for a new release of the software to change them.

## Example

A new loan purpose is needed. An authorised user adds it to the reference data, and it can be used without a software release.

## Terms to know

- **Upazila:** one of the five kinds of reference data the BRD lists; it does not define it.
- **Supplementary field definitions:** the definitions of the extra fields in BR-LOS-172.
