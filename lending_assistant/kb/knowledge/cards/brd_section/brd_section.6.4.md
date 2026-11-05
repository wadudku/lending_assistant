---
id: brd_section.6.4
type: brd_section
title: BRD 6.4 Application scoring
summary: "Section 6.4 holds fifteen rules for scoring every application against a scorecard that Credit Risk owns, and for how scores are recorded, used, overridden and reported."
br_ids: [BR-LOS-300, BR-LOS-301, BR-LOS-302, BR-LOS-303, BR-LOS-304, BR-LOS-305, BR-LOS-306, BR-LOS-307, BR-LOS-308, BR-LOS-309, BR-LOS-310, BR-LOS-311, BR-LOS-312, BR-LOS-313, BR-LOS-314]
brd_section: 6.4
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.4"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p33"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p34"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p35"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-300"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-301"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-302"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-303"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-304"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-305"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-306"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-307"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-308"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-309"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-310"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-311"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-312"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-313"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-314"
related: [bridge.BR-LOS-300, bridge.BR-LOS-301, bridge.BR-LOS-302, bridge.BR-LOS-303, bridge.BR-LOS-304, bridge.BR-LOS-305, bridge.BR-LOS-306, bridge.BR-LOS-307, bridge.BR-LOS-308, bridge.BR-LOS-309, bridge.BR-LOS-310, bridge.BR-LOS-311, bridge.BR-LOS-312, bridge.BR-LOS-313, bridge.BR-LOS-314]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 6.4 holds fifteen rules for scoring every application against a scorecard that Credit Risk owns, and for how scores are recorded, used, overridden and reported.

## What this section says

BRD 6.4 (PDF pages 33 to 35) says sampling gives the Bank oversight of a subset of applications, while scoring gives it a consistent credit opinion on every one. Scoring runs on every submitted application, after account and identity validation and before sampling selection. It holds fifteen requirements, BR-LOS-300 to BR-LOS-314: every submitted application is scored (300); the scorecard can use seven kinds of input (301); Credit Risk owns the scorecard and changes it without a software release (302); scoring gives a score, a grade and a recommended decision (303); each score is recorded and cannot be changed (304); refer and decline outcomes carry reason codes (305); the grade can set limits and extra steps (306); the score feeds sampling (307); a score-declined application is not shown its score (308); an authorised person can override with a second approver (309); absent data is never treated as good news (310); a second scorecard can run in shadow (311, a Should); scorecard performance is reported (312); any past decision can be reproduced (313); and the field officer's device never holds the score (314).

## Why the bank wants it

The BRD gives the reason in the section introduction: at partner-sourced volume the Bank cannot underwrite each file individually, and a decision that depends on which reviewer or officer handled the case is neither defensible to audit nor stable enough to price against (PDF page 33).

## How it meets Frappe Lending

The section holds 15 requirements (BR-LOS-300 to BR-LOS-314). The team has not analysed them: the analysis covered the 103 servicing requirements of BRD section 7, so this card gives no verdict. Each row has a concept card with the rule and a not-analysed bridge card with pointers only.

## Related cards

Requirement cards: `concept.BR-LOS-300` to `concept.BR-LOS-314` with matching bridge cards. Section: `brd_section.6.4.1`. Terms: `glossary.maker-checker`.
