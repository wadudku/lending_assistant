---
id: concept.BR-LMS-110
type: concept
title: Five ways of working out repayments
summary: "The bank needs at least five repayment methods: equal monthly instalments, pro-rated, fixed cycle date, flat interest and a revolving line of credit."
br_ids: [BR-LMS-110]
brd_section: 7.2
doctypes: []
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-110"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p47"
  - "sources/verification/reqs.json#BR-LMS-110"
  - "sources/verification/verification_report.md#BR-LMS-110"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-110"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-110"
related: [bridge.BR-LMS-110, brd_section.7.2, glossary.emi, glossary.loc, glossary.bpi]
version: 1
status: approved
approved_by: Owner
---
**In short:** The bank needs at least five repayment methods: equal monthly instalments, pro-rated, fixed cycle date, flat interest and a revolving line of credit.

## What the rule says

BR-LMS-110 (priority Must, BRD 7.2, PDF page 47) says the platform supports the schedule methods the bank requires, and names five as the minimum: monthly equated instalment, pro-rated, cycle-date, flat interest, and revolving line of credit.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the bank sells different kinds of loans, and each kind is repaid in a different pattern. One method cannot produce a correct repayment plan for all of them.

## Example

A loan of 100,000 BDT at 14% for 12 months. With a reducing EMI, total interest is about 7,750, because interest is charged on a shrinking balance. With flat interest it is 14,000 (100,000 x 14%), because interest is always charged on the full 100,000.

## Terms to know

- **EMI (equated monthly instalment):** the same payment every month. See `glossary.emi`.
- **Pro-rated:** due dates sit on a calendar boundary, so the first period is shorter or longer and its interest is charged only for those days.
- **Cycle date:** every borrower pays on the same fixed day, for example the 5th.
- **Flat interest:** interest is always charged on the original amount.
- **Line of credit:** a limit that can be drawn, repaid and drawn again. See `glossary.loc`.
