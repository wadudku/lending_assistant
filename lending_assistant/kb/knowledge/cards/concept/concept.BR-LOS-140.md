---
id: concept.BR-LOS-140
type: concept
title: A rejection needs a reason code from a list; free text is extra
summary: A rejection must carry a reason code chosen from a configurable list; free text may be added but never replaces the code.
br_ids: [BR-LOS-140]
brd_section: 6.5.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-140"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p37"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-145"
related: [bridge.BR-LOS-140, concept.BR-LOS-305, concept.BR-LOS-145]
version: 1
status: approved
approved_by: Owner
---
**In short:** A rejection must carry a reason code chosen from a configurable list; free text may be added but never replaces the code.

## What the rule says

BR-LOS-140 (Must, BRD 6.5.1, PDF page 37) says rejection requires a reason code selected from a configurable list. Free text is additional, never a substitute. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that coded reasons can be counted and compared across reviewers, partners and time, which free text cannot.

## Example

A reviewer rejects an application and picks “Income not supported by documents” from the list. They may add a note, but the form refuses to save without the code.

## Terms to know

- **Reason code:** a short coded reason picked from a list.
- **Configurable list:** a list the Bank can change without a software release.
- **Free text:** a note typed in the reviewer's own words.
- **Substitute:** something used in place of another.
