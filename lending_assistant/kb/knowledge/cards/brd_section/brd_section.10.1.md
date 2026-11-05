---
id: brd_section.10.1
type: brd_section
title: BRD 10.1 Origination entities
summary: "Section 10.1 is a table of 16 origination entities, from Partner and Product to HandoffPackage, each with its purpose and notable attributes."
br_ids: []
brd_section: 10.1
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#10.1"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p66"
related: [brd_section.10, brd_section.10.2, glossary.partner]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 10.1 is a table of 16 origination entities, from Partner and Product to HandoffPackage, each with its purpose and notable attributes.

## What this section says

BRD 10.1 (PDF page 66) is a table of 16 entities used by origination: Partner, Product, Batch, Application, ValidationResult, SamplingDecision, CIBInquiry, eKYCRecord, VerificationSession, EvidenceCapture, MeetingEvent, FieldOfficer, Scorecard, ScoreResult, SanctionDecision and HandoffPackage. For example, Partner is the aggregator master, with legal identity, ceilings, permitted products, guarantee terms and status as its notable attributes. HandoffPackage is the funded-loan transfer to servicing, with origination reference, terms, disbursement reference and acceptance state. The section 10 note calls the tables indicative only.

## Why the bank wants it

The BRD gives the reason for all of Section 10 in its opening (PDF page 66): the table “establishes the shared vocabulary in which the two systems and the business describe the same things”.

## How it meets Frappe Lending

This section holds no requirement row, so there is nothing in it to compare with Frappe Lending, and the team has made no statement about it.

## Related cards

Parent: `brd_section.10`. Next: `brd_section.10.2`. Term: `glossary.partner`.
