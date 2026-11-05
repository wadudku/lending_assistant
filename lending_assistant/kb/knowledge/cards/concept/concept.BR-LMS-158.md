---
id: concept.BR-LMS-158
type: concept
title: "Skip loans that shouldn't be repriced, automatically"
summary: "Fixed-rate, closed, written-off, frozen and other ineligible loans are left out automatically, and the reason is recorded."
br_ids: [BR-LMS-158]
brd_section: 7.6
doctypes: []
verdict: gap
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-158"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p50"
  - "sources/verification/reqs.json#BR-LMS-158"
  - "sources/verification/verification_report.md#BR-LMS-158"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-158"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-158"
related: [bridge.BR-LMS-158, brd_section.7.6, decision.freeze, glossary.write-off, glossary.repricing]
version: 1
status: approved
approved_by: Owner
---
**In short:** Fixed-rate, closed, written-off, frozen and other ineligible loans are left out automatically, and the reason is recorded.

## What the rule says

BR-LMS-158 (priority Must, BRD 7.6, PDF page 50) says fixed-rate, closed, written-off, frozen and otherwise ineligible or conflicting loans are excluded automatically, and the exclusion is recorded.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a repricing must not touch a loan whose rate is fixed or whose account is closed or frozen, and a person should not have to find those loans by hand.

## Example

A loan frozen after the borrower's death is skipped with the reason "frozen since 15 August 2026".

## Terms to know

- **Ineligible loan:** a loan that must not be repriced, such as a fixed-rate or closed loan.
- **Frozen:** the account is blocked. See `decision.freeze`.
- **Written off:** see `glossary.write-off`.
- **Conflicting loan:** a loan with another change already in progress, such as an open restructure.
- **Recorded exclusion:** the reason a loan was skipped is stored, so staff can review it later.
