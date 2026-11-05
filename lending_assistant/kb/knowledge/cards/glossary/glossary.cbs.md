---
id: glossary.cbs
type: glossary
title: CBS (Core Banking System)
summary: "The bank's main system. It holds the real customer accounts and money, and the loan system must agree with it."
br_ids: []
brd_section: 1.5
doctypes: []
dev_items: []
terms: [cbs, core banking system, core banking]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#1.5"
  - "sources/NRB_LMS_Requirements_Plain_English.md#glossary-of-abbreviations"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#9.2"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p60"
related: [devitem.D13, concept.BR-LMS-170r]
version: 1
status: approved
approved_by: Owner
---
**In short:** The bank's main system. It holds the real customer accounts and money, and the loan system must agree with it.

## Plain meaning

CBS stands for Core Banking System: the bank's system of record for customers, accounts and money (BRD 1.5). NRB's CBS has no programming interface, so the BRD's route is a software robot (RPA) that signs in and drives the CBS screens as a trained operator would (BRD 9.2, PDF page 60).

## Example

When Rahim pays at a branch, the CBS records the transaction and gives it a reference such as CBS-TXN-0001. The loan system records the same payment and stores that reference.

## Why it matters here

Many requirements depend on the CBS: confirming payments (BR-LMS-161), applying each reference once (BR-LMS-162) and reconciling (BR-LMS-170, BR-LMS-171). Frappe Lending has no link to a CBS, which is why several verdicts are "gap (needs the CBS link)" (see `devitem.D13`).

## See also

`devitem.D13`, `concept.BR-LMS-170r`, `concept.BR-GOV-002`.
