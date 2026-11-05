---
id: concept.BR-LOS-120
type: concept
title: No application is submitted without a successful bank account check
summary: "Before an application reaches submitted status, the account must pass a check against the bank's core system: it is found, is active, has a permitted type, carries the applicant's name and the customer's KYC is current."
br_ids: [BR-LOS-120]
brd_section: 6.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-120"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p32"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p32"
related: [bridge.BR-LOS-120, glossary.cbs, glossary.rpa, glossary.cif]
version: 1
status: approved
approved_by: Owner
---
**In short:** Before an application reaches submitted status, the account must pass a check against the bank's core system: it is found, is active, has a permitted type, carries the applicant's name and the customer's KYC is current.

## What the rule says

BR-LOS-120 (Must, BRD 6.3, PDF page 32) says no application reaches submitted status without a successful account validation against the CBS covering: the account exists; the account status is active, excluding dormant, closed, frozen, blocked and lien-marked; the account type is in the product's permitted list; the account title matches the applicant name at or above the configured similarity threshold; and the CIF-level KYC status is current. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD gives the reason in the 6.3 introduction: this is the single most important control in the Partner Portal. It guarantees that a disbursement instruction issued weeks later will land in a live, correctly titled, eligible account belonging to the named applicant. A failure here shows up as a failed or misdirected payout, at the point of greatest cost (PDF page 32).

## Example

A row names an applicant and an account number. The platform asks the core system about the account: it is found, active, a savings account, titled with the applicant’s name, and the customer’s KYC is up to date. All five pass, so the application may move to submitted.

## Terms to know

- **CBS:** the bank's core banking system. See `glossary.cbs`.
- **Dormant / frozen / lien-marked:** account states in which money cannot freely move.
- **CIF:** the customer information file: the Bank's single record of a customer.
- **KYC:** know-your-customer: the identity checks a bank must keep current.
