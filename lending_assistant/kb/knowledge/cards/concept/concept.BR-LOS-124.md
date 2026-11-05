---
id: concept.BR-LOS-124
type: concept
title: The account is checked again just before the payout
summary: "Validation is repeated immediately before the disbursement instruction is sent; an account that has become dormant, closed or otherwise ineligible halts the payout and raises an exception."
br_ids: [BR-LOS-124]
brd_section: 6.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-124"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p32"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-120"
related: [bridge.BR-LOS-124, concept.BR-LOS-120, glossary.cbs]
version: 1
status: approved
approved_by: Owner
---
**In short:** Validation is repeated immediately before the disbursement instruction is sent; an account that has become dormant, closed or otherwise ineligible halts the payout and raises an exception.

## What the rule says

BR-LOS-124 (Must, BRD 6.3, PDF page 32) says validation is performed again immediately before the disbursement instruction is issued. An account that has become dormant, closed or otherwise ineligible in the interim halts disbursement and raises an exception. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD gives the reason in the 6.3 introduction: the check exists so that a disbursement instruction issued weeks later lands in a live, eligible account. A second check at the last moment covers the weeks in between (PDF page 32).

## Example

An application is sanctioned on the 1st and the payout is due on the 25th. On the 25th the account is found dormant. The payout is not sent, and an exception is raised for the Bank to deal with.

## Terms to know

- **Disbursement:** paying out the loan.
- **Ineligible:** no longer able to receive the payout.
- **Exception:** a flagged event that someone must review.
- **In the interim:** in the time between the first check and the payout.
