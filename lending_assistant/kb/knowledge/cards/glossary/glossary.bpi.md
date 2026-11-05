---
id: glossary.bpi
type: glossary
title: BPI (broken-period interest)
summary: "Interest for the odd days between payout and the first regular due date, which do not fit the normal instalment cycle."
br_ids: [BR-LMS-141]
brd_section: 7.5
doctypes: [Loan Product]
dev_items: []
terms: [bpi, broken-period interest, broken period interest]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#1.5"
  - "sources/NRB_LMS_Requirements_Plain_English.md#glossary-of-abbreviations"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-141"
related: []
version: 1
status: approved
approved_by: Owner
---
**In short:** Interest for the odd days between payout and the first regular due date, which do not fit the normal instalment cycle.

## Plain meaning

The BRD defines BPI as interest for a partial period falling outside the regular instalment cycle (BRD 1.5). The plain-English guide gives the usual case: the extra days between the payout date and the first regular due date.

## Example

Rahim's loan is paid out on 25 June and his first EMI is due on 5 August. The days from 25 June to the first full period are broken-period days, and the bank charges interest for them.

## Why it matters here

BR-LMS-141 asks that broken-period interest is handled for partial periods arising at disbursement. The verification lists broken-period interest among what the core engine does, and the product can recover it in the first EMI or spread it over the tenor.

## See also

`glossary.emi`, `glossary.penal-interest`.
