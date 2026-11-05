---
id: brd_section.7.11
type: brd_section
title: "BRD 7.11 Settlement, write-off and recovery"
summary: "Section 7.11 says a settlement, waiver or write-off needs a shown figure, approval within delegated authority and a complete record, and that a write-off never destroys history."
br_ids: []
brd_section: 7.11
doctypes: []
dev_items: [D8, D13, D18]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#7.11"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p54"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#7.11-settlement-write-off-and-recovery"
  - "sources/NRB_LMS_Requirements_Plain_English.md#7.11-settlement-write-off-and-recovery"
  - "sources/verification/reqs.json#BR-LMS-200"
related: [devitem.D8, devitem.D13, devitem.D18, decision.settlement, decision.waiver, decision.write-off, lifecycle.SETTLED, lifecycle.WRITTEN_OFF, glossary.write-off, glossary.waiver]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 7.11 says a settlement, waiver or write-off needs a shown figure, approval within delegated authority and a complete record, and that a write-off never destroys history.

## What this section says

BRD 7.11 (PDF page 54, 6 requirements, BR-LMS-200 to BR-LMS-205) has the platform calculate a settlement figure and show how it is made up before approval (200). Settlement, waiver and write-off need maker-checker approval within the delegated authority for the amount and the role (201). A write-off keeps the loan, its schedule versions, postings and classification history retrievable (202). Money recovered later is recorded as a write-off recovery against the original loan (203). Accounting effects go to the CBS with the returned journal reference kept (204). Every event keeps before and after amounts, the reason, maker, checker, approval date and external reference (205).

## Why the bank wants it

The BRD doesn't say why; the usual reason is that these events give up money the bank is owed, so they need a visible figure, an authorised approver and a full trail that an auditor can follow. BR-LMS-202 states the history rule: a write-off must not destroy the loan's history (PDF page 54).

## How it meets Frappe Lending

Of the 6 requirements, the verified result on 16.5.1 is 2 covered (202, 203); 3 partly covered (200, 201, 205); 1 a gap that needs the CBS link (204). Verification confirmed every verdict from the analysis. Dev items: D8 (approval and audit pack), D13 (the CBS and RPA posting bridge) and D18 (settlement proposal).

## Related cards

Dev items: `devitem.D8`, `devitem.D13`, `devitem.D18`. Decisions: `decision.settlement`, `decision.waiver`, `decision.write-off`. States: `lifecycle.SETTLED`, `lifecycle.WRITTEN_OFF`. Terms: `glossary.write-off`, `glossary.waiver`.
