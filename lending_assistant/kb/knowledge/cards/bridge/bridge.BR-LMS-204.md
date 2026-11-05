---
id: bridge.BR-LMS-204
type: bridge
title: Send settlements and write-offs to the CBS
summary: Gap (needs the CBS link). Frappe Lending posts these entries in its own ledger. It has no link to send them to a CBS and no field to keep a CBS journal reference.
br_ids: [BR-LMS-204]
brd_section: 7.11
doctypes: [Loan Write Off, Loan Repayment]
verdict: gap_cbs
analysis_status: verified
dev_items: [D13]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-204"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p54"
  - "sources/verification/reqs.json#BR-LMS-204"
  - "sources/verification/verification_report.md#BR-LMS-204"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-204"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-204"
  - "sources/verification/FINAL_REPORT.md#D13"
related: [concept.BR-LMS-204, concept.BR-LMS-204, bridge.BR-LMS-170r, devitem.D13]
version: 1
status: approved
approved_by: Owner
---
**In short:** Gap (needs the CBS link). Frappe Lending posts these entries in its own ledger. It has no link to send them to a CBS and no field to keep a CBS journal reference.

## Business need

Settlement, write-off and recovery entries must be sent to the CBS and the returned journal reference kept (BR-LMS-204 in section 7.11, BRD PDF page 54). See `concept.BR-LMS-204`.

## Frappe Lending today

A **Loan Write Off** has a posting date, a value date, a write-off account, a write-off amount and some links. It has no CBS or journal reference field (checked in the definitions). A settlement or recovery uses the **Loan Repayment**, whose only reference is the **Reference Number** and **Reference Date** for the payment. The app has no connection to a CBS (see `bridge.BR-LMS-170r` for the missing feed in the other direction).

## Match or gap, and why

This is a **gap (needs the CBS link)**, and the verification confirmed it from the metadata (J3 and J8). It is a gap of data and a link, which Frappe cannot supply alone: the robot or interface that posts to the CBS and returns the journal number does not exist in the app.

- Not tested live, because the answer is the absence of a field and of an interface.
- The ledger entries for these events exist in Frappe's own accounts, so there is something to send.

## What to do today

Post the entries in the CBS by hand from the Frappe ledger. Write the CBS journal number in the Reference Number of the Loan Repayment. For a Loan Write Off, which has no reference field, keep a register of the journal numbers outside the system.

## Planned fix

Dev item D13 (the CBS and RPA posting bridge, sized large) covers this row. The final report notes that all servicing entries post on the entry date, so the bridge needs the accounting-date fix (ND-12) first.
