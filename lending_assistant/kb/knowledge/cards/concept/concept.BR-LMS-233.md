---
id: concept.BR-LMS-233
type: concept
title: Refund what is left
summary: "Any remaining security deposit or overpayment is refunded to the borrower, and the refund is recorded with its bank reference."
br_ids: [BR-LMS-233]
brd_section: 7.14
doctypes: []
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-233"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p56"
  - "sources/verification/reqs.json#BR-LMS-233"
  - "sources/verification/verification_report.md#BR-LMS-233"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-233"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-233"
related: [bridge.BR-LMS-233, brd_section.7.14, concept.BR-LMS-186, concept.BR-LMS-187]
version: 1
status: approved
approved_by: Owner
---
**In short:** Any remaining security deposit or overpayment is refunded to the borrower, and the refund is recorded with its bank reference.

## What the rule says

BR-LMS-233 in section 7.14 (Must, BRD PDF page 56) says any remaining eligible security deposit or excess payment shall be refunded, and the refund recorded with its external reference.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the bank holds the borrower's money after closure and must return it, with a reference that lets anyone trace the payment in the bank's records.

## Example

200 left in the security deposit is refunded, reference CBS-TXN-0300. Anyone who looks up that transaction in the bank's records can match it to the refund and to the loan it came from, and the bank can show the borrower that the money went back.

## Terms to know

- **Security deposit:** money the borrower leaves with the bank as cover. See `bridge.BR-LMS-187`.
- **Excess payment:** money paid above what was owed.
- **External reference:** the bank transaction number of the refund.
