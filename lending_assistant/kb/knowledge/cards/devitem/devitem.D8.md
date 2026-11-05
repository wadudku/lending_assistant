---
id: devitem.D8
type: devitem
title: D8 Approval and audit pack
summary: "A planned add-on to Frappe Lending that puts a second-person approval, a reason and before-and-after amounts on the manual corrections the BRD controls. Verification made it larger."
br_ids: [BR-LMS-133, BR-LMS-185, BR-LMS-196, BR-LMS-201, BR-LMS-205, BR-LMS-221, BR-LMS-234]
brd_section: 7.9
doctypes: [Loan Repayment, Loan Write Off, Loan Balance Adjustment, Loan Restructure, Loan Freeze Log]
dev_items: [D8]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D8"
  - "sources/verification/FINAL_REPORT.md#D8"
  - "sources/verification/reqs.json#BR-LMS-133"
  - "sources/verification/reqs.json#BR-LMS-185"
  - "sources/verification/reqs.json#BR-LMS-196"
  - "sources/verification/reqs.json#BR-LMS-201"
  - "sources/verification/reqs.json#BR-LMS-205"
  - "sources/verification/reqs.json#BR-LMS-221"
  - "sources/verification/reqs.json#BR-LMS-234"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-133"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-185"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-196"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-201"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-205"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-221"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-234"
  - "sources/verification/verification_report.md#BR-LMS-185"
  - "sources/verification/verification_report.md#BR-LMS-201"
  - "sources/verification/FINAL_REPORT.md#revised-suggested-order"
related: [decision.waiver, devitem.D12]
version: 1
status: approved
approved_by: Owner
---
**In short:** A planned add-on to Frappe Lending that puts a second-person approval, a reason and before-and-after amounts on the manual corrections the BRD controls. Verification made it larger.

## What we plan to build

D8 adds a Frappe Workflow with maker-checker steps and amount-based conditions on Loan Repayment (the waiver and settlement types), Loan Write Off, Loan Balance Adjustment, Loan Restructure, refunds, security moves and freeze. It makes a reason mandatory on cancel, stores before and after amounts in fields filled just before submit, adds reason and approver to the freeze and limit-change logs, and removes Delete rights on the servicing doctypes. It is built in a custom app.

## The gap it closes

The BRD asks for two people, a reason and a full record on its controlled changes, and verification found those controls missing in the test: a bill could be cancelled with no reason or approver (BR-LMS-133), a manual correction recorded no approver and no before-and-after pair (BR-LMS-185), a freeze had no approver (BR-LMS-196), and no workflow or role limit existed on waivers, settlements or write-offs (BR-LMS-201, BR-LMS-205). The final report lists waivers, balance adjustments, refunds, write-off, settlement, bill cancel, the limit log, release and freeze among the missing controls. See `decision.waiver` for the waiver case in detail.

## Requirements it closes

BR-LMS-133, BR-LMS-185, BR-LMS-196, BR-LMS-201, BR-LMS-205, BR-LMS-221 and BR-LMS-234. All seven are verified as partly covered.

## How, size and dependencies

Size: M in the analysis, now L. The new items ND-23, ND-30, ND-34, ND-35, ND-37, ND-45 and ND-47 land here, and the Delete rights on logs must also go (ND-15). A Workflow on Loan Repayment also applies to the repayments the system creates itself (waivers, capitalisations); that was not tested. The analysis puts D8 in the first group to build, with D1, D2 and D12; the final report keeps it in the foundation pack (Pack B).
