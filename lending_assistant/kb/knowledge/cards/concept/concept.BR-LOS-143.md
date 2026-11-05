---
id: concept.BR-LOS-143
type: concept
title: The review queue is driven from the keyboard and shows how many remain
summary: The review queue can be driven from the keyboard and shows the number of applications remaining.
br_ids: [BR-LOS-143]
brd_section: 6.5.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-143"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p37"
related: [bridge.BR-LOS-143, concept.BR-LOS-142]
version: 1
status: approved
approved_by: Owner
---
**In short:** The review queue can be driven from the keyboard and shows the number of applications remaining.

## What the rule says

BR-LOS-143 (Should, BRD 6.5.1, PDF page 37) says the queue supports keyboard navigation and displays the number of applications remaining. This is a Should requirement. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD gives the reason in the 6.5.1 introduction: the review screen must be designed for throughput, so that a reviewer working several hundred applications can reach a defensible decision on each in well under a minute (PDF page 36).

## Example

A reviewer works through 300 applications. They move from one to the next with the keyboard, and a counter at the top says “212 remaining”.

## Terms to know

- **Queue:** the list of cases waiting for a reviewer.
- **Keyboard navigation:** moving and acting without the mouse.
- **Throughput:** how many cases a reviewer can finish in a period.
- **Should:** a requirement with priority Should, not Must.
