---
id: concept.BR-LOS-209
type: concept
title: The borrower is told of the payment and a failed message never blocks or reverses the loan
summary: "The borrower is notified of the disbursement through the configured channel, a failed notification is retried and reported, and it never blocks or reverses a loan action."
br_ids: [BR-LOS-209]
brd_section: 6.9
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-209"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p44"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.9"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-054"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p60"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p65"
related: [bridge.BR-LOS-209, concept.BR-LOS-208, concept.BR-LOS-201a]
version: 1
status: approved
approved_by: Owner
---
**In short:** The borrower is notified of the disbursement through the configured channel, a failed notification is retried and reported, and it never blocks or reverses a loan action.

## What the rule says

BR-LOS-209 (Must, BRD 6.9, PDF page 44) says "The borrower shall be notified of the disbursement through the configured notification channel." A failed notification "shall be retried and reported and shall never block or reverse a loan action". So a failed message is retried and reported, and the loan itself is not affected.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a problem with a message should not undo or hold up a payment that has been made.

## Example

A disbursement is completed and the platform sends the notification through the configured channel. The message fails. The platform retries and reports the failure. The disbursement stays as it is.

## Terms to know

- **Configured channel:** the way the borrower is told. The BRD lists an SMS gateway for borrower notification (BRD 9.1, PDF page 60) and leaves the channels to be confirmed by the Bank (BR-INT-054).
- **Action on the loan:** a step taken on the loan, such as the disbursement.
