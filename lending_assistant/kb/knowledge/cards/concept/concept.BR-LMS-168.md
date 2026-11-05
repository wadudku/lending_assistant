---
id: concept.BR-LMS-168
type: concept
title: How much to close today?
summary: "The system must be able to say, at any moment, the exact amount that would close a loan today, and support approved partial and full settlements against it."
br_ids: [BR-LMS-168]
brd_section: 7.7
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-168"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p51"
  - "sources/verification/reqs.json#BR-LMS-168"
  - "sources/verification/verification_report.md#BR-LMS-168"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-168"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-168"
related: [bridge.BR-LMS-168, decision.waiver]
version: 1
status: approved
approved_by: Owner
---
**In short:** The system must be able to say, at any moment, the exact amount that would close a loan today, and support approved partial and full settlements against it.

## What the rule says

BR-LMS-168 (Must, BRD 7.7.1, PDF page 51) says the platform calculates a current payoff figure on demand and supports approved partial and full settlement against it.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a borrower who wants to close early, or who negotiates a settlement, first asks how much to pay today, and staff must answer exactly, including interest up to that day and any penalty. If the figure quoted differs from what the system later books, either the borrower pays too much or the bank loses money, and both lead to disputes. A settlement is a negotiated lower amount, so it needs the true figure as its starting point.

## Example

On 20 September, Rahim's payoff is the remaining principal plus interest up to that day plus any penalty, for example about 76,900.

## Terms to know

- **Payoff figure:** everything needed to close the loan on a given day.
- **Partial settlement:** the bank accepts an agreed part to reduce the loan.
- **Full settlement:** the bank accepts an agreed amount and closes the loan, forgiving the rest.
- **Waiver:** forgiven amount. See `decision.waiver`.
