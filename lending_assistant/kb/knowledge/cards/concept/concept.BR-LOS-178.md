---
id: concept.BR-LOS-178
type: concept
title: Evidence cannot be changed once sent; a correction is a new capture
summary: "Once evidence has been synchronised it is fixed. A correction needs a new capture, both are kept, and the audit trail shows their order."
br_ids: [BR-LOS-178]
brd_section: 6.7.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-178"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p41"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.7.3"
related: [bridge.BR-LOS-178, concept.BR-LOS-176]
version: 1
status: approved
approved_by: Owner
---
**In short:** Once evidence has been synchronised it is fixed. A correction needs a new capture, both are kept, and the audit trail shows their order.

## What the rule says

BR-LOS-178 (Must, BRD 6.7.3, PDF page 41) says "evidence shall be immutable once synchronised". "A correction shall require a new capture, with both retained and the sequence visible in the audit trail." The first capture is never overwritten or deleted.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that evidence that could be edited afterwards would be weak proof, so a correction is made as a second capture and the first stays on record.

## Example

An officer notices the stored signature is smudged after it has been synchronised. The officer cannot edit it. A new signature is captured. Both images are kept, and the audit trail shows that the second came after the first.

## Terms to know

- **Immutable:** cannot be changed.
- **Audit trail:** the record of what was captured and done, with its sequence.
