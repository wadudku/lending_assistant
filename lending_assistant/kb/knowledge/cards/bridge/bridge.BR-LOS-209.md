---
id: bridge.BR-LOS-209
type: bridge
title: The borrower is told of the payment and a failed message never blocks or reverses the loan
summary: "Not analysed. The team has not compared BR-LOS-209 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-209]
brd_section: 6.9
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-209"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p44"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.9"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-054"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p65"
related: [concept.BR-LOS-209, concept.BR-LOS-208, concept.BR-LOS-201a]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-209 with Frappe Lending, so there is no verdict.

## Business need

“The borrower shall be notified of the disbursement through the configured notification channel. Notification failure shall be retried and reported and shall never block or reverse a loan action.” (BR-LOS-209, BRD 6.9, PDF page 44). See `concept.BR-LOS-209` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-209 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Notification** is Frappe's document for alert rules.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-209 sits in section 6.9. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Read BR-INT-054 in BRD 9.7, which leaves the notification channels to the Bank, and ask NRB which channel is configured for borrowers.
2. Read BR-LOS-201a, which also says the borrower is notified of an outcome.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
