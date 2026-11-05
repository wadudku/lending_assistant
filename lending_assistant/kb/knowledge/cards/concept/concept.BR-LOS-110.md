---
id: concept.BR-LOS-110
type: concept
title: Applications come in as a versioned CSV or XLSX template
summary: "Partners send applications as a CSV or XLSX file in a template issued by the platform, downloadable from the upload screen, versioned, with the version recorded against each batch."
br_ids: [BR-LOS-110]
brd_section: 6.2
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-110"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p30"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-111"
related: [bridge.BR-LOS-110, glossary.batch, concept.BR-LOS-111]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partners send applications as a CSV or XLSX file in a template issued by the platform, downloadable from the upload screen, versioned, with the version recorded against each batch.

## What the rule says

BR-LOS-110 (Must, BRD 6.2, PDF page 30) says partner users submit applications as a CSV or XLSX file conforming to a platform-issued template. The template is downloadable from the upload screen, is versioned, and the version used is recorded against the batch for audit and for future format migration. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a fixed, versioned template lets the platform read every file the same way and still read old files after the format changes.

## Example

A partner downloads template version 2 from the upload screen, fills it in and uploads it. The batch record shows version 2. Later the template changes to version 3, and the Bank can still tell which batches used version 2.

## Terms to know

- **CSV / XLSX:** two common spreadsheet file formats.
- **Template:** a file layout the platform issues for partners to fill in.
- **Versioned:** each change to the template gets a new number.
- **Batch:** a group of applications sent together. See `glossary.batch`.
