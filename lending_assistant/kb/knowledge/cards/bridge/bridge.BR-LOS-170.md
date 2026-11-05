---
id: bridge.BR-LOS-170
type: bridge
title: An officer starts a verification from the list or by manual lookup
summary: "Not analysed. The team has not compared BR-LOS-170 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-170]
brd_section: 6.7.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-170"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p40"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.7.3"
related: [concept.BR-LOS-170]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-170 with Frappe Lending, so there is no verdict.

## Business need

“The officer shall initiate verification either by selecting from the assigned list, or by entering an account number together with a mobile number for an applicant not on the list. In the latter case the platform shall confirm that the applicant holds a valid and unexpired sanction before allowing the officer to proceed, and shall record that the verification was initiated by manual lookup rather than assignment.” (BR-LOS-170, BRD 6.7.3, PDF page 40). See `concept.BR-LOS-170` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-170 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- None given.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-170 sits in section 6.7.3. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. Read BR-LOS-330 in BRD 6.6, which says when a sanction lapses, because BR-LOS-170 depends on a valid and unexpired sanction.
2. Ask NRB what the officer should be told when the number pair finds no valid sanction.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
