---
id: concept.BR-INT-062
type: concept
title: Credentials sit in a secured store and can be rotated without a release
summary: "Credentials are held in a secured credential store, never appear in code, configuration, screenshots or logs, and can be rotated without a software release."
br_ids: [BR-INT-062]
brd_section: 9.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-062"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p63"
related: [bridge.BR-INT-062, glossary.rpa]
version: 1
status: approved
approved_by: Owner
---
**In short:** Credentials are held in a secured credential store, never appear in code, configuration, screenshots or logs, and can be rotated without a software release.

## What the rule says

BR-INT-062 (Must, BRD 9.3, PDF page 63) says credentials are held in a secured credential store. They never appear in source code, configuration files, screenshots or logs. They can be rotated without a software release.

## Why the bank wants it

The BRD gives the reason in section 9.2, where it calls the account privileged and requires “vaulted credentials”: “The automation signs in with real Core Banking System credentials holding real transaction rights. It must be treated as a privileged account” (PDF page 61).

## Example

The password sits in the bank's credential store. When the bank changes it every 90 days, an administrator updates the store and the automation picks up the new value; nobody rebuilds or redeploys the software.

## Terms to know

- **Credential store:** a secured place where passwords are kept.
- **Rotated:** changed on a regular schedule.
- **Software release:** a new version of the software put into use.
