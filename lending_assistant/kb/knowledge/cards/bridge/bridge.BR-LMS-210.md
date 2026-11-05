---
id: bridge.BR-LMS-210
type: bridge
title: A list of co-lending partners
summary: "Covered. The Loan Partner master holds the partner's name, code, addresses, share, rate and FLDG terms, and checks the percentages. The FLDG fields are data only: nothing in the app acts on them."
br_ids: [BR-LMS-210]
brd_section: 7.12
doctypes: [Loan Partner, Loan Partner Address, Loan Partner Shareable]
verdict: covered
analysis_status: verified
dev_items: []
fields: [Loan Partner.Partner Loan Share Percentage, Loan Partner.Type Of FLDG Applicable]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan_partner/loan_partner.py:71-92"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-210"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p55"
  - "sources/verification/reqs.json#BR-LMS-210"
  - "sources/verification/verification_report.md#BR-LMS-210"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-210"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-210"
  - "sources/verification/FINAL_REPORT.md#new-items-found-in-verification-nd-1-...-nd-47"
related: [concept.BR-LMS-210, bridge.BR-LMS-211, bridge.BR-LMS-214]
version: 1
status: approved
approved_by: Owner
---
**In short:** Covered. The Loan Partner master holds the partner's name, code, addresses, share, rate and FLDG terms, and checks the percentages. The FLDG fields are data only: nothing in the app acts on them.

## Business need

The platform must keep a partner master with the partner, its addresses and the type of first-loss guarantee or other risk sharing in force (BR-LMS-210 in section 7.12, BRD PDF page 55). See `concept.BR-LMS-210`.

## Frappe Lending today

A **Loan Partner** holds a Partner Name, a Partner Code, an Effective Date, a primary address and the address list, the share of the loan (**Partner Loan Share Percentage**), the **Partner Base Interest Rate** and a **Repayment Schedule Type**. For the guarantee it holds **Type Of FLDG Applicable** (Fixed Deposit Only, Corporate Guarantee Only, or both), a fixed-deposit percentage, a corporate-guarantee percentage, a trigger days-past-due and the basis for the limit (`lending/loan_management/doctype/loan_partner/loan_partner.json`). On save, the share and the base rate must each be between 1 and 99, and the guarantee percentages that apply to the chosen type must be between 1 and 99 (`lending/loan_management/doctype/loan_partner/loan_partner.py:71-92`). In the test, a partner with a 20% share, a 10% base rate, a 5% fixed deposit, a 5% guarantee, a trigger of 30 days and five accounts was saved.

## Match or gap, and why

This is **covered**, and the verification confirmed the verdict with a caveat (J10).

- The guarantee fields are recorded and nothing else. The trigger days-past-due field is read by no code, and the two Loan fields that would show a guarantee being called (Fldg Triggered and Fldg Trigger Date) are never set by the app. So the app does not check a loan against the trigger or draw on a guarantee.
- The guarantee used is a reporting item; see `bridge.BR-LMS-214`.

## What to do today

Keep the guarantee terms in the partner master and check by hand, each month, which loans have passed the trigger. Record any guarantee called in a register outside the system.

## Planned fix

No development item is assigned. The final report proposes ND-41 (a FLDG engine, medium).
