---
id: concept.BR-LMS-100
type: concept
title: Accept only loans that are really paid out
summary: "The loan system takes on a loan only when it arrives confirmed as paid out, with its approved terms, its payout reference and the record of who approved it."
br_ids: [BR-LMS-100]
brd_section: 7.1
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-100"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p46"
  - "sources/verification/reqs.json#BR-LMS-100"
  - "sources/verification/verification_report.md#BR-LMS-100"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-100"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-100"
related: [bridge.BR-LMS-100, brd_section.7.1, devitem.D1, glossary.los, glossary.cbs, lifecycle.BOOKED]
version: 1
status: approved
approved_by: Owner
---
**In short:** The loan system takes on a loan only when it arrives confirmed as paid out, with its approved terms, its payout reference and the record of who approved it.

## What the rule says

BR-LMS-100 (priority Must, BRD 7.1, PDF page 46) says the Loan Management System (LMS) accepts only a confirmed funded loan. The loan must carry three things: its approved terms, a disbursement reference, and the origination audit data. The BRD points to BR-LMS-010 for the exact content of that package. A loan that arrives without all three is not accepted.

## Why the bank wants it

The BRD gives no reason inside BR-LMS-100 itself. Two nearby statements show the intent. BR-LMS-102 says servicing ownership begins only after confirmed funding (PDF page 46). The opening of BRD Section 7 says the loan book must be correct, explicable and reproducible, with every balance traceable to a posting and every posting to an approved event (PDF page 46). A loan that was never paid out, or that has no approval trail, would break that chain from the first day.

## Example

The origination system (LOS) sends "Rahim, 100,000 BDT, approved", but the bank's payout reference is missing. The LMS must not create the loan. The handover waits in an error list until someone supplies the reference and sends it again.

## Terms to know

- **Disbursement reference:** the number the bank gave to the actual payout. See `glossary.cbs` for the bank's main system.
- **Origination audit data:** the record of who approved the loan and on what basis, kept by the origination system. See `glossary.los`.
- **Funded loan:** a loan whose money has already reached the borrower.
- **Handover (handoff):** the package the origination system sends when a loan has been paid out.
