---
id: concept.BR-LMS-165
type: concept
title: All the payment types the bank needs
summary: "The loan system must handle nine kinds of money movement against a loan, from a normal instalment to a recovery after a write-off."
br_ids: [BR-LMS-165]
brd_section: 7.7
doctypes: []
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-165"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p51"
  - "sources/verification/reqs.json#BR-LMS-165"
  - "sources/verification/verification_report.md#BR-LMS-165"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-165"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-165"
related: [bridge.BR-LMS-165, decision.waiver]
version: 1
status: approved
approved_by: Owner
---
**In short:** The loan system must handle nine kinds of money movement against a loan, from a normal instalment to a recovery after a write-off.

## What the rule says

BR-LMS-165 (Must, BRD 7.7.1, PDF page 51) says the platform supports the full range of repayment types the bank requires: normal repayment, advance payment, prepayment, waiver, adjustment, capitalisation, settlement, subsidy and write-off recovery.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that money does not only arrive as an instalment. Borrowers pay early or pay extra, the bank forgives part of what is owed or adds unpaid interest to the principal, and sometimes a third party pays. Each case has different accounting and a different effect on the schedule. With one generic payment type, staff would use workarounds that hide what really happened; distinct types keep each event traceable and reportable.

## Example

Rahim pays 20,000 extra: a prepayment. The government pays 1,000 of his interest: a subsidy. Three years after a write-off, he pays 10,000: a write-off recovery.

## Terms to know

- **Prepayment:** extra money that cuts the principal.
- **Advance payment:** paying future instalments early.
- **Waiver:** the bank forgives part of the amount. See `decision.waiver`.
- **Capitalisation:** adding unpaid interest to the principal.
- **Settlement:** the bank accepts less to close the loan.
- **Subsidy:** a third party pays part.
- **Write-off recovery:** money collected after the bank wrote the loan off.
