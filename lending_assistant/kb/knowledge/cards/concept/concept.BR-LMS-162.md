---
id: concept.BR-LMS-162
type: concept
title: Apply each payment only once
summary: "The same payment must never be counted twice, however many times the loan system hears about it. The CBS transaction reference is the key."
br_ids: [BR-LMS-162]
brd_section: 7.7
doctypes: []
verdict: gap
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-162"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p51"
  - "sources/verification/reqs.json#BR-LMS-162"
  - "sources/verification/verification_report.md#BR-LMS-162"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-162"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-162"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p52"
related: [bridge.BR-LMS-162, glossary.cbs, bridge.BR-GOV-002]
version: 1
status: approved
approved_by: Owner
---
**In short:** The same payment must never be counted twice, however many times the loan system hears about it. The CBS transaction reference is the key.

## What the rule says

BR-LMS-162 (Must, BRD 7.7.1, PDF page 51) says a payment is applied once and only once, keyed on the CBS transaction reference, however many times the platform observes or is told about it.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the loan system will hear about the same payment more than once. BRD 7.7.2 expects the platform to detect credits by a pull, such as a scheduled extract, an account-level read or a file from the bank (PDF page 52), and a file can be loaded twice or an entry typed again. If each sighting reduced the loan again, the borrower would be credited twice for one payment, and the loan system would disagree with the CBS. Using the CBS reference as a unique key makes a repeat harmless. This idea is called idempotency: doing it twice has the same effect as doing it once.

## Example

The robot reads CBS-TXN-0001 from the CBS twice. The second time, the loan system sees that reference is already applied and ignores it.

## Terms to know

- **Idempotent:** a repeat has no further effect.
- **CBS transaction reference:** the unique number the CBS gives each transaction. See `glossary.cbs`.
- **Duplicate:** the same payment recorded twice.
- A related rule for outgoing instructions is BR-GOV-002, which covers instructions the platform sends.
