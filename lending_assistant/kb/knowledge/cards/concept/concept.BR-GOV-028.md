---
id: concept.BR-GOV-028
type: concept
title: "Approval limits by role and amount, and a case over the limit escalates"
summary: "Limits for score override, sampling override, sanction and sanction variation, waiver, settlement, write-off and rate change can be set by role and amount band, are enforced when the action is taken, and a case above a user's limit goes up to someone else."
br_ids: [BR-GOV-028]
brd_section: 4.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-028"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p23"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p23"
related: [bridge.BR-GOV-028, glossary.waiver, glossary.write-off, concept.BR-GOV-020, concept.BR-GOV-022, glossary.sampling]
version: 1
status: approved
approved_by: Owner
---
**In short:** Limits for score override, sampling override, sanction and sanction variation, waiver, settlement, write-off and rate change can be set by role and amount band, are enforced when the action is taken, and a case above a user's limit goes up to someone else.

## What the rule says

BR-GOV-028 (Must, BRD 4.3, PDF page 23) says delegated authority limits can be configured by role and by amount band, and are enforced by the platform at the point of action. The BRD lists score override, sampling override, sanction and sanction variation, waiver, settlement, write-off and rate change. A case above the acting user's limit escalates and cannot be acted on by that user.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that larger or riskier decisions should be taken by more senior people, and the limit is part of the bank's internal control.

## Example

An officer's waiver limit is 10,000. A waiver of 25,000 is not allowed to that officer. It is passed to a role with a higher limit, and the officer cannot approve it.

## Terms to know

- **Delegated authority:** the right to decide up to a set size, given to a role by the bank.
- **Amount band:** a range of amounts, such as 0 to 10,000.
- **Escalate:** pass a case to someone with a higher limit.
- **Sanction variation:** a change to terms that were already sanctioned.
