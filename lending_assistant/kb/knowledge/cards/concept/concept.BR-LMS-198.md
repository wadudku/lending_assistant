---
id: concept.BR-LMS-198
type: concept
title: Chasing late payers (collections)
summary: "Late loans enter a collections process: a record of every contact, promises to pay and whether they were kept, follow-up dates, and escalation to recovery or legal action."
br_ids: [BR-LMS-198]
brd_section: 7.10
doctypes: []
verdict: gap
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-198"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p54"
  - "sources/verification/reqs.json#BR-LMS-198"
  - "sources/verification/verification_report.md#BR-LMS-198"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-198"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-198"
related: [bridge.BR-LMS-198, brd_section.7.10, glossary.ptp, glossary.dpd]
version: 1
status: approved
approved_by: Owner
---
**In short:** Late loans enter a collections process: a record of every contact, promises to pay and whether they were kept, follow-up dates, and escalation to recovery or legal action.

## What the rule says

BR-LMS-198 in section 7.10 (Must, BRD PDF page 54) says delinquent loans shall enter a collections workflow supporting contact history, promises to pay and their fulfilment, follow-up scheduling, and escalation to recovery.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that chasing late payers is a series of dated steps by different people, and the bank must be able to show what was done, what was promised and when it was escalated.

## Example

On 21 October a call is made and Rahim promises to pay by 25 October. On 26 October the promise is broken. On 1 November a field visit is booked. At 120 days late the case is escalated to legal.

## Terms to know

- **Collections:** the work of getting late payments in.
- **Promise to pay (PTP):** a borrower's dated promise to pay. See `glossary.ptp`.
- **Escalation:** passing a case to a stronger step, such as recovery or legal action.
- **Contact history:** the dated list of calls and visits.
