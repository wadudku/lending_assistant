---
id: concept.BR-LOS-322
type: concept
title: "Outside a threshold, the case waits in a credit approval queue"
summary: An application outside an auto-sanction threshold goes to a credit approval queue and cannot move to assignment until a credit approver has decided it.
br_ids: [BR-LOS-322]
brd_section: 6.6
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-322"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p38"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-321"
related: [bridge.BR-LOS-322, concept.BR-LOS-321, concept.BR-LOS-324, glossary.scorecard, glossary.field-officer]
version: 1
status: approved
approved_by: Owner
---
**In short:** An application outside an auto-sanction threshold goes to a credit approval queue and cannot move to assignment until a credit approver has decided it.

## What the rule says

BR-LOS-322 (Must, BRD 6.6, PDF page 38) says any application falling outside an auto-sanction threshold is routed to a credit approval queue and does not advance to assignment until a credit approver has decided it. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD gives the reason in the 6.6 introduction: sanction is the Bank's decision to lend, on stated terms, to a named applicant. The scorecard and product configuration should carry the routine cases, and a credit officer should see everything above that line. Sanction happens before assignment, so that no field officer is sent to meet an applicant the Bank has not agreed to lend to (PDF page 37).

## Example

An application asks for 300,000, above the automatic limit. It goes to the credit approval queue. No field officer is assigned until a credit approver sanctions or declines it.

## Terms to know

- **Credit approver:** a Bank officer who decides cases above the automatic line.
- **Queue:** the list of cases waiting for a decision.
- **Assignment:** giving the case to a field officer.
- **Routed:** sent to a particular place for action.
