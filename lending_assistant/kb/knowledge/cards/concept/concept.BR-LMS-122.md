---
id: concept.BR-LMS-122
type: concept
title: Rebuild the plan when money is paid out in parts
summary: "When a loan is paid out in stages, the repayment plan is rebuilt or adjusted each time a part is released, following the approved tranche rules."
br_ids: [BR-LMS-122]
brd_section: 7.3
doctypes: []
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-122"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p48"
  - "sources/verification/reqs.json#BR-LMS-122"
  - "sources/verification/verification_report.md#BR-LMS-122"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-122"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-122"
related: [bridge.BR-LMS-122, brd_section.7.3, lifecycle.PARTIALLY_DISBURSED, glossary.loc]
version: 1
status: approved
approved_by: Owner
---
**In short:** When a loan is paid out in stages, the repayment plan is rebuilt or adjusted each time a part is released, following the approved tranche rules.

## What the rule says

BR-LMS-122 (priority Must, BRD 7.3, PDF page 48) says that where a product supports scheduled or tranche disbursement, the schedule is regenerated or adjusted according to the approved tranche rules on each confirmed drawdown.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that each part released adds to what is owed, so the instalments and the end date must change with it.

## Example

A home loan of 1,000,000 is paid out as 400,000, then 300,000, then 300,000. After the second part is released, the EMI goes up because more money is now owed.

## Terms to know

- **Tranche:** one part of a loan paid out in stages.
- **Drawdown:** the release of a tranche.
- **Partially disbursed:** some of the approved money is still to come. See `lifecycle.PARTIALLY_DISBURSED`.
