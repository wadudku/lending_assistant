---
id: concept.BR-LMS-222
type: concept
title: Close repaid credit lines automatically
summary: "Credit lines that are fully repaid are closed by a scheduled job, as the product is set up to do."
br_ids: [BR-LMS-222]
brd_section: 7.13
doctypes: []
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-222"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p55"
  - "sources/verification/reqs.json#BR-LMS-222"
  - "sources/verification/verification_report.md#BR-LMS-222"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-222"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-222"
related: [bridge.BR-LMS-222, brd_section.7.13, glossary.loc, concept.BR-LMS-221]
version: 1
status: approved
approved_by: Owner
---
**In short:** Credit lines that are fully repaid are closed by a scheduled job, as the product is set up to do.

## What the rule says

BR-LMS-222 in section 7.13 (Should, BRD PDF page 55) says fully repaid revolving facilities shall be closed through scheduled processing, subject to the product's configured behaviour.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a credit line left open after it has ended and been repaid is clutter and a risk, and nobody should have to close each one by hand.

## Example

Rahim's credit line ended on 31 October with nothing drawn, and he repaid everything he used. The nightly job finds it, sees that the end date has passed and that nothing is drawn, and closes it without anyone opening the loan.

## Terms to know

- **Revolving facility (credit line):** a limit that can be drawn and repaid again. See `glossary.loc`.
- **Scheduled processing:** a job that runs by itself at set times.
- **Fully repaid:** nothing is drawn against the limit.
