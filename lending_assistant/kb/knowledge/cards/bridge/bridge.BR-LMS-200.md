---
id: bridge.BR-LMS-200
type: bridge
title: Work out a settlement offer and show its make-up
summary: "Partly covered. The Loan Repayment form shows the make-up of a settlement before it is submitted, but there is no settlement proposal and nothing is held for approval. A Full Settlement creates the waivers and write-off for what is left unpaid when it is submitted; any repayment short by no more than the product's Auto Write Off Amount, a Partial Settlement included, also gets an automatic waiver on submit."
br_ids: [BR-LMS-200]
brd_section: 7.11
doctypes: [Loan Repayment, Loan Write Off]
verdict: partial
analysis_status: verified
dev_items: [D18]
fields: [Loan Repayment.Repayment Type]
options: [Loan Repayment.Repayment Type=Partial Settlement, Loan Repayment.Repayment Type=Full Settlement, Loan Repayment.Repayment Type=Write Off Settlement]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_repayment/loan_repayment.py:279-284", "lending/loan_management/doctype/loan_repayment/loan_repayment.py:1290-1336"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-200"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p54"
  - "sources/verification/reqs.json#BR-LMS-200"
  - "sources/verification/verification_report.md#BR-LMS-200"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-200"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-200"
  - "sources/verification/FINAL_REPORT.md#new-items-found-in-verification-nd-1-...-nd-47"
  - "sources/verification/FINAL_REPORT.md#D18"
related: [concept.BR-LMS-200, decision.settlement, decision.waiver, devitem.D18, bridge.BR-LMS-185]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. The Loan Repayment form shows the make-up of a settlement before it is submitted, but there is no settlement proposal and nothing is held for approval. A Full Settlement creates the waivers and write-off for what is left unpaid when it is submitted; any repayment short by no more than the product's Auto Write Off Amount, a Partial Settlement included, also gets an automatic waiver on submit.

## Business need

The platform must calculate a settlement figure of principal, interest, penalties, charges and approved waivers, and show it before approval (BR-LMS-200 in section 7.11, BRD PDF page 54). See `concept.BR-LMS-200`. Settlement and waiver paths: `decision.settlement`, `decision.waiver`.

## Frappe Lending today

A settlement is a **Loan Repayment** with a **Repayment Type** of Partial Settlement, Full Settlement or Write Off Settlement. On the form, the payable figures are filled in before submit: Interest Payable, Penalty Amount, Payable Amount, Payable Principal Amount and Total Charges Payable (`lending/loan_management/doctype/loan_repayment/loan_repayment.js:94-97`). On submit, a Full Settlement queues one more step (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:279-284`). That step creates an Interest Waiver, a Penalty Waiver and a Charges Waiver repayment for what was not paid, and a settlement Loan Write Off for the unpaid principal (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:1290-1336`). Imported and bulk-posted repayments skip it (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:184-187`, `lending/loan_management/doctype/loan_repayment/loan_repayment.py:209-210`). A Partial Settlement does not get this step, so whatever it leaves unpaid stays open unless the automatic waiver below applies. Separately, as `decision.waiver` explains, a repayment short by no more than the loan product's Auto Write Off Amount, a Partial Settlement included, creates an automatic waiver on submit (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:394`, `lending/loan_management/doctype/loan_repayment/loan_repayment.py:1438-1473`; the shortfall test is `lending/loan_management/doctype/loan_repayment/loan_repayment.py:1360-1420`). A back-dated, imported or bulk-posted repayment does not (`lending/loan_management/doctype/loan_repayment/loan_repayment.py:384-392`).

## Match or gap, and why

This is **partly covered**, and the verification confirmed the verdict (J8).

- There is no settlement proposal. No doctype has Settlement, Proposal or Offer in its name, and nothing is held for approval.
- The waivers do not exist until submit, so they are not shown before money moves.
- In the test, posting went wrong. On the test company's allocation order, a Partial Settlement of 20,000 went all to principal with 0 interest (DEF-3); with the other order it paid 3,252.36 of interest and 16,747.64 of principal. A Full Settlement of 84,000 refunded 3,332.13 to the borrower while 4,277.18 was waived.
- A Full Settlement that cleared all the principal left the loan flagged NPA with its suspense (DEF-33), and left an unbooked interest demand open (DEF-34).
- No single record ties the payment, the waivers and the write-off together.

## What to do today

Work out the settlement figure and the waivers on paper, get the approval outside the system, and then enter the Full Settlement. Then check the allocation, NPA flag and suspense by hand.

## Planned fix

Dev item D18 (settlement proposal, sized medium) covers this row. The final report adds ND-32 (a settlement offer record and approval), ND-33 (posting fixes: unbooked interest, suspense release, the right account) and ND-38 (one write-off recovery figure).
