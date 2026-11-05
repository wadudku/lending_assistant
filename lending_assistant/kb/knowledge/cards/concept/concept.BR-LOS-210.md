---
id: concept.BR-LOS-210
type: concept
title: "Bank staff can open the full application detail, including the data a partner cannot see"
summary: "Bank staff can open everything a partner sees plus seven more kinds of detail, from the full bureau data to the complete audit trail."
br_ids: [BR-LOS-210]
brd_section: 6.10.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-210"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p44"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.10.1"
related: [bridge.BR-LOS-210, concept.BR-LOS-193, concept.BR-LOS-222, glossary.cib, glossary.field-officer]
version: 1
status: approved
approved_by: Owner
---
**In short:** Bank staff can open everything a partner sees plus seven more kinds of detail, from the full bureau data to the complete audit trail.

## What the rule says

BR-LOS-210 (Must, BRD 6.10.1, PDF page 44) says Bank staff "shall have access to full application detail: everything visible to the partner", plus seven things: credit bureau data in full, the identity verification payload including portrait match confidence and liveness result, field officer captured data, the signature image, fingerprint capture metadata and quality score, request and response payloads exchanged with external systems, and the complete audit trail. BR-LOS-193 (BRD 6.8, PDF page 42) separately says the full bureau response is "visible only to separately permissioned Bank users".

## Why the bank wants it

The BRD doesn't say why; the usual reason is that Bank staff who investigate or review an application need the whole record, while the partner sees only part of it (BR-LOS-221 and BR-LOS-222).

## Example

A Bank staff member opens an application. They see what the partner sees, and also the bureau data, the identity verification result with the portrait match confidence and liveness result, the officer's captured data, the signature image, the fingerprint metadata and quality score, the messages exchanged with external systems and the audit trail.

## Terms to know

- **Payload:** the content of a message sent to or received from an external system, as the BRD uses the word.
- **Audit trail:** the record of what happened on the application; the BRD says the complete one is shown.
