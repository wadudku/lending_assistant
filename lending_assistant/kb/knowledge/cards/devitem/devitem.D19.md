---
id: devitem.D19
type: devitem
title: D19 Co-lending reports
summary: "A planned add-on to Frappe Lending that reports a co-lending partner's share of what was disbursed, collected and is outstanding, with the partner's days past due and the guarantee used. This is our item D19, not the BRD's dependency D19."
br_ids: [BR-LMS-214]
brd_section: 7.12
doctypes: [Loan Partner, Loan]
dev_items: [D19]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D19"
  - "sources/verification/FINAL_REPORT.md#D19"
  - "sources/verification/reqs.json#BR-LMS-214"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-214"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#7.7.2"
  - "sources/verification/FINAL_REPORT.md#revised-suggested-order"
related: [devitem.D12]
version: 1
status: approved
approved_by: Owner
---
**In short:** A planned add-on to Frappe Lending that reports a co-lending partner's share of what was disbursed, collected and is outstanding, with the partner's days past due and the guarantee used. This is our item D19, not the BRD's dependency D19.

## What we plan to build

D19 adds a partner portfolio report: the partner's share of disbursed, collected and outstanding amounts, the partner's days past due, and the first-loss default guarantee (FLDG) used. It is built in a custom app. The name D19 is used twice in the project: here it means this development item, while the BRD's own dependency D19 is the set of open questions about repayment collection in section 7.7.2. See `devitem.D12`.

## The gap it closes

BR-LMS-214 asks for partner reports. In the test, there was no co-lending report. Verification grew the item with the work behind the report: the partner settlement document, the closure and pre-payment share, the guarantee engine and the share per product (ND-40, ND-41 and ND-42).

## Requirements it closes

BR-LMS-214 (verified as a gap).

## How, size and dependencies

Size: M in the analysis, now L. The final report adds the partner settlement document, the closure and pre-payment share, the FLDG engine and the share per product (ND-40, ND-41, ND-42). The partner position check of `devitem.D10` now sits in ND-40 and this item. The final report places D19 in its last group, Pack G.
