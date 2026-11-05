---
id: concept.BR-LOS-311
type: concept
title: A second scorecard can run quietly alongside the live one
summary: "The platform can run a second scorecard in shadow, recording its outcome without acting on it, so a new scorecard can be tested on live applications before adoption."
br_ids: [BR-LOS-311]
brd_section: 6.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-311"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p34"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-302"
related: [bridge.BR-LOS-311, concept.BR-LOS-302, glossary.scorecard]
version: 1
status: approved
approved_by: Owner
---
**In short:** The platform can run a second scorecard in shadow, recording its outcome without acting on it, so a new scorecard can be tested on live applications before adoption.

## What the rule says

BR-LOS-311 (Should, BRD 6.4, PDF page 34) says the platform supports running a second scorecard in shadow, recording its outcome without acting on it, so that a replacement or recalibrated scorecard can be validated against the live population before it is adopted. This is a Should requirement. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD gives the reason in the row itself: so a replacement or recalibrated scorecard can be validated against the live population before it is adopted (PDF page 34).

## Example

A new scorecard is built. For three months every application is scored by both. Only the live scorecard decides; the new one's results are stored. Credit Risk compares the two before switching.

## Terms to know

- **Shadow run:** a trial whose result is recorded but not used.
- **Recalibrated:** adjusted using newer data.
- **Live population:** the real applications flowing through now.
- **Should:** a requirement with priority Should, not Must.
