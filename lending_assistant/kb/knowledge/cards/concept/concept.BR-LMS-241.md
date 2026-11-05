---
id: concept.BR-LMS-241
type: concept
title: Every report states when and how it was produced
summary: "Every report states the date and time it was generated, the parameters used and the data cut-off applied."
br_ids: [BR-LMS-241]
brd_section: 8.2
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-241"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p58"
related: [bridge.BR-LMS-241]
version: 1
status: approved
approved_by: Owner
---
**In short:** Every report states the date and time it was generated, the parameters used and the data cut-off applied.

## What the rule says

BR-LMS-241 (Must, BRD 8.2, PDF page 58) says every report states when it was generated, the parameters used to produce it and the data cut-off applied. The id carries the LMS prefix, but the row sits in Section 8.2, outside the 103 requirements of Section 7.

## Why the bank wants it

The BRD gives one general reason for the whole of Section 8: “Reporting is not a by-product of this programme; for several stakeholders it is the programme. Credit Risk, Finance, Compliance and Internal Audit each need a view that the current process cannot produce reliably at volume.” (PDF page 57). The BRD doesn't say why this row is needed; the usual reason is that two copies of one report can differ only because they were run at different times or with different settings, and the header lets a reader tell which is which.

## Example

A finance officer receives a repayment report and later a second copy with different totals. The header of each states the time it was produced, the date range and branch it was run for, and that the data stopped at the end of the previous day. The difference is explained by the cut-off.

## Terms to know

- **Parameters:** the choices made when the report was run, such as the date range or branch.
- **Data cut-off:** the point in time after which new data is not in the report.
