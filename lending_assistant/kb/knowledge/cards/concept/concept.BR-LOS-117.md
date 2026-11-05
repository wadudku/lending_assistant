---
id: concept.BR-LOS-117
type: concept
title: No application is accepted without recorded borrower consent
summary: "The platform accepts no application without a recorded consent covering data sharing with the Bank, a credit bureau inquiry and identity verification, with the reference, method and time kept for Bank compliance."
br_ids: [BR-LOS-117]
brd_section: 6.2.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-117"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p31"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p32"
related: [bridge.BR-LOS-117, glossary.partner, glossary.field-officer]
version: 1
status: approved
approved_by: Owner
---
**In short:** The platform accepts no application without a recorded consent covering data sharing with the Bank, a credit bureau inquiry and identity verification, with the reference, method and time kept for Bank compliance.

## What the rule says

BR-LOS-117 (Must, BRD 6.2.3, PDF page 31) says the platform accepts no application without a recorded borrower consent covering, at minimum: the partner's sharing of the individual's personal data with the Bank; the Bank's inquiry to the credit bureau; and identity verification against the national database. The partner retains the underlying evidence. The platform records the consent reference, the method of capture and the timestamp, and makes these available to Bank compliance. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't state the reason in the row. It does flag a legal question for NRB: whether a consent reference supplied in a file is enough authority for a credit bureau inquiry, or whether a signed instrument must be in place first. If a signed instrument is needed, bureau checking cannot happen before the field officer captures the signature, and the platform must enforce that order (PDF pages 31 and 32).

## Example

A row in the file carries a consent reference. Before the application is accepted, the platform checks that the reference is present and stores it with how it was captured (for example, a signed form) and the time. A compliance officer can later list all three.

## Terms to know

- **Consent:** the borrower's agreement to the use of their data.
- **Credit bureau:** an agency that holds borrowers' credit history.
- **National database:** the government identity register used to confirm a person.
- **Evidence:** the signed form or record that proves the consent.
