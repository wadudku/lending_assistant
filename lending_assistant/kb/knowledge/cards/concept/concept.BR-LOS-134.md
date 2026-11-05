---
id: concept.BR-LOS-134
type: concept
title: Applications not picked advance as a system decision stating the rate
summary: "Applications not selected advance automatically and the audit trail records them as a system decision stating the rate applied, not as a person's decision."
br_ids: [BR-LOS-134]
brd_section: 6.5
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-134"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p36"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-130"
related: [bridge.BR-LOS-134, concept.BR-LOS-130, concept.BR-LOS-133, glossary.sampling]
version: 1
status: approved
approved_by: Owner
---
**In short:** Applications not selected advance automatically and the audit trail records them as a system decision stating the rate applied, not as a person's decision.

## What the rule says

BR-LOS-134 (Must, BRD 6.5, PDF page 36) says applications not selected advance automatically and are recorded in the audit trail as a system decision stating the rate applied, not as a person's decision. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD gives the reason in the 6.5 introduction: sampling is how the Bank keeps credit judgement over a volume too large to review one by one, and its integrity (genuinely random selection, a controlled rate, decisions that can be attributed and reproduced) is what makes partner-sourced origination defensible to internal audit and the regulator (PDF page 35).

## Example

An application is not picked for review. It moves to the next step on its own, and its history shows “Passed by sampling at 10%, system decision”, with no staff name.

## Terms to know

- **Audit trail:** the history of who or what did what and when.
- **System decision:** a decision taken by the platform, not a person.
- **Person's decision:** a decision taken by a named person.
- **Rate applied:** the sampling rate used for that batch.
