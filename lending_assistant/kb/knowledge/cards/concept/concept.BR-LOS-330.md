---
id: concept.BR-LOS-330
type: concept
title: A sanction lapses after a set validity period
summary: "A sanction lapses after a configured validity period; a lapsed sanction blocks assignment and disbursement and needs a new sanction, with score and account check refreshed where they have expired."
br_ids: [BR-LOS-330]
brd_section: 6.6
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-330"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p38"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-123"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-124"
related: [bridge.BR-LOS-330, concept.BR-LOS-123, concept.BR-LOS-124]
version: 1
status: approved
approved_by: Owner
---
**In short:** A sanction lapses after a configured validity period; a lapsed sanction blocks assignment and disbursement and needs a new sanction, with score and account check refreshed where they have expired.

## What the rule says

BR-LOS-330 (Must, BRD 6.6, PDF page 38) says a sanction lapses after a configurable validity period. A lapsed sanction blocks assignment and disbursement and requires re-sanction, with the score and account validation refreshed where they have themselves expired. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a borrower's position changes with time, so an old approval should not be relied on for a payout.

## Example

A sanction is valid for 30 days. The meeting is delayed and the payout is due on day 40. The sanction has lapsed, so assignment and payout are blocked until the approver re-sanctions, after the score and account check are refreshed.

## Terms to know

- **Lapse:** stop being valid because time has passed.
- **Validity period:** how long a sanction stays valid.
- **Re-sanction:** sanction again.
- **Refreshed:** run again to get a current result.
