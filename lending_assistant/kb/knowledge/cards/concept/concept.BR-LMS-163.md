---
id: concept.BR-LMS-163
type: concept
title: Use the date the money actually arrived
summary: "A payment is applied as at its value date. Days past due, penalty and grade are recalculated as of that date, so a borrower is never punished for the bank's own delay."
br_ids: [BR-LMS-163]
brd_section: 7.7
doctypes: []
verdict: covered
analysis_status: verified
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-163"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p51"
  - "sources/verification/reqs.json#BR-LMS-163"
  - "sources/verification/verification_report.md#BR-LMS-163"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-163"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-163"
related: [bridge.BR-LMS-163, glossary.value-date, glossary.dpd]
version: 1
status: approved
approved_by: Owner
---
**In short:** A payment is applied as at its value date. Days past due, penalty and grade are recalculated as of that date, so a borrower is never punished for the bank's own delay.

## What the rule says

BR-LMS-163 (Must, BRD 7.7.1, PDF page 51) says a payment is allocated as at its value date, not the date the platform became aware of it. Days past due, penal interest, classification and any consequent treatment are recalculated as at that value date.

## Why the bank wants it

The BRD gives the reason in the rule itself: so that "a borrower is never charged or classified on the strength of the platform's own processing lag" (BR-LMS-163, PDF page 51). In plain words, if a branch enters a payment days after the money arrived, the borrower must not pay penalty, or be graded worse, for those days. The loan history follows what the borrower actually did, on the day they did it.

## Example

Rahim pays on 5 July but the bank only enters it on 12 July. After entry, he must show 0 days past due and no penalty, because he paid on time.

## Terms to know

- **Value date:** the real arrival day. See `glossary.value-date`.
- **Days past due (DPD):** how many days a payment is late. See `glossary.dpd`.
- **Penal interest:** the extra interest charged on late amounts.
- **Classification:** the loan's health grade, which depends on DPD.
