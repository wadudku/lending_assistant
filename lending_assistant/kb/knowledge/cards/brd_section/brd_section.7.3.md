---
id: brd_section.7.3
type: brd_section
title: BRD 7.3 Repayment schedule management
summary: "Section 7.3 says schedules are versioned and never overwritten, so the bank can explain later why a borrower owed what they owed."
br_ids: []
brd_section: 7.3
doctypes: []
dev_items: [D1, D6]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#7.3"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p47"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p48"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#7.3-repayment-schedule-management"
  - "sources/NRB_LMS_Requirements_Plain_English.md#7.3-repayment-schedule-management"
  - "sources/verification/reqs.json#BR-LMS-120"
related: [devitem.D6, glossary.schedule-version, glossary.emi, glossary.moratorium, decision.restructure]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 7.3 says schedules are versioned and never overwritten, so the bank can explain later why a borrower owed what they owed.

## What this section says

BRD 7.3 (PDF pages 47 and 48, 7 requirements, BR-LMS-120 to BR-LMS-126) states one rule: when approved terms change, the platform creates a new authoritative schedule and keeps the old one as a superseded version with the event that replaced it. Paid instalments, completed repayments and posted history are never rewritten. The requirements then cover the first schedule on booking (120), the split in each line (121), changes at each tranche (122), a partner schedule beside the borrower schedule for co-lent loans (123), a simulation that posts nothing (124), preserving prior versions (125), and rebuilding only on an approved change with the trigger recorded (126).

## Why the bank wants it

The BRD gives its reason in the section introduction (PDF page 47): keeping every version is what allows the bank to explain, years later, why a borrower owed what they owed on a given date.

## How it meets Frappe Lending

Of the 7 requirements, the verified result on 16.5.1 is 4 covered (120, 121, 122, 123); 2 partly covered (124, 125); 1 a gap (126). Verification moved 1 of these verdicts: 126. Dev item: D6 (schedule versions, triggers and what-if).

## Related cards

Dev item: `devitem.D6`. Terms: `glossary.schedule-version`, `glossary.emi`, `glossary.moratorium`. Decision: `decision.restructure`.
