---
id: concept.BR-LOS-127
type: concept
title: Check requests are queued and paced to what the bank's system can take
summary: "Validation requests are queued and rate-limited to what the core system and the automation can sustain, and a long queue is never shown to the partner as an error."
br_ids: [BR-LOS-127]
brd_section: 6.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-127"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p32"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-126"
related: [bridge.BR-LOS-127, glossary.cbs, glossary.rpa, concept.BR-LOS-126]
version: 1
status: approved
approved_by: Owner
---
**In short:** Validation requests are queued and rate-limited to what the core system and the automation can sustain, and a long queue is never shown to the partner as an error.

## What the rule says

BR-LOS-127 (Must, BRD 6.3, PDF page 32) says validation requests are queued and rate-limited to the throughput the CBS and the available automation capacity can sustain. Queue depth never surfaces to the partner as an error. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD gives the reason in the 6.3 introduction: the check is done by automation driving the CBS enquiry screens, so only so many can run at a time (PDF page 32).

## Example

A partner uploads 5,000 rows when the automation can check 100 an hour. The batch waits in line and the partner sees “in progress”, not an error about the length of the queue.

## Terms to know

- **Rate limit:** a cap on how many requests are sent per period.
- **Throughput:** how much work can be done in a period.
- **Queue depth:** how many requests are waiting.
- **CBS:** the bank's core banking system. See `glossary.cbs`.
