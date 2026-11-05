---
id: concept.BR-LOS-113
type: concept
title: Every row is checked and results are sorted into three groups
summary: "Each row is validated, results are shown as valid, invalid-and-correctable, and duplicate, and every error names the field and gives a reason the partner can act on."
br_ids: [BR-LOS-113]
brd_section: 6.2
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-113"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p30"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-116"
related: [bridge.BR-LOS-113, concept.BR-LOS-116]
version: 1
status: approved
approved_by: Owner
---
**In short:** Each row is validated, results are shown as valid, invalid-and-correctable, and duplicate, and every error names the field and gives a reason the partner can act on.

## What the rule says

BR-LOS-113 (Must, BRD 6.2, PDF page 30) says every row is validated for field-level correctness. Results are presented in three groups: valid, invalid and correctable, and duplicate. Each error names the offending field and states the reason in language a partner operations user can act on. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a partner clerk can fix a file quickly only if each message says which cell is wrong and what is wrong with it.

## Example

After upload the partner sees 480 valid rows, 15 invalid rows and 5 duplicates. One invalid row says: “Mobile number: must be 11 digits; found 10.”

## Terms to know

- **Field-level validation:** a check of each single value, such as a date or a number.
- **Correctable:** an error the partner can fix and send again.
- **Duplicate:** a row that repeats a person or account already seen. See BR-LOS-116.
- **Operations user:** a partner staff member who handles the files.
