---
id: concept.BR-LOS-160
type: concept
title: Officers can capture data offline and send it later
summary: "The app downloads each officer's assigned applications in advance and lets them finish data capture with no signal, sending it when a connection returns."
br_ids: [BR-LOS-160]
brd_section: 6.7.2
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-160"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p40"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.7.2"
related: [bridge.BR-LOS-160, concept.BR-LOS-155]
version: 1
status: approved
approved_by: Owner
---
**In short:** The app downloads each officer's assigned applications in advance and lets them finish data capture with no signal, sending it when a connection returns.

## What the rule says

BR-LOS-160 (Must, BRD 6.7.2, PDF page 40) says the application shall pre-download the officer's assigned applications, "including retrieved KYC and the retained identity portrait", whenever connectivity is available. The officer can then complete data capture, meaning "additional fields, signature, fingerprint and liveness", with no connection. Captures are queued on the device for synchronisation.

## Why the bank wants it

The BRD gives the operating context for section 6.7 (PDF page 39): officers often work in rural places with unreliable mobile data. Section 6.7.2 (PDF page 40) is the part that deals with that. The BRD doesn't say why; the usual reason is that an officer at a village meeting cannot wait for a signal in order to serve a queue of applicants.

## Example

An officer downloads the day's assigned applications while connected. At a meeting with no mobile data, the officer takes a signature and a fingerprint for three applicants. The captures wait in a queue on the device and are sent when the officer is back in signal.

## Terms to know

- **Pre-download:** copying the assigned applications to the device before they are needed.
- **Synchronisation:** sending the locally queued captures (BR-LOS-160).
- **KYC:** know your customer. The KYC data is submitted at application and retrieved for the officer.
