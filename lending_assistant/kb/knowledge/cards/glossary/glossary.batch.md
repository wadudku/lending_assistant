---
id: glossary.batch
type: glossary
title: Batch
summary: "In the BRD's definitions, one file uploaded by a partner with many applications. In Section 7 the word is also used for a job that runs over many loans at once."
br_ids: [BR-LMS-135, BR-LMS-223]
brd_section: 7.13
doctypes: []
dev_items: []
terms: [batch, partner file, batch run]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#1.5"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-135"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-223"
related: [devitem.D9]
version: 1
status: approved
approved_by: Owner
---
**In short:** In the BRD's definitions, one file uploaded by a partner with many applications. In Section 7 the word is also used for a job that runs over many loans at once.

## Plain meaning

The BRD defines a batch as one file uploaded by a partner, containing many applications (BRD 1.5). Section 7 uses the word in a second way: a job that processes many loans, such as the demand run or a repricing run.

## Example

A partner sends one file with 500 applications. That file is a batch. Separately, the nightly job that raises demands for 10,000 loans is also called a batch process.

## Why it matters here

BR-LMS-223 says each batch process keeps an explicit state (draft, queued, in process, completed or cancelled) with row-level outcomes, and can be resumed without double posting. The verification found that the accrual, demand and classification runs lack this state.

## See also

`devitem.D9`.
