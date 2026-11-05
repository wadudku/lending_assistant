---
id: brd_section.3.2
type: brd_section
title: BRD 3.2 The ownership boundary
summary: "Section 3.2 says the boundary is a business control: servicing accepts only a confirmed funded loan, and lists the six things the handoff carries."
br_ids: []
brd_section: 3.2
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#3.2"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p17"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p18"
related: []
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 3.2 says the boundary is a business control: servicing accepts only a confirmed funded loan, and lists the six things the handoff carries.

## What this section says

BRD 3.2 (PDF pages 17 and 18) says the boundary is “a business control, not a technical convenience”. The LMS accepts a loan only when it arrives as a confirmed funded loan carrying approved terms, a disbursement reference from the Core Banking System and the origination audit record. A loan that is approved but not confirmed as funded does not enter servicing, is not scheduled and does not appear in the loan book. A table gives the six items the handoff carries and what each is for in servicing: borrower identity and KYC with references to the retained evidence; product code and approved terms (sanctioned amount, rate, rate type, tenor, frequency, moratorium, fees); disbursed amount, disbursement reference, value date and target CBS account; collateral and security references where the product is secured; partner and co-lending share where applicable; and the origination audit reference.

## Why the bank wants it

The BRD gives the reason in the section itself: the rule prevents the most damaging failure mode of an integrated lending platform, a loan that is being serviced but was never funded, or one that was funded but is not being serviced (PDF page 17).

## How it meets Frappe Lending

This section holds no requirement row, so there is nothing in it to compare with Frappe Lending, and the team has made no statement about it. The handoff rules appear as rows in section 5.4 (BR-LOS-010, BR-LMS-010, BR-LMS-011); the team has not analysed those rows. It also describes the origination system (LOS), which the team has not analysed.

## Related cards

Related: `brd_section.5.4`, `concept.BR-LOS-010`, `concept.BR-LMS-010`, `concept.BR-LMS-011`, `brd_section.3.1`.
