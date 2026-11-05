---
id: concept.BR-LMS-167
type: concept
title: Money nobody can match goes to a queue
summary: "Money that cannot be matched to a loan waits in an unidentified-receipts queue with an owner and an age, and does not reduce anyone's balance until it is matched."
br_ids: [BR-LMS-167]
brd_section: 7.7
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-167"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p51"
  - "sources/verification/reqs.json#BR-LMS-167"
  - "sources/verification/verification_report.md#BR-LMS-167"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-167"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-167"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p52"
related: [bridge.BR-LMS-167, devitem.D12]
version: 1
status: approved
approved_by: Owner
---
**In short:** Money that cannot be matched to a loan waits in an unidentified-receipts queue with an owner and an age, and does not reduce anyone's balance until it is matched.

## What the rule says

BR-LMS-167 (Must, BRD 7.7.1, PDF page 51) says money that cannot be attributed to a loan is held in an unidentified-receipts queue with an owner and visible ageing. It does not reduce any borrower's outstanding position until it has been attributed, and the attribution is recorded with its actor and reason.

## Why the bank wants it

The BRD gives the reason in its open items for 7.7: unattributed money "is both a customer service failure and a reconciliation break", so it needs a named owner and a clearance standard. Attribution depends on a reference the payer must quote, or on the credit landing in an account dedicated to one loan; where neither holds, unidentified receipts pile up and become manual matching work (BRD 7.7.2, PDF page 52). Recording who attributed the money, and why, keeps an audit trail.

## Example

5,000 BDT arrives with the note "Rahim" only. It sits in the queue, 3 days old, owned by Operations, until someone confirms which loan it belongs to and records the reason.

## Terms to know

- **Attribution:** deciding which loan a receipt belongs to.
- **Ageing:** how long an item has been waiting.
- **Unidentified receipt:** money received but not yet linked to a loan.
- **Reconciliation:** comparing two records and reporting differences.
