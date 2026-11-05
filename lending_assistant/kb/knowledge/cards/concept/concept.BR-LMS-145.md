---
id: concept.BR-LMS-145
type: concept
title: Check that interest numbers agree everywhere
summary: "The system compares the interest in the plan, the bills, the accruals, the collected income and the ledger, and reports every difference."
br_ids: [BR-LMS-145]
brd_section: 7.5
doctypes: []
verdict: gap
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-145"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p49"
  - "sources/verification/reqs.json#BR-LMS-145"
  - "sources/verification/verification_report.md#BR-LMS-145"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-145"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-145"
related: [bridge.BR-LMS-145, brd_section.7.5, devitem.D10, glossary.gl, glossary.cbs, glossary.demand]
version: 1
status: approved
approved_by: Owner
---
**In short:** The system compares the interest in the plan, the bills, the accruals, the collected income and the ledger, and reports every difference.

## What the rule says

BR-LMS-145 (priority Must, BRD 7.5, PDF page 49) says the platform reconciles, and reports differences between, five figures: schedule interest, demanded interest, accrued interest, collected income, and the general ledger or Core Banking System position.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that interest passes through five records, and a small difference in any of them can grow unnoticed unless a report compares them.

## Example

Plan: 1,151. Bill: 1,151. Accrued: 1,150. Ledger: 1,151. The report flags the 1 BDT difference so someone can fix it.

## Terms to know

- **Reconcile:** compare two sets of figures and explain every difference.
- **Schedule, demand, accrual, collected income:** the four stages of interest. See `glossary.demand`.
- **General ledger (GL) and CBS position:** the bank's official books. See `glossary.gl` and `glossary.cbs`.
