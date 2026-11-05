---
id: concept.BR-INT-072
type: concept
title: The daily reconciliation checks every instruction in both directions
summary: "Daily reconciliation compares every instruction the platform believes it issued with the transactions present in the core banking system, in both directions, and raises each difference as an exception."
br_ids: [BR-INT-072]
brd_section: 9.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-072"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p63"
related: [bridge.BR-INT-072, concept.BR-GOV-050, concept.BR-GOV-051, brd_section.8.4, glossary.cbs, glossary.idempotency]
version: 1
status: approved
approved_by: Owner
---
**In short:** Daily reconciliation compares every instruction the platform believes it issued with the transactions present in the core banking system, in both directions, and raises each difference as an exception.

## What the rule says

BR-INT-072 (Must, BRD 9.3, PDF page 63) says the daily reconciliation under Section 8.4 compares every instruction the platform believes it issued against the transactions actually present in the core banking system, in both directions. It raises every difference as an exception requiring documented closure.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that an instruction may have run without the platform knowing, or the platform may think one ran that did not, and only a two-way comparison finds both.

## Example

The platform issued 300 instructions today. The core banking system shows 299 of them and one more transaction the platform never sent. The reconciliation lists both differences as exceptions, and each is closed with a written reason.

## Terms to know

- **Both directions:** from the platform to the core banking system, and back.
- **Exception requiring documented closure:** a flagged difference that someone must close with a written reason.
- **Reconciliation:** see `concept.BR-GOV-050`.
