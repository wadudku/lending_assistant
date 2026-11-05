---
id: brd_section.6.9
type: brd_section
title: "BRD 6.9 Approval, loan account opening and disbursement"
summary: "Section 6.9 holds eleven requirements for approval, loan account opening and disbursement, the point where the BRD says the platform causes money to move."
br_ids: [BR-LOS-200, BR-LOS-201, BR-LOS-201a, BR-LOS-202, BR-LOS-203, BR-LOS-204, BR-LOS-205, BR-LOS-206, BR-LOS-207, BR-LOS-208, BR-LOS-209]
brd_section: 6.9
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.9"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p43"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p44"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-200"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-201"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-201a"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-202"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-203"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-204"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-205"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-206"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-207"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-208"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-209"
related: [bridge.BR-LOS-200, bridge.BR-LOS-201, bridge.BR-LOS-201a, bridge.BR-LOS-202, bridge.BR-LOS-203, bridge.BR-LOS-204, bridge.BR-LOS-205, bridge.BR-LOS-206, bridge.BR-LOS-207, bridge.BR-LOS-208, bridge.BR-LOS-209, glossary.cbs, glossary.rpa, brd_section.6]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 6.9 holds eleven requirements for approval, loan account opening and disbursement, the point where the BRD says the platform causes money to move.

## What this section says

BRD 6.9 (PDF pages 43 and 44) opens with a short paragraph and holds eleven requirements, BR-LOS-200 to BR-LOS-209 and BR-LOS-201a, all Must. They cover what the officer sees and confirms before approval (200), opening the account and disbursing as two separate steps (201), concluding the visit when funding takes too long (201a), confirming the account before disbursement (202), holding when disbursement fails after opening (203), re-reading the core banking system before a retry (204), validating the account again (205), halting on an unclear automation outcome (206), blocking disbursement for a lapsed sanction or unevidenced condition (207), the receipt (208) and the borrower notification (209).

## Why the bank wants it

The BRD gives the reason on PDF page 43: "This is the point at which the platform causes money to move. The controlling risk is duplicate disbursement arising from an uncertain response to an instruction that has in fact already executed." It adds that the risk is sharper because account opening and disbursement are done by robotic process automation driving the Core Banking System (Section 9.2), and "a screen-driven session gives a weaker guarantee of what did and did not happen than an application interface does".

## How it meets Frappe Lending

The team has not analysed the LOS (the origination system, BRD section 6), so this section carries no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7. None of the eleven rows is among the 103 requirements the team verified. The team analysed a related servicing requirement, BR-LMS-100, and that is not a comparison with these rows.

## Related cards

Rows: `bridge.BR-LOS-200`, `bridge.BR-LOS-201`, `bridge.BR-LOS-201a` and `bridge.BR-LOS-202` to `bridge.BR-LOS-209`. Parent section: `brd_section.6`.
