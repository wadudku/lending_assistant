---
id: concept.BR-LMS-159
type: concept
title: Tell the borrowers
summary: "After a repricing is approved and active, the affected borrowers are told through the configured notification channel."
br_ids: [BR-LMS-159]
brd_section: 7.6
doctypes: []
verdict: gap
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-159"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p50"
  - "sources/verification/reqs.json#BR-LMS-159"
  - "sources/verification/verification_report.md#BR-LMS-159"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-159"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-159"
related: [bridge.BR-LMS-159, brd_section.7.6, glossary.repricing]
version: 1
status: approved
approved_by: Owner
---
**In short:** After a repricing is approved and active, the affected borrowers are told through the configured notification channel.

## What the rule says

BR-LMS-159 (priority Must, BRD 7.6, PDF page 50) says affected borrowers are notified after the repricing is approved and activated, through the configured notification channel.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a borrower whose rate and instalment change must hear about it from the bank, in time, rather than find out from a bill.

## Example

SMS: "Your loan rate changes to 15% from 1 January 2027. Your new EMI is 9,019."

## Terms to know

- **Notification channel:** SMS, email or another way to reach the borrower.
- **Activated:** the new rate and plan are in force.
- **Repricing:** see `glossary.repricing`.
- **Borrower notice:** the message that tells a borrower the new rate, the effective date and the new instalment.
- **Approved and activated:** the checker has accepted the change and the new plan is in force.
