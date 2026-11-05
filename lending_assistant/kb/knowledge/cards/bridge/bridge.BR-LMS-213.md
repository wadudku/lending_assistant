---
id: bridge.BR-LMS-213
type: bridge
title: Partner settlements and checks
summary: "Partly covered. The app can show what is payable to each partner from the ledger through one interface call, but it has no partner settlement document, no scheduled reconciliation and no report of unmatched items. The hourly credit-note job has nothing to do with partners."
br_ids: [BR-LMS-213]
brd_section: 7.12
doctypes: [Loan Partner, Loan Repayment]
verdict: partial
analysis_status: verified
dev_items: [D10]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_partner/loan_partner.py:141-142", "lending/loan_management/doctype/loan_repayment/loan_repayment.py:3560-3584"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-213"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p55"
  - "sources/verification/reqs.json#BR-LMS-213"
  - "sources/verification/verification_report.md#BR-LMS-213"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-213"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-213"
  - "sources/verification/FINAL_REPORT.md#D10"
  - "sources/verification/FINAL_REPORT.md#D19"
related: [concept.BR-LMS-213, bridge.BR-LMS-212, bridge.BR-LMS-214, devitem.D10]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. The app can show what is payable to each partner from the ledger through one interface call, but it has no partner settlement document, no scheduled reconciliation and no report of unmatched items. The hourly credit-note job has nothing to do with partners.

## Business need

The platform must process partner credit notes and reconcile the partner's position on a schedule, reporting unmatched items (BR-LMS-213 in section 7.12, BRD PDF page 55). See `concept.BR-LMS-213`.

## Frappe Lending today

The scheduler runs `process_pending_credit_notes` every hour (`lending/hooks.py:200`). It picks up submitted Loan Repayments of type Charges Waiver that have no invoice yet, makes a credit note for the waived charges and posts the suspense entries (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:3560-3584`). It has no partner filter. For partners, the app has a whitelisted function, `get_colender_payout_details`, that returns for a date the payable principal, interest and guarantee balance per loan, taken from the ledger (`lending/loan_management/doctype/loan_partner/loan_partner.py:141-142`). It has no screen. In the test, the job's filter matched nothing on the site, and the job was not run, because it is site-wide.

## Match or gap, and why

This is **partly covered**, and the verification confirmed the verdict (J10). The older text credited the hourly job to this row; that job handles waived charges only, so the credit comes from the payout function instead.

- There is no document for a partner payment, receipt, settlement or reconciliation, and no scheduled check.
- In the test the partner's cash funding, and the payment of the amount payable to the partner, were not posted, so the ledger balance on the partner accounts did not close. The app's partner postings are made only where partner accounting is read: disbursement, repayment and charge invoices.
- Nothing in the app compares the ledger with a partner statement or lists unmatched items; the only reconciliation code is the bank-reconciliation hooks (`lending/hooks.py:205-225`), which do not read partners.

## What to do today

Each month, run the payout function for the month end (through the API) or read the five partner accounts in the ledger, compare with the partner's statement by hand, and keep the list of differences in a register.

## Planned fix

Dev item D10 (reconciliation reports, sized medium) covers this row. The final report notes that the partner position now sits in ND-40 and D19 (a partner settlement document).
