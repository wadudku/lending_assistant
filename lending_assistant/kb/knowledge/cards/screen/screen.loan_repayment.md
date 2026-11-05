---
id: screen.loan_repayment
type: screen
title: "Screen: Loan Repayment"
summary: "The Loan Repayment screen records money received against a loan, splits it across what is owed, and posts the accounting entries when submitted."
br_ids: []
brd_section: 7.7
doctypes: [Loan Repayment]
dev_items: [D8, D12]
fields: [Loan Repayment.Against Loan, Loan Repayment.Repayment Type, Loan Repayment.Value Date, Loan Repayment.Posting Date, Loan Repayment.Mode Of Payment, Loan Repayment.Reference Number, Loan Repayment.Amount Paid, Loan Repayment.Payable Amount, Loan Repayment.Repayment Details]
menus: [Lending > Loan Management > Loan Repayment]
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_repayment/loan_repayment.py, "lending/loan_management/doctype/loan_repayment/loan_repayment.json:601"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#7.7"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#7.7-repayment-collection-and-allocation"
  - "sources/verification/reqs.json#BR-LMS-160"
  - "sources/verification/verification_report.md#BR-LMS-160"
  - "sources/verification/reqs.json#BR-LMS-161"
  - "sources/verification/reqs.json#BR-LMS-162"
  - "sources/verification/reqs.json#BR-LMS-163"
  - "sources/verification/reqs.json#BR-LMS-164"
related: [brd_section.7.7, bridge.BR-LMS-160, bridge.BR-LMS-162, bridge.BR-LMS-165, bridge.BR-LMS-168, decision.waiver]
version: 1
status: approved
approved_by: Owner
---
**In short:** The Loan Repayment screen records money received against a loan, splits it across what is owed, and posts the accounting entries when submitted.

## What this screen is for

Use **Loan Repayment** (menu: Lending > Loan Management > Loan Repayment) to record any money that comes in against a loan: instalments, early payments, waivers, settlements and write-off recoveries. The **Repayment Type** decides what the entry does; there are 20 types. The same form quotes the payoff figure for a given type and date. It is a submittable document: while it is a draft, nothing changes in the loan or the ledger.

## Before and after

Before: the loan exists, its repayment schedule is active, and the daily jobs have raised **Loan Demand** bills. On submit, Frappe Lending splits the amount across the open demands in the offset order (the set payment order, see `glossary.allocation-order`), fills the Repayment Details table, posts the accounting entries and updates days past due. After: corrections go through **Loan Repayment Repost** (see `bridge.BR-LMS-169`).

## Key fields

**Against Loan**, **Repayment Type**, **Value Date** (the day the money arrived), **Posting Date** (set by the system), **Mode Of Payment**, **Reference Number** and **Reference Date** (the CBS reference), **Amount Paid**, **Payable Amount** and the **Repayment Details** table. The document has no status field. The installed doctype gives System Manager and Loan Manager read, write, create, submit, cancel and delete, and Loan Reporter read only. Frappe deletes only draft or cancelled documents, so a submitted repayment cannot be deleted: it must be cancelled first.

## BRD needs it serves

BR-LMS-160 to BR-LMS-169 in BRD 7.7 (see `brd_section.7.7`), and the waiver and settlement rules BR-LMS-185, BR-LMS-200 and BR-LMS-201 (see `decision.waiver`). Weak points to remember: the reference is not unique (`bridge.BR-LMS-162`), no approval is built in, and a draft or cancelled repayment can be deleted.
