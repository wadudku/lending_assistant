---
id: devitem.D13
type: devitem
title: D13 CBS and RPA posting bridge
summary: "A planned add-on, sized L, that sends accounting entries to the CBS through a software robot and brings back the CBS journal number."
br_ids: [BR-LMS-115, BR-LMS-134, BR-LMS-170, BR-LMS-204, BR-LMS-231]
brd_section: 7.7
doctypes: [Loan Repayment]
dev_items: [D13]
fields: [Company.Consolidate Loan GL Monthly]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D13"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#gap-3-no-link-to-the-core-banking-system-5-requirements-plus-parts-of-4-others"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#8.-notes-on-the-brd-itself"
  - "sources/verification/FINAL_REPORT.md#D13"
  - "sources/verification/FINAL_REPORT.md#d1-d20-what-moved"
  - "sources/verification/FINAL_REPORT.md#revised-suggested-order"
  - "sources/verification/verification_report.md#BR-LMS-115"
related: [bridge.BR-LMS-170r, bridge.BR-LMS-171r, devitem.D12, glossary.cbs]
version: 1
status: approved
approved_by: Owner
---
**In short:** A planned add-on, sized L, that sends accounting entries to the CBS through a software robot and brings back the CBS journal number.

## What we plan to build

D13 is a CBS Posting Request outbox. Each request holds the source document, the entries, a unique reference, a status (Pending, Sent, Verified or Failed), the CBS journal number and the number of attempts. The robot (RPA) picks up requests, writes the entries into the CBS, and writes the result back. A check after execution and a two-way reconciliation follow. The Company setting Consolidate Loan GL Monthly can batch entries to cut the number of robot postings.

## The gap it closes

Frappe Lending either posts to its own ledger or posts nothing. Nothing is sent to the CBS, nothing keeps a CBS journal reference, nothing confirms a payment with the CBS and nothing detects a payment made directly in the CBS. These are the "gap (needs the CBS link)" verdicts. The coverage analysis calls this CBS/RPA layer "the biggest single build" (§4, Gap 3), and says it also decides the accounting mode (BR-LMS-115).

## Requirements it closes

BR-LMS-115 (two accounting modes), BR-LMS-134 (send bills to the CBS), BR-LMS-170 in 7.7 (see `bridge.BR-LMS-170r`), BR-LMS-204 (settlements and write-offs to the CBS) and BR-LMS-231 (check the CBS before closure).

## How, size and dependencies

Size: L (over three weeks), unchanged by verification; eight other D items are also L. It must wait for ND-12, because all servicing entries are dated with the day of entry instead of the business date, which would break any CBS match. It also depends on the RPA team and BRD section 9, and on NRB's choice between the platform ledger and demand-only mode, where the CBS keeps the ledger (BR-LMS-115): the analysis says the cost of the bridge is very different between the two. The final report puts it in Pack C, the operations and ledger bridge, after the foundation items.
