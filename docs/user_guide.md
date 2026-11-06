# User guide: how to ask good questions

This guide is for the team that uses the Lending Assistant on the dev site. You need the role **Assistant User**. If you do not see the round chat button (bottom-right; tooltip 'Ask the Lending Assistant'), ask your admin for it.

## What to trust (read this first)

**End-to-end evaluation has not been run yet.** The labelling score (does every part of every answer carry the right source label), the red-team set (attempts to make it write, leak or ignore its rules) and a measured cost per user are planned as milestone M7, which is postponed. What exists today: automated tests of the guardrails (606 bench + 14 widget source tests at `c6990d3`, 2026-11-06), a code scanner, and a few small live checks with the real model. Those are not an accuracy figure.

Treat every answer as a draft from a colleague who reads fast. **`[General knowledge]` answers are a starting point, not a conclusion.** Check them.

Our analysis covers **103** of the BRD's requirements (Section 7) with a verified or code-read verdict. The other **220** requirement cards are "not analysed". For those the advisor says "Our analysis does not cover this." and then reasons from the live site, the code or general knowledge, each part labelled.

## 1. Open the panel

Click the round chat button (bottom-right of any Desk page; tooltip 'Ask the Lending Assistant'). The panel is called **Lending Assistant**. Buttons at the top: **History**, **New conversation**, and **x** to close. Esc also closes it (unless a Frappe dialog is open). Type in the box and press Enter to send (Shift+Enter makes a new line). Questions can be up to 4,000 characters.

## 2. The context chip

Under the title you see a chip with the page you are on, for example `Loan ACC-LOAN-2026-00050` or `Loan list`. The advisor uses it to know what "this loan" means. Click the **x** on the chip to ask without that context. It comes back when you go to another page.

Use the chip for "this record" questions: open the Loan first, then ask.

## 3. Depth and Deep analysis

Under the conversation there are two controls:

| Control | What it does | Use it when |
|---|---|---|
| **Depth: Business** | Plain banking words; screens as the user sees them; no code detail. | You want to understand the rule or the process. |
| **Depth: Technical** | Doctypes, field names, jobs, file and line references; no basic banking explanations. | You are a developer tracing behaviour. |
| **Depth: Both** (default) | Business view first, then how Frappe Lending does it, side by side. | Bridge questions, or when unsure. |
| **Deep analysis (slower, larger model)** | Uses the larger model, up to 12 tool rounds, compares BRD text, cards and code, and states its confidence. Can take up to about 100 seconds and costs several times more. | A hard bridge question, or a conclusion you may want to save. Not for quick look-ups. |

Both settings are remembered in your browser.

## 4. The six kinds of question, with examples

Treat the wording as a template. Answers vary.

### Business: banking terms, BRD rules

1. "What is DPD (days past due) and how does it drive a loan's grade and NPA status?" Related: BR-LMS-190 (count days late every day; covered) and BR-LMS-191 (give each loan a health grade; partly covered). In Frappe the history is the **Days Past Due Log** (Lending > Loan Management > DPD Log).
2. "What does BR-LMS-150 ask for, in plain words, and why does the bank care?" It is about choosing which loans to reprice (BRD 7.6).

### System: how Frappe works

3. "Which job raises the EMI bills in Frappe Lending, and which doctypes does it create?" (Technical.) Expect **Process Loan Demand** and **Loan Demand** (Lending > Loan Management > Loan Demand). Process Loan Demand has no sidebar entry; use the search bar.
4. "Where in the code does the daily interest accrual start, and what runs it?" Expect **Process Loan Interest Accrual** and **Loan Interest Accrual** (Lending > Loan Management > Loan Interest Accrual), with `[Code]` references.

### Bridge: a BR requirement against Frappe

5. "BR-LMS-162 versus Frappe: match or gap, and why?" The analysis rates it a **gap**: Reference Number on **Loan Repayment** is not unique (planned item D12).
6. "BR-LMS-113 on fees and charges: the coverage analysis said covered. What did the test show?" The verified verdict is **partly covered**. The product can name a fee, but its percentage, amount and basis are not used (Lending > Setup > Loan Product).

### How-to: exact steps on a screen

7. "How do I submit a repayment and see how it was applied to interest and principal?" Menu: Lending > Loan Management > Loan Repayment.
8. "A Process Loan Demand run failed for some loans. How do I find out and re-run it?" Related: BR-LMS-223 and BR-LMS-135 (both partly covered). Look in the Error Log (use the search bar).

If you cannot do the step, the answer starts with a notice such as: "⚠ You don't have permission to **Submit** a **Loan Repayment**. The role *Loan Manager* can."

### This record: the loan you are looking at

Open the Loan first so the chip shows it.

9. "What is due on this loan right now?" It reads the billed demands (Loan Demand rows) with your own permissions. It says it does **not** include interest that has accrued but is not billed yet, nor future interest.
10. "What is this loan's status and days past due, and what does that mean?" (Doctype Loan; Lending > Loan Management > Loan.)

If the loan does not exist **or** you may not read it, you get the same reply: "I can't find a record with that ID that you have access to."

### Beyond the analysis: what we have not analysed

11. "BR-GOV-002 says every outgoing instruction needs a unique key. How would Frappe Lending deal with that?" The advisor opens with "Our analysis does not cover this." and then reasons with labels.
12. "How do other banks usually reprice floating-rate loans?" Expect `[General knowledge]` with a confidence word. Verify before relying on it.

## 5. Reading an answer

Each part of an answer should start with a coloured label. If labels are missing, the answer ends with a warning.

| Label | Means | How far to trust it |
|---|---|---|
| `[Analysis]` | From the team's approved knowledge cards (BRD text, verified test results). | Highest. Cites a BRD section or BR id. |
| `[Team finding]` | A conclusion a colleague saved. Shown as `(draft, name, date)` or `(confirmed, name, date)`. | A team note, not proof. The advisor is told to show a conflict with an `[Analysis]` verdict, never to prefer the finding. |
| `[Live site]` | Meta or records read from this site, with your permissions. | Accurate for this site now. |
| `[Code]` | Source code, with a file and line. | Accurate for the installed version. |
| `[General knowledge]` | The model's own knowledge, not checked against our analysis or this site. | **A starting point, not a conclusion.** Should come with a confidence word (high, medium or low) and what to verify; if it doesn't, treat it as low. |
| `[Web]` | A cited web page (only when Web search is on). | Check the page. |

Other things you may see:

- "Our analysis does not cover this." at the start: the requirement has not been analysed.
- A **⚠** line: a permission notice.
- "Partial answer: a limit was reached before it was finished." and "(I reached my limit for this question before I could finish.)": the advisor ran out of rounds or time. Ask a narrower question.
- "Source labels are missing in this reply; treat it as unverified.": the advisor could not label it properly (after one repair attempt when there was time).
- "(This answer was cut short because it reached the length limit. Ask me to continue if you need the rest.)": ask it to continue.

Use the thumbs up and thumbs down under an answer, and **Comment** to say why. This helps the admin.

## 6. Team findings

When an answer reaches a new and useful conclusion, a **Save as finding** button appears under it. Nothing is saved until you click it.

- A dialog lets you edit the Title (up to 140 characters) and Summary (up to 4,000). The question, sources, cards used and Lending version come from the answer and can never be changed. The BR ids and doctypes can be corrected later in the form. Click **Save**. The answer then shows "Saved as AF-00001".
- A new finding is **Draft**. Only a person with **Assistant Reviewer** can set it to **Confirmed**.
- If a reviewer-confirmed finding is edited by someone who is not a reviewer, it goes back to Draft.
- You can edit and delete your own findings. Reviewers can edit and delete all.
- A finding shows an orange **check again** banner when a card it relied on changed or was removed, or when the Lending version changed.
- If a finding disagrees with an `[Analysis]` bridge verdict, the advisor shows both and calls it a conflict. It does not pick the finding.
- Open findings with the search bar: **Assistant Finding**. In the list, **Export to Markdown** downloads the selected rows (or the current filter, at most 200) as a `.md` file.
- You can save at most 20 findings per window (one hour by default).

## 7. What it will refuse

- **Writes.** It cannot write: the code blocks every create, change, submit, cancel and delete. If you ask, it explains the steps instead ("I can only read. Here's how you would do it:").
- **Other people's data.** It reads with your permissions. A record you may not see looks the same as one that does not exist.
- **Personal data fields.** A list of fields (phone, email, tax id, addresses, bank accounts) is never sent to the model, and password fields are always dropped.
- **Secrets.** It never has the API key or any password (they are not sent to the model). It is told not to reveal its instructions; this has not been tested yet (M7).
- **Files outside the allowed apps.** The code reader refuses everything else ("That path is not available to the code reader.").
- It may reply "I can't help with that request." when the model declines.

## 8. Limits

- Up to 8 tool rounds per answer (12 with Deep analysis), 20 rows per list, about 8,000 characters per tool result, 200 lines per code read.
- The advisor remembers your last 4 exchanges in a conversation.
- By default you can ask 30 questions per hour. Over that: "You have asked too many questions for now. Please try again later."
- If the advisor takes longer than 130 seconds, the panel says "The advisor took too long. The answer may still have been saved: open History."

## 9. History

**History** lists your latest 30 conversations. Click one to reopen it (up to 50 messages are shown). **New conversation** starts a fresh one. You see only your own conversations.

## 10. Good habits

- Name the BR id or the screen.
- Ask for the *why*, not only the verdict.
- Open the record first for "this record" questions.
- Use Business depth to learn a rule, Technical depth to find code.
- Check every `[General knowledge]` part.
- Save a finding only if you would defend it in front of the senior.
- Costs (estimates from the small live checks, not a measured cost per user): a normal question cost from under one cent to about six cents (M4b smoke run 5: USD 0.003-0.028; M5 live check: about 0.05, an upper bound; M6 live check: USD 0.19 for 3 asks, about 0.06 each). A Deep analysis question cost about USD 0.18-0.21 (M4b smoke run 5, M5). Long questions with many tool rounds cost more.
