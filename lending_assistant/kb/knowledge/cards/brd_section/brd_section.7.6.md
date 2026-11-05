---
id: brd_section.7.6
type: brd_section
title: BRD 7.6 Interest-rate repricing
summary: "Section 7.6 makes repricing a floating-rate portfolio safe: a practice run, two people, a new schedule version for each loan and no rewriting of paid history."
br_ids: []
brd_section: 7.6
doctypes: []
dev_items: [D11]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#7.6"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p49"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p50"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#7.6-interest-rate-repricing"
  - "sources/NRB_LMS_Requirements_Plain_English.md#7.6-interest-rate-repricing"
  - "sources/verification/reqs.json#BR-LMS-150"
related: [devitem.D11, glossary.repricing, glossary.maker-checker, glossary.idempotency, glossary.schedule-version, glossary.effective-date]
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 7.6 makes repricing a floating-rate portfolio safe: a practice run, two people, a new schedule version for each loan and no rewriting of paid history.

## What this section says

BRD 7.6 (PDF pages 49 and 50, 10 requirements, BR-LMS-150 to BR-LMS-159) covers the whole repricing run. Staff select eligible active floating-rate loans (150). The new rate starts from an approved effective date (151). Paid instalments and posted history are never rewritten (152). Both modes are supported: fixed maturity with a revised instalment, or fixed instalment with a revised tenor (153). A dry run comes first (154). A maker creates the run and an independent checker approves it (155). Each repriced loan gets a new schedule version (156). The batch is idempotent and resumable (157). Ineligible loans are excluded automatically (158). Borrowers are notified (159).

## Why the bank wants it

The BRD gives its reason in the section introduction (PDF page 49): repricing a floating-rate portfolio is high-volume and high-consequence, and done wrongly it silently rewrites the amounts owed by thousands of borrowers. The requirements exist to make it safe.

## How it meets Frappe Lending

Of the 10 requirements, the verified result on 16.5.1 is 3 partly covered (152, 153, 156); 7 a gap (150, 151, 154, 155, 157, 158, 159). Verification confirmed every verdict from the analysis. Dev item: D11 (Loan Repricing Run), which closes all ten.

## Related cards

Dev item: `devitem.D11`. Terms: `glossary.repricing`, `glossary.maker-checker`, `glossary.idempotency`, `glossary.schedule-version`, `glossary.effective-date`.
