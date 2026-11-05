---
id: concept.BR-LOS-114
type: concept
title: Wrong rows can be fixed in the browser or exported for offline correction
summary: "Invalid rows can be edited in the browser, re-checked one by one without re-uploading the batch, and exported as a corrections file for offline handling."
br_ids: [BR-LOS-114]
brd_section: 6.2
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-114"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p30"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-113"
related: [bridge.BR-LOS-114, glossary.batch, concept.BR-LOS-113]
version: 1
status: approved
approved_by: Owner
---
**In short:** Invalid rows can be edited in the browser, re-checked one by one without re-uploading the batch, and exported as a corrections file for offline handling.

## What the rule says

BR-LOS-114 (Must, BRD 6.2, PDF page 30) says invalid rows are editable in the browser, individually re-validatable without re-uploading the batch, and exportable as a corrections file for offline handling. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that sending a whole file again for a few bad rows wastes time and risks new errors.

## Example

Twelve rows fail. The partner fixes three in the browser and re-checks them at once. The other nine are exported as a corrections file and fixed outside the platform.

## Terms to know

- **Re-validate:** run the checks again on one row.
- **Corrections file:** a file of the invalid rows, for fixing outside the platform.
- **Offline:** outside the platform.
- **Batch:** a group of applications sent together. See `glossary.batch`.
