---
id: concept.BR-LOS-331
type: concept
title: The borrower's total exposure is added up before sanction and held to a limit
summary: "Before sanction the platform adds up the borrower's exposure across every application and loan on the platform, and across the Bank where it can be retrieved, and applies the single-borrower limit."
br_ids: [BR-LOS-331]
brd_section: 6.6
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-331"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p38"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-320"
related: [bridge.BR-LOS-331, concept.BR-LOS-320, concept.BR-LOS-332]
version: 1
status: approved
approved_by: Owner
---
**In short:** Before sanction the platform adds up the borrower's exposure across every application and loan on the platform, and across the Bank where it can be retrieved, and applies the single-borrower limit.

## What the rule says

BR-LOS-331 (Must, BRD 6.6, PDF page 38) says before sanction the platform aggregates the borrower's exposure across every application and loan held on the platform, and across the Bank where that position can be retrieved, and applies the configured single-borrower exposure limit. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a Bank limits what it lends to one borrower in total, not loan by loan.

## Example

A borrower has two loans on the platform worth 90,000 and a 60,000 loan at another Bank branch. The limit is 200,000. A new request for 80,000 would reach 230,000, so the platform stops it.

## Terms to know

- **Aggregate exposure:** the total owed by one borrower across loans.
- **Single-borrower limit:** the highest total the Bank will lend to one borrower.
- **Retrieved:** fetched from another system.
- **Open application:** an application not yet finished.
