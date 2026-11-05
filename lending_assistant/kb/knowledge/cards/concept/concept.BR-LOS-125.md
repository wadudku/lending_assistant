---
id: concept.BR-LOS-125
type: concept
title: "If the bank's system is down, rows wait and retry; a timeout is never a pass"
summary: "When the core system or the automation session is unavailable, affected rows are held pending and retried on a schedule; the partner is told validation is in progress, need not re-upload, and a timeout is never recorded as a pass."
br_ids: [BR-LOS-125]
brd_section: 6.3
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-125"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p32"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-003"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
related: [bridge.BR-LOS-125, concept.BR-GOV-003, glossary.cbs, glossary.rpa]
version: 1
status: approved
approved_by: Owner
---
**In short:** When the core system or the automation session is unavailable, affected rows are held pending and retried on a schedule; the partner is told validation is in progress, need not re-upload, and a timeout is never recorded as a pass.

## What the rule says

BR-LOS-125 (Must, BRD 6.3, PDF page 32) says where the CBS is unreachable, an automation session cannot be established, or the outcome indicates unavailability rather than a business result, affected rows are held pending and re-attempted automatically on a configurable schedule. The partner sees a clear message stating that validation is in progress and is not required to re-upload the file. A timeout is never recorded as a validation pass. This is an origination rule (the LOS side of the BRD), not a servicing rule.

## Why the bank wants it

The BRD doesn't state the reason in the row. It fits the guiding principle that the platform does not infer an outcome after a failed call (BR-GOV-003, PDF page 19) and the 6.3 introduction, which calls this the single most important control (PDF page 32).

## Example

The core system is down for two hours. The rows of a batch stay “pending”, the partner sees “Validation in progress”, and the platform tries again on its schedule. No row is marked as passed because the call timed out.

## Terms to know

- **Unavailability:** the system could not be reached, so there is no business answer.
- **Pending:** waiting for a result.
- **Business result:** a real answer such as “account closed”.
- **Retry schedule:** the times at which the platform tries again.
