---
id: concept.BR-INT-032
type: concept
title: Bureau credentials are kept separate from the rest of the system
summary: "Bureau credentials and session handling are isolated from the main application and from the core banking system automation, and reachable only by the component that needs them."
br_ids: [BR-INT-032]
brd_section: 9.5
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-032"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p64"
related: [bridge.BR-INT-032, glossary.rpa]
version: 1
status: approved
approved_by: Owner
---
**In short:** Bureau credentials and session handling are isolated from the main application and from the core banking system automation, and reachable only by the component that needs them.

## What the rule says

BR-INT-032 (Must, BRD 9.5, PDF page 64) says bureau credentials and session handling are isolated from the main application and from the core banking system automation. They are accessible only to the component that needs them.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a bureau sign-in exposed through another component would give that component access it should not have.

## Example

The bureau password sits in its own vault entry that only the bureau component can read. The core banking system automation and the main application cannot open it.

## Terms to know

- **Isolated:** kept apart so one cannot reach the other.
- **Session handling:** how a signed-in session is started, kept and ended.
