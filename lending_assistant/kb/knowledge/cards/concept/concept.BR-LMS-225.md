---
id: concept.BR-LMS-225
type: concept
title: Alerts when jobs fail
summary: "Scheduled jobs and connections are monitored. When one fails, or fails several times in a row, someone is alerted, and nothing is allowed to fail silently."
br_ids: [BR-LMS-225]
brd_section: 7.13
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-225"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p55"
  - "sources/verification/reqs.json#BR-LMS-225"
  - "sources/verification/verification_report.md#BR-LMS-225"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-225"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-225"
related: [bridge.BR-LMS-225, brd_section.7.13, glossary.batch, concept.BR-LMS-224]
version: 1
status: approved
approved_by: Owner
---
**In short:** Scheduled jobs and connections are monitored. When one fails, or fails several times in a row, someone is alerted, and nothing is allowed to fail silently.

## What the rule says

BR-LMS-225 in section 7.13 (Must, BRD PDF page 55) says scheduled and integration jobs shall be monitored, and shall alert on failure or on consecutive failure rather than degrading silently.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a nightly job that stops without a word leaves the loan book wrong by morning, and a person must be told while there is still time to fix it.

## Example

The nightly interest job fails at 2 a.m., and the operations team gets an email and an SMS at once.

## Terms to know

- **Monitoring:** watching that each job ran and finished.
- **Alert:** a message sent to a person when something fails.
- **Consecutive failure:** the same job failing several times in a row.
- **Silent failure:** a failure no one is told about.
