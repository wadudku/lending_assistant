---
id: concept.BR-LOS-164
type: concept
title: Old downloaded sanction data is refreshed before approval
summary: "If the app has been offline too long, its downloaded sanction details count as stale and must be refreshed before approval can go ahead."
br_ids: [BR-LOS-164]
brd_section: 6.7.2
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-164"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p40"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.7.2"
related: [bridge.BR-LOS-164, concept.BR-LOS-163, glossary.sanctioned-amount]
version: 1
status: approved
approved_by: Owner
---
**In short:** If the app has been offline too long, its downloaded sanction details count as stale and must be refreshed before approval can go ahead.

## What the rule says

BR-LOS-164 (Must, BRD 6.7.2, PDF page 40) says that where the application has been offline beyond a configurable period, "pre-downloaded sanction data shall be treated as stale and refreshed before approval proceeds". The sanction details held on the device are not relied on after that period.

## Why the bank wants it

The BRD gives the operating context for section 6.7 (PDF page 39): officers often work in rural places with unreliable mobile data. Section 6.7.2 (PDF page 40) is the part that deals with that. The BRD doesn't say why; the usual reason is that approval and payout use the sanction terms, so the officer must not approve against terms that may have been changed or cancelled since they were downloaded.

## Example

An officer downloaded a sanction on Monday and has been offline since. On Friday, before approving, the app finds its sanction data is older than the allowed period and refuses to go on until it has downloaded the current details.

## Terms to know

- **Sanctioned amount:** the BRD's glossary defines the sanctioned amount as the amount the Bank agrees to lend, which may be lower than the amount requested.
- **Stale:** too old to be relied on.
