---
id: concept.BR-LMS-201
type: concept
title: "Approval limits for settlements, waivers and write-offs"
summary: "Settlements, waivers and write-offs need a second person's approval, and who may approve depends on the amount and on the person's role."
br_ids: [BR-LMS-201]
brd_section: 7.11
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-201"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p54"
  - "sources/verification/reqs.json#BR-LMS-201"
  - "sources/verification/verification_report.md#BR-LMS-201"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-201"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-201"
related: [bridge.BR-LMS-201, brd_section.7.11, glossary.maker-checker, glossary.waiver, glossary.write-off]
version: 1
status: approved
approved_by: Owner
---
**In short:** Settlements, waivers and write-offs need a second person's approval, and who may approve depends on the amount and on the person's role.

## What the rule says

BR-LMS-201 in section 7.11 (Must, BRD PDF page 54) says settlement, waiver and write-off shall require maker-checker approval within the delegated authority applicable to the amount and the role.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that forgiving money is a decision with a price, so the bank wants bigger amounts to go to more senior people.

## Example

Waivers up to 10,000 are approved by the branch manager. Up to 100,000 by the head of credit. Above that by the credit committee. A branch manager who is asked to approve a 40,000 waiver must pass it up, and cannot approve it alone.

## Terms to know

- **Maker-checker:** one person prepares, another approves. See `glossary.maker-checker`.
- **Delegated authority:** the limit of what a role may approve.
- **Approval band:** an amount range tied to a role.
