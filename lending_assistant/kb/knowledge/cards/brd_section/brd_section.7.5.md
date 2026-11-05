---
id: brd_section.7.5
type: brd_section
title: BRD 7.5 Interest and accrual management
summary: "Section 7.5 says interest is counted every period, penalty interest is kept apart, and unpaid interest on bad loans stops counting as income."
br_ids: []
brd_section: 7.5
doctypes: []
dev_items: [D10]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#7.5"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p49"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#7.5-interest-and-accrual-management"
  - "sources/NRB_LMS_Requirements_Plain_English.md#7.5-interest-and-accrual-management"
  - "sources/verification/reqs.json#BR-LMS-140"
related: [devitem.D10, glossary.penal-interest, glossary.income-suspense, glossary.bpi, glossary.npa]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 7.5 says interest is counted every period, penalty interest is kept apart, and unpaid interest on bad loans stops counting as income.

## What this section says

BRD 7.5 (PDF page 49, 6 requirements, BR-LMS-140 to BR-LMS-145) covers normal interest accrual by the product's frequency and day-count convention (140), penal interest tracked separately (141), broken-period interest at disbursement, a change of terms and closure (142), an approved batch reversal and repost of accruals for a date range (143), the income treatment on non-performing classification, which stops normal income and moves qualifying unpaid interest and charges to suspense under Bangladesh Bank rules (144) and a reconciliation of schedule, demand, accrual, income and ledger positions (145).

## Why the bank wants it

The BRD doesn't say why; the usual reason is that accrued interest is both what the borrower owes and what the bank earns, so it has to be counted by clear rules, kept separate from penalty interest, and checked against the ledger. BR-LMS-144 ties the income treatment to Bangladesh Bank rules (PDF page 49).

## How it meets Frappe Lending

Of the 6 requirements, the verified result on 16.5.1 is 3 covered (140, 142, 144); 2 partly covered (141, 143); 1 a gap (145). Verification moved 2 of these verdicts: 141, 143. Dev item: D10 (reconciliation reports).

## Related cards

Dev item: `devitem.D10`. Terms: `glossary.penal-interest`, `glossary.income-suspense`, `glossary.bpi`, `glossary.npa`.
