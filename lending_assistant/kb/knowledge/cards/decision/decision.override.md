---
id: decision.override
type: decision
title: "Decision: overriding a loan's classification by hand"
summary: "An override lets an authorised person change a loan's grade against the days-past-due bands, with a reason and an approver. Frappe Lending's only override is the Manual NPA tick, with no reason, approver or history."
br_ids: [BR-LMS-191, BR-LMS-192]
brd_section: 7.10
doctypes: [Loan, Loan NPA Log]
dev_items: [D15]
decision: override
actions: ["Loan:manual_npa"]
options: []
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan/loan.py:488", "lending/loan_management/doctype/loan/loan.py:486"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-191"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-192"
  - "sources/verification/reqs.json#BR-LMS-191"
  - "sources/verification/reqs.json#BR-LMS-192"
  - "sources/verification/FINAL_REPORT.md#D15"
  - "sources/verification/verification_report.md#BR-LMS-191"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-309"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-133"
related: [lifecycle.NPA, glossary.dpd, devitem.D15]
version: 2
status: approved
approved_by: Owner
---
**In short:** An override lets an authorised person change a loan's grade against the days-past-due bands, with a reason and an approver. Frappe Lending's only override is the Manual NPA tick, with no reason, approver or history.

## The rule

BR-LMS-191 says the platform assigns an asset classification from configured days-past-due bands and can also record a qualitative override with a reason and an approver. BR-LMS-192 says movements into and out of the early-warning and non-performing classes are kept as a history, and a prior classification is never deleted. The BRD's data list for classification names the class, effective date, rule version and qualitative override. The BRD does not name who may override or by how much. The BRD also uses "override" for a score-driven decision (BR-LOS-309) and for a sampling rate (BR-LOS-133) in the LOS; the team has not analysed these.

## Options

Frappe Lending has two switches on the **Loan**: **Manual NPA** and **Unmark NPA**. Ticking Manual NPA marks the borrower's loans NPA together (`lending/loan_management/doctype/loan/loan.py:488`, `lending/loan_management/doctype/loan/loan.py:489`) and moves the unpaid interest to suspense (`lending/loan_management/doctype/loan/loan.py:498`). Unmark NPA clears the NPA flag, but is refused before the **Watch Period End Date** (`lending/loan_management/doctype/loan/loan.py:486`). The grade itself (**Classification Code**) is a read-only field set by the classification run, so there is no way to override the grade directly.

## Who approves

The BRD asks for an override to carry a reason and an approver. In the test, Manual NPA had no reason and no approver, and the installed Loan doctype gives the Loan Manager role create, write and submit on a loan, so one person can tick it. The proposed Classification Override (D15) would be a submittable record with a reason and an approver that the daily classification respects.

## How Frappe Lending does it today

The verified results are partly covered for BR-LMS-191 and BR-LMS-192. In the test, the NPA flag and the grade disagreed (DEF-7): ticking NPA on a borrower's loan marked their other loans NPA while the good loan kept grade STD with 0 days past due. Removing a manual NPA did not reverse its suspense (DEF-13). Back-dated NPA processing moved too little to suspense (DEF-9), and interest collected on an NPA loan stayed in suspense until the loan was upgraded (DEF-15). The grade moves leave no history (BR-LMS-192). D15, with ND-14 and ND-15, plans a history record, an override with a reason and append-only logs. See `lifecycle.NPA`, `lifecycle.SMA` and `glossary.asset-classification`.

*Codes:* DEF = defect, ND = new item, both found in verification (final report, sections 5 and 7).
