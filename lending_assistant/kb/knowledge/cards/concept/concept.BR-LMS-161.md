---
id: concept.BR-LMS-161
type: concept
title: A payment counts only after the CBS confirms it
summary: "A payment that is started but not confirmed by the CBS must never reduce what the borrower owes, and must show as pending, not paid."
br_ids: [BR-LMS-161]
brd_section: 7.7
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-161"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p50"
  - "sources/verification/reqs.json#BR-LMS-161"
  - "sources/verification/verification_report.md#BR-LMS-161"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-161"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-161"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-001"
related: [bridge.BR-LMS-161, glossary.cbs]
version: 1
status: approved
approved_by: Owner
---
**In short:** A payment that is started but not confirmed by the CBS must never reduce what the borrower owes, and must show as pending, not paid.

## What the rule says

BR-LMS-161 (Must, BRD 7.7.1, PDF page 50) says a payment is not successful until the Core Banking System confirms it. A pending, initiated or unconfirmed collection never reduces the borrower's outstanding position, and it is visible as pending rather than as paid.

## Why the bank wants it

The BRD's reason is its general principle: the platform never moves money on its own authority, every financial action is an instruction to the CBS and a record of its reply (BR-GOV-001, PDF page 19), and the CBS is authoritative for every financial fact after booking (BRD 3.3, PDF page 19). The BRD doesn't say why in more detail for this rule; the usual reason is that a payment can be started and then fail, and a loan system that counted it at once would show the borrower as up to date, and grade the loan as healthy, while the bank has received nothing.

## Example

Rahim starts a mobile payment of 8,979, but the CBS has not confirmed it. The loan shows the 8,979 as pending, and the amount owed is unchanged. When the CBS confirms, the payment becomes real and the amount owed falls.

## Terms to know

- **Pending:** started but not yet confirmed. It has no effect on balances.
- **Confirmation:** the CBS saying the money has really moved.
- **Outstanding position:** everything the borrower still owes.
- **CBS:** the bank's main system. See `glossary.cbs`.
