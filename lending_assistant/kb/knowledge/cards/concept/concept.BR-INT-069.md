---
id: concept.BR-INT-069
type: concept
title: "When the automation is down, the step pauses and retries"
summary: "When the automation is unavailable the affected step pauses with a clear message and retries by itself; it never fails an application, corrupts a loan's state or invents an outcome."
br_ids: [BR-INT-069]
brd_section: 9.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-069"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p63"
related: [bridge.BR-INT-069, glossary.rpa, glossary.cbs]
version: 1
status: approved
approved_by: Owner
---
**In short:** When the automation is unavailable the affected step pauses with a clear message and retries by itself; it never fails an application, corrupts a loan's state or invents an outcome.

## What the rule says

BR-INT-069 (Must, BRD 9.3, PDF page 63) says that where the automation is unavailable, the affected step pauses with clear user messaging and automatic retry. It never fails an application, never corrupts a loan's state, and never produces an outcome the core banking system did not give.

## Why the bank wants it

The BRD gives its reason in the intro to 9.3: the automation's “failure stops both origination and servicing” (PDF page 62).

## Example

The automation is down at 2 p.m. An officer who submits a payout sees a message that the step is waiting. The step retries on its own and goes through when the automation is back; the application is not rejected.

## Terms to know

- **Pause:** stop and wait without discarding the work.
- **Automatic retry:** trying again without a person asking.
- **Corrupt a state:** leave a record in a wrong or half-changed condition.
