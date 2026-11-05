---
id: concept.BR-INT-066
type: concept
title: The automation is monitored and alerts on repeated failure
summary: "The automation is monitored continuously for availability, queue depth, transaction duration, failure rate and interface change, and alerts on consecutive failures."
br_ids: [BR-INT-066]
brd_section: 9.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-066"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p63"
related: [bridge.BR-INT-066, glossary.rpa]
version: 1
status: approved
approved_by: Owner
---
**In short:** The automation is monitored continuously for availability, queue depth, transaction duration, failure rate and interface change, and alerts on consecutive failures.

## What the rule says

BR-INT-066 (Must, BRD 9.3, PDF page 63) says the automation is monitored continuously for five things: availability, queue depth, transaction duration, failure rate and interface change. It alerts on consecutive failures rather than degrading silently.

## Why the bank wants it

The BRD gives the reason in the intro to 9.3: the automation “holds banking credentials, it moves money, and its failure stops both origination and servicing” (PDF page 62). The row adds “rather than degrading silently”.

## Example

Three payouts in a row fail on the same screen. An alert goes to the operations team at once with the queue depth and the failure rate, so they act before the queue of waiting loans grows.

## Terms to know

- **Queue depth:** how many items are waiting.
- **Failure rate:** the share of transactions that fail.
- **Interface change:** a change in the screens the automation drives.
