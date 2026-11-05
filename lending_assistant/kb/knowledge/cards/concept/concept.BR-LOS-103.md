---
id: concept.BR-LOS-103
type: concept
title: A submission that would break the partner's exposure ceiling is stopped
summary: "The platform keeps a running total of each partner's exposure against its agreed ceiling, stops a submission that would go over, and tells the partner how much room is left."
br_ids: [BR-LOS-103]
brd_section: 6.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-103"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p29"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-100"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-115"
related: [bridge.BR-LOS-103, glossary.partner]
version: 1
status: approved
approved_by: Owner
---
**In short:** The platform keeps a running total of each partner's exposure against its agreed ceiling, stops a submission that would go over, and tells the partner how much room is left.

## What the rule says

BR-LOS-103 (Must, BRD 6.1, PDF page 29) says the platform tracks partner aggregate exposure against the agreed ceiling and prevents a submission that would breach it, with a clear message stating the remaining headroom. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD gives the reason in the 6.1 introduction: exposure ceilings are commercial terms, and the platform must enforce them rather than rely on operational vigilance (PDF page 29).

## Example

A partner's ceiling is 50,000,000 and 48,000,000 is already lent. It tries to submit applications worth 3,000,000. The platform refuses and says the remaining headroom is 2,000,000.

## Terms to know

- **Exposure:** the total still owed on loans from the partner.
- **Ceiling:** the highest total allowed.
- **Headroom:** the room left under the ceiling.
- **Aggregate:** added up across all the partner's loans.
