---
id: concept.BR-LOS-193
type: concept
title: The full bureau response is kept centrally and seen only by permitted Bank users
summary: "The full bureau response is kept centrally and shown only to separately permissioned Bank users in a dedicated panel, and every view is logged."
br_ids: [BR-LOS-193]
brd_section: 6.8
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-193"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p42"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.8"
related: [bridge.BR-LOS-193, concept.BR-LOS-191, concept.BR-LOS-196]
version: 1
status: approved
approved_by: Owner
---
**In short:** The full bureau response is kept centrally and shown only to separately permissioned Bank users in a dedicated panel, and every view is logged.

## What the rule says

BR-LOS-193 (Must, BRD 6.8, PDF page 42) says the full bureau response "shall be retained centrally" and "visible only to separately permissioned Bank users", in a dedicated panel. The panel shows seven things: "inquiry timestamp, inquiry reference, evaluated outcome, decision rule version applied, existing exposure across institutions, classification status and overdue history". "Every view shall be logged with user, application and timestamp." So the data is kept in one central place, only specially permitted users can open it, and each opening leaves a record with three items.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the bank needs to keep the bureau answer for later checks while keeping it away from the officer, and a log of views shows who looked at sensitive data.

## Example

A Bank user who has the separate permission opens the panel for an application. They see the inquiry time and reference, the outcome, the rule version, the exposure across institutions, the classification status and the overdue history. The view is logged with their user, the application and the time.

## Terms to know

- **Separately permissioned:** given a permission of its own, as the BRD says; the BRD does not name it.
- **Dedicated panel:** the screen the BRD describes, with the seven items listed above.
