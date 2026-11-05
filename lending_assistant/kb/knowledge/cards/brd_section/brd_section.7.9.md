---
id: brd_section.7.9
type: brd_section
title: "BRD 7.9 Prepayment, restructuring and adjustments"
summary: "Section 7.9 covers changes to a running loan: paying early, restructuring, manual adjustments and refunds, each with limits, approvals and a record."
br_ids: []
brd_section: 7.9
doctypes: []
dev_items: [D8, D16, D20]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#7.9"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p53"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#7.9-prepayment-restructuring-and-adjustments"
  - "sources/NRB_LMS_Requirements_Plain_English.md#7.9-prepayment-restructuring-and-adjustments"
  - "sources/verification/reqs.json#BR-LMS-180"
related: [devitem.D8, devitem.D16, devitem.D20, decision.restructure, decision.waiver, glossary.prepayment, glossary.advance-payment, glossary.restructuring, glossary.rescheduling, glossary.waiver, lifecycle.RESTRUCTURED]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 7.9 covers changes to a running loan: paying early, restructuring, manual adjustments and refunds, each with limits, approvals and a record.

## What this section says

BRD 7.9 (PDF page 53, 9 requirements, BR-LMS-180 to BR-LMS-188) covers advance payment applied to future obligations (180), prepayment that revises the instalment or the tenor, with any prepayment charge (181), restructuring with its type recorded (182), a new schedule with the prior one kept as restructured and superseded (183), restructuring limits by branch and by period with a utilisation log (184), manual adjustments under maker-checker with before and after amounts (185), refunds of excess payments under approval (186), tracking a security deposit (187) and reporting restructures, reschedules and waivers to Bangladesh Bank with the treatment recorded (188).

## Why the bank wants it

The BRD doesn't say why; the usual reason is that each of these events changes what a borrower owes outside the normal repayment path, so the bank wants limits, two-person approval and a record of before and after. BR-LMS-188 adds that the regulator must be told (PDF page 53).

## How it meets Frappe Lending

Of the 9 requirements, the verified result on 16.5.1 is 2 covered (183, 187); 5 partly covered (180, 181, 182, 185, 186); 2 a gap (184, 188). Verification moved 3 of these verdicts: 180, 184, 186. Dev items: D8 (approval and audit pack), D16 (Bangladesh Bank treatment) and D20 (small items).

## Related cards

Dev items: `devitem.D8`, `devitem.D16`, `devitem.D20`. Decisions: `decision.restructure`, `decision.waiver`. Terms: `glossary.prepayment`, `glossary.advance-payment`, `glossary.restructuring`, `glossary.rescheduling`, `glossary.waiver`. State: `lifecycle.RESTRUCTURED`.
