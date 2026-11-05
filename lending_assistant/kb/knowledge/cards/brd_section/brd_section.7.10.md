---
id: brd_section.7.10
type: brd_section
title: "BRD 7.10 Delinquency, classification and provisioning"
summary: "Section 7.10 covers late payment from first day to loss: counting days past due, grading loans, setting money aside, suspending income, write-off, freezing and collections."
br_ids: []
brd_section: 7.10
doctypes: []
dev_items: [D5, D8, D14, D15, D17]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#7.10"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p53"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p54"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#7.10-delinquency-classification-and-provisioning"
  - "sources/NRB_LMS_Requirements_Plain_English.md#7.10-delinquency-classification-and-provisioning"
  - "sources/verification/reqs.json#BR-LMS-190"
related: [devitem.D5, devitem.D8, devitem.D14, devitem.D15, devitem.D17, decision.override, decision.freeze, decision.write-off, lifecycle.OVERDUE, lifecycle.SMA, lifecycle.NPA, lifecycle.FROZEN, glossary.dpd, glossary.asset-classification, glossary.provisioning, glossary.income-suspense]
version: 2
status: approved
approved_by: Owner
---
**In short:** Section 7.10 covers late payment from first day to loss: counting days past due, grading loans, setting money aside, suspending income, write-off, freezing and collections.

## What this section says

BRD 7.10 (PDF pages 53 and 54, 9 requirements, BR-LMS-190 to BR-LMS-198) has the platform do these things. It calculates days past due daily and keeps a daily history (190). It assigns an asset classification from configured bands, with a qualitative override that has a reason and an approver (191). It keeps a history of movements between classes and never deletes a prior one (192). It calculates provisions by classification and by secured, semi-secured or unsecured status (193). It moves qualifying unpaid interest to income suspense and restores it only on actual recovery (194). It assesses write-off eligibility against its own threshold (195). It records authorised freezes (196). It versions the classification, provisioning and income rules under maker-checker (197). It runs a collections workflow (198).

## Why the bank wants it

The BRD doesn't say why; the usual reason is that the grade of a loan decides how much income the bank may count and how much it must set aside, so the grade, its history and the rules behind it must be reliable and approved. BR-LMS-197 states the ownership rule: Credit Risk and Finance own the bands and percentages (PDF page 54).

## How it meets Frappe Lending

Of the 9 requirements, the verified result on 16.5.1 is 2 covered (190, 195); 4 partly covered (191, 192, 194, 196); 3 a gap (193, 197, 198). Verification moved 2 of these verdicts: 194, 198. Dev items: D5 (versioned, approved configuration), D8 (approval and audit pack), D14 (provisioning engine), D15 (classification history and override) and D17 (collections escalation).

## Related cards

Dev items: `devitem.D5`, `devitem.D8`, `devitem.D14`, `devitem.D15`, `devitem.D17`. Decisions: `decision.override`, `decision.freeze`, `decision.write-off`. States: `lifecycle.OVERDUE`, `lifecycle.SMA`, `lifecycle.NPA`, `lifecycle.FROZEN`. Terms: `glossary.dpd`, `glossary.asset-classification`, `glossary.provisioning`, `glossary.income-suspense`.
