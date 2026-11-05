---
id: concept.BR-LOS-112
type: concept
title: File size and row limits are shown before upload
summary: "The upload screen states the file size limit and the row count limit up front, so the partner does not learn them only from an error."
br_ids: [BR-LOS-112]
brd_section: 6.2
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-112"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p30"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-111"
related: [bridge.BR-LOS-112, concept.BR-LOS-111]
version: 1
status: approved
approved_by: Owner
---
**In short:** The upload screen states the file size limit and the row count limit up front, so the partner does not learn them only from an error.

## What the rule says

BR-LOS-112 (Must, BRD 6.2, PDF page 30) says file size and row count limits are stated on screen before upload, not only in the resulting error. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a partner who knows the limits can split a file in advance and avoid a rejected upload.

## Example

Before choosing a file, the partner reads: “Maximum 5 MB and 500 rows.” A file of 800 rows is split in two before upload, instead of being rejected after the wait.

## Terms to know

- **Row count:** the number of applications (rows) in the file.
- **Limit:** the highest size or count allowed.
- **Upload screen:** the page where the partner selects and sends the file.
- **Rejected:** refused as a whole. See BR-LOS-111.
