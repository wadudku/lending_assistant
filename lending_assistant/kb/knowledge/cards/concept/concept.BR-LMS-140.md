---
id: concept.BR-LMS-140
type: concept
title: Count interest every day (accrual)
summary: "The system counts normal interest as it builds up, following the product's accrual frequency and using the balance, rate, day-count convention and dates."
br_ids: [BR-LMS-140]
brd_section: 7.5
doctypes: []
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-140"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p49"
  - "sources/verification/reqs.json#BR-LMS-140"
  - "sources/verification/verification_report.md#BR-LMS-140"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-140"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-140"
related: [bridge.BR-LMS-140, brd_section.7.5, glossary.bpi, glossary.emi]
version: 1
status: approved
approved_by: Owner
---
**In short:** The system counts normal interest as it builds up, following the product's accrual frequency and using the balance, rate, day-count convention and dates.

## What the rule says

BR-LMS-140 (priority Must, BRD 7.5, PDF page 49) says the platform accrues normal interest according to the product's accrual frequency. It is calculated from the applicable balance, rate, day-count convention and effective dates.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that interest is earned a day at a time but billed monthly, so the books must count it daily to show the bank's income in the right period.

## Example

100,000 x 14% / 365 = 38.36 BDT a day. After 30 days, about 1,151 has accrued. That is the interest part of EMI 1.

## Terms to know

- **Accrual:** counting interest as it is earned, before it is billed.
- **Day-count convention:** the rule for the number of days in a year, such as Actual/365.
- **Accrual frequency:** how often the interest is counted.
