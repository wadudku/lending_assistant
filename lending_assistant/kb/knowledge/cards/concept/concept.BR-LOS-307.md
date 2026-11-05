---
id: concept.BR-LOS-307
type: concept
title: "The score feeds sampling, with a floor that is never zero"
summary: "Referred applications are always sampled, grade bands carry their own sampling rate, and auto-approve bands may be sampled at a reduced rate that never falls to zero."
br_ids: [BR-LOS-307]
brd_section: 6.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-307"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p34"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-300"
related: [bridge.BR-LOS-307, concept.BR-LOS-300, glossary.sampling, glossary.scorecard]
version: 1
status: approved
approved_by: Owner
---
**In short:** Referred applications are always sampled, grade bands carry their own sampling rate, and auto-approve bands may be sampled at a reduced rate that never falls to zero.

## What the rule says

BR-LOS-307 (Must, BRD 6.4, PDF page 34) says the scorecard outcome feeds sampling selection. Referred applications are sampled mandatorily; configured grade bands carry their own sampling rate; and auto-approve bands may be sampled at a reduced rate, subject to a configurable floor that is never zero. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD gives the reason in the 6.4 introduction: scoring lets sampling and field effort be concentrated where the risk actually sits (PDF page 33). The floor keeps some oversight of auto-approved cases.

## Example

Referred applications are all reviewed. The moderate band is sampled at 20%. The low-risk band is sampled at 5%. The floor is 2%, so the low-risk rate cannot be set below that.

## Terms to know

- **Sampling rate:** the share of applications picked for review.
- **Floor:** the lowest rate allowed.
- **Mandatory sampling:** an application that is always reviewed.
- **Grade band:** a range of scores sharing one grade.
