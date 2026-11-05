---
id: concept.BR-LOS-111
type: concept
title: A bad upload file is rejected whole
summary: "If a partner's application file has the wrong format, wrong columns or too many rows, the whole file is refused with a clear reason, and nothing from it is loaded."
br_ids: [BR-LOS-111]
brd_section: 6.2
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-111"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p30"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p29"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-110"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-113"
related: [bridge.BR-LOS-111]
version: 1
status: approved
approved_by: Owner
---
**In short:** If a partner's application file has the wrong format, wrong columns or too many rows, the whole file is refused with a clear reason, and nothing from it is loaded.

## What the rule says

BR-LOS-111 (Must, BRD 6.2, PDF page 30) says a structurally invalid file is rejected in its entirety with a clear reason. A file is structurally invalid if its format is wrong, its columns are wrong or reordered, or its row count is above the configured or partner-specific ceiling. "There shall be no partial ingestion." This is an origination rule (the LOS side of the BRD, section 6), not a servicing rule.

## Why the bank wants it

The BRD gives the context in the introduction to 6.2: bulk submission "carries the greatest data quality risk in origination", and the aim is that a partner operations user, without banking knowledge, can find and correct every defect in a file without escalation to the bank (PDF page 29). The BRD doesn't say why a bad file is refused whole; the usual reason is that a half-loaded file leaves the partner unsure which rows went in, and loading the corrected file again could create duplicates. Row errors are the subject of the next rules in 6.2 (BR-LOS-113).

## Example

A partner uploads a file whose columns are in a different order from the template. The system rejects the whole file with a message naming the wrong column. No application from the file is created. The partner fixes the order and uploads again.

## Terms to know

- **Ingestion:** loading file contents into the system. For a bad file, the BRD allows no rows at all to be loaded.
- **Template:** the file layout the platform issues, versioned (see BR-LOS-110).
- **Partner:** an outside organisation that sends applications to the bank.
- **Structurally invalid:** wrong at file level (format, columns, row count), as opposed to a wrong value in one row.
