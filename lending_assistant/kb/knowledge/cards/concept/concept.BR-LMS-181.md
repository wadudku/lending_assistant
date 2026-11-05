---
id: concept.BR-LMS-181
type: concept
title: Paying extra to cut the loan (prepayment)
summary: "A prepayment lowers the principal early and may carry a fee. After it, either the instalment falls or the loan ends sooner, as the borrower chooses and the bank approves."
br_ids: [BR-LMS-181]
brd_section: 7.9
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-181"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p53"
  - "sources/verification/reqs.json#BR-LMS-181"
  - "sources/verification/verification_report.md#BR-LMS-181"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-181"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-181"
related: [bridge.BR-LMS-181, brd_section.7.9, glossary.prepayment, concept.BR-LMS-180]
version: 1
status: approved
approved_by: Owner
---
**In short:** A prepayment lowers the principal early and may carry a fee. After it, either the instalment falls or the loan ends sooner, as the borrower chooses and the bank approves.

## What the rule says

BR-LMS-181 in section 7.9 (Must, BRD PDF page 53) says a prepayment shall reduce outstanding principal early and apply any configured prepayment charge. It shall also revise either the instalment or the tenor, according to the borrower's approved election.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the borrower's choice changes what he pays each month or how long the bank earns interest, so the bank wants the choice recorded and approved.

## Example

Rahim prepays 20,000 after two EMIs. Choice A: the EMI stays at 8,979 and he finishes two to three months early. Choice B: he keeps the end date and the EMI drops to about 6,850.

## Terms to know

- **Prepayment:** a payment above what is due that reduces principal. See `glossary.prepayment`.
- **Prepayment charge:** a fee the bank takes for paying early.
- **Tenor:** the number of months the loan runs.
- **Election:** the borrower's choice between a lower instalment and a shorter loan.
