---
id: concept.BR-LMS-240
type: concept
title: A servicing dashboard shows the state of the loan book
summary: "The platform presents a servicing dashboard of book size and composition, collections against demand, DPD distribution, classification movement, provision position and exception queues."
br_ids: [BR-LMS-240]
brd_section: 8.2
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-240"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p58"
related: [bridge.BR-LMS-240, glossary.dpd, glossary.asset-classification, glossary.provisioning]
version: 1
status: approved
approved_by: Owner
---
**In short:** The platform presents a servicing dashboard of book size and composition, collections against demand, DPD distribution, classification movement, provision position and exception queues.

## What the rule says

BR-LMS-240 (Must, BRD 8.2, PDF page 58) says the platform presents a servicing dashboard. It shows six things: book size and composition; collection performance against demand; DPD distribution; classification movement; provision position; and exception queue volumes. The id carries the LMS prefix, but the row sits in Section 8.2, outside the 103 requirements of Section 7.

## Why the bank wants it

The BRD gives one general reason for the whole of Section 8: “Reporting is not a by-product of this programme; for several stakeholders it is the programme. Credit Risk, Finance, Compliance and Internal Audit each need a view that the current process cannot produce reliably at volume.” (PDF page 57). The BRD doesn't say why this row asks for a dashboard; the usual reason is that Credit Risk and Finance want the state of the whole book on one screen each morning.

## Example

A risk officer opens the dashboard. It shows the book at 500 million across 3,000 loans, 92% of what fell due this month collected, and a count of loans in each band of days past due. Beside them are the loans that moved to a worse classification this month, the provision held and the number of items waiting in each exception queue.

## Terms to know

- **Book:** all the loans the bank holds.
- **Demand:** the amount that has fallen due from a borrower.
- **DPD:** days past due. See `glossary.dpd`.
- **Classification:** the grade of a loan by repayment record. See `glossary.asset-classification`.
- **Provision:** money set aside against loans that may not be repaid. See `glossary.provisioning`.
- **Exception queue:** a list of items that need a person to decide.
