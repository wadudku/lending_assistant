---
id: bridge.BR-LOS-321
type: bridge
title: Automatic sanction only inside every configured threshold
summary: "Not analysed. The team has not compared BR-LOS-321 with Frappe Lending, so there is no verdict."
br_ids: [BR-LOS-321]
brd_section: 6.6
doctypes: [Authorization Rule, Loan Product]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-321"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p37"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-322"
related: [concept.BR-LOS-321]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-LOS-321 with Frappe Lending, so there is no verdict.

## Business need

“The platform shall sanction automatically only where the application falls within every configured auto-sanction threshold. Thresholds shall be configurable by amount band, risk grade, tenor, product and partner, and shall be versioned, effective-dated and subject to maker-checker.” (BR-LOS-321, BRD 6.6, PDF page 37). See `concept.BR-LOS-321` for why the BRD asks for it. The BRD places this in the origination system (LOS, section 6), which is separate from the servicing system the team analysed.

## Frappe Lending today

The team has not looked at BR-LOS-321 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Authorization Rule** is ERPNext's document for approval limits; its list of documents holds sales and purchase documents only, such as Sales Order and Purchase Invoice.
- **Loan Product** is the document that holds a loan product's settings.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-LOS-321 sits in section 6.6. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List what the first item above can base a rule on.
2. Check whether a rule can be dated and kept in versions.
3. Ask NRB for the thresholds by amount band, grade, tenor, product and partner.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
