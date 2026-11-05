---
id: concept.BR-GOV-040
type: concept
title: A changed regulatory rule takes effect from a date and leaves past returns alone
summary: "A change to a regulatory rule is made as a versioned, effective-dated configuration change, and returns for earlier periods keep the rules in force in those periods."
br_ids: [BR-GOV-040]
brd_section: 8.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-040"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p58"
related: [bridge.BR-GOV-040, glossary.bb]
version: 1
status: approved
approved_by: Owner
---
**In short:** A change to a regulatory rule is made as a versioned, effective-dated configuration change, and returns for earlier periods keep the rules in force in those periods.

## What the rule says

BR-GOV-040 (Must, BRD 8.3, PDF page 58) says that when a regulatory rule changes, the change is implemented as a versioned, effective-dated configuration change. Returns for prior periods continue to reflect the rules in force in those periods.

## Why the bank wants it

A note on PDF page 58 says the regulatory obligations are the Bank's to set, not the supplier's, and that the Bank supplies the rule set, the return formats and the submission calendar. The BRD doesn't say why changes are dated and versioned; the usual reason is that a rule change must not rewrite what was filed under the old rule.

## Example

From 1 July the regulator raises a provisioning rate from 20% to 25%. The new rate is added as a new version that starts on 1 July. A return for May is re-run later and still uses 20%, while a return for July uses 25%.

## Terms to know

- **Versioned:** each change keeps the earlier version.
- **Effective-dated:** the change applies from a stated date, not from the day it is typed in.
- **Prior period:** an earlier reporting period.
