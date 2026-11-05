---
id: concept.BR-LMS-115
type: concept
title: Two ways of keeping the accounts
summary: "The bank must choose whether the loan system keeps its own accounts and posts to the general ledger, or only works out what borrowers owe while the CBS keeps the official accounts."
br_ids: [BR-LMS-115]
brd_section: 7.2
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-115"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p47"
  - "sources/verification/reqs.json#BR-LMS-115"
  - "sources/verification/verification_report.md#BR-LMS-115"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-115"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-115"
related: [bridge.BR-LMS-115, brd_section.7.2, devitem.D13, glossary.gl, glossary.cbs, glossary.rpa]
version: 1
status: approved
approved_by: Owner
---
**In short:** The bank must choose whether the loan system keeps its own accounts and posts to the general ledger, or only works out what borrowers owe while the CBS keeps the official accounts.

## What the rule says

BR-LMS-115 (priority Must, BRD 7.2, PDF page 47) says the platform supports two accounting modes. In the first, it keeps servicing ledgers and posts to the general ledger. In the second, it does demand-only servicing and the Core Banking System (CBS) owns the general ledger. The mode is configurable, and the bank must confirm the choice before design.

## Why the bank wants it

The BRD gives the reason in the rule: postings reach the CBS through robotic process automation (RPA) rather than an interface (BRD Section 9.2), so the cost of each entry on that route is a material input to the choice (BR-LMS-115, PDF page 47).

## Example

With 50,000 loans and one daily interest entry each, mode one means 50,000 robot entries every day. Grouping them into one monthly entry per loan cuts that a lot. NRB must decide the mode before design starts.

## Terms to know

- **General ledger (GL):** the bank's official books. See `glossary.gl`.
- **CBS:** the bank's main system. See `glossary.cbs`.
- **RPA:** a software robot that types entries into the CBS screens. See `glossary.rpa`.
- **Demand-only servicing:** the loan system works out what is owed; it does not post to the ledger.
