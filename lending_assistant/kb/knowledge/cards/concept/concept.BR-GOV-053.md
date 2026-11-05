---
id: concept.BR-GOV-053
type: concept
title: The platform checks its own records against each other
summary: "The platform reconciles internally across schedule, demand, accrual, repayment allocation and accounting posting, and reports any inconsistency as an exception."
br_ids: [BR-GOV-053]
brd_section: 8.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-053"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p59"
related: [bridge.BR-GOV-053]
version: 1
status: approved
approved_by: Owner
---
**In short:** The platform reconciles internally across schedule, demand, accrual, repayment allocation and accounting posting, and reports any inconsistency as an exception.

## What the rule says

BR-GOV-053 (Must, BRD 8.4, PDF page 59) says the platform reconciles internally across five things: schedule, demand, accrual, repayment allocation and accounting posting. It reports any internal inconsistency as an exception.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that these five records are produced by different steps, so a fault in one step can leave them disagreeing even when nothing outside has changed.

## Example

For one loan the schedule says 12,000 of interest was due this month, but the amount posted to the books is 11,500. The internal check lists the loan as an exception, with both amounts, so someone can find the missing 500.

## Terms to know

- **Schedule:** the plan of instalments for a loan.
- **Demand:** the amount that has fallen due.
- **Accrual:** interest counted day by day before it is billed.
- **Allocation:** how a payment is split across what is due.
- **Posting:** the entry in the accounting books.
