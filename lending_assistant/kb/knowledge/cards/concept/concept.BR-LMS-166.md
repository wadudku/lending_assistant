---
id: concept.BR-LMS-166
type: concept
title: Upload many payments in one file
summary: "Many payments can be loaded from one file. Every row is checked before anything posts, each row reports success or failure, and a stopped upload can continue."
br_ids: [BR-LMS-166]
brd_section: 7.7
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-166"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p51"
  - "sources/verification/reqs.json#BR-LMS-166"
  - "sources/verification/verification_report.md#BR-LMS-166"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-166"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-166"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p52"
related: [bridge.BR-LMS-166, devitem.D12]
version: 1
status: approved
approved_by: Owner
---
**In short:** Many payments can be loaded from one file. Every row is checked before anything posts, each row reports success or failure, and a stopped upload can continue.

## What the rule says

BR-LMS-166 (Must, BRD 7.7.1, PDF page 51) says bulk repayment upload is supported, with validation before posting and row-level success and failure reporting, and that the upload is resumable.

## Why the bank wants it

The BRD doesn't say why for this rule; the usual reason is that partners and branches send many payments at once, and a big file brings its own risks: one bad row should not spoil the others, nobody should have to guess which rows went in, and a stop halfway should not leave the file half posted with no way to continue. For partner bulk remittances the BRD adds one control: the file total must reconcile to the credit before any allocation is made (BRD 7.7.2, PDF page 52).

## Example

A partner sends a file of 2,000 payments. 1,990 are posted, and 10 are rejected, each with a reason such as an unknown loan number. If the system stops after 1,200 rows, the next run continues from row 1,201 and does not repeat the first 1,200.

## Terms to know

- **Validation before posting:** every row is checked first, then the good rows are posted.
- **Row-level result:** a success or failure status for each line.
- **Resumable:** a stopped job continues from where it stopped.
- **Batch:** many items processed in one run.
