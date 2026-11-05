---
id: bridge.BR-LMS-133
type: bridge
title: Never delete or quietly change a bill
summary: "Partly covered. A submitted bill is cancelled, not deleted, and stays visible, but in the test a cancel needed no reason and no approver."
br_ids: [BR-LMS-133]
brd_section: 7.4
doctypes: [Loan Demand]
verdict: partial
analysis_status: verified
dev_items: [D8]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_demand/loan_demand.json:324", "lending/loan_management/doctype/loan_demand/loan_demand.py:107"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-133"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p48"
  - "sources/verification/reqs.json#BR-LMS-133"
  - "sources/verification/verification_report.md#BR-LMS-133"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-133"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-133"
related: [concept.BR-LMS-133, brd_section.7.4, devitem.D8, glossary.demand, glossary.maker-checker]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. A submitted bill is cancelled, not deleted, and stays visible, but in the test a cancel needed no reason and no approver.

## Business need

The bank wants a demand corrected only through a controlled reversal with a reason and an approver, with both records visible (BR-LMS-133, BRD 7.4, PDF page 48). See `concept.BR-LMS-133`.

## Frappe Lending today

A **Loan Demand** is submittable (`loan_demand.json` line 324), so a submitted demand can be cancelled, not edited. On cancel the ledger entries are reversed (`loan_demand.py` lines 107-113) and the demand stays visible as Cancelled. The Loan Demand form has no field for a reason or an approver (a search of `loan_demand.json` for "reason" and "approv" finds nothing).

## Match or gap, and why

This is **partly covered**. In the test, a System Manager cancelled two unpaid demands in one step, with no reason field, no approver, no workflow, no Version row and no comment (verification_report.md:823). The original ledger entries stayed, a reversing pair was added, and the demand showed as Cancelled. Days past due went from 30 to 0 after the cancel, so one click erased a 30-day delinquency, and a new bill run raised the same instalment again at once. Cancelling a partly paid demand was blocked until the repayment was cancelled first (DEF-47). In the test, Loan Manager had no cancel right on Loan Demand. The coverage analysis rated it partly covered, and verification confirmed that.

## What to do today

Keep the cancel right on Loan Demand with as few people as possible, and record the reason and approver outside the system.

## Planned fix

Dev item D8 (`devitem.D8`) adds a controlled reversal with a reason and an approver. Verification added ND-45.
