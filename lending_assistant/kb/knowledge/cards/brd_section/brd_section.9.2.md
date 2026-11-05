---
id: brd_section.9.2
type: brd_section
title: "BRD 9.2 Core Banking System: the constraint and the approach"
summary: "Section 9.2 states that the core banking system has no programmatic interface, that robotic process automation is the only route, and six business consequences the bank is asked to accept knowingly."
br_ids: []
brd_section: 9.2
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#9.2"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p60"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p61"
related: [brd_section.9, brd_section.9.1, brd_section.9.2.1, brd_section.9.3, brd_section.7, glossary.cbs, glossary.rpa, glossary.idempotency]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 9.2 states that the core banking system has no programmatic interface, that robotic process automation is the only route, and six business consequences the bank is asked to accept knowingly.

## What this section says

BRD 9.2 (PDF pages 60 and 61) begins: “There is no programmatic route into the Core Banking System.” It says NRB Bank Limited runs a legacy core banking system with no application programming interface, and no integration or API management layer in front of it. The only route is robotic process automation: software that signs in as a controlled service user and drives the screens as a trained operator would. The BRD calls this “a workable approach” but “not, however, equivalent to an interface”. A table then lists six consequences: throughput is bounded by screen speed; funding may not complete inside the meeting; idempotency must be manufactured; the automation is sensitive to change; the service user is a privileged user; and capacity is a licensed, physical resource. The section has no row of its own; the 12 rows of 9.2.1 follow it.

## Why the bank wants it

The BRD states its reason in the section: the consequences are “stated here so that NRB Bank Limited accepts them knowingly rather than discovers them during user acceptance testing” (PDF page 60).

## How it meets Frappe Lending

The team's analysis covered Section 7 only. This section was not analysed, so the team makes no statement about it. For the Section 7 totals, see `brd_section.7`. The statement about the core banking system is the BRD's own description of NRB's system, not a finding about Frappe Lending.

## Related cards

Parent: `brd_section.9`. Rows: `brd_section.9.2.1`. Next: `brd_section.9.3`. Terms: `glossary.cbs`, `glossary.rpa`, `glossary.idempotency`.
