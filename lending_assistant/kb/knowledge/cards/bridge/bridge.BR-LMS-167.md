---
id: bridge.BR-LMS-167
type: bridge
title: Money nobody can match goes to a queue
summary: "Partly covered. ERPNext keeps unreconciled bank transactions that can be matched to repayments, but there is no owner, ageing or reason, and no create-repayment action in 16.5.1."
br_ids: [BR-LMS-167]
brd_section: 7.7
doctypes: [Bank Transaction, Loan Repayment]
verdict: partial
analysis_status: verified
dev_items: [D12]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-167"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p51"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p52"
  - "sources/verification/reqs.json#BR-LMS-167"
  - "sources/verification/verification_report.md#BR-LMS-167"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-167"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-167"
related: [concept.BR-LMS-167, devitem.D12, bridge.BR-LMS-162]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. ERPNext keeps unreconciled bank transactions that can be matched to repayments, but there is no owner, ageing or reason, and no create-repayment action in 16.5.1.

## Business need

Unattributed money needs a queue with an owner and ageing, and the match must be recorded with who did it and why (BR-LMS-167, BRD 7.7.1, PDF page 51). See `concept.BR-LMS-167`.

## Frappe Lending today

ERPNext's **Bank Transaction** keeps imported bank lines that are not yet reconciled. Lending registers its loan documents for ERPNext's Bank Reconciliation Tool, so an existing **Loan Repayment** can be matched to a bank line. This was confirmed from the code and the installed metadata, not by a live test.

## Match or gap, and why

This is **partly covered**. A list of unmatched bank lines exists, and matching a line to an existing repayment is possible. But the queue has no owner, no ageing and no reason field, which the BRD rule asks for. In 16.5.1 there is also no action to create a repayment from a bank transaction, and Bank Transaction has no loan field. The original analysis assumed that action existed, so the verification corrected it.

The design also waits on NRB. BRD section 7.7.2 lists open items: which channels carry payments, how a credit is detected, and who owns the queue (PDF pages 51 and 52). The BRD says each must be answered before repayment collection can be designed.

## What to do today

Keep unmatched bank lines in Bank Transaction and match them in the Bank Reconciliation Tool once the loan is known. Track the owner and age outside the system, for example in a shared sheet.

## Planned fix

D12 (`devitem.D12`) adds an Unidentified Receipt queue with owner, ageing and attribution reason. Its final design waits on the answers to BRD section 7.7.2.
