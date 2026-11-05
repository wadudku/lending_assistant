---
id: bridge.BR-LMS-182
type: bridge
title: Changing the terms for a struggling borrower (restructuring)
summary: "Partly covered. A Loan Restructure changes rate, term, EMI and the treatment of overdue amounts, with a type recorded. The types are not the regulator's, and a restructure re-ages the loan to zero days past due."
br_ids: [BR-LMS-182]
brd_section: 7.9
doctypes: [Loan Restructure, Loan, Loan Repayment Schedule]
verdict: partial
analysis_status: verified
dev_items: [D16]
fields: [Loan Restructure.Restructure Type]
options: [Loan Restructure.Restructure Type=Normal Restructure, Loan Restructure.Restructure Type=Pre Payment, Loan Restructure.Restructure Type=Advance Payment]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_restructure/loan_restructure.py:598"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-182"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p53"
  - "sources/verification/reqs.json#BR-LMS-182"
  - "sources/verification/verification_report.md#BR-LMS-182"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-182"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-182"
  - "sources/verification/FINAL_REPORT.md#new-items-found-in-verification-nd-1-...-nd-47"
  - "sources/verification/FINAL_REPORT.md#D16"
related: [concept.BR-LMS-182, decision.restructure, lifecycle.RESTRUCTURED, bridge.BR-LMS-180, bridge.BR-LMS-181, devitem.D16]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. A Loan Restructure changes rate, term, EMI and the treatment of overdue amounts, with a type recorded. The types are not the regulator's, and a restructure re-ages the loan to zero days past due.

## Business need

The platform must support restructuring, including rescheduling and wider changes of terms, and record the type (BR-LMS-182 in section 7.9, BRD PDF page 53). See `concept.BR-LMS-182`. The missing controls (two people, limits, reporting) are in `decision.restructure`.

## Frappe Lending today

A **Loan Restructure** has a **Restructure Type** of Normal Restructure, Pre Payment or Advance Payment (`lending/loan_management/doctype/loan_restructure/loan_restructure.json:264`). The Normal Restructure is the one meant to be entered by hand, although the form offers all three types; the other two are made by the payment types of the same name (see `bridge.BR-LMS-180` and `bridge.BR-LMS-181`). The form holds a new interest rate, a new number of periods, a new monthly amount, and the treatment of overdue interest and penalty (Capitalize, Add To First EMI or Carry Forward). Approving a Normal Restructure sets the loan's days past due to 0 (`lending/loan_management/doctype/loan_restructure/loan_restructure.py:598`).

## Match or gap, and why

This is **partly covered**, and the verification confirmed the verdict (J6).

- There is no Bangladesh Bank style category of reschedule versus restructure, and no field for the regulatory treatment. See `bridge.BR-LMS-188`.
- In the test, a loan 60 days overdue was re-aged to 0 days past due at approval. Capitalisation made three automatic repayments, and the classification fell from SMA to STD within seconds, through the runs that those repayments queued.
- On an NPA loan, the restructure kept SS and NPA and set a watch period to 3 November 2027 (365 days). The classification run queued by the capitalisation then moved all 5,612.92 of suspense interest to income and cleared the customer's NPA flag (DEF-22).
- A Normal Restructure added accrued interest to the principal as well (DEF-18), and a Credit Adjustment made before a restructure was deducted twice from the pending principal (DEF-24).

## What to do today

Use a Normal Restructure only with a person checking the result: confirm the new schedule, the principal against the ledger, and, on an NPA loan, the suspense and the customer's NPA flag. Record the Bangladesh Bank category outside the system.

## Planned fix

Dev item D16 (Bangladesh Bank treatment, sized large) covers this row. The final report proposes a restructure model that does not re-age (ND-22).
