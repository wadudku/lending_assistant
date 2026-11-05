---
id: brd_section.14.2
type: brd_section
title: BRD 14.2 Servicing acceptance conditions
summary: "Section 14.2 gives 18 acceptance conditions for servicing, from the funded-loan handoff to case-file reproduction."
br_ids: []
brd_section: 14.2
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#14.2"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p75"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p77"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p78"
related: [brd_section.14, brd_section.14.1]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 14.2 gives 18 acceptance conditions for servicing, from the funded-loan handoff to case-file reproduction.

## What this section says

BRD 14.2 (PDF pages 77 and 78) has 18 acceptance conditions: AC-20 to AC-23 (4), AC-24, AC-24a and AC-24b (3), and AC-25 to AC-35 (11). They cover the handoff and booking, payment allocation, value dating, prepayment, repricing, classification, suspense, write-off and recovery, closure, restarting a failed batch, end-of-day reconciliation and reproducing a loan's state at a past date. Example AC-21 reads: “Given the same handoff is transmitted twice, when the second is processed, then the original booked loan is returned and no second loan is created.” (PDF page 77). The team has not tested these conditions.

## Why the bank wants it

The BRD gives the reason for all of Section 14 in its opening (PDF page 75): the conditions are “written so that a business tester, not a developer, can determine whether the condition is met”.

## How it meets Frappe Lending

This section holds no requirement row, so there is nothing in it to compare with Frappe Lending, and the team has made no statement about it. The team has not tested the acceptance criteria and says nothing here about whether any is met.

## Related cards

Parent: `brd_section.14`. Before it: `brd_section.14.1`.
