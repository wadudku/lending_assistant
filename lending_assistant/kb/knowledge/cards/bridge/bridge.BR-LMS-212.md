---
id: bridge.BR-LMS-212
type: bridge
title: The partner's share of each plan and of charges
summary: "Partly covered. A Co-Lender Schedule is built beside the borrower's plan and each EMI is split, but a Loan Closure on a co-lent loan posts nothing to the partner. The document named Loan Partner Adhoc Charges Shared is not used by any code. The original analysis said covered."
br_ids: [BR-LMS-212]
brd_section: 7.12
doctypes: [Loan Repayment Schedule, Co-Lender Schedule, Loan Repayment, Loan Partner, Sales Invoice]
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_repayment_schedule/loan_repayment_schedule.py:346-366", "lending/overrides/sales_invoice.py:92-123"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-212"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p55"
  - "sources/verification/reqs.json#BR-LMS-212"
  - "sources/verification/verification_report.md#BR-LMS-212"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-212"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-212"
  - "sources/verification/FINAL_REPORT.md#new-items-found-in-verification-nd-1-...-nd-47"
  - "sources/verification/FINAL_REPORT.md#D19"
related: [concept.BR-LMS-212, bridge.BR-LMS-211, bridge.BR-LMS-213, devitem.D19]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. A Co-Lender Schedule is built beside the borrower's plan and each EMI is split, but a Loan Closure on a co-lent loan posts nothing to the partner. The document named Loan Partner Adhoc Charges Shared is not used by any code. The original analysis said covered.

## Business need

The platform must generate the partner's share of each repayment schedule and share configured ad-hoc charges as agreed (BR-LMS-212 in section 7.12, BRD PDF page 55). See `concept.BR-LMS-212`.

## Frappe Lending today

When a **Loan Repayment Schedule** is made for a loan with a partner, the code also builds a **Co-Lender Schedule** beside it, with a payment date, days, principal, interest, total and balance for each period. The partner's amount and rate depend on the partner's schedule type (`lending/loan_management/doctype/loan_repayment_schedule/loan_repayment_schedule.py:346-366`). When an EMI is paid, the partner's share of each paid demand is worked out and stored on the repayment details (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:2046-2056`, `lending/loan_management/doctype/loan_repayment/loan_repayment.py:2074-2085`). Charges are shared by the Sales Invoice: on submit, a hook posts the partner's part of each item, using the partner's **Loan Partner Shareable** percentage for that item, when the partner has accounting enabled (`lending/overrides/sales_invoice.py:92-123`). In the test, the first month of a 100,000 loan at 14% with a 20,000 partner share at 10% gave a borrower interest of 1,150.68, a partner interest of 164.38 and a partner principal of 1,594.62, and the repayment posted the shares to the ledger.

## Match or gap, and why

This is **partly covered**. The original analysis said covered, and the verification moved it (J10).

- A Loan Closure on a co-lent loan posted no partner share: the principal share and interest share were 0 and there were no repayment-detail rows, so the partner's remaining 18,405.38 of principal and its interest were never settled (DEF-44). The partner share is worked out only for EMI demands (the two code spots above), which fits that result.
- The partner schedule runs on its own payment, so its share of principal in an EMI was 20.4% of the borrower's principal, not 20%, and its balance drifts from 20% of the borrower's.
- A document named Loan Partner Adhoc Charges Shared exists, but no table or code in the installed app uses it. Charges are shared through the Loan Partner Shareable rows instead.
- The credit note for a waived charge does not reverse the partner's charge entry. This was found in the code, not in a live test (DEF-45).

## What to do today

Do not close a co-lent loan without working out the partner's closing share by hand and posting it. Check each month that the partner schedule and the borrower's agree.

## Planned fix

Dev item D19 (co-lending reports, which also holds the partner settlement and closure share) is the nearest item. The final report proposes ND-40 (partner settlement: closure, pre-payment, credit-note share, a settlement document and a report, large), and it logs the two defects DEF-44 and DEF-45.
