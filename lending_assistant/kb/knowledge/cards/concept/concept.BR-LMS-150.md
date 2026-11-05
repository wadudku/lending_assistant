---
id: concept.BR-LMS-150
type: concept
title: Choose which loans to reprice
summary: "Staff can select the loans to reprice by product, customer segment, branch or loan number, limited to active floating-rate loans."
br_ids: [BR-LMS-150]
brd_section: 7.6
doctypes: []
verdict: gap
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-150"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p49"
  - "sources/verification/reqs.json#BR-LMS-150"
  - "sources/verification/verification_report.md#BR-LMS-150"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-150"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-150"
related: [bridge.BR-LMS-150, brd_section.7.6, glossary.repricing]
version: 1
status: approved
approved_by: Owner
---
**In short:** Staff can select the loans to reprice by product, customer segment, branch or loan number, limited to active floating-rate loans.

## What the rule says

BR-LMS-150 (priority Must, BRD 7.6, PDF page 49) says staff can select eligible loans for repricing by product, customer segment, branch or explicit loan identifiers. The selection is restricted to active floating-rate loans.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a rate change touches thousands of loans at once, so the bank needs a controlled way to pick exactly which loans are included, and must not touch a loan whose rate is fixed.

## Example

"All Home Loan - Floating loans in Dhaka branches": 5,000 loans selected.

## Terms to know

- **Repricing:** changing the interest rate on existing loans. See `glossary.repricing`.
- **Floating-rate loan:** a loan whose rate follows a reference rate.
- **Eligible loan:** a loan that is active and floating, and not otherwise excluded.
- **Segment:** a group of customers, such as retail or SME.
