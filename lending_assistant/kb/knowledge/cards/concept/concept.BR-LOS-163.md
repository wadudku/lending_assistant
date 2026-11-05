---
id: concept.BR-LOS-163
type: concept
title: "Every screen shows connection and sync state, with a queue view"
summary: "Officers can always see whether the device is online and what has been sent, and a queue screen lists each pending item."
br_ids: [BR-LOS-163]
brd_section: 6.7.2
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-163"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p40"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.7.2"
related: [bridge.BR-LOS-163, concept.BR-LOS-162]
version: 1
status: approved
approved_by: Owner
---
**In short:** Officers can always see whether the device is online and what has been sent, and a queue screen lists each pending item.

## What the rule says

BR-LOS-163 (Must, BRD 6.7.2, PDF page 40) says "connectivity and synchronisation state shall be visible on every screen". A queue view "shall list all pending items with their capture time and sync state". The officer can tell at a glance whether work is safe on the server or still only on the device.

## Why the bank wants it

The BRD gives the operating context for section 6.7 (PDF page 39): officers often work in rural places with unreliable mobile data. Section 6.7.2 (PDF page 40) is the part that deals with that. The BRD doesn't say why; the usual reason is that an officer who cannot tell what has been sent may leave a meeting with captures still unsent, or repeat work that is already saved.

## Example

At the end of a meeting an officer opens the queue view. The queue view lists two items as waiting, each with the time it was captured. The officer stays in range of a signal until the two waiting items change to sent.

## Terms to know

- **Queue view:** a list of items waiting to be sent.
- **Sync state:** the state of an item's synchronisation, shown in the queue view.
