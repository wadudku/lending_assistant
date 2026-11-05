---
id: concept.BR-LMS-205
type: concept
title: "Full record for every settlement, waiver, write-off and recovery"
summary: "Each settlement, waiver, write-off and recovery keeps the amounts before and after, the reason, the person who made it, the person who approved it, the approval date and any external reference."
br_ids: [BR-LMS-205]
brd_section: 7.11
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-205"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p54"
  - "sources/verification/reqs.json#BR-LMS-205"
  - "sources/verification/verification_report.md#BR-LMS-205"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-205"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-205"
related: [bridge.BR-LMS-205, brd_section.7.11, glossary.maker-checker, glossary.waiver, decision.waiver]
version: 1
status: approved
approved_by: Owner
---
**In short:** Each settlement, waiver, write-off and recovery keeps the amounts before and after, the reason, the person who made it, the person who approved it, the approval date and any external reference.

## What the rule says

BR-LMS-205 in section 7.11 (Must, BRD PDF page 54) says every settlement, waiver, write-off and recovery shall preserve before and after amounts, the stated reason, the maker, the checker, the approval date and any external reference.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that these actions give up or reshape money the bank is owed, so an auditor must be able to read the full story from the record alone.

## Example

A settlement is recorded as: before 95,000, after 0, waived 15,000, reason "hardship", maker Officer A, checker Manager B, approved 10 November 2026, reference CBS-TXN-0150.

## Terms to know

- **Maker:** the person who enters the action.
- **Checker:** the different person who approves it. See `glossary.maker-checker`.
- **Before and after amounts:** what was owed before the action and what is owed after it.
- **External reference:** a number from outside the system, such as a bank or memo number.
