---
id: concept.BR-LOS-137
type: concept
title: Some applications are always reviewed under seven mandatory rules
summary: "Beyond the random rate, Credit Risk configures mandatory sampling rules for large amounts, new partners, cross-partner duplicates, referred or risky grades, requested overrides, partners with high rejection rates and new districts."
br_ids: [BR-LOS-137]
brd_section: 6.5
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-137"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p36"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-116"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-309"
related: [bridge.BR-LOS-137, concept.BR-LOS-116, concept.BR-LOS-309, concept.BR-LOS-130, glossary.sampling, glossary.scorecard]
version: 1
status: approved
approved_by: Owner
---
**In short:** Beyond the random rate, Credit Risk configures mandatory sampling rules for large amounts, new partners, cross-partner duplicates, referred or risky grades, requested overrides, partners with high rejection rates and new districts.

## What the rule says

BR-LOS-137 (Must, BRD 6.5, PDF page 36) says that in addition to the random rate the platform supports rule-based mandatory sampling, configurable by Credit Risk, covering at minimum: applications above a configurable amount threshold; applications from a partner within its first configurable number of batches; applications flagged as cross-partner duplicates; applications the scorecard referred or that fall in a configured risk grade band; applications where a score override has been requested; applications from a partner whose recent sample rejection rate exceeds a configured threshold; and a configurable proportion of applications from any newly added district or upazila. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD gives the reason in the 6.5 introduction: sampling is how the Bank keeps credit judgement over a volume too large to review one by one, and its integrity (genuinely random selection, a controlled rate, decisions that can be attributed and reproduced) is what makes partner-sourced origination defensible to internal audit and the regulator (PDF page 35).

## Example

A partner is in its second batch and one application asks for an amount above the Bank's threshold. Both rules apply, so the application goes to a reviewer whatever the random draw says.

## Terms to know

- **Mandatory sampling:** a rule that always sends certain applications to review.
- **Threshold:** a limit above which a rule applies.
- **Cross-partner duplicate:** a person submitted by two partners. See BR-LOS-116.
- **Upazila:** a local administrative area below district.
