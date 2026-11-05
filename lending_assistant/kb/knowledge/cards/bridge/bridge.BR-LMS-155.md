---
id: bridge.BR-LMS-155
type: bridge
title: "One person prepares, another approves"
summary: "Gap. There is no repricing run to approve, and one user can submit and approve a restructure."
br_ids: [BR-LMS-155]
brd_section: 7.6
doctypes: [Loan Restructure]
verdict: gap
analysis_status: verified
dev_items: [D11]
fields: [Loan Restructure.Status]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_restructure/loan_restructure.json:283"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-155"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p50"
  - "sources/verification/reqs.json#BR-LMS-155"
  - "sources/verification/verification_report.md#BR-LMS-155"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-155"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-155"
related: [concept.BR-LMS-155, brd_section.7.6, devitem.D11, decision.restructure, glossary.maker-checker]
version: 1
status: approved
approved_by: Owner
---
**In short:** Gap. There is no repricing run to approve, and one user can submit and approve a restructure.

## Business need

The bank wants a repricing run prepared by a maker and approved by a different checker (BR-LMS-155, BRD 7.6, PDF page 50). See `concept.BR-LMS-155`.

## Frappe Lending today

There is no repricing run document. A single-loan **Loan Restructure** has a **Status** of Initiated, Approved or Rejected (`loan_restructure.json` lines 283-286) and no workflow. Who approves a restructure is described in `decision.restructure`.

## Match or gap, and why

This is a **gap**. In the test, the same user created and submitted a restructure (status Initiated) and then approved it by a plain save, and the Version log showed both steps by that user (verification_report.md, BR-LMS-155, J5). There was no workflow on Loan Restructure or Loan Repayment Schedule. The coverage analysis rated it a gap, and verification confirmed that.

## What to do today

Keep the approval outside the system, for example a signed request, and limit who can change a restructure's status.

## Planned fix

Dev item D11 (`devitem.D11`) adds a repricing run for floating-rate loans, with selection, effective date, a dry run, maker-checker, new schedule versions and a restartable batch.
