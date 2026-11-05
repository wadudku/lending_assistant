---
id: concept.BR-LMS-194
type: concept
title: Unpaid interest waits in suspense
summary: "After a loan turns bad, its unpaid interest and charges are moved to a holding account called suspense, and go back to income only when the money is actually collected."
br_ids: [BR-LMS-194]
brd_section: 7.10
doctypes: []
verdict: partial
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-194"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p54"
  - "sources/verification/reqs.json#BR-LMS-194"
  - "sources/verification/verification_report.md#BR-LMS-194"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-194"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-194"
related: [bridge.BR-LMS-194, brd_section.7.10, glossary.income-suspense, glossary.npa, lifecycle.NPA]
version: 1
status: approved
approved_by: Owner
---
**In short:** After a loan turns bad, its unpaid interest and charges are moved to a holding account called suspense, and go back to income only when the money is actually collected.

## What the rule says

BR-LMS-194 in section 7.10 (Must, BRD PDF page 54) says qualifying unpaid interest and charges shall be moved to income suspense after non-performing treatment is applied. They shall be restored to income only on actual recovery.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a bank should not report as profit interest it has not been paid, so the interest is held aside until cash arrives.

## Example

3,300 of interest is in suspense. Rahim pays 1,151, so 1,151 moves back to income and 2,149 stays in suspense.

## Terms to know

- **Income suspense:** a holding account for interest earned on paper but not collected. See `glossary.income-suspense`.
- **Non-performing (NPA):** the state that triggers the move. See `glossary.npa`.
- **Recovery:** cash actually received.
