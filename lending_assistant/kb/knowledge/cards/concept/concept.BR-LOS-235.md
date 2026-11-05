---
id: concept.BR-LOS-235
type: concept
title: Configuration can be exported and imported between environments
summary: "Configuration can be exported and imported between environments, so a change can be promoted from test to production in a controlled way. This one is a Should."
br_ids: [BR-LOS-235]
brd_section: 6.11
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-235"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p45"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.11"
related: [bridge.BR-LOS-235, concept.BR-LOS-232]
version: 1
status: approved
approved_by: Owner
---
**In short:** Configuration can be exported and imported between environments, so a change can be promoted from test to production in a controlled way. This one is a Should.

## What the rule says

BR-LOS-235 (Should, BRD 6.11, PDF page 45) says configuration "shall be exportable and importable between environments to support controlled promotion from test to production". So there are two directions, out of one environment and into another, and the purpose the BRD gives is controlled promotion. Its priority is Should, not Must.

## Why the bank wants it

The BRD gives the reason in the row on PDF page 45: "to support controlled promotion from test to production".

## Example

A new product setting is tried in a test environment. Once it is as wanted, it is exported from test and imported into production.

## Terms to know

- **Environment:** the BRD names test and production; it does not define the word.
- **Promotion:** the BRD's word in "controlled promotion from test to production"; it does not define it further.
