---
id: concept.BR-GOV-021
type: concept
title: A partner's users see only their own partner's data
summary: "A partner's users can reach only their own organisation's data, and cannot see, work out or export another partner's data by any route, including error messages."
br_ids: [BR-GOV-021]
brd_section: 4.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-021"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p23"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p23"
related: [bridge.BR-GOV-021, glossary.partner, concept.BR-GOV-020]
version: 1
status: approved
approved_by: Owner
---
**In short:** A partner's users can reach only their own organisation's data, and cannot see, work out or export another partner's data by any route, including error messages.

## What the rule says

BR-GOV-021 (Must, BRD 4.3, PDF page 23) says partner users are scoped to their own partner organisation. No partner user can view, infer or export data belonging to another partner under any circumstance, including through search, reporting, export or error messages.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that partners are separate businesses, some of them competitors, and their customers' data is confidential to each.

## Example

A user of partner A searches for a borrower's name that belongs to partner B. The search returns nothing, and the report totals show only partner A's loans. A mistyped reference does not produce a message that reveals partner B's record exists.

## Terms to know

- **Partner:** an outside organisation that sends applications or co-lends with the bank. See `glossary.partner`.
- **Scoped:** limited to one organisation's own data.
- **Infer:** work out something from clues, such as a count or an error message.
