---
id: bridge.BR-LMS-197
type: bridge
title: "Grade, provision and income rules are owned and versioned"
summary: "Gap. The bands and rates are rows on the Company form. They have no version, effective date or approval, and no grade or provision stores which rules it used."
br_ids: [BR-LMS-197]
brd_section: 7.10
doctypes: [Company, Loan Classification Range, Loan IRAC Provisioning Configuration]
verdict: gap
analysis_status: verified
dev_items: [D5]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-197"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p54"
  - "sources/verification/reqs.json#BR-LMS-197"
  - "sources/verification/verification_report.md#BR-LMS-197"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-197"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-197"
  - "sources/verification/FINAL_REPORT.md#D5"
related: [concept.BR-LMS-197, concept.BR-LMS-191, bridge.BR-LMS-191, bridge.BR-LMS-193, devitem.D5]
version: 1
status: approved
approved_by: Owner
---
**In short:** Gap. The bands and rates are rows on the Company form. They have no version, effective date or approval, and no grade or provision stores which rules it used.

## Business need

The grade bands, provision rates and income rules must be owned, versioned, effective-dated and approved by a second person, and each result must record the rule version (BR-LMS-197 in section 7.10, BRD PDF page 54). See `concept.BR-LMS-197`.

## Frappe Lending today

The **Company** form holds two tables: the **Loan Classification Range** rows (code, name, minimum and maximum days past due, written-off tick) and the **Loan IRAC Provisioning Configuration** rows (classification, security type, provision rate). Neither row has a version, a start date or an approver field (`lending/loan_management/doctype/loan_classification_range/loan_classification_range.json`, `lending/loan_management/doctype/loan_irac_provisioning_configuration/loan_irac_provisioning_configuration.json`). The Company's own change history is the standard Version log. The income rules are code paths with the NPA threshold on the Loan Product and a switch on the loan (see `bridge.BR-LMS-194`).

## Match or gap, and why

This is a **gap**, and the verification confirmed it from the metadata (J4, meta check only, because the Company was not to be changed).

- Editing a band replaces it. The old values remain only in the Company's Version log.
- No Workflow is shipped for the Company, so one person can change a band or a rate.
- The grade on the Loan and the rows of the Days Past Due Log and the Loan NPA Log carry no rule version (see `bridge.BR-LMS-190` and `bridge.BR-LMS-192`).

## What to do today

Control access to the Company form, record each change of band or rate with its date and approver in a register outside the system, and keep the old values there.

## Planned fix

Dev item D5 (versioned, approved configuration, sized large) covers this row. The final report notes that 197 stays a gap and adds cache clearing (ND-25).
