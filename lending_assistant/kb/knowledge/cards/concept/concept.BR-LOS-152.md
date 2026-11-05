---
id: concept.BR-LOS-152
type: concept
title: Officers log in with two factors and the session locks when idle
summary: "Login needs credentials plus a second factor, and the app locks after a set idle time and asks the officer to sign in again."
br_ids: [BR-LOS-152]
brd_section: 6.7.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-152"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p39"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.7.1"
related: [bridge.BR-LOS-152, concept.BR-LOS-151, glossary.field-officer]
version: 1
status: approved
approved_by: Owner
---
**In short:** Login needs credentials plus a second factor, and the app locks after a set idle time and asks the officer to sign in again.

## What the rule says

BR-LOS-152 (Must, BRD 6.7.1, PDF page 39) says login "shall require credentials and a second factor". The session locks after a "configurable idle period" and re-authentication is then needed. The idle period is a setting the bank can change, not a fixed number in the BRD.

## Why the bank wants it

The BRD gives the operating context for all of section 6.7 (PDF page 39): field officers work at gatherings arranged by the partner, often in rural places with unreliable mobile data. They stand rather than sit, work under time pressure with a queue of applicants waiting, and serve applicants who may have limited literacy. The BRD doesn't say why; the usual reason is that an unlocked device left on a table at a village meeting would otherwise expose applicant data, so a second factor and an idle lock limit what a finder or bystander can see.

## Example

An officer puts the device down to help an applicant sign. After the idle period the screen locks. When the officer picks it up again, the app asks for the credentials and the second factor before it shows any applicant.

## Terms to know

- **Second factor:** the extra login step the BRD requires in addition to credentials.
- **Idle period:** the time without use after which the session locks.
- **Re-authentication:** signing in again after a lock.
