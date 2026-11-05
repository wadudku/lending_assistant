---
id: devitem.D12
type: devitem
title: D12 Payment confirmation and receipts
summary: "A planned add-on to Frappe Lending that confirms payments with the CBS, blocks duplicate references and holds unmatched money in an owned queue."
br_ids: [BR-LMS-161, BR-LMS-162, BR-LMS-167]
brd_section: 7.7
doctypes: [Loan Repayment, Bank Transaction]
dev_items: [D12]
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/NRB_LMS_vs_Frappe_Lending_Coverage_Analysis.md#D12"
  - "sources/verification/FINAL_REPORT.md#D12"
  - "sources/NRB_LMS_Team_Discussion_Summary.md#4.-proposed-development-custom-app-no-core-changes"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p51"
  - "sources/verification/FINAL_REPORT.md#revised-suggested-order"
related: [bridge.BR-LMS-161, bridge.BR-LMS-162, bridge.BR-LMS-167, devitem.D13]
version: 1
status: approved
approved_by: Owner
---
**In short:** A planned add-on to Frappe Lending that confirms payments with the CBS, blocks duplicate references and holds unmatched money in an owned queue.

## What we plan to build

D12 adds three things in a custom app, without changing Frappe Lending itself. First, a CBS status field on a repayment with the values Pending, Confirmed and Failed, and a rule that a repayment is submitted automatically only when it is Confirmed. Second, a uniqueness check on the Reference Number, together with the channel, across submitted repayments. Third, an Unidentified Receipt queue with an owner, an age and a reason for each attribution.

## The gap it closes

Today a payment can be applied before the CBS confirms it, the same reference can be applied twice, and money that cannot be matched has no owner. In the live test the same reference was accepted twice, both payments posted, and a duplicate Pre Payment also rescheduled the loan.

## Requirements it closes

BR-LMS-161 (pending and confirmed), BR-LMS-162 (each payment once) and BR-LMS-167 (unmatched-receipts queue). See `bridge.BR-LMS-161`, `bridge.BR-LMS-162` and `bridge.BR-LMS-167`.

## How, size and dependencies

Size: M (one to three weeks), unchanged by verification. The verification added ND-6: the duplicate guard must also block duplicate Pre Payment and Advance Payment, because those create a restructure (a change of the loan's terms and schedule). Frappe Lending 16.5.1 has no action to create a repayment from a bank transaction, so the queue has to be built. The final design waits on NRB's answers to the BRD's open items in section 7.7.2, which the BRD groups as its own dependency D19 (not this team's item D19). The analysis puts D12 in the first group to build, with D1, D2 and D8, and the final report keeps it in the foundation pack (Pack B).
