---
id: brd_section.6.2
type: brd_section
title: BRD 6.2 Bulk application submission
summary: "Section 6.2 holds seven rules for bulk application files: a versioned template, whole-file rejection, limits shown first, row checks in three groups, browser corrections, partial submission and three-level duplicate detection."
br_ids: [BR-LOS-110, BR-LOS-111, BR-LOS-112, BR-LOS-113, BR-LOS-114, BR-LOS-115, BR-LOS-116]
brd_section: 6.2
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.2"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p29"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p30"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-110"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-111"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-112"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-113"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-114"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-115"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-116"
related: [bridge.BR-LOS-110, bridge.BR-LOS-111, bridge.BR-LOS-112, bridge.BR-LOS-113, bridge.BR-LOS-114, bridge.BR-LOS-115, bridge.BR-LOS-116]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 6.2 holds seven rules for bulk application files: a versioned template, whole-file rejection, limits shown first, row checks in three groups, browser corrections, partial submission and three-level duplicate detection.

## What this section says

BRD 6.2 (PDF pages 29 and 30) says bulk submission is the single write-heavy flow in the Partner Portal and carries the greatest data quality risk in origination. The objective is that a partner operations user, without banking knowledge, can identify and correct every defect in a file without escalation to the Bank. It holds seven requirements, BR-LOS-110 to BR-LOS-116: applications come in as a versioned CSV or XLSX template (110); a bad file is rejected whole (111); file size and row limits are shown before upload (112); every row is checked and results are sorted into three groups (113); wrong rows can be fixed in the browser or exported (114); the partner can submit the valid rows and keep the rest, with a confirmation summary (115); and duplicates are caught at three levels (116). The sub-sections 6.2.1 to 6.2.3 hold the duplicate table, the application field list and the borrower consent rule.

## Why the bank wants it

The BRD gives the reason in the section introduction: the aim is that a partner operations user without banking knowledge can find and fix every defect in a file without asking the Bank (PDF page 29).

## How it meets Frappe Lending

The section holds 7 requirements (BR-LOS-110 to BR-LOS-116, of which BR-LOS-111 is an approved pilot). The team has not analysed them: the analysis covered the 103 servicing requirements of BRD section 7, so this card gives no verdict. Each row has a concept card with the rule and a not-analysed bridge card with pointers only.

## Related cards

Requirement cards: `concept.BR-LOS-110` to `concept.BR-LOS-116` with matching bridge cards. Sections: `brd_section.6.2.1`, `brd_section.6.2.2`, `brd_section.6.2.3`. Term: `glossary.batch`.
