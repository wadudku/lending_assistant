---
id: concept.BR-LMS-160
type: concept
title: Record a confirmed payment with full details
summary: "Every repayment is stored with its channel, its CBS reference, the amount and two dates: when the money really arrived and when staff entered it."
br_ids: [BR-LMS-160]
brd_section: 7.7
doctypes: []
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-160"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p50"
  - "sources/verification/reqs.json#BR-LMS-160"
  - "sources/verification/verification_report.md#BR-LMS-160"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-160"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-160"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-010"
related: [bridge.BR-LMS-160, glossary.value-date, glossary.posting-date, glossary.cbs]
version: 1
status: approved
approved_by: Owner
---
**In short:** Every repayment is stored with its channel, its CBS reference, the amount and two dates: when the money really arrived and when staff entered it.

## What the rule says

BR-LMS-160 (priority Must, BRD 7.7.1, PDF page 50) says the platform records a confirmed borrower payment against the loan. The record carries the payment channel, the external reference by which the payment can be traced in the Core Banking System (CBS), the amount, the value date and the posting date.

## Why the bank wants it

The BRD gives the reason in two places. The reference is the one "by which it can be traced in the Core Banking System" (BR-LMS-160, PDF page 50), and the CBS is authoritative for every financial fact after booking (BRD 3.3, PDF page 19). So each payment must lead back to one CBS transaction. For the dates, a guiding principle says value date, posting date, effective date and system timestamp are recorded and used as distinct concepts and never conflated (BR-GOV-010, PDF page 19). The BRD doesn't say why in more detail; the usual reason is that the two dates answer different questions: lateness and interest follow the day the money arrived, while bookkeeping follows the day the entry was made.

## Example

Rahim pays 8,979 at a branch on 5 July. Staff enter it on 6 July. The CBS reference is CBS-TXN-0001 and the channel is Branch. The payment record shows all five facts: channel Branch, reference CBS-TXN-0001, amount 8,979, value date 5 July, posting date 6 July.

## Terms to know

- **Value date:** the day the money actually arrived. See `glossary.value-date`.
- **Posting date:** the day the entry was recorded in the loan system. See `glossary.posting-date`.
- **CBS reference:** the transaction number the CBS gave the payment. See `glossary.cbs`.
- **Channel:** how the money came in, for example branch, mobile or bank transfer.
