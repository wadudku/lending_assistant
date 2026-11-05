---
id: glossary.cif
type: glossary
title: CIF (Customer Information File)
summary: The customer master record inside the bank's core banking system.
br_ids: []
brd_section: 1.5
doctypes: []
dev_items: []
terms: [cif, customer information file]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#1.5"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-120"
related: [glossary.cbs, concept.BR-LOS-120]
version: 1
status: approved
approved_by: Owner
---
**In short:** The customer master record inside the bank's core banking system.

## Plain meaning

The BRD defines CIF as the Customer Information File, the customer master record within the CBS (BRD 1.5).

## Example

Rahim has one CIF record at the bank, with his name, address and KYC status. All his accounts hang off that record.

## Why it matters here

The account check before submission looks at KYC at the CIF level: it must be current (BR-LOS-120). The team has analysed only the LMS requirements (Section 7). The LOS requirements have not been analysed.

## See also

`glossary.cbs`, `concept.BR-LOS-120`.
