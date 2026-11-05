---
id: brd_section.3.1
type: brd_section
title: "BRD 3.1 Two systems, one lending lifecycle"
summary: "Section 3.1 splits the lending lifecycle at one point, the moment the Core Banking System confirms a disbursement: before it is origination, after it is servicing."
br_ids: []
brd_section: 3.1
doctypes: []
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#3.1"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p17"
related: []
version: 1
status: approved
approved_by: Owner
---
**In short:** Section 3.1 splits the lending lifecycle at one point, the moment the Core Banking System confirms a disbursement: before it is origination, after it is servicing.

## What this section says

BRD 3.1 (PDF page 17) says the lifecycle is divided at a single point: the moment a disbursement is confirmed by the Core Banking System. Everything before is origination, everything after is servicing. A table sets the two systems side by side. The LOS answers “Should the Bank lend to this person, on what terms, and has the money actually reached them?”; it starts with a partner or branch submission and ends at confirmed disbursement or a terminal rejection or withdrawal; it owns the credit decision (scoring, sampling and sanction) and its evidence; and it does not own any balance, schedule or accounting entry. The LMS answers “What does this borrower owe, what have they paid, what risk does the loan carry, and how does it end?”; it starts on receipt of a confirmed funded loan with approved terms and a disbursement reference, and ends at closure, settlement or write-off; it owns the loan book position (schedules, demands, accruals, allocations, classification and provisions); and it does not own customer acquisition, underwriting or the sanction decision. Primary users of the LOS are partner staff, Bank sampling reviewers and field officers; of the LMS, loan processors, collections officers, finance and credit risk.

## Why the bank wants it

The BRD doesn't say why in this section; the usual reason is that one dividing point makes clear which system answers which question and who is responsible (PDF page 17). The next section, 3.2, explains why the point is a control and not only a convenience.

## How it meets Frappe Lending

This section holds no requirement row, so there is nothing in it to compare with Frappe Lending, and the team has made no statement about it. Frappe Lending is a servicing system; the team's analysis covers the LMS requirements of BRD section 7 only. It also describes the origination system (LOS), which the team has not analysed.

## Related cards

Related: `brd_section.3.2`, `brd_section.5.4`. Terms: `glossary.los`, `glossary.lms`, `glossary.cbs`.
