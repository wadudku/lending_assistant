---
id: concept.BR-GOV-030
type: concept
title: A daily check compares payouts in origination with loans in servicing
summary: "Every day the platform compares confirmed payouts recorded in origination with loans booked in servicing, and every difference in either direction becomes an exception to be closed with a written reason."
br_ids: [BR-GOV-030]
brd_section: 5.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-030"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p28"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-004"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
related: [bridge.BR-GOV-030, glossary.los, glossary.lms, concept.BR-GOV-004, concept.BR-LMS-010]
version: 1
status: approved
approved_by: Owner
---
**In short:** Every day the platform compares confirmed payouts recorded in origination with loans booked in servicing, and every difference in either direction becomes an exception to be closed with a written reason.

## What the rule says

BR-GOV-030 (Must, BRD 5.4, PDF page 28) says a daily control compares confirmed disbursements recorded in origination against loans booked in servicing, and raises every difference in either direction as an exception requiring documented closure.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a payout with no loan, or a loan with no payout, means money or records are lost between the two systems, and a daily comparison catches it early.

## Example

Origination shows 40 confirmed payouts today and servicing shows 39 new loans. The check finds the payout with no loan, opens an exception, and a named person records the cause and closes it. A loan in servicing with no matching payout would be raised in the same way.

## Terms to know

- **Control:** a regular check built into the process.
- **Difference in either direction:** a payout with no loan, or a loan with no payout.
- **Documented closure:** closing an exception with a written reason.
- **Origination:** the stage before servicing, handled by the LOS.
