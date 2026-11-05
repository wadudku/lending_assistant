---
id: concept.BR-LOS-197
type: concept
title: A repeat inquiry for the same applicant reuses the kept response
summary: Repeat inquiries for the same applicant within a configurable window reuse the retained response instead of asking the bureau again.
br_ids: [BR-LOS-197]
brd_section: 6.8
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-197"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p42"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.8"
related: [bridge.BR-LOS-197, concept.BR-LOS-196]
version: 1
status: approved
approved_by: Owner
---
**In short:** Repeat inquiries for the same applicant within a configurable window reuse the retained response instead of asking the bureau again.

## What the rule says

BR-LOS-197 (Must, BRD 6.8, PDF page 42) says that repeat inquiries against the same applicant within a configurable window "shall reuse the retained response rather than generating a new bureau inquiry". The BRD gives the purpose in the same sentence: "to control cost and inquiry-footprint effects". The length of the window is configurable and this row gives no figure.

## Why the bank wants it

The BRD gives the reason in the row on PDF page 42: "to control cost and inquiry-footprint effects".

## Example

An applicant's application is sent for bureau verification a second time within the configured window. The platform uses the response it already holds, and no new inquiry goes to the bureau.

## Terms to know

- **Window:** the configurable period within which a repeat inquiry reuses the kept response.
- **Inquiry footprint:** the BRD's phrase for the effect of making an inquiry; it does not define it further.
