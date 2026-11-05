---
id: brd_section.9.3
type: brd_section
title: BRD 9.3 Robotic process automation controls
summary: "Section 9.3 sets 13 controls on the robotic process automation that drives the core banking system: where it runs, who it signs in as, how it is watched and what happens when it fails."
br_ids: []
brd_section: 9.3
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#9.3"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p62"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p63"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-060"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-061"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-062"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-063"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-064"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-065"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-066"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-067"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-068"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-069"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-070"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-071"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-072"
related: [brd_section.9, brd_section.9.2, brd_section.9.2.1, brd_section.8.4, brd_section.7, glossary.rpa, glossary.cbs, glossary.maker-checker]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 9.3 sets 13 controls on the robotic process automation that drives the core banking system: where it runs, who it signs in as, how it is watched and what happens when it fails.

## What this section says

BRD 9.3 (PDF pages 62 and 63) opens with a paragraph that says the automation “is not an incidental utility”: it holds banking credentials, moves money, and its failure stops both origination and servicing, so it is specified, controlled and monitored as a banking component in its own right. It has 13 requirements, BR-INT-060 to BR-INT-072, all Must. They cover running only inside the bank's network (060); dedicated least-privilege service accounts (061); a secured credential store (062); traceability of each transaction to its initiator (063); evidence of each run (064); safe abort on an unexpected screen (065); continuous monitoring and alerts (066); an operations view with retry, cancel and escalate under maker-checker (067); horizontal scaling (068); pause and retry when unavailable (069); a manual fallback (070); re-validation before core banking system changes (071); and a daily two-way reconciliation under Section 8.4 (072).

## Why the bank wants it

The BRD gives its reason in the first paragraph: the automation “holds banking credentials, it moves money, and its failure stops both origination and servicing” (PDF page 62).

## How it meets Frappe Lending

The team's analysis covered Section 7 only. This section holds 13 requirement rows and none was analysed, so the team makes no statement about them. For the Section 7 totals, see `brd_section.7`.

## Related cards

Parent: `brd_section.9`. Before it: `brd_section.9.2`. Reconciliation: `brd_section.8.4`. Terms: `glossary.rpa`, `glossary.cbs`, `glossary.maker-checker`.
