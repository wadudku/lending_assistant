---
id: concept.BR-LOS-106
type: concept
title: Partner performance is visible on one partner record
summary: "The Bank sees each partner's submission volume, validation failure rate, sampling rejection rate, disbursement conversion and, where servicing can supply it, arrears performance on a single record."
br_ids: [BR-LOS-106]
brd_section: 6.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-106"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p29"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-100"
related: [bridge.BR-LOS-106, glossary.partner, glossary.sampling]
version: 1
status: approved
approved_by: Owner
---
**In short:** The Bank sees each partner's submission volume, validation failure rate, sampling rejection rate, disbursement conversion and, where servicing can supply it, arrears performance on a single record.

## What the rule says

BR-LOS-106 (Must, BRD 6.1, PDF page 29) says partner performance is visible to the Bank on a single partner record: submission volume, validation failure rate, sampling rejection rate, disbursement conversion and, where available from servicing, arrears performance. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the Bank decides on ceilings and suspension by looking at how each partner performs, so the figures should be in one place.

## Example

An officer opens one partner's record and sees: 1,200 applications sent this quarter, 8% failed validation, 3% rejected at sampling, 70% reached disbursement, and the share of its loans that are overdue.

## Terms to know

- **Validation failure rate:** the share of submitted rows that failed the checks.
- **Sampling rejection rate:** the share of sampled applications rejected on review.
- **Disbursement conversion:** the share of applications that end in a payout.
- **Arrears:** money past its due date.
