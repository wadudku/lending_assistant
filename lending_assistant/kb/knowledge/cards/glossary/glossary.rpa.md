---
id: glossary.rpa
type: glossary
title: RPA (robotic process automation)
summary: "Software that works another system through its screens, as a person would, when that system has no programming interface."
br_ids: []
brd_section: 1.5
doctypes: []
dev_items: []
terms: [rpa, robotic process automation, bot]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#1.5"
  - "sources/NRB_LMS_Requirements_Plain_English.md#glossary-of-abbreviations"
related: [glossary.cbs, devitem.D13]
version: 1
status: approved
approved_by: Owner
---
**In short:** Software that works another system through its screens, as a person would, when that system has no programming interface.

## Plain meaning

The BRD defines RPA as software that drives another system through its own user interface, as a human operator would, where no programmatic interface exists (BRD 1.5). The plain-English guide says a software robot types entries into the CBS screens, because the CBS has no posting interface.

## Example

Rahim's repayment must be recorded in the core banking system. No interface exists, so a bot logs in and keys the entry, then reports back the journal reference.

## Why it matters here

The BRD says the lack of a posting interface limits posting volume and favours batching. The planned posting bridge is `devitem.D13`. The verification marked the requirements that need this link as gaps that need the CBS link.

## See also

`glossary.cbs`, `devitem.D13`.
