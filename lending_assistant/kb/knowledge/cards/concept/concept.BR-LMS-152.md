---
id: concept.BR-LMS-152
type: concept
title: Never change what is already paid
summary: "Repricing never rewrites paid instalments, completed repayments or posted history. Only the outstanding principal and unpaid instalments are recalculated."
br_ids: [BR-LMS-152]
brd_section: 7.6
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-152"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p49"
  - "sources/verification/reqs.json#BR-LMS-152"
  - "sources/verification/verification_report.md#BR-LMS-152"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-152"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-152"
related: [bridge.BR-LMS-152, brd_section.7.6, glossary.repricing, decision.restructure]
version: 1
status: approved
approved_by: Owner
---
**In short:** Repricing never rewrites paid instalments, completed repayments or posted history. Only the outstanding principal and unpaid instalments are recalculated.

## What the rule says

BR-LMS-152 (priority Must, BRD 7.6, PDF page 49) says repricing never rewrites paid instalments, completed repayments or posted history. Recalculation applies to outstanding principal and unpaid instalments only.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that what a borrower has already paid, and what the bank has already booked, are facts; changing them would break the record. This follows the BRD's principle that every posting traces to an approved event (BRD 7 opening, PDF page 46).

## Example

Rahim has paid 6 EMIs at 14%. Those 6 stay exactly as they are, and only the remaining 6 are recalculated at 15%.

## Terms to know

- **Paid instalment:** a due amount already settled by a repayment.
- **Posted history:** entries already made in the books.
- **Outstanding principal:** the part of the loan still owed.
- **Repricing:** see `glossary.repricing`.
