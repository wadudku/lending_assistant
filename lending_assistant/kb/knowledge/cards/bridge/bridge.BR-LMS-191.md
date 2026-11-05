---
id: bridge.BR-LMS-191
type: bridge
title: Give each loan a health grade
summary: "Partly covered. The bands are a table on the Company and the run grades each loan from them, but the only override is the Manual NPA tick, with no reason or approver, and the grade itself cannot be changed."
br_ids: [BR-LMS-191]
brd_section: 7.10
doctypes: [Loan, Company, Loan Classification Range, Process Loan Classification]
verdict: partial
analysis_status: verified
dev_items: [D15]
fields: [Loan.Manual NPA, Loan.Classification Code]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan/loan.py:1548-1553"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-191"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p53"
  - "sources/verification/reqs.json#BR-LMS-191"
  - "sources/verification/verification_report.md#BR-LMS-191"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-191"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-191"
  - "sources/verification/FINAL_REPORT.md#new-items-found-in-verification-nd-1-...-nd-47"
  - "sources/verification/FINAL_REPORT.md#D15"
related: [concept.BR-LMS-191, decision.override, lifecycle.NPA, bridge.BR-LMS-192, devitem.D15]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. The bands are a table on the Company and the run grades each loan from them, but the only override is the Manual NPA tick, with no reason or approver, and the grade itself cannot be changed.

## Business need

Each loan must be graded from configured bands, with a qualitative override that has a reason and an approver (BR-LMS-191 in section 7.10, BRD PDF page 53). See `concept.BR-LMS-191`. The approved decision on overrides is `decision.override`, and the NPA state is `lifecycle.NPA`.

## Frappe Lending today

The **Company** holds a table of **Loan Classification Range** rows: a classification code and name, a minimum and maximum days past due, and a tick for written off (`lending/loan_management/doctype/loan_classification_range/loan_classification_range.json`). The daily classification run sets the **Classification Code** on the **Loan** from these rows (`lending/loan_management/doctype/loan/loan.py:1548-1553`). The Classification Code and Classification Name are read-only fields (`lending/loan_management/doctype/loan/loan.json`). In the test, on the site's bands, one loan was Standard to 59 days, SMA at 60, SS at 90, NPA from 91 and DF from 180.

## Match or gap, and why

This is **partly covered**, and the verification confirmed the verdict (J4).

- The only override is the **Manual NPA** tick on the Loan. It is a yes or no for NPA. It has no reason field and no approver field, and the Version log shows only that the tick changed. Saving a changed Classification Code after submit was refused in the test, so the grade cannot be overridden at all. The detail is in `decision.override`.
- The grade and the NPA flag can disagree: in the test 13 loans were flagged NPA while graded Standard (DEF-7).
- Unticking a manual NPA did not reverse the interest moved to suspense (DEF-13).
- A new product's NPA threshold was missing from a one-hour cache, so a loan 152 days late stayed non-NPA until the cache was cleared (DEF-20).

## What to do today

Record each override, its reason and its approver in a register outside the system, and have the second person check the tick on the Loan. After you change a product's NPA threshold, clear the site cache.

## Planned fix

Dev item D15 (classification history and override, sized medium) covers this row. The final report adds ND-14 and ND-15 (NPA integrity, an override with a reason) and ND-25 (clear caches when a product or Company is saved).
