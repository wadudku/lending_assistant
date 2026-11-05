---
id: brd_section.7.13
type: brd_section
title: BRD 7.13 Portfolio operations
summary: "Section 7.13 covers running the whole loan book: moving loans between branches, credit-line limits, batch states, exception queues and job alerts."
br_ids: []
brd_section: 7.13
doctypes: []
dev_items: [D8, D9]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#7.13"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p55"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#7.13-portfolio-operations"
  - "sources/NRB_LMS_Requirements_Plain_English.md#7.13-portfolio-operations"
  - "sources/verification/reqs.json#BR-LMS-220"
related: [devitem.D8, devitem.D9, glossary.loc, glossary.batch, glossary.idempotency]
version: 2
status: approved
approved_by: Owner
---
**In short:** Section 7.13 covers running the whole loan book: moving loans between branches, credit-line limits, batch states, exception queues and job alerts.

## What this section says

BRD 7.13 (PDF page 55, 6 requirements, BR-LMS-220 to BR-LMS-225) has the platform do these things. It transfers loans between branches in bulk and keeps the same record and history (220). It tracks maximum, utilised and available limit on a line of credit with a change log (221). It closes fully repaid revolving facilities by a scheduled job (222). It gives every batch an explicit state with row-level outcomes, resumable without double posting (223). It presents exception work queues with an owner, ageing and a documented closure (224). It monitors scheduled and integration jobs and alerts on failure (225). BR-LMS-222 is a Should; the others are Must.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a large loan book is run mostly by batches, so staff need to see which batch failed, which loans it left unprocessed and who is dealing with them, rather than discovering gaps later. BR-LMS-225 asks for alerts rather than silent degradation (PDF page 55).

## How it meets Frappe Lending

Of the 6 requirements, the verified result on 16.5.1 is 2 covered (220, 222); 3 partly covered (221, 223, 225); 1 a gap (224). Verification confirmed the other five verdicts. Row 220 was not tested during verification; its verdict (covered) comes from the code reading. Dev items: D8 (approval and audit pack) and D9 (batch run and exception framework).

## Related cards

Dev items: `devitem.D8`, `devitem.D9`. Terms: `glossary.loc`, `glossary.batch`, `glossary.idempotency`.
