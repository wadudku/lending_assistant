---
id: devitem.D11
type: devitem
title: D11 Loan Repricing Run
summary: "A planned add-on to Frappe Lending for changing the interest rate of many floating-rate loans at once: select, practice run, second-person approval, then one safe job per loan and a notice to the borrower."
br_ids: [BR-LMS-150, BR-LMS-151, BR-LMS-152, BR-LMS-153, BR-LMS-154, BR-LMS-155, BR-LMS-156, BR-LMS-157, BR-LMS-158, BR-LMS-159]
brd_section: 7.6
doctypes: [Loan, Loan Restructure, Loan Repayment Schedule]
dev_items: [D11]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D11"
  - "sources/verification/FINAL_REPORT.md#D11"
  - "sources/verification/reqs.json#BR-LMS-150"
  - "sources/verification/reqs.json#BR-LMS-151"
  - "sources/verification/reqs.json#BR-LMS-152"
  - "sources/verification/reqs.json#BR-LMS-153"
  - "sources/verification/reqs.json#BR-LMS-154"
  - "sources/verification/reqs.json#BR-LMS-155"
  - "sources/verification/reqs.json#BR-LMS-156"
  - "sources/verification/reqs.json#BR-LMS-157"
  - "sources/verification/reqs.json#BR-LMS-158"
  - "sources/verification/reqs.json#BR-LMS-159"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-150"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-159"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#7.6"
  - "sources/verification/FINAL_REPORT.md#revised-suggested-order"
related: [devitem.D13]
version: 1
status: approved
approved_by: Owner
---
**In short:** A planned add-on to Frappe Lending for changing the interest rate of many floating-rate loans at once: select, practice run, second-person approval, then one safe job per loan and a notice to the borrower.

## What we plan to build

D11 adds a submittable Loan Repricing Run record with filters (product, category, branch, loan list), an effective date, a new rate or a benchmark move, and a mode (keep tenor or keep EMI). A Dry Run fills a table with the old and new rate, EMI, tenor, total interest and the reason a loan was excluded. A maker-checker workflow approves the run. On approval, one background job per loan rebuilds the schedule from the effective date, with one transaction per loan and a unique run-and-loan key so a re-run does nothing twice. A borrower notification follows, and the leftover Process Loan Interest Change is blocked.

## The gap it closes

BR-LMS-150 to BR-LMS-159 are the requirements of BRD section 7.6, and the test found no bulk repricing, benchmark, dry run or maker-checker. In the test, seven of the ten requirements are gaps (150, 151, 154, 155, 157, 158, 159) and three are partly covered (152, 153, 156). The only tool is a single-loan Normal Restructure, which failed on all four test products (DEF-17) and counted accrued interest twice (DEF-18).

## Requirements it closes

BR-LMS-150 to BR-LMS-159, the whole of BRD section 7.6.

## How, size and dependencies

Size: L, unchanged by verification, with a tighter specification: the final report's repricing table (ND-18) gives the full spec. D11 must not reuse the restructure path until DEF-17, DEF-18 and DEF-19 are fixed. The analysis names D11, D14 and D5 as the big bank-grade pieces, and the final report places D11 in step 3, after those defects are fixed.
