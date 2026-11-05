---
id: bridge.BR-LMS-115
type: bridge
title: Two ways of keeping the accounts
summary: "Partly covered. A Company switch turns loan accounting on or off and a consolidation option reduces posting volume, but 16.5.1 has no code that posts to the CBS."
br_ids: [BR-LMS-115]
brd_section: 7.2
doctypes: [Company]
verdict: partial
analysis_status: verified
dev_items: [D13]
fields: [Company.Enable Loan Accounting, Company.Consolidate Loan GL Monthly]
lending_version: 16.5.1
code_refs: ["lending/install.py:93", "lending/loan_management/utils.py:321"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-115"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p47"
  - "sources/verification/reqs.json#BR-LMS-115"
  - "sources/verification/verification_report.md#BR-LMS-115"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-115"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-115"
related: [concept.BR-LMS-115, brd_section.7.2, devitem.D13, glossary.gl, glossary.rpa]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. A Company switch turns loan accounting on or off and a consolidation option reduces posting volume, but 16.5.1 has no code that posts to the CBS.

## Business need

The bank wants two accounting modes, one that posts to its own ledger and one where the CBS keeps the ledger, and the choice must be configurable (BR-LMS-115, BRD 7.2, PDF page 47). See `concept.BR-LMS-115`.

## Frappe Lending today

The **Company** has **Enable Loan Accounting** (`install.py` line 93); the code reads it through `loan_accounting_enabled` (`utils.py` lines 321-322). It also has **Consolidate Loan GL Monthly** with a start date (`install.py` lines 113-120): a Company checkbox that posts one consolidated ledger voucher a month for accruals and demands, which reduces the number of postings. It is not a separate document type.

## Match or gap, and why

This is **partly covered**. Switching loan accounting off gives demand-only servicing, and switching it on gives a ledger inside Frappe Lending. In the test, the site had loan accounting on (verification_report.md:139). A search of the installed 16.5.1 code (Python, JSON and JavaScript, outside tests) for CBS, core banking and RPA finds no match, so nothing sends an entry to the CBS. The coverage analysis says the RPA route has to be built, and the decision between the modes is the bank's (the BRD asks NRB to confirm it before design).

## What to do today

Ask NRB to confirm the mode. Until then keep loan accounting as set on the site. Use Consolidate Loan GL Monthly to reduce volume if the robot route is chosen.

## Planned fix

Dev item D13 (`devitem.D13`) builds the outbox that sends entries to the CBS through a robot and brings the CBS journal number back.
