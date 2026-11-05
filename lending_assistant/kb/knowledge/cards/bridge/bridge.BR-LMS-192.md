---
id: bridge.BR-LMS-192
type: bridge
title: Keep the history of grade changes
summary: "Partly covered. Moves into and out of NPA are logged, but a change of grade such as STD to SMA leaves no record, and the logs can be edited or deleted without a trace."
br_ids: [BR-LMS-192]
brd_section: 7.10
doctypes: [Loan NPA Log, Days Past Due Log, Loan]
verdict: partial
analysis_status: verified
dev_items: [D15]
lending_version: 16.5.1
code_refs: ["lending/loan_management/doctype/loan/loan.py:1738", "lending/loan_management/doctype/loan/loan.py:1662-1670"]
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LMS-192"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p53"
  - "sources/verification/reqs.json#BR-LMS-192"
  - "sources/verification/verification_report.md#BR-LMS-192"
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#BR-LMS-192"
  - "sources/NRB_LMS_Requirements_Plain_English.md#BR-LMS-192"
  - "sources/verification/FINAL_REPORT.md#new-items-found-in-verification-nd-1-...-nd-47"
  - "sources/verification/FINAL_REPORT.md#D15"
related: [concept.BR-LMS-192, bridge.BR-LMS-190, decision.override, lifecycle.NPA, devitem.D15]
version: 1
status: approved
approved_by: Owner
---
**In short:** Partly covered. Moves into and out of NPA are logged, but a change of grade such as STD to SMA leaves no record, and the logs can be edited or deleted without a trace.

## Business need

Moves into and out of early-warning and non-performing categories must be kept as a history that never loses a prior class (BR-LMS-192 in section 7.10, BRD PDF page 53). See `concept.BR-LMS-192`. See also `decision.override` for the override half of this area.

## Frappe Lending today

A **Loan NPA Log** row is written each time a loan goes into or out of NPA, with the loan, the NPA and Manual NPA ticks, the event and the date (`lending/loan_management/doctype/loan/loan.py:1738`). The **Days Past Due Log** keeps a daily figure (see `bridge.BR-LMS-190`) from which a grade could be worked out. The grade on the Loan is written straight to the database without updating the modified time (`lending/loan_management/doctype/loan/loan.py:1662-1670`), so the change does not appear in the Loan's Version log.

## Match or gap, and why

This is **partly covered**, and the verification confirmed the verdict (J4).

- In the test one loan had five grade moves (STD to SMA, SMA to SS, SS to DF, and back to STD). The Loan's Version log held only the booking entry, and the Loan NPA Log held two rows: the entry into NPA and the exit.
- The Days Past Due Log, from which grades could be rebuilt, is rewritten by back-dated payments (see `bridge.BR-LMS-190`).
- Neither log is submittable or tracks changes. The Loan NPA Log has every field editable and the System Manager can write and delete rows. The Days Past Due Log can be written and deleted by the System Manager and Loan Manager roles. In the test a row was changed through the API with no Version row and no activity entry.
- So a past class can be lost by editing or deleting a row, which the BRD forbids.

## What to do today

Export the Loan NPA Log and the grade of each loan at every month end to a file kept outside the system. Restrict the roles that can write or delete the two logs.

## Planned fix

Dev item D15 (classification history and override, sized medium) covers this row. The final report adds ND-14 and ND-15: a grade history record and append-only logs.
