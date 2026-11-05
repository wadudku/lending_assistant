---
id: concept.BR-LOS-312
type: concept
title: Scorecard performance is reported so the scorecard can be recalibrated
summary: "The platform reports score and grade distribution, approval and decline rates by grade, override volume and reason, spread by partner and geography and, once servicing data is in use, delinquency and loss by grade band."
br_ids: [BR-LOS-312]
brd_section: 6.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-312"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p34"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-309"
related: [bridge.BR-LOS-312, concept.BR-LOS-309, glossary.scorecard, glossary.score-cut-off]
version: 1
status: approved
approved_by: Owner
---
**In short:** The platform reports score and grade distribution, approval and decline rates by grade, override volume and reason, spread by partner and geography and, once servicing data is in use, delinquency and loss by grade band.

## What the rule says

BR-LOS-312 (Must, BRD 6.4, PDF page 34) says the platform reports scorecard performance: score and grade distribution, approval and decline rates by grade, override volume and reason, distribution by partner and by geography, and, once servicing data exists, delinquency and loss by grade band, to support recalibration. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD gives the reason in the row itself: to support recalibration (PDF page 34).

## Example

Every quarter Credit Risk opens the report and sees that grade C has twice the arrears expected. It uses this to adjust the cut-offs and weights.

## Terms to know

- **Recalibration:** adjusting the scorecard using results.
- **Delinquency:** late repayment.
- **Loss:** money not recovered.
- **Distribution:** how cases spread across scores, grades, partners or places.
