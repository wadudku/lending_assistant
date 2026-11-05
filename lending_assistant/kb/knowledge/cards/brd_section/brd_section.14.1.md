---
id: brd_section.14.1
type: brd_section
title: BRD 14.1 Origination acceptance conditions
summary: "Section 14.1 gives 30 acceptance conditions for origination, from account validation and sampling to scoring, sanction and funding."
br_ids: []
brd_section: 14.1
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#14.1"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p75"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p76"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p77"
related: [brd_section.14, brd_section.14.2]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 14.1 gives 30 acceptance conditions for origination, from account validation and sampling to scoring, sanction and funding.

## What this section says

BRD 14.1 (PDF pages 75 to 77) has 30 acceptance conditions: AC-01 to AC-09 (9), AC-10 and AC-10a to AC-10k (12), AC-11 to AC-13 (3), AC-14 and AC-14a to AC-14d (5), and AC-15 (1). They cover validating a row against a Core Banking System account, batch validation within a time, sampling and its reproduction, the scorecard, sanction and approval limits, bureau data kept off the device, and funding with the automation. Example AC-03 reads: “Given the Core Banking System returns a server error for a row, when the row is validated, then the row is held pending rather than failed, and is retried automatically.” (PDF page 75). The team has not tested these conditions.

## Why the bank wants it

The BRD gives the reason for all of Section 14 in its opening (PDF page 75): the conditions are “written so that a business tester, not a developer, can determine whether the condition is met”.

## How it meets Frappe Lending

This section holds no requirement row, so there is nothing in it to compare with Frappe Lending, and the team has made no statement about it. The team has not tested the acceptance criteria and says nothing here about whether any is met.

## Related cards

Parent: `brd_section.14`. Next: `brd_section.14.2`.
