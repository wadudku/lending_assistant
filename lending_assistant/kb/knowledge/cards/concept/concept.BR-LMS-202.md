---
id: concept.BR-LMS-202
type: concept
title: A write-off keeps the history
summary: "A write-off takes the expected loss off the bank's books, but the loan, its repayment plans, its payments and its grade history must stay fully viewable."
br_ids: [BR-LMS-202]
brd_section: 7.11
doctypes: []
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-202"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p54"
  - "sources/verification/reqs.json#BR-LMS-202"
  - "sources/verification/verification_report.md#BR-LMS-202"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-202"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-202"
related: [bridge.BR-LMS-202, brd_section.7.11, glossary.write-off, glossary.schedule-version, decision.write-off, lifecycle.WRITTEN_OFF]
version: 1
status: approved
approved_by: Owner
---
**In short:** A write-off takes the expected loss off the bank's books, but the loan, its repayment plans, its payments and its grade history must stay fully viewable.

## What the rule says

BR-LMS-202 in section 7.11 (Must, BRD PDF page 54) says a write-off shall record the accounting and business effect without destroying the loan's history. The loan record, its schedule versions, its postings and its classification history shall remain fully retrievable.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a written-off loan can still be recovered, audited or questioned years later, and the history is the evidence.

## Example

Five years after the write-off, an auditor can still open Rahim's loan and see every bill and payment.

## Terms to know

- **Write-off:** removing a loan from the books as a loss. See `glossary.write-off`.
- **Schedule version:** one numbered repayment plan. See `glossary.schedule-version`.
- **Retrievable:** can still be opened and read in full.
