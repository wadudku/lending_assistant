---
id: concept.BR-INT-011
type: concept
title: "Log every interaction, masking customer details"
summary: "Every interaction with the core banking system is logged with request reference, timestamp, initiating user, outcome and duration, with customer details masked and shown unmasked only under privileged access."
br_ids: [BR-INT-011]
brd_section: 9.2.1
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-011"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p62"
related: [bridge.BR-INT-011, glossary.cbs]
version: 1
status: approved
approved_by: Owner
---
**In short:** Every interaction with the core banking system is logged with request reference, timestamp, initiating user, outcome and duration, with customer details masked and shown unmasked only under privileged access.

## What the rule says

BR-INT-011 (Must, BRD 9.2.1, PDF page 62) says all interaction is logged with five facts: request reference, timestamp, initiating platform user, outcome and duration. Customer-identifying content is masked in operational logs and available unmasked only under privileged access.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a log lets the bank trace a problem or a dispute to one request, while masking keeps customer data out of the view of the people who only read logs.

## Example

The operations team reads the log of a failed payout. It shows the request reference, the time, which user started it, the outcome and that it took 40 seconds. The borrower's name and account number appear as asterisks. A privileged user can open them.

## Terms to know

- **Log:** a record of what happened and when.
- **Masked:** hidden, for example shown as asterisks.
- **Privileged access:** a special right given to few people.
