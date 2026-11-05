---
id: brd_section.7.7
type: brd_section
title: "BRD 7.7 Repayment, collection and allocation"
summary: "Section 7.7 says what must hold for every payment once the bank knows it has arrived, and leaves the question of how a payment reaches the system to NRB."
br_ids: []
brd_section: 7.7
doctypes: []
dev_items: [D12, D13]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#7.7"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p50"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p51"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p52"
  - "sources/verification/reqs.json#BR-LMS-164"
  - "sources/verification/reqs.json#BR-LMS-168"
  - "sources/verification/verification_report.md#BR-LMS-164"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#7.7-repayment-collection-and-allocation"
  - "sources/NRB_LMS_Requirements_Plain_English.md#7.7-repayment-collection-and-allocation"
related: [bridge.BR-LMS-160, bridge.BR-LMS-161, bridge.BR-LMS-162, bridge.BR-LMS-163, bridge.BR-LMS-164, bridge.BR-LMS-165, bridge.BR-LMS-166, bridge.BR-LMS-167, bridge.BR-LMS-168, bridge.BR-LMS-169, bridge.BR-LMS-170r, bridge.BR-LMS-171r, devitem.D12, devitem.D13, screen.loan_repayment]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 7.7 says what must hold for every payment once the bank knows it has arrived, and leaves the question of how a payment reaches the system to NRB.

## What this section says

BRD 7.7 (PDF pages 50 to 52, 12 requirements numbered BR-LMS-160 to BR-LMS-171) opens with a deferral: how a repayment reaches the bank, and how the platform learns about it, is for NRB to decide and is not specified. The section therefore states only what is true whatever channel is chosen: record the payment with its references (160), wait for confirmation (161), apply it once (162), as at its value date (163), in the set order (164), for all payment types (165), in bulk (166), park unattributed money (167), quote a payoff (168), correct by repost (169), and reconcile with the CBS (170, 171).

Section 7.7.2 lists seven open questions for NRB. They cover the channels in use, whether the CBS collects by standing instruction, how a credit is detected and attributed, how partner bulk remittances are controlled, the detection cycle, and who owns the unidentified-receipts queue. They are not baselined and not estimated.

## Why the bank wants it

The BRD explains its own structure. How a repayment reaches the bank is NRB's decision, so the section states only what holds whatever that decision is; everything after a payment is known (how it is allocated, what types exist, how corrections are made, how the position is reconciled) does not depend on the channel (PDF page 50). The open items show why the rest matters: the detection cycle decides how current the platform's days past due, classification and provisioning can be (PDF page 52).

## How it meets Frappe Lending

Of the 12 requirements, the verified result on 16.5.1 is: 4 covered (160, 163, 165, 169), 5 partly covered (161, 164, 166, 167, 168), 1 gap (162, duplicate references) and 2 gap (needs the CBS link) (170r, 171r). Two verdicts moved from covered to partly covered during verification: 164 and 168. In J3 the verification called the payment-order defect behind 164 (DEF-3) the biggest operational risk found so far, because on-time borrowers go overdue.

## Related cards

Requirement cards: `concept.BR-LMS-160` to `concept.BR-LMS-171r` with matching bridge cards. Development items: `devitem.D12` and `devitem.D13`. Terms: `glossary.value-date`, `glossary.posting-date`, `glossary.allocation-order`, `glossary.cbs`. Screen: `screen.loan_repayment`. Decision: `decision.waiver`.
