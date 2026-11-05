---
id: concept.BR-LMS-242
type: concept
title: "Servicing reports can be exported, scheduled and sent"
summary: "Servicing reports can be exported to XLSX and CSV, run on a schedule, and delivered to chosen recipients."
br_ids: [BR-LMS-242]
brd_section: 8.2
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-242"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p58"
related: [bridge.BR-LMS-242]
version: 1
status: approved
approved_by: Owner
---
**In short:** Servicing reports can be exported to XLSX and CSV, run on a schedule, and delivered to chosen recipients.

## What the rule says

BR-LMS-242 (Must, BRD 8.2, PDF page 58) says reports are exportable to XLSX and CSV, schedulable, and deliverable to configured recipients. The id carries the LMS prefix, but the row sits in Section 8.2, outside the 103 requirements of Section 7. Unlike BR-LOS-242 it does not say “by email”.

## Why the bank wants it

The BRD gives one general reason for the whole of Section 8: “Reporting is not a by-product of this programme; for several stakeholders it is the programme. Credit Risk, Finance, Compliance and Internal Audit each need a view that the current process cannot produce reliably at volume.” (PDF page 57). The BRD doesn't say why this row is needed; the usual reason is that the readers of a servicing report are often outside the system, so it has to reach them as a file on a fixed rhythm.

## Example

On the first working day of each month the provisioning report is produced on its own and delivered to the Finance mailbox as an XLSX file. A risk analyst also exports the delinquency report to CSV for a separate calculation.

## Terms to know

- **XLSX:** the file format of a Microsoft Excel workbook.
- **CSV:** a plain text file of rows with values separated by commas.
- **Schedulable:** can be set to run by itself at chosen times.
