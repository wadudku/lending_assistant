---
id: concept.BR-LMS-111
type: concept
title: "Store the interest rate, how it is calculated, and whether it is fixed or floating"
summary: "For each product the loan system stores the rate, the calculation method and the rate type. A floating product also stores how often the rate is reviewed and which reference rate it follows."
br_ids: [BR-LMS-111]
brd_section: 7.2
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-111"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p47"
  - "sources/verification/reqs.json#BR-LMS-111"
  - "sources/verification/verification_report.md#BR-LMS-111"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-111"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-111"
related: [bridge.BR-LMS-111, brd_section.7.2, devitem.D4, glossary.repricing]
version: 1
status: approved
approved_by: Owner
---
**In short:** For each product the loan system stores the rate, the calculation method and the rate type. A floating product also stores how often the rate is reviewed and which reference rate it follows.

## What the rule says

BR-LMS-111 (priority Must, BRD 7.2, PDF page 47) says rate configuration stores four things: the applicable rate, the calculation method, and the rate type as fixed or floating. For floating products it also stores the repricing frequency and the reference against which repricing is applied.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a floating-rate loan changes with a published benchmark, so the system needs to know both which benchmark it follows and how often to look at it.

## Example

"Reference rate plus 3%, reviewed every 6 months." If the reference rate moves from 9% to 10%, the loan rate moves from 12% to 13% at the next review.

## Terms to know

- **Fixed rate:** the rate does not change during the loan.
- **Floating rate:** the rate moves with a published reference rate.
- **Reference rate (benchmark):** the published rate that a floating loan follows.
- **Repricing:** changing the rate on existing loans. See `glossary.repricing`.
