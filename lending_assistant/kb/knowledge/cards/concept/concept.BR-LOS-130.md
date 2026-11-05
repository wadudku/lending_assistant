---
id: concept.BR-LOS-130
type: concept
title: "After scoring, a share of applications is picked for manual review"
summary: "Once applications are scored, the platform picks a share for manual review at a configured rate, plus every referred or mandatory-sampling case, and passes the rest automatically."
br_ids: [BR-LOS-130]
brd_section: 6.5
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-130"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p35"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-307"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-137"
related: [bridge.BR-LOS-130, concept.BR-LOS-307, concept.BR-LOS-137, glossary.sampling, glossary.scorecard]
version: 1
status: approved
approved_by: Owner
---
**In short:** Once applications are scored, the platform picks a share for manual review at a configured rate, plus every referred or mandatory-sampling case, and passes the rest automatically.

## What the rule says

BR-LOS-130 (Must, BRD 6.5, PDF page 35) says once applications have been scored, the platform selects a subset for manual review at a rate determined by configuration, together with every application the scorecard referred and every application caught by a mandatory sampling rule, and passes the remainder automatically. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD gives the reason in the 6.5 introduction: sampling is how the Bank keeps credit judgement over a volume too large to review one by one, and its integrity (genuinely random selection, a controlled rate, decisions that can be attributed and reproduced) is what makes partner-sourced origination defensible to internal audit and the regulator (PDF page 35).

## Example

A batch of 100 scored applications has 6 referred and 3 caught by a mandatory rule. The configured rate picks 10 more at random. 19 go to a reviewer; the other 81 pass on automatically.

## Terms to know

- **Sampling:** picking some applications for manual review.
- **Subset:** a part of the whole batch.
- **Referred:** sent to a person by the scorecard. See BR-LOS-303.
- **Mandatory sampling rule:** a rule that always sends a case for review. See BR-LOS-137.
