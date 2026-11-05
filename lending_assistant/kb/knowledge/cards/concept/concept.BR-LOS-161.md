---
id: concept.BR-LOS-161
type: concept
title: Offline data is encrypted and biometric copies are erased after sync
summary: "Data waiting on the device must be encrypted, and once the bank confirms receipt the device deletes its copies of biometrics and identity images."
br_ids: [BR-LOS-161]
brd_section: 6.7.2
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-161"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p40"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.7.2"
related: [bridge.BR-LOS-161, concept.BR-LOS-160]
version: 1
status: approved
approved_by: Owner
---
**In short:** Data waiting on the device must be encrypted, and once the bank confirms receipt the device deletes its copies of biometrics and identity images.

## What the rule says

BR-LOS-161 (Must, BRD 6.7.2, PDF page 40) has two parts. Data queued locally "shall be encrypted at rest", meaning it is scrambled while stored on the device. And "on acknowledged synchronisation", the local copies of "biometric captures and identity images" shall be purged from the device.

## Why the bank wants it

The BRD gives the operating context for section 6.7 (PDF page 39): officers often work in rural places with unreliable mobile data. Section 6.7.2 (PDF page 40) is the part that deals with that. The BRD doesn't say why; the usual reason is that fingerprints, faces and ID images are among the most sensitive data the bank holds, and a lost device should not carry them longer than needed.

## Example

An officer's device is lost on the way home. Unsent captures on it are unreadable without the key. Fingerprint and face captures and identity images that were sent and acknowledged earlier were already purged from the device.

## Terms to know

- **Encrypted at rest:** stored in a scrambled form that cannot be read without a key.
- **Acknowledged synchronisation:** a synchronisation that has been acknowledged. The BRD does not say who acknowledges it.
- **Purge:** remove from the device.
