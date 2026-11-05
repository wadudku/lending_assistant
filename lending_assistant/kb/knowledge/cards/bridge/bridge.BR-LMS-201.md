---
id: bridge.BR-LMS-201
type: bridge
title: "Approval limits for settlements, waivers and write-offs"
summary: "Partly covered. Frappe's workflow feature could give approval by amount and role, but no workflow is set up, and no limit exists except two small product settings. The automatic write-off is submitted by the system with no approver."
br_ids: [BR-LMS-201]
brd_section: 7.11
doctypes: [Loan Repayment, Loan Write Off, Loan Balance Adjustment, Loan Product]
verdict: partial
analysis_status: verified
dev_items: [D8]
fields: [Loan Product.Auto Write Off Amount, Loan Product.Excess Amount Acceptance Limit]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-201"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p54"
  - "sources/verification/reqs.json#BR-LMS-201"
  - "sources/verification/verification_report.md#BR-LMS-201"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-201"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-201"
  - "sources/verification/FINAL_REPORT.md#new-items-found-in-verification-nd-1-...-nd-47"
  - "sources/verification/FINAL_REPORT.md#D8"
related: [concept.BR-LMS-201, decision.settlement, decision.waiver, decision.write-off, devitem.D8, bridge.BR-LMS-185]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. Frappe's workflow feature could give approval by amount and role, but no workflow is set up, and no limit exists except two small product settings. The automatic write-off is submitted by the system with no approver.

## Business need

Settlements, waivers and write-offs must need maker-checker approval within limits set by amount and role (BR-LMS-201 in section 7.11, BRD PDF page 54). See `concept.BR-LMS-201`. The same gap is described for each kind of action in `decision.settlement`, `decision.waiver` and `decision.write-off`.

## Frappe Lending today

The Loan Manager role has create, submit and cancel together on **Loan Repayment** and **Loan Write Off** (`lending/loan_management/doctype/loan_write_off/loan_write_off.json`, `lending/loan_management/doctype/loan_repayment/loan_repayment.json`). The lending app ships no workflow for these documents. The two amount settings on the **Loan Product** are **Auto Write Off Amount** and **Excess Amount Acceptance Limit**; neither is an approval limit. In the test, the site had workflows only for Loan Lead and Loan Application (inactive), none for Loan Repayment, Loan Write Off or Loan Balance Adjustment, and no Authorization Rule.

## Match or gap, and why

This is **partly covered**, and the verification confirmed the verdict by showing the absence (J8). Frappe's workflow feature could supply approval by role and amount, so the missing piece is configuration and rules, not a new engine.

- No document in the settlement, waiver and write-off family has an approval step or an amount and role limit.
- In the test the nightly classification created and submitted a write-off with no approver.
- The Authorization Rule on the site offers sales and purchase documents only.
- A workflow on Loan Repayment would also act on repayments the system creates itself, such as waivers and capitalisations. That was not tested.

## What to do today

Require a second person to approve each settlement, waiver and write-off outside the system, at the limits the bank sets, and check the Loan Write Off list the morning after the nightly run.

## Planned fix

Dev item D8 (approval and audit pack, sized large) covers this row. The final report adds ND-23 (maker-checker on waivers, capitalisation and balance adjustment), ND-32 (settlement approval) and ND-34 (write-off control).
