---
id: concept.BR-LOS-303
type: concept
title: "Scoring gives a score, a risk grade and a recommended decision"
summary: "Scoring produces a numeric score, a risk grade and a recommended decision of auto-approve, refer or decline, set by cut-offs that can differ by product and partner."
br_ids: [BR-LOS-303]
brd_section: 6.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-303"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p34"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-302"
related: [bridge.BR-LOS-303, concept.BR-LOS-302, glossary.score-cut-off]
version: 1
status: approved
approved_by: Owner
---
**In short:** Scoring produces a numeric score, a risk grade and a recommended decision of auto-approve, refer or decline, set by cut-offs that can differ by product and partner.

## What the rule says

BR-LOS-303 (Must, BRD 6.4, PDF page 34) says scoring produces a numeric score, a risk grade and a recommended decision of auto-approve, refer or decline, determined by configured cut-offs that may differ by product and by partner. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't say why in this row; the 6.4.1 table shows the idea: each band carries a recommended decision and a downstream treatment (PDF page 35).

## Example

An application scores 640. For this product and partner the cut-offs give grade C and the recommendation “refer”. Under another partner’s cut-offs the same score could give “auto-approve”.

## Terms to know

- **Risk grade:** a band such as low or high risk that the score falls in.
- **Auto-approve:** the application moves on without a person deciding.
- **Refer:** a person reviews it.
- **Decline:** the application is refused.
