---
id: glossary.demand
type: glossary
title: Demand
summary: "An amount the bank has formally raised as due for payment, such as an instalment, principal, interest, a penalty or a charge."
br_ids: [BR-LMS-133]
brd_section: 7.4
doctypes: [Loan Demand]
dev_items: []
terms: [demand, bill, amount due]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#1.5"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-133"
related: [glossary.dpd]
version: 1
status: approved
approved_by: Owner
---
**In short:** An amount the bank has formally raised as due for payment, such as an instalment, principal, interest, a penalty or a charge.

## Plain meaning

The BRD defines a demand as an amount formally raised as due for payment: installment, principal, interest, penalty or charge (BRD 1.5). A demand is the bill. Until a demand exists, the amount is only scheduled.

## Example

On 5 July Rahim's instalment falls due. The system raises a demand for it, and it stays unpaid until Rahim's payment is allocated to it. If it is still unpaid after 5 July, the loan becomes overdue.

## Why it matters here

BRD 7.4 is about demand, billing and charges. Frappe Lending raises demands in the **Loan Demand** doctype, and the verification lists billing on due dates among what the core engine does well. BR-LMS-133 asks that a demand is never silently deleted or amended; the verified result is partly covered.

## See also

`devitem.D8`, `glossary.dpd`.
