---
id: bridge.BR-GOV-009
type: bridge
title: Financial histories are never overwritten; corrections add entries
summary: "Not analysed. The team has not compared BR-GOV-009 with Frappe Lending, so there is no verdict."
br_ids: [BR-GOV-009]
brd_section: 3.4
doctypes: [Loan Repayment, Loan Repayment Repost]
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: [lending/loan_management/doctype/loan_repayment_repost/loan_repayment_repost.py]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-009"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
related: [concept.BR-GOV-009]
version: 1
status: approved
approved_by: Owner
---
**In short:** Not analysed. The team has not compared BR-GOV-009 with Frappe Lending, so there is no verdict.

## Business need

“Repayment, schedule and accounting histories shall be immutable. A correction shall be made through a controlled reversal and re-entry that preserves the original, never through silent amendment or deletion.” (BR-GOV-009, BRD 3.4, PDF page 19). See `concept.BR-GOV-009` for why the BRD asks for it.

## Frappe Lending today

The team has not looked at BR-GOV-009 in Frappe Lending, so this card makes no statement about it.

### Not verified by the team

Pointers only, so a developer knows where a look could start. Nothing here has been tested or read, and none of it is a finding:
- **Loan Repayment** is the document for payments and other postings on a loan, such as waivers; its Repayment Type field lists the kinds.
- **Loan Repayment Repost** is the document used to redo repayments after a back-dated change.
- The code for Loan Repayment Repost is in `lending/loan_management/doctype/loan_repayment_repost/loan_repayment_repost.py`.

The drift check confirms these names exist on this site, and nothing more.

## Match or gap, and why

The team has **not analysed** this requirement, so there is no verdict. The analysis was limited to the 103 servicing requirements in BRD section 7, and BR-GOV-009 sits in section 3.4. Treat anything said about it, here or in a chat answer, as general reasoning and not as a finding of the team.

## What to do today

To find out, the team would need to:
1. List the history records named in the rule: repayments, schedules and accounting entries.
2. Read how each is cancelled or amended, and whether the original stays visible.
3. Test cancelling one repayment on a copy of the site and look at what remains in the history.

This card suggests no result.

## Planned fix

None. No development item is assigned, because the requirement has not been analysed.
