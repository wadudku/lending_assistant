---
id: bridge.BR-LOS-201
type: bridge
title: "Opening the loan account and paying out are two steps, each retryable with its own reference and progress"
summary: "Not analysed. The team has not compared BR-LOS-201 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-201]
brd_section: 6.9
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-201"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p43"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.9"
related: [concept.BR-LOS-201, glossary.cbs, concept.BR-LOS-202]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-201 with Frappe Lending, so there is no verdict.

## Business need

“Loan account opening and disbursement shall be two distinct steps, each independently retryable, each carrying a distinct platform-generated unique reference written into the Core Banking System record, and each with its own progress state visible to the officer.” (BR-LOS-201, BRD 6.9, PDF page 43). See `concept.BR-LOS-201` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-201 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- The team analysed a related servicing requirement, BR-LMS-100 (accepting only loans that are really paid out). That is not a comparison with BR-LOS-201.
- **Loan Disbursement** is a Frappe Lending document with that name.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-201 sits in section 6.9. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Read BRD 9.2, which the BRD cites for how account opening and disbursement are done by robotic process automation.
2. Ask NRB where the platform-generated reference is to be written in the core banking record.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
