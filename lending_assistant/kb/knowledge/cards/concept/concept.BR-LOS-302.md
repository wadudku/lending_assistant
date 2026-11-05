---
id: concept.BR-LOS-302
type: concept
title: Credit Risk owns the scorecard and changes it without a software release
summary: "Scorecards are configuration owned by Credit Risk; attributes, bands, weights, exclusions and cut-offs can be changed without a release, and every change is versioned, effective-dated and approved by a second person with a stated reason."
br_ids: [BR-LOS-302]
brd_section: 6.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-302"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p34"
related: [bridge.BR-LOS-302, glossary.maker-checker, glossary.scorecard, glossary.score-cut-off]
version: 1
status: approved
approved_by: Owner
---
**In short:** Scorecards are configuration owned by Credit Risk; attributes, bands, weights, exclusions and cut-offs can be changed without a release, and every change is versioned, effective-dated and approved by a second person with a stated reason.

## What the rule says

BR-LOS-302 (Must, BRD 6.4, PDF page 34) says scorecards are configuration owned by Credit Risk. Attributes, bands, weights, exclusions and cut-offs are maintainable without a software release, and every change is versioned, effective-dated and subject to maker-checker with a stated justification. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that credit policy changes more often than software, and a changed scorecard must be traceable and approved by someone other than the person who proposed it.

## Example

Credit Risk raises the weight of one attribute. The change is saved as scorecard version 4, starts on a set date, is approved by a second officer, and carries a written reason. Version 3 stays on record.

## Terms to know

- **Maker-checker:** one person makes a change and a second approves it. See `glossary.maker-checker`.
- **Effective-dated:** the change starts on a stated date.
- **Cut-off:** the score at which the recommended decision changes.
- **Exclusion:** a condition that removes an application from scoring or forces a result.
