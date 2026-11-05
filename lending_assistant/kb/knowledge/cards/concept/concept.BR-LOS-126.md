---
id: concept.BR-LOS-126
type: concept
title: Account checks run in the background and show progress
summary: "Validation runs as a queued background process; the partner sees progress, an estimated finish time and each row's state, can leave and return, and is notified when the batch finishes."
br_ids: [BR-LOS-126]
brd_section: 6.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-126"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p32"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p32"
related: [bridge.BR-LOS-126, glossary.rpa, glossary.cbs]
version: 1
status: approved
approved_by: Owner
---
**In short:** Validation runs as a queued background process; the partner sees progress, an estimated finish time and each row's state, can leave and return, and is notified when the batch finishes.

## What the rule says

BR-LOS-126 (Must, BRD 6.3, PDF page 32) says validation runs as a queued background process. On upload the partner is shown the batch's validation progress, an expected completion time and a per-row state, can leave the screen and return, and is notified when the batch reaches a terminal validation state. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD gives the reason in the 6.3 introduction: the CBS has no programmatic interface, so the check is done by robotic process automation driving the CBS enquiry screens. That makes validation a queued background process rather than an instant one (PDF page 32).

## Example

A partner uploads 500 rows and sees “120 of 500 checked, expected finish 15:40”. It closes the page, returns later, and has also received a message that the batch is complete.

## Terms to know

- **Queued:** waiting in line to be processed.
- **Per-row state:** the status of each application row: waiting, passed, failed.
- **Terminal state:** a final state: nothing more will happen.
- **RPA:** software that works a screen as a person would. See `glossary.rpa`.
