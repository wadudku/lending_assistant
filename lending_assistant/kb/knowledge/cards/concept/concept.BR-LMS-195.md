---
id: concept.BR-LMS-195
type: concept
title: Write-off has its own trigger
summary: "The point at which a loan may be written off is set by its own threshold, separate from the grade bands."
br_ids: [BR-LMS-195]
brd_section: 7.10
doctypes: []
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-195"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p54"
  - "sources/verification/reqs.json#BR-LMS-195"
  - "sources/verification/verification_report.md#BR-LMS-195"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-195"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-195"
related: [bridge.BR-LMS-195, brd_section.7.10, glossary.write-off, concept.BR-LMS-191, decision.write-off]
version: 1
status: approved
approved_by: Owner
---
**In short:** The point at which a loan may be written off is set by its own threshold, separate from the grade bands.

## What the rule says

BR-LMS-195 in section 7.10 (Must, BRD PDF page 54) says write-off eligibility shall be assessed against a separately configured threshold, distinct from the classification bands.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that being graded as a bad loan and being removed from the books are different decisions, and the bank wants to set the second one on its own.

## Example

The grade Bad/Loss starts at 365 days late, but write-off is allowed only after 1,080 days late. A loan that is 400 days late is graded Bad/Loss and is not yet eligible to be written off.

## Terms to know

- **Write-off:** removing a loan from the books as a loss. See `glossary.write-off`.
- **Threshold:** the number of days late after which the event applies.
- **Classification bands:** the grade ranges. See `concept.BR-LMS-191`.
- **Auto write-off:** the platform writes the loan off by itself once the threshold is passed, without waiting for a person to start it.
