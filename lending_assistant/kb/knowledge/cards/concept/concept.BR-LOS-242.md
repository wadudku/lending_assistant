---
id: concept.BR-LOS-242
type: concept
title: "Origination reports can be exported, scheduled and emailed"
summary: "Origination reports can be exported to XLSX and CSV, run on a schedule, and sent to chosen recipients by email."
br_ids: [BR-LOS-242]
brd_section: 8.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-242"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p57"
related: [bridge.BR-LOS-242]
version: 1
status: approved
approved_by: Owner
---
**In short:** Origination reports can be exported to XLSX and CSV, run on a schedule, and sent to chosen recipients by email.

## What the rule says

BR-LOS-242 (Must, BRD 8.1, PDF page 57) says reports are exportable to XLSX and CSV, schedulable, and deliverable to configured recipients by email. It applies to the origination reports of section 8.1.

## Why the bank wants it

The BRD gives one general reason for the whole of Section 8: “Reporting is not a by-product of this programme; for several stakeholders it is the programme. Credit Risk, Finance, Compliance and Internal Audit each need a view that the current process cannot produce reliably at volume.” (PDF page 57). The BRD doesn't say why this row is needed; the usual reason is that the readers of a report are often not system users, so the report has to reach them as a file or an email on a fixed rhythm.

## Example

Every Monday at 7 a.m. the approval funnel report is produced on its own and emailed to a list of five people as an XLSX file. One of them also exports the same report to CSV to load it into another tool.

## Terms to know

- **XLSX:** the file format of a Microsoft Excel workbook.
- **CSV:** a plain text file of rows with values separated by commas.
- **Schedulable:** can be set to run by itself at chosen times.
- **Recipient:** a person or mailbox the report is sent to.
