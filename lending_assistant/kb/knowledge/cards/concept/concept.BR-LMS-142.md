---
id: concept.BR-LMS-142
type: concept
title: Interest for odd days (broken period)
summary: "When a partial period arises at payout, at a change of terms or at closure, the interest for those odd days is handled and charged."
br_ids: [BR-LMS-142]
brd_section: 7.5
doctypes: []
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-142"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p49"
  - "sources/verification/reqs.json#BR-LMS-142"
  - "sources/verification/verification_report.md#BR-LMS-142"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-142"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-142"
related: [bridge.BR-LMS-142, brd_section.7.5, glossary.bpi, glossary.restructuring]
version: 1
status: approved
approved_by: Owner
---
**In short:** When a partial period arises at payout, at a change of terms or at closure, the interest for those odd days is handled and charged.

## What the rule says

BR-LMS-142 (priority Must, BRD 7.5, PDF page 49) says broken-period interest is handled for partial periods that arise at disbursement, at a change of terms and at closure.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a loan seldom starts exactly one period before its first due date, and the bank should not lose the interest for the days in between.

## Example

A loan is paid out on 25 June and the first EMI is due on 5 August. The 10 odd days from 25 June to 5 July cost about 384 extra interest (10 x 38.36).

## Terms to know

- **Broken-period interest (BPI):** interest for the odd days before the first full period. See `glossary.bpi`.
- **Partial period:** a period shorter or longer than a normal month.
- **Change of terms:** a restructure or a rate change. See `glossary.restructuring`.
