---
id: concept.BR-LMS-251
type: concept
title: Classification and provisioning returns for Bangladesh Bank
summary: "The platform produces the classification and provisioning returns Bangladesh Bank prescribes, from the same records that drive the bank's internal position."
br_ids: [BR-LMS-251]
brd_section: 8.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-251"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p58"
related: [bridge.BR-LMS-251, glossary.asset-classification, glossary.provisioning, glossary.bb]
version: 1
status: approved
approved_by: Owner
---
**In short:** The platform produces the classification and provisioning returns Bangladesh Bank prescribes, from the same records that drive the bank's internal position.

## What the rule says

BR-LMS-251 (Must, BRD 8.3, PDF page 58) says the platform supports classification and provisioning returns on the basis prescribed by Bangladesh Bank. They are produced from the same underlying records that drive the bank's internal position. The id carries the LMS prefix, but the row sits in Section 8.3, outside the 103 requirements of Section 7.

## Why the bank wants it

A note on PDF page 58 says the regulatory obligations are the Bank's to set, not the supplier's, and that the Bank supplies the rule set, the return formats and the submission calendar. The BRD doesn't say why the return must come from the same records as the internal position; the usual reason is that a return built separately can disagree with the books and then has to be explained.

## Example

For one reporting period the regulator's return shows 120 loans as sub-standard with a provision of 8 million. The bank's own report, drawn from the same records, shows the same 120 loans and the same 8 million, so nothing needs reconciling.

## Terms to know

- **Classification:** the grade of a loan by repayment record. See `glossary.asset-classification`.
- **Provisioning:** money set aside against loans that may not be repaid. See `glossary.provisioning`.
- **Return:** a formal report a bank files with the regulator.
