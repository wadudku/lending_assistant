---
id: concept.BR-LMS-155
type: concept
title: "One person prepares, another approves"
summary: "A repricing run needs two people: a maker creates it and an independent checker approves it before any loan is changed."
br_ids: [BR-LMS-155]
brd_section: 7.6
doctypes: []
verdict: gap
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-155"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p50"
  - "sources/verification/reqs.json#BR-LMS-155"
  - "sources/verification/verification_report.md#BR-LMS-155"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-155"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-155"
related: [bridge.BR-LMS-155, brd_section.7.6, glossary.maker-checker, glossary.repricing]
version: 1
status: approved
approved_by: Owner
---
**In short:** A repricing run needs two people: a maker creates it and an independent checker approves it before any loan is changed.

## What the rule says

BR-LMS-155 (priority Must, BRD 7.6, PDF page 50) says execution requires maker-checker: a maker creates the repricing run, and an independent checker approves it before any loan is changed.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a rate change on many loans moves real money, so no single person should be able to prepare and approve it.

## Example

Officer A prepares the run. Manager B reviews the dry run and approves it. Officer A cannot approve their own run.

## Terms to know

- **Maker:** the person who prepares the change.
- **Checker:** the independent person who approves it. See `glossary.maker-checker`.
- **Run:** one repricing batch.
- **Before any loan is changed:** the approval comes first, so a prepared run changes nothing until the checker accepts it.
- **Independent:** the checker is a different person from the maker.
