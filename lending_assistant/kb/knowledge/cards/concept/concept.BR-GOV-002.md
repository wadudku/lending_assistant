---
id: concept.BR-GOV-002
type: concept
title: Every outgoing instruction carries a unique key
summary: "Each financial instruction the platform sends carries a unique key, so that a repeat can never create a second loan, a second payout or a second posting."
br_ids: [BR-GOV-002]
brd_section: 3.4
doctypes: []
verdict: not_analysed
analysis_status: not_analysed
dev_items: []
lending_version: 16.5.1
code_refs: []
images: []
sources:
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-002"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p19"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-001"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-GOV-003"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#BR-INT-006"
  - "sources/brd/NRB_LOS_LMS_BRD_v1.0.txt#p62"
related: [bridge.BR-GOV-002, concept.BR-LMS-162, glossary.cbs]
version: 1
status: approved
approved_by: Owner
---
**In short:** Each financial instruction the platform sends carries a unique key, so that a repeat can never create a second loan, a second payout or a second posting.

## What the rule says

BR-GOV-002 (Must, BRD 3.4, PDF page 19) says every outbound financial instruction carries a platform-generated idempotency key. A repeat instruction with the same key never results in a duplicate loan account, a duplicate disbursement or a duplicate posting. BRD 3.4 lists it among the guiding principles that are binding on the design: a design that conflicts with one needs NRB's written approval.

## Why the bank wants it

The BRD gives the reason in three of its own rules. First, the platform never moves money itself: every financial action is an instruction to the Core Banking System (CBS) and a record of the reply (BR-GOV-001, PDF page 19). Second, the CBS has no native idempotency: it cannot recognise a repeated instruction by itself. So the platform must carry the control: a state query before execution, execution carrying the unique reference, a check after execution, and a blocking exception on any doubt. The BRD adds that this control is a risk mitigation and must not be presented as equal to true idempotency (BR-INT-006, PDF page 62). Third, when a call fails or times out, the platform must not guess the outcome. It queries the CBS for the definitive state before any retry, because "absence of a response is not a response" (BR-GOV-003, PDF page 19).

## Example

The platform sends "pay out 100,000 to Rahim" with the unique reference K-001, and the reply is lost. The platform does not simply send it again. It first asks the CBS for the state of K-001. If the CBS shows the payout was made, the platform records that result and sends nothing more. Only if the CBS confirms that the instruction was not executed does the platform retry, still with K-001. If the answer is unclear, the case is blocked as an exception for a person to resolve.

## Terms to know

- **Idempotency key:** a unique label that lets a repeat be recognised, so it has no second effect.
- **Outbound instruction:** a request the platform sends to another system, here the CBS.
- **State query:** asking the CBS what really happened before acting again.
- **Duplicate disbursement:** the same payout made twice.
- **CBS:** the bank's main system. See `glossary.cbs`.
