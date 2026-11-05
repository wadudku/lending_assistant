---
id: brd_section.7.7.2
type: brd_section
title: BRD 7.7.2 Open items for NRB Bank Limited
summary: "Section 7.7.2 lists seven questions the bank must answer before repayment collection can be designed, and none of them is a requirement yet."
br_ids: []
brd_section: 7.7.2
doctypes: []
dev_items: [D12, D13]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#7.7.2"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p51"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p52"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#7.7-repayment-collection-and-allocation"
  - "sources/NRB_LMS_Requirements_Plain_English.md#7.7-repayment-collection-and-allocation"
related: [brd_section.7.7, brd_section.7.7.1, devitem.D12, devitem.D13, devitem.D19, glossary.cbs, glossary.rpa, glossary.mfs, glossary.dpd]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 7.7.2 lists seven questions the bank must answer before repayment collection can be designed, and none of them is a requirement yet.

## What this section says

BRD 7.7.2 (PDF pages 51 and 52) lists seven open questions for NRB, stated as questions rather than requirements. They are: which repayment channels carry the product; whether the CBS supports a standing instruction on the loan account; how the platform detects that a credit has arrived; how a credit is attributed to a loan; how a partner's bulk remittance is broken down and controlled; what the detection and posting cycle is and whether intraday is needed; and who owns the unidentified-receipts queue and within what period items must be cleared.

## Why the bank wants it

The BRD gives its reason on PDF page 51: each question must be answered before repayment collection can be designed, estimated or built. The table on PDF page 52 adds reasons for individual questions. The detection cycle decides how stale the platform's days past due, classification and provisioning can get, and that is a Credit Risk and Finance decision.

## How it meets Frappe Lending

The questions have no requirement ids, so there is no verdict to count. The BRD says the items are not baselined and not estimated, and that they are consolidated as its own dependency D19 in Section 12. That is a different D19 from our development item D19 (co-lending reports). The nearest dev items are D12 (payment confirmation and receipts) and D13 (the CBS and RPA posting bridge), but neither answers the questions, because the answers are NRB's to give.

## Related cards

Parent: `brd_section.7.7` and `brd_section.7.7.1`. Dev items: `devitem.D12`, `devitem.D13`, `devitem.D19`. Terms: `glossary.cbs`, `glossary.rpa`, `glossary.mfs`, `glossary.dpd`.
