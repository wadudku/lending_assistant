---
id: concept.BR-INT-021
type: concept
title: Servicing reports loan status back to origination
summary: "Servicing gives origination back the loan account status, sanctioned amount, disbursement date, tenor, instalment amount and arrears position."
br_ids: [BR-INT-021]
brd_section: 9.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-021"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p64"
related: [bridge.BR-INT-021, glossary.los, glossary.lms, glossary.partner, concept.BR-LOS-312]
version: 1
status: approved
approved_by: Owner
---
**In short:** Servicing gives origination back the loan account status, sanctioned amount, disbursement date, tenor, instalment amount and arrears position.

## What the rule says

BR-INT-021 (Must, BRD 9.4, PDF page 64) says servicing exposes six things back to origination: loan account status, sanctioned amount, disbursement date, tenor, instalment amount and arrears position. The BRD gives three uses: partner disbursed-account views, partner quality monitoring and scorecard performance monitoring under BR-LOS-312.

## Why the bank wants it

The BRD gives the reason in the row: the data is for “partner disbursed-account views, for partner quality monitoring and for scorecard performance monitoring under BR-LOS-312” (PDF page 64).

## Example

A partner opens its list of disbursed loans and sees each one's status, instalment and arrears. Separately, the bank's quality team uses the same figures to see which partner's loans fall behind.

## Terms to know

- **Arrears position:** how much is overdue and for how long.
- **Tenor:** the length of the loan.
- **Partner quality monitoring:** watching how well the loans from each partner perform. See `glossary.partner`.
