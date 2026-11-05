---
id: brd_section.9.4
type: brd_section
title: BRD 9.4 Origination to servicing
summary: Section 9.4 sets three rules for the handoff of a funded loan from origination to servicing and for the status that flows back.
br_ids: []
brd_section: 9.4
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#9.4"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p64"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-020"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-021"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-022"
related: [brd_section.9, brd_section.7, glossary.los, glossary.lms, glossary.idempotency, concept.BR-LOS-010]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 9.4 sets three rules for the handoff of a funded loan from origination to servicing and for the status that flows back.

## What this section says

BRD 9.4 (PDF page 64) has 3 requirements, all Must. BR-INT-020: the handoff of a confirmed funded loan carries the complete package specified in BR-LOS-010 and is idempotent. BR-INT-021: servicing exposes loan account status, sanctioned amount, disbursement date, tenor, instalment amount and arrears position back to origination, for partner disbursed-account views, partner quality monitoring and scorecard performance monitoring under BR-LOS-312. BR-INT-022: a failed or rejected handoff raises an exception on both sides, and neither side progresses the loan until it is closed.

## Why the bank wants it

The BRD gives one reason, in BR-INT-021: the data flows back for partner views, quality monitoring and scorecard monitoring (PDF page 64). It doesn't say why 020 and 022 are needed.

## How it meets Frappe Lending

The team's analysis covered Section 7 only. This section holds 3 requirement rows and none was analysed, so the team makes no statement about them. For the Section 7 totals, see `brd_section.7`.

## Related cards

Parent: `brd_section.9`. Terms: `glossary.los`, `glossary.lms`, `glossary.idempotency`.
