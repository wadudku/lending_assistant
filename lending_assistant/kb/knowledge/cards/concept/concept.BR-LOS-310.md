---
id: concept.BR-LOS-310
type: concept
title: Absent data is never treated as good news
summary: "An absent or unavailable input never silently defaults to a favourable value; the configured treatment is applied and recorded, and an absent mandatory input leads to a referral, not an auto-approval."
br_ids: [BR-LOS-310]
brd_section: 6.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-310"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p34"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-301"
related: [bridge.BR-LOS-310, concept.BR-LOS-301, glossary.scorecard]
version: 1
status: approved
approved_by: Owner
---
**In short:** An absent or unavailable input never silently defaults to a favourable value; the configured treatment is applied and recorded, and an absent mandatory input leads to a referral, not an auto-approval.

## What the rule says

BR-LOS-310 (Must, BRD 6.4, PDF page 34) says a missing or unavailable input never silently defaults to a favourable value. The platform applies the configured treatment for missing data and records that it was applied. Where a mandatory input is unavailable the application is referred rather than auto-approved. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that an empty value read as a good one would let weak applications pass without anyone noticing.

## Example

The credit bureau does not answer. The platform applies the configured treatment for “bureau data missing”, records that it did so, and, because bureau data is mandatory for this product, refers the application to a person.

## Terms to know

- **Default:** a value assumed when none is given.
- **Favourable:** in the applicant's favour.
- **Mandatory input:** a value the score cannot be fair without.
- **Treatment:** what the scorecard does when a value is missing.
