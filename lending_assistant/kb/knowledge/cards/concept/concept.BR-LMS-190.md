---
id: concept.BR-LMS-190
type: concept
title: "Count days late every day, and keep the history"
summary: "Every day the platform works out how many days late each loan is, from its unpaid bills, and keeps that day's figure on record."
br_ids: [BR-LMS-190]
brd_section: 7.10
doctypes: []
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-190"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p53"
  - "sources/verification/reqs.json#BR-LMS-190"
  - "sources/verification/verification_report.md#BR-LMS-190"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-190"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-190"
related: [bridge.BR-LMS-190, brd_section.7.10, glossary.dpd, glossary.demand]
version: 1
status: approved
approved_by: Owner
---
**In short:** Every day the platform works out how many days late each loan is, from its unpaid bills, and keeps that day's figure on record.

## What the rule says

BR-LMS-190 in section 7.10 (Must, BRD PDF page 53) says the platform shall calculate days past due daily from unpaid demands and shall maintain a daily history of the days-past-due position of every loan.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a loan's grade, its interest treatment and its reporting all depend on how late it is, so the bank needs the figure for every day and not only for today.

## Example

EMI 1, due on 5 July, is unpaid. On 4 August the loan is 31 days late, and every day's figure from 5 July is kept.

## Terms to know

- **Days past due (DPD):** the number of days since the oldest unpaid amount fell due. See `glossary.dpd`.
- **Demand:** the bill raised for an instalment or charge when it falls due. See `glossary.demand`.
- **Daily history:** one stored figure per loan per day.
