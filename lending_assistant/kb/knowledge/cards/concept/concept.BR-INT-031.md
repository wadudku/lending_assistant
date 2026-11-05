---
id: concept.BR-INT-031
type: concept
title: The bureau automation is monitored and alerts on repeated failure
summary: "The bureau automation is monitored for failure and for interface change, and alerts on consecutive failures rather than degrading silently."
br_ids: [BR-INT-031]
brd_section: 9.5
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-031"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p64"
related: [bridge.BR-INT-031, concept.BR-INT-066, glossary.rpa]
version: 1
status: approved
approved_by: Owner
---
**In short:** The bureau automation is monitored for failure and for interface change, and alerts on consecutive failures rather than degrading silently.

## What the rule says

BR-INT-031 (Must, BRD 9.5, PDF page 64) says the automation component is monitored for failure and for interface change. It alerts on consecutive failures rather than degrading silently. It repeats, for the bureau automation, the monitoring rule that section 9.3 sets for the core banking system automation in BR-INT-066. The wording “rather than degrading silently” is the same in both rows.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that approvals wait on the bureau inquiry (BRD 9.1 says no approval without it), so a silent failure would stall applications unseen.

## Example

Three bureau inquiries in a row fail because the bureau changed a screen. An alert reaches the operations team at once, and they fix the automation before the approval queue builds up.

## Terms to know

- **Interface change:** a change in the screens the automation drives.
- **Consecutive failures:** failures one after another with no success between.
