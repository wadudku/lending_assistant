---
id: concept.BR-LMS-203
type: concept
title: Money collected after a write-off
summary: Money collected later on a loan that was written off is recorded as a write-off recovery on the original loan and treated according to the bank's policy.
br_ids: [BR-LMS-203]
brd_section: 7.11
doctypes: []
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-203"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p54"
  - "sources/verification/reqs.json#BR-LMS-203"
  - "sources/verification/verification_report.md#BR-LMS-203"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-203"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-203"
related: [bridge.BR-LMS-203, brd_section.7.11, glossary.write-off, concept.BR-LMS-202, decision.write-off]
version: 1
status: approved
approved_by: Owner
---
**In short:** Money collected later on a loan that was written off is recorded as a write-off recovery on the original loan and treated according to the bank's policy.

## What the rule says

BR-LMS-203 in section 7.11 (Must, BRD PDF page 54) says money recovered later against a written-off balance shall be recorded as a write-off recovery against the original loan and treated in accordance with policy. The BRD does not state the policy.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that a recovery after write-off is a gain the bank did not expect, so it is booked apart from ordinary repayments and tied to the loan it came from.

## Example

Two years after the write-off, Rahim pays 10,000. It is booked as recovery income on the same loan.

## Terms to know

- **Write-off recovery:** cash received on a loan already written off.
- **Recovery income:** where the bank books that cash.
- **Original loan:** the same loan record, not a new one.
