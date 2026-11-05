---
id: concept.BR-LOS-300
type: concept
title: Every submitted application is scored before it moves on
summary: The platform scores every submitted application against the scorecard for its product and does not move an unscored application to sampling or to sanction.
br_ids: [BR-LOS-300]
brd_section: 6.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-300"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p33"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p34"
related: [bridge.BR-LOS-300, glossary.partner, glossary.sampling, glossary.scorecard]
version: 1
status: approved
approved_by: Owner
---
**In short:** The platform scores every submitted application against the scorecard for its product and does not move an unscored application to sampling or to sanction.

## What the rule says

BR-LOS-300 (Must, BRD 6.4, PDF page 33) says the platform scores every submitted application against the scorecard configured for its product, and does not advance an unscored application to sampling or to sanction. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD gives the reason in the 6.4 introduction: at partner-sourced volume the Bank cannot underwrite each file individually, and a decision that depends on which reviewer or officer handled the case is neither defensible to audit nor stable enough to price against. The scorecard applies one credit policy uniformly (PDF page 33).

## Example

An application is submitted for a farm loan. The platform scores it with the scorecard set for that product. Until the score exists, the application cannot go to sampling or to the sanction step.

## Terms to know

- **Scorecard:** a set of weighted questions that turns an application into a score.
- **Submitted:** sent in by the partner and passed the earlier checks.
- **Sampling:** the Bank picks some applications for manual review.
- **Sanction:** the Bank's decision to lend an amount.
