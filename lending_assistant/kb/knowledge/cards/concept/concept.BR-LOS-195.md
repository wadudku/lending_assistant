---
id: concept.BR-LOS-195
type: concept
title: "If the bureau cannot be reached the application waits, and a timeout never counts as a pass"
summary: "When the bureau or the designated host is unavailable the application holds and retries automatically with a clear message to the officer, and a timeout or transport error is never read as a pass."
br_ids: [BR-LOS-195]
brd_section: 6.8
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-LOS-195"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p42"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#6.8"
related: [bridge.BR-LOS-195, concept.BR-LOS-190, brd_section.6.7.2, glossary.cib]
version: 1
status: approved
approved_by: Owner
---
**In short:** When the bureau or the designated host is unavailable the application holds and retries automatically with a clear message to the officer, and a timeout or transport error is never read as a pass.

## What the rule says

BR-LOS-195 (Must, BRD 6.8, PDF page 42) says that where the bureau or the designated host is unavailable the application "shall hold rather than fail, with automatic retry and clear officer messaging". The last sentence reads "A timeout or transport error shall never be interpreted as a pass." So an outage does not fail the application and does not pass it. It waits and retries, and the officer is told. BRD 6.7.2 (PDF page 40) separately says credit bureau verification shall not be performed offline under any circumstance.

## Why the bank wants it

The BRD doesn't say why; the usual reason is that an unreachable bureau says nothing about the applicant, so failing the application would be unfair to them and passing it would skip the check.

## Example

The designated host cannot be reached when an application is sent for bureau verification. The application holds, the system retries by itself, and the officer sees a clear message. When the bureau answers, the result is judged as normal. The timeout is never treated as a pass.

## Terms to know

- **Hold:** the application waits rather than failing, as the BRD says.
- **Transport error:** the BRD's term, used with timeout; it does not define it further.
