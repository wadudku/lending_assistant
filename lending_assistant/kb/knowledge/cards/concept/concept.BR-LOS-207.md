---
id: concept.BR-LOS-207
type: concept
title: Payment is blocked when the sanction has lapsed or a sanction condition is not evidenced
summary: Disbursement is blocked where the sanction has lapsed under BR-LOS-330 or a sanction condition remains unevidenced.
br_ids: [BR-LOS-207]
brd_section: 6.9
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-207"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p43"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.9"
related: [bridge.BR-LOS-207, concept.BR-LOS-202, concept.BR-LOS-330]
version: 1
status: approved
approved_by: Owner
---
**In short:** Disbursement is blocked where the sanction has lapsed under BR-LOS-330 or a sanction condition remains unevidenced.

## What the rule says

BR-LOS-207 (Must, BRD 6.9, PDF page 43) says "Disbursement shall be blocked where the application's sanction has lapsed under BR-LOS-330, or where a sanction condition remains unevidenced." So there are two conditions, and either one blocks disbursement. BR-LOS-330 is the BRD row on lapse of a sanction after its validity period.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that money should be paid out only against a sanction that is still valid and whose conditions have been met.

## Example

An application was sanctioned some time ago and the sanction has lapsed. When the officer tries to take the application to disbursement, disbursement is blocked.

## Terms to know

- **Lapsed sanction:** a sanction that has passed its validity period, under BR-LOS-330.
- **Unevidenced condition:** a sanction condition for which no evidence is held, as the BRD puts it.
