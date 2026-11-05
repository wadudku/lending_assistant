---
id: concept.BR-LOS-305
type: concept
title: Refer and decline outcomes carry reason codes
summary: "Every refer and decline records the main adverse factors as reason codes from a configurable list, so the Bank can explain the decision inside and, where required, to the applicant."
br_ids: [BR-LOS-305]
brd_section: 6.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-305"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p34"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-308"
related: [bridge.BR-LOS-305, concept.BR-LOS-308]
version: 1
status: approved
approved_by: Owner
---
**In short:** Every refer and decline records the main adverse factors as reason codes from a configurable list, so the Bank can explain the decision inside and, where required, to the applicant.

## What the rule says

BR-LOS-305 (Must, BRD 6.4, PDF page 34) says every refer and every decline records the principal adverse factors that drove the outcome, as reason codes drawn from a configurable list, so that the Bank can explain the decision internally and to the applicant where policy or law requires it. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD gives the reason in the row itself: so that the Bank can explain the decision internally and to the applicant where policy or law requires it (PDF page 34).

## Example

An application is declined. The record carries two reason codes from the Bank's list: “Instalment too high for income” and “Negative list match”. A clerk can later read them to the applicant if the rules require.

## Terms to know

- **Reason code:** a short coded reason picked from a list.
- **Adverse factor:** a fact that pushed the result towards refusal or review.
- **Configurable list:** a list the Bank can change without a software release.
- **Principal:** main; the biggest causes.
