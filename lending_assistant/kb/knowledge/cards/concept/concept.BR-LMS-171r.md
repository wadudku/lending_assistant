---
id: concept.BR-LMS-171r
type: concept
title: Match every payment end to end
summary: "For every payment the system checks that the CBS reference, the way the money was split and the accounting entry all agree, and reports anything that does not."
br_ids: [BR-LMS-171]
brd_section: 7.7
doctypes: []
verdict: gap_cbs
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-171r"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p51"
  - "sources/verification/reqs.json#BR-LMS-171r"
  - "sources/verification/verification_report.md#BR-LMS-171r"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-171"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-171"
related: [bridge.BR-LMS-171r, concept.BR-LMS-170r]
version: 1
status: approved
approved_by: Owner
---
**In short:** For every payment the system checks that the CBS reference, the way the money was split and the accounting entry all agree, and reports anything that does not.

## What the rule says

BR-LMS-171 in section 7.7 (Must, BRD PDF page 51) says the platform reconciles each repayment against its CBS reference, the demand allocation it produced and the resulting accounting posting. It reports every unmatched item under BRD section 8.4. The number 171 is used twice in the BRD; this is the repayment one (card suffix r). The other, in section 7.8, is about the life of a pledge.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a payment touches three records: the CBS transaction, the split of the payment across what was owed, and the accounting entry. If any of the three is missing or different, the books are wrong somewhere. A report of every payment that does not agree on all three finds breaks in days rather than at audit time.

## Example

CBS-TXN-0001 (8,979) matches the split 1,151 + 7,828 and journal JV-2026-000500: matched. CBS-TXN-0002 has no journal: reported.

## Terms to know

- **Allocation:** how a payment was split across the amounts owed. A demand is a bill raised on a due date.
- **Posting:** the accounting entry made for the payment.
- **Unmatched item:** a payment where the three records do not agree.
- **Reconciliation report:** the list of unmatched items. See `concept.BR-LMS-170r`.
