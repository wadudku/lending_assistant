---
id: concept.BR-LMS-164
type: concept
title: Split the payment in the set order and show it
summary: "A payment is split across what is owed in an order the bank sets, and the split is shown line by line on the loan."
br_ids: [BR-LMS-164]
brd_section: 7.7
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-164"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p51"
  - "sources/verification/reqs.json#BR-LMS-164"
  - "sources/verification/verification_report.md#BR-LMS-164"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-164"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-164"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-005"
related: [bridge.BR-LMS-164, glossary.allocation-order]
version: 1
status: approved
approved_by: Owner
---
**In short:** A payment is split across what is owed in an order the bank sets, and the split is shown line by line on the loan.

## What the rule says

BR-LMS-164 (Must, BRD 7.7.1, PDF page 51) says payments are allocated using the configured offset sequence across charges, penalty, interest, principal and other components, and that the allocation is visible line by line on the loan record.

## Why the bank wants it

The BRD gives part of the reason in a guiding principle: offset sequences are configuration, not code (BR-GOV-005, PDF page 19), so the order is set by bank policy and not by whoever enters a payment. The BRD doesn't say why the split must be visible; the usual reason is that when a payment is smaller than the total owed, the order decides which parts are cleared first. That changes the borrower's debt, the bank's income and the loan's grade, so anyone checking a loan needs to see the split.

## Example

Rahim pays 8,979. The loan record shows two lines: interest 1,151 and principal 7,828, one for each part of the bill that was cleared.

## Terms to know

- **Offset sequence (allocation order):** the priority order for clearing what is owed. See `glossary.allocation-order`.
- **Allocation:** deciding which parts of the debt a payment clears.
- **Penalty:** extra charge for late payment.
