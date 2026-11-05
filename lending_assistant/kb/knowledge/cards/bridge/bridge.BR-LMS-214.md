---
id: bridge.BR-LMS-214
type: bridge
title: Partner reports
summary: "Gap. Frappe Lending has no co-lending report. One interface call returns payable amounts per loan from the ledger, but it is not a report and shows the whole loan's figures, not the partner's."
br_ids: [BR-LMS-214]
brd_section: 7.12
doctypes: [Loan Partner]
verdict: gap
analysis_status: verified
dev_items: [D19]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_partner/loan_partner.py:141-142"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-214"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p55"
  - "sources/verification/reqs.json#BR-LMS-214"
  - "sources/verification/verification_report.md#BR-LMS-214"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-214"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-214"
  - "sources/verification/FINAL_REPORT.md#D19"
related: [concept.BR-LMS-214, bridge.BR-LMS-210, bridge.BR-LMS-213, devitem.D19]
version: 1
status: approved
approved_by: Owner
---
**In short:** Gap. Frappe Lending has no co-lending report. One interface call returns payable amounts per loan from the ledger, but it is not a report and shows the whole loan's figures, not the partner's.

## Business need

Partner economics must be reportable: disbursed, collected and outstanding share, delinquency in the partner's portfolio and guarantee use (BR-LMS-214 in section 7.12, BRD PDF page 55). This requirement is Should, not Must. See `concept.BR-LMS-214`.

## Frappe Lending today

None of the eleven reports in the lending app is about partners. The **Loan Partner** form has no list of linked loans and no ledger view. The one related function is `get_colender_payout_details`, a whitelisted call that returns for a date, per loan, the payable principal and interest, the guarantee balance, the amount invoked and paid, the guarantee trigger date and the principal outstanding (`lending/loan_management/doctype/loan_partner/loan_partner.py:141-142`). In the test, called as the test user for 3 November 2026, it returned a payable of 1,759.00 for the one co-lent loan, and the figure was out of date after the loan closed.

## Match or gap, and why

This is a **gap**, and the verification confirmed it (J10). The call is not a report: it has no screen, and its principal outstanding is the whole loan's figure and not the partner's share. The verification left a note to decide with the owner whether it should count as partly covered; the verdict recorded in the verified requirements file is a gap.

- No report shows disbursed, collected or outstanding share.
- Nothing shows the late loans in the partner's portfolio or the guarantee used, because the guarantee is never drawn (see `bridge.BR-LMS-210`).

## What to do today

Build the partner statements from the ledger accounts of the partner and the Loan list filtered by partner, and call the payout function through the API for the payable figures.

## Planned fix

Dev item D19 (co-lending reports, sized large) covers this row, together with the partner settlement document, the closure and pre-payment share, the FLDG engine and a share per product (ND-40, ND-41, ND-42).
