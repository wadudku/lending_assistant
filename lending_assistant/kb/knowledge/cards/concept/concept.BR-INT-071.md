---
id: concept.BR-INT-071
type: concept
title: Re-test the automation before any change to the core banking system
summary: "The automation is re-validated in a representative test environment before any core banking system change reaches production, and the bank gives advance notice of such changes."
br_ids: [BR-INT-071]
brd_section: 9.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-071"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p63"
related: [bridge.BR-INT-071, glossary.rpa, glossary.cbs]
version: 1
status: approved
approved_by: Owner
---
**In short:** The automation is re-validated in a representative test environment before any core banking system change reaches production, and the bank gives advance notice of such changes.

## What the rule says

BR-INT-071 (Must, BRD 9.3, PDF page 63) says the automation is re-validated against a representative test environment before any core banking system change, patch or upgrade reaches production. The bank gives advance notice of such changes.

## Why the bank wants it

The BRD gives the reason in section 9.2: the bank “must provide advance notice of any Core Banking System change, patch or upgrade, and a test environment in which the automation can be revalidated before that change reaches production” (PDF page 61).

## Example

The bank plans a patch for the first of next month and tells the supplier three weeks ahead. The supplier runs the automation against the patched test copy, fixes a moved field, and only then does the patch go live.

## Terms to know

- **Re-validated:** tested again to show it still works.
- **Test environment:** a copy of the system used for testing.
- **Patch:** a small change to fix or update software.
