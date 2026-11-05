---
id: bridge.BR-LMS-172
type: bridge
title: Watch for a collateral shortfall
summary: "Partly covered. Frappe Lending finds a real shortfall exactly, but the run cannot be limited to one loan, makes two records per exposure and, in the test, flagged borrowers who had no collateral. The original analysis said covered."
br_ids: [BR-LMS-172]
brd_section: 7.8
doctypes: [Process Loan Security Shortfall, Loan Security Shortfall, Loan Security Assignment]
verdict: partial
analysis_status: verified
dev_items: []
fields: [Loan Security Shortfall.Shortfall Amount, Loan Security Shortfall.Shortfall Percentage, Loan Security Shortfall.Status]
options: [Loan Security Shortfall.Status=Pending, Loan Security Shortfall.Status=Completed]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/process_loan_security_shortfall/process_loan_security_shortfall.py:32", "lending/loan_management/doctype/loan_disbursement/loan_disbursement.py:1005-1008"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-172"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p52"
  - "sources/verification/reqs.json#BR-LMS-172"
  - "sources/verification/verification_report.md#BR-LMS-172"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-172"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-172"
  - "sources/verification/FINAL_REPORT.md#new-items-found-in-verification-nd-1-...-nd-47"
related: [concept.BR-LMS-172, bridge.BR-LMS-170c, bridge.BR-LMS-173]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. Frappe Lending finds a real shortfall exactly, but the run cannot be limited to one loan, makes two records per exposure and, in the test, flagged borrowers who had no collateral. The original analysis said covered.

## Business need

The platform must compare eligible collateral with secured exposure, on a schedule and on demand (BR-LMS-172 in section 7.8, BRD PDF page 52). See `concept.BR-LMS-172`.

## Frappe Lending today

A **Process Loan Security Shortfall** runs every day from the scheduler (`lending/hooks.py:190`) and after every bulk price update through the whitelisted `update_loan_security_price` call (`lending/api.py:56-76`). It can also be created by hand. It writes **Loan Security Shortfall** records with a Shortfall Amount, a Shortfall Percentage and a Status of Pending or Completed. In the test, detection was exact: a loan of 100,000 against 120,000 of collateral at 70% loan-to-value gave a shortfall of 16,000 (100,000 minus 120,000 times 0.70), at 83.33%. After the price recovered, a scoped run left no record. A Pending record sets the disbursable amount of that loan to 0 (`lending/loan_management/doctype/loan_disbursement/loan_disbursement.py:1005-1008`).

## Match or gap, and why

This is **partly covered**. The original analysis said covered, and the verification moved it (J7).

- A manual run cannot be limited to one loan or borrower. The form's Loan and Applicant (Borrower) fields are ignored, because the submit handler passes only the run's own name (`lending/loan_management/doctype/process_loan_security_shortfall/process_loan_security_shortfall.py:32`) (DEF-27).
- Each exposure gets two records, a loan-wise one and an applicant-wise one, with different values of Security Value.
- In the test, the nightly applicant-wise pass flagged 24 of 26 customers, all of whom had only unsecured loans (DEF-32). Once any secured loan exists, the daily job would raise these false shortfalls every night.
- The daily job does nothing until a secured loan or a pledged assignment exists (lines 46 to 49 of the same file).

## What to do today

Run the check by hand for the secured loans you care about and read the loan-wise records only. Ignore applicant-wise records for borrowers without collateral. Keep the scheduler for this job off until the nightly pass is fixed.

## Planned fix

No development item is assigned in the verified list. The final report proposes ND-27 (scope and clean the shortfall run, medium) and ND-29 (price integrity, small).
