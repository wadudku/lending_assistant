---
id: brd_section.7.4
type: brd_section
title: "BRD 7.4 Demand, billing and charges"
summary: "Section 7.4 says the LMS raises the bills (demands) on their due dates, never deletes or quietly changes one, and sends the accounting effect to the CBS."
br_ids: []
brd_section: 7.4
doctypes: []
dev_items: [D7, D8, D9, D13]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#7.4"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p48"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p49"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#7.4-demand-billing-and-charges"
  - "sources/NRB_LMS_Requirements_Plain_English.md#7.4-demand-billing-and-charges"
  - "sources/verification/reqs.json#BR-LMS-130"
related: [devitem.D7, devitem.D8, devitem.D9, devitem.D13, glossary.demand, glossary.rpa, glossary.cbs, glossary.batch]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 7.4 says the LMS raises the bills (demands) on their due dates, never deletes or quietly changes one, and sends the accounting effect to the CBS.

## What this section says

BRD 7.4 (PDF pages 48 and 49, 6 requirements, BR-LMS-130 to BR-LMS-135) starts with a note that every accounting effect is written into the Core Banking System by robotic process automation, because no posting interface exists. The requirements cover raising demands on their due dates (130), attaching charges (131), a due-details view for any date that posts nothing (132), corrections only by a controlled reversal with a reason and an approver (133), exporting accounting effects to the CBS and keeping its journal reference (134) and demand generation as a batch that can restart (135).

## Why the bank wants it

The BRD gives its reason for the posting note on PDF page 48: no posting interface exists, so the volume of posting is limited and batching is favoured where the bank's accounting policy allows. The BRD says no more about the other requirements.

## How it meets Frappe Lending

Of the 6 requirements, the verified result on 16.5.1 is 1 covered (130); 4 partly covered (131, 132, 133, 135); 1 a gap that needs the CBS link (134). Verification moved 1 of these verdicts: 131. Dev items: D7 (dues as on a date), D8 (approval and audit pack), D9 (batch run and exception framework) and D13 (the CBS and RPA posting bridge).

## Related cards

Dev items: `devitem.D7`, `devitem.D8`, `devitem.D9` and `devitem.D13`. Terms: `glossary.demand`, `glossary.rpa`, `glossary.cbs`, `glossary.batch`.
