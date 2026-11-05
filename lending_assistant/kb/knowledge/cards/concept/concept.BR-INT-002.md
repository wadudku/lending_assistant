---
id: concept.BR-INT-002
type: concept
title: "Account lookups are queued, with an agreed rate or an offline file"
summary: "Account enquiries are queued at a throughput agreed at design stage; if a same-day batch cannot be checked fast enough, the bank and supplier agree more automation capacity or an offline file."
br_ids: [BR-INT-002]
brd_section: 9.2.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-002"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p61"
related: [bridge.BR-INT-002, glossary.cbs, glossary.rpa]
version: 1
status: approved
approved_by: Owner
---
**In short:** Account enquiries are queued at a throughput agreed at design stage; if a same-day batch cannot be checked fast enough, the bank and supplier agree more automation capacity or an offline file.

## What the rule says

BR-INT-002 (Must, BRD 9.2.1, PDF page 61) says account enquiry is queued and sustains the throughput the bank agrees at design stage. Where a same-day batch cannot be validated at the required rate, the bank and the supplier agree one of two things: additional automation capacity, or a file-based extract from the core banking system against which validation is done offline.

## Why the bank wants it

The BRD gives the reason in section 9.2: “Account validation of a 500-row batch cannot complete synchronously in minutes; it becomes a queued process measured in tens of minutes to hours, sized by the concurrency the Bank can make available.” (PDF page 60).

## Example

A partner sends 500 accounts on the morning of a disbursement meeting. The lookups join a queue and are answered over the next hour. If that is too slow for the meeting, the bank and supplier have already agreed to add a second automation session or to use a file the core banking system produces each morning.

## Terms to know

- **Queued:** waiting in line, handled one after another.
- **Throughput:** how many items are handled in a given time.
- **File-based extract:** a file of account data the core banking system produces for use elsewhere.
- **Offline:** checked against a copy, without asking the core banking system each time.
