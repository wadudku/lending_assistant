---
id: concept.BR-LOS-132
type: concept
title: The seed and rate are saved so a pick can be reproduced for audit
summary: The selection seed and the rate applied are recorded against the batch so the pick can be independently reproduced and shown to audit at any later date.
br_ids: [BR-LOS-132]
brd_section: 6.5
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-132"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p36"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-131"
related: [bridge.BR-LOS-132, glossary.batch, concept.BR-LOS-131, concept.BR-LOS-133, glossary.sampling]
version: 1
status: approved
approved_by: Owner
---
**In short:** The selection seed and the rate applied are recorded against the batch so the pick can be independently reproduced and shown to audit at any later date.

## What the rule says

BR-LOS-132 (Must, BRD 6.5, PDF page 36) says the selection seed and the rate applied are recorded against the batch, such that the selection can be independently reproduced and demonstrated to audit at any future date. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD gives the reason in the 6.5 introduction: sampling is how the Bank keeps credit judgement over a volume too large to review one by one, and its integrity (genuinely random selection, a controlled rate, decisions that can be attributed and reproduced) is what makes partner-sourced origination defensible to internal audit and the regulator (PDF page 35).

## Example

Two years later an auditor asks why a certain application was not reviewed. The Bank takes the stored seed and rate for that batch, repeats the pick and shows the same result.

## Terms to know

- **Seed:** the starting value of a random draw; the same seed gives the same draw.
- **Reproduce:** repeat and get the same result.
- **Batch:** a group of applications sent together. See `glossary.batch`.
- **Audit:** an independent check of what was done and why.
