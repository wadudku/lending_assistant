---
id: concept.BR-LOS-131
type: concept
title: The random pick must use a sound random source
summary: Selection uses a cryptographically sound random source; a predictable or sequence-based pick is not acceptable.
br_ids: [BR-LOS-131]
brd_section: 6.5
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-131"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p35"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-130"
related: [bridge.BR-LOS-131, concept.BR-LOS-130, concept.BR-LOS-132, glossary.sampling]
version: 1
status: approved
approved_by: Owner
---
**In short:** Selection uses a cryptographically sound random source; a predictable or sequence-based pick is not acceptable.

## What the rule says

BR-LOS-131 (Must, BRD 6.5, PDF page 35) says selection uses a cryptographically sound random source. A predictable or sequence-based selection is not acceptable. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD gives the reason in the 6.5 introduction: sampling is how the Bank keeps credit judgement over a volume too large to review one by one, and its integrity (genuinely random selection, a controlled rate, decisions that can be attributed and reproduced) is what makes partner-sourced origination defensible to internal audit and the regulator (PDF page 35).

## Example

Picking every tenth application would be predictable, so a partner could place weak cases at the other positions. A cryptographically sound random draw gives no such pattern.

## Terms to know

- **Cryptographically sound random source:** a random generator that cannot be guessed from earlier results.
- **Sequence-based:** chosen by position, such as every tenth.
- **Predictable:** can be worked out in advance.
- **Selection:** the act of picking which applications go to review.
