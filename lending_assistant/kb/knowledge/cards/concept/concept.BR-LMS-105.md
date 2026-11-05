---
id: concept.BR-LMS-105
type: concept
title: "Bring existing loans over from the old system, and prove the totals match"
summary: "On go-live the bank's current loans move over with their balances and a reference to the old record, and the totals are checked against the old system before the loans start running."
br_ids: [BR-LMS-105]
brd_section: 7.1
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-105"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p46"
  - "sources/verification/reqs.json#BR-LMS-105"
  - "sources/verification/verification_report.md#BR-LMS-105"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-105"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-105"
related: [bridge.BR-LMS-105, brd_section.7.1, devitem.D3, glossary.cbs]
version: 1
status: approved
approved_by: Owner
---
**In short:** On go-live the bank's current loans move over with their balances and a reference to the old record, and the totals are checked against the old system before the loans start running.

## What the rule says

BR-LMS-105 (priority Must, BRD 7.1, PDF page 46) says the LMS supports migration of an existing loan position. The migrated loan carries its opening principal, interest, penalty and charge balances, with source references. The LMS must also reconcile the imported control totals against the source system before the migrated loans become active.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a migrated loan starts with figures nobody at the bank created in this system, so the only proof they are right is that the totals agree with the old system before billing and interest begin.

## Example

The old system holds 12,000 loans with a total principal of 4.5 billion BDT. After the import, the LMS must show the same total. If it shows 4.49 billion, the difference is found and fixed before go-live.

## Terms to know

- **Opening balance:** the amount owed on the day the loan moves over.
- **Control total:** a sum taken from the old system, such as total principal, used to prove the import is complete.
- **Source reference:** the old system's number for the loan.
- **Reconcile:** compare two sets of figures and explain every difference.
