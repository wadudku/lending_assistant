# Lending Assistant

An AI advisor inside the Frappe Lending desk. It helps a small team understand two things together: the NRB Bank BRD (the business) and Frappe Lending (the system). It explains what the bank needs, how Frappe does it, where the two match, where they differ, and why.

It is built for a **dev site** with test data. Not for the bank's staff, and not for production.

## What it is, and what it is not

It is:

- A chat panel on every Desk page. Open it with the **Ask** button. It knows which page or record you are on.
- A reader. It answers six kinds of question: business, system, bridge (a BR requirement against Frappe), how-to, "this record", and "beyond the analysis".
- Honest about its sources. It is told to label every part of an answer (`[Analysis]`, `[Team finding]`, `[Live site]`, `[Code]`, `[General knowledge]` or `[Web]`), and a code check adds a warning when labels for the sources it used are missing.
- A shared memory. A user can save a useful conclusion as a **team finding**. Only a click saves it; the advisor never saves by itself.
- Logged. Every question and answer is stored for audit.

It is not:

- Anything that writes business data. It only reads. Its only writes are its own audit log and the findings a user saves.
- A tool for bank clients or portal users.
- Self-learning, streaming, embeddings, Bangla, or a production deployment.

## Status and limits

**End-to-end evaluation has not been run yet.** The labelling score (does every part of every answer carry the right source label), the red-team set (attempts to make it write, leak or ignore its rules) and a measured cost per user are planned as milestone M7, which is postponed. What exists today is the full test suite and the code scan (both pass; 606 bench + 14 widget source tests at `c6990d3`, 2026-11-06) and a few small live checks with the real model. Those are not an accuracy figure.

Treat every answer as a draft from a colleague who reads fast. **`[General knowledge]` answers are a starting point, not a conclusion.** Check them. Look for the confidence word (high, medium, low) and the "what to verify" line.

The team's analysis covers **103** BRD requirements (Section 7) with a verified or code-read verdict. The other 220 requirement cards are "not analysed". For those the advisor says "Our analysis does not cover this." and then reasons from the live site, the code or general knowledge, with labels.

Limits per answer: 8 tool rounds (12 with Deep analysis), 20 rows per list, about 8,000 characters per tool result, 200 lines per code read, a time budget of 90 seconds (100 for Deep analysis).

Known gaps:

- `Log retention (days)` is stored but nothing deletes old logs yet.
- A fresh install starts with `Default model effort = high` (see Settings below).
- Web search has not been tried live.
- There is no Desk shortcut for the settings, conversations, messages or findings. Open them from the search bar.

Costs are **estimates** taken from the small live checks (see "Cost" below). There is no measured cost per user.

## Requirements

Use the same version line as the dev site (`bench version`):

| App | Version |
|---|---|
| frappe | 16.34.0 (tag `v16.34.0`) |
| erpnext | 16.35.0 (tag `v16.35.0`) |
| lending | 16.5.1 (tag `v16.5.1`) |
| lending_assistant | 0.0.1 (branch `main`) |

The shipped knowledge was verified on Lending **16.5.1**. On another Lending version, expect drift findings (step 8).

Also needed:

- Python 3.14 and Node 24 or newer (what Frappe 16 asks for).
- A MariaDB server and its root password (bench asks for it; never put it in a file).
- Redis (`bench start` runs it). Rate limits use it.
- The `anthropic` package. `bench get-app` installs it from `pyproject.toml` (`anthropic~=1.17`). Do not `pip install` into the system Python.
- A Claude API key, for you to enter in the UI (step 6).

## Install on a new site

Run every command from `frappe-bench/`. Replace `<site>` with the site name.

### 1. Get the apps

**On a bench that already has these apps, skip this step.** Check with `bench version`. If `bench get-app` asks "A directory for the application '<app>' already exists. Do you want to continue and overwrite it?", answer **No**. Answering yes moves the existing app folder, and any unpushed work in it, to `archived/apps/`.

On a new machine, first create a bench: `bench init --frappe-branch v16.34.0 frappe-bench && cd frappe-bench`.

`bench get-app` does not fetch `required_apps` by itself, so get ERPNext and Lending first, then this app:

```bash
bench get-app erpnext --branch v16.35.0
bench get-app lending --branch v16.5.1
bench get-app https://github.com/wadudku/lending_assistant.git --branch main
```

These are tags, and git checks them out detached. Using `version-16` gets the newest 16.x. That works, but the shipped knowledge was checked on 16.5.1, so expect drift findings and "check again" on findings.

The repository is public, so no key is needed. If you prefer SSH, use `git@github.com:wadudku/lending_assistant.git` instead of the https address. That needs an SSH key on your GitHub account.

One-line alternative: add `--resolve-deps` to the last command and bench works out the required apps itself. It was not tried for this guide.

### 2. Create the site

```bash
bench new-site <site>
```

It asks for the MariaDB root password (`MySQL root password:`) and for an Administrator password. Type them at the prompt. Never write either into a file.

To open the site in a browser on the same machine, add `127.0.0.1 <site>` to `/etc/hosts` (or run `bench add-to-hosts`), then use `http://<site>:8000/` after `bench start`.

### 3. Install the apps, in this order

```bash
bench --site <site> install-app erpnext
bench --site <site> install-app lending
bench --site <site> install-app lending_assistant
```

Installing `lending_assistant` would install the other two first anyway; the explicit order just makes problems easier to see.

### 4. Migrate, build, restart

```bash
bench --site <site> migrate
bench build --app lending_assistant
```

Then restart. In development, stop `bench start` (Ctrl-C) and start it again. In production, run `bench restart`.

What the install created for you:

- **Roles:** `Assistant User` and `Assistant Reviewer` (from the app's fixtures).
- **Doctypes:** `Assistant Settings` (one record), `Assistant Conversation`, `Assistant Message`, `Assistant Finding`, and three small child tables for the lists in Settings.
- **Default settings** (`after_install`, which only fills empty tables and never overwrites an edit):
  - the doctype allowlist: 20 Lending doctypes (Loan, Loan Product, Loan Application, Loan Disbursement, Loan Repayment, Loan Demand, Loan Interest Accrual, Loan Repayment Schedule, Loan Restructure, Loan Write Off, Loan Security, Loan Security Assignment, Loan Security Shortfall, Loan Freeze Log, Loan NPA Log, Days Past Due Log, Loan Partner, Loan Category, Loan Classification, Customer);
  - the code app allowlist: `lending`, `erpnext`, `frappe`;
  - the **never send to model** list: 15 personal contact, identity and bank fields (for example `Customer.mobile_no`, `Customer.email_id`, `Loan Disbursement.bank_account`). Password fields are always dropped as well.
- **Switches:** all four are off.
- The data patches in `patches.txt` do not run on a fresh install. They matter only for sites that already had the app.

### 5. Finish ERPNext's Setup Wizard

Desk sends every page to the wizard until it is finished, so the advisor can't be used before then. Complete it: language, country, currency and time zone; your name, email and password; a company name and abbreviation; a chart of accounts; the financial year dates. A test company is enough.

### 6. Settings

Open **Assistant Settings** from the search bar (System Manager only). The table lists every field.

| Field (label) | Default | Meaning |
|---|---|---|
| Enabled | off | Master switch. Off: everyone gets "The assistant is turned off." |
| Live data | off | Lets tools read live site records (lists, one record, what is due) using the asking user's own permissions. |
| Code reader | off | Lets the advisor search and read code under the allowlisted apps. |
| Web search | off | Lets the model use the Claude web search tool (at most 3 uses per answer). Not tried live. |
| API key | empty | The Claude API key. A Password field: type it **in this form only**, never in a file. Readable by System Manager only. |
| Default model | `claude-sonnet-5-5` | Model for normal questions. |
| Deep analysis model | `claude-opus-5-5` | Model when the user ticks Deep analysis. |
| Default model effort | `high` on a fresh install; `medium` on the dev site | How hard the default model thinks. A fresh install starts at `high` because that is the doctype's built-in default and the seeding only fills blanks. The dev site is `medium` because a patch changed it. **Recommended: set it to `medium`.** |
| Deep analysis effort | `medium` | Same, for the Deep model. |
| Max tokens | 16000 | Longest answer the model may write. |
| Requests per user per window | 30 | Questions one user may ask per window. |
| Window (seconds) | 3600 | The window for that limit. |
| Log retention (days) | 180 | Stored only. Nothing deletes old logs yet. |
| Doctype allowlist | 20 doctypes | The only doctypes the live-data tools may read. |
| Code app allowlist | lending, erpnext, frappe | The only apps the code reader may read. |
| Never send to model | 15 fields | Fields that are never sent to the model. |

Other limits that are not in Settings: 120 questions per IP address per hour, 60 feedback clicks and 20 finding saves per user per window.

**API key and spend limit.** Both are set by the admin. Type the key into the Password field and save. In the Anthropic Console, set a monthly spend limit on the workspace or key **before** you turn Enabled on. Without a key the panel answers "The advisor has no API key yet."

Switch **Live data** and **Code reader** on to get "this record" and code answers. Leave **Web search** off unless you need it. Do not point the advisor at a site with real bank data without the bank's approval; if you ever do, turn Live data and Web search off first.

### 7. Roles and first users

- **Assistant User:** may use the panel. The Ask button only appears for users with this role.
- **Assistant Reviewer:** may confirm findings. It does **not** give panel access by itself, so **give a reviewer both roles**.
- Users also need the normal Lending roles for what they want to see. The advisor reads with the user's own permissions and says so when the user cannot do something.

The `ast-*` users in this project's notes (a senior with both assistant roles and Loan Manager; a developer with Assistant User; a limited user with Loan Reporter and a Loan Product restriction; a user with no assistant role) are **dev-site examples only**. They are not shipped. Create real users on your site.

### 8. Check the shipped knowledge

The knowledge cards and their index ship inside the app (`lending_assistant/kb/knowledge/`) and are read from files. A fresh site needs **no ingest** and nothing from the build repo. Check them against this site:

```bash
bench --site <site> execute lending_assistant.kb.validate.run
```

A clean result prints `validate: 0 finding(s), 5 note(s), 941 cards checked`, then the same result as JSON (`"findings": []`). The 5 notes are menu paths outside the Lending sidebar, which are not checked. The card count changes when the knowledge changes. What matters is `0 finding(s)`.

A `FINDING` line means a card names a doctype, field label, Select option, Lending menu path or code file that this site does not have. This usually happens on a different Lending version. The check reads only the cards' front matter, not their text. Nothing is written.

### 9. Ask a first question

Log in as a user with Assistant User and click **Ask**. Leave Depth on Both and ask:

> What is DPD (days past due) and why does the bank care?

You should see an answer with an `[Analysis]` badge, BR ids such as BR-LMS-190 and BR-LMS-191, thumbs up and thumbs down buttons, and no red error line. If you see "The assistant is turned off.", Enabled is off. "The advisor has no API key yet." means the key is empty. See `docs/admin_runbook.md`.

For more questions to try, see "Questions to start with" below.

## Questions to start with

These are good first questions for the team. The answers have not been evaluated yet (M7, #173), so treat each "Expect" column as what the knowledge says, not as a promise of what the advisor will write. For more examples, see `docs/user_guide.md`.

### Ten BRD questions

| # | Question | Why it matters | Expect |
|---|---|---|---|
| 1 | Does Frappe Lending apply each repayment only once? Look at BR-LMS-162. | A payment that is posted twice or lost breaks the borrower's balance and the bank's books. | Gap (Reference Number on Loan Repayment is not unique) · [Analysis] |
| 2 | Why is BR-LMS-162 a gap, and what would we build? | The team has to plan the custom work before go-live. | Gap; test accepted one reference twice, planned item D12 · [Analysis] |
| 3 | In what order does a payment pay off interest, principal and charges (BR-LMS-164)? | The order decides what the borrower still owes and when a loan turns overdue. | Partly covered; split is shown, but an offset order using Interest never pays interest · [Analysis] |
| 4 | How does Frappe handle interest for odd days, the broken period (BR-LMS-142)? | The first and last instalment often cover part of a month, and the bank must charge the right interest. | Covered · [Analysis] |
| 5 | How does a loan get its health grade and become an NPA (BR-LMS-191)? | The grade drives provisioning, income recognition and reports to Bangladesh Bank. | Partly covered; bands on Company, only override is the Manual NPA tick, planned item D15 · [Analysis] |
| 6 | Why can't Frappe Lending set money aside for expected losses (BR-LMS-193)? | Provisioning is a regulatory duty and affects the bank's profit. | Gap; the provision rate table exists but nothing reads it, planned item D14 · [Analysis] |
| 7 | How is unpaid interest held in suspense (BR-LMS-194)? | Interest that is not being paid must not be counted as income. | Partly covered; moved to suspense on NPA, released only on upgrade, settlement or write-off · [Analysis] |
| 8 | Why is there a gap on limits for how much can be restructured (BR-LMS-184)? | Bangladesh Bank limits restructuring, so the bank must stop loans being rescheduled again and again. | Gap; the monthly limit job selected no loan in the test and nothing checks a limit on approval · [Analysis] |
| 9 | Can Frappe Lending send each bill to the CBS and keep the CBS journal number (BR-LMS-134)? | The CBS is the bank's book of record, so a bill without its journal number cannot be proved. | Gap that needs the CBS link; no code or field for it, planned item D13 · [Analysis] |
| 10 | What does BR-LMS-250 ask for on the Credit Information Bureau extract, and what does the bank send them? | The monthly CIB return is a legal duty. | "Our analysis does not cover this." · [General knowledge] with a confidence word |

### Ten technical questions

Questions marked **Code reader** need the Code reader switch on; **Live data** needs the Live data switch on (see step 6).

| # | Question | Why it matters | Expect |
|---|---|---|---|
| 1 | Which jobs run every day in Lending, and what does each one do? (Code reader) | A developer needs to know what runs overnight before changing data. | The `daily_long` list in `lending/hooks.py` (line 187): interest accrual, loan demands, security shortfall, classification, accounting · [Code] |
| 2 | In what order is a repayment applied to interest, principal and charges, and where is that set? (Code reader) | The order is configuration, so the developer must know where to change it. | The Collection Offset Sequence fields on **Loan Product** and **Company**; `get_allocation_order` in `loan_repayment.py` (line 2525) · [Code] [Live site] |
| 3 | How does a loan restructure work in Frappe Lending, step by step? | A restructure changes a live loan's plan, so the steps must be right. | **Loan Restructure** doctype; BR-LMS-182 partly covered, the loan is re-aged to zero days past due · [Analysis] [Live site] |
| 4 | What accounting entries does a write-off post? (Code reader) | Finance must be able to check the write-off against the ledger. | `make_gl_entries` of **Loan Write Off** in `loan_write_off.py` (line 211) · [Code] |
| 5 | How does the security shortfall check work, and which job runs it? (Code reader) | A shortfall can force a call for more collateral. | **Process Loan Security Shortfall** and **Loan Security Shortfall**, run by `create_process_loan_security_shortfall` in `hooks.py` (line 190) · [Code] |
| 6 | What are the possible status values of a Loan? | Reports and filters depend on the exact status words. | Draft, Sanctioned, Partially Disbursed, Disbursed, Active, Loan Closure Requested, Closed, Written Off, Settled · [Live site] |
| 7 | A repayment was posted with a wrong date. How do I repost it? | A back-dated fix must rebuild interest and demands from that date. | **Loan Repayment Repost** doctype · [Live site] [Analysis] (BR-LMS-169, covered; no approval step) |
| 8 | What is due on this loan right now? (Live data; open the Loan first) | It shows what the borrower owes today, from the billed demands. | The billed **Loan Demand** rows, with a note that accrued but unbilled interest is not included · [Live site] |
| 9 | Who can submit a Loan Repayment? (ask as a user without the role) | A developer needs to know which role to give a new team member. | A ⚠ notice that the role *Loan Manager* can; System Manager can too · [Live site] |
| 10 | What does `allocate_amount_against_demands` do in `loan_repayment.py`? (Code reader) | This is the heart of how a payment is split, so developers read it before any change. | The function at line 1814 of `loan_repayment.py`, with its allocation order · [Code] |

## Clean up a throwaway site

```bash
bench drop-site <site>
```

- It asks for the MariaDB root password.
- It takes a backup first by default (`--no-backup` skips it).
- The backup is made inside the site's own folder and then the whole site folder is moved to `frappe-bench/archived/sites/<site>/`. So the backup is in `frappe-bench/archived/sites/<site>/private/backups/`.
- That folder also holds the site's configuration and encryption key, and the database dump holds the encrypted API key. After a throwaway test, delete the archived folder yourself, remove the `/etc/hosts` line, and revoke or rotate the API key you used.

## Update an existing site

```bash
bench --site <site> backup --with-files
git -C apps/lending_assistant pull
bench setup requirements --python   # only if pyproject.toml dependencies changed
bench --site <site> migrate
bench build --app lending_assistant
```

Then restart, and run `kb.validate.run` again. The first time on a site that does not have the app yet, run `bench --site <site> install-app lending_assistant` before `migrate`. Restoring a backup is a decision for the site owner.

## Cost (estimates)

All figures are **estimates** from the small live checks, not a measured cost per user:

- About USD 0.31 for 8 asks in the M4b smoke run 5 (single normal asks USD 0.003 to 0.028; one Deep analysis ask USD 0.178). Source: `build/reports/M4b_smoke_run5.md` in the build repo.
- About USD 0.42 for 5 asks in the M5 live check (about USD 0.05 per normal ask and 0.21 for the Deep ask; an upper bound because prompt-cache discounts were not applied). Source: `build/reports/M5_report.md`.
- USD 0.19 for 3 asks in the M6 live check. Source: DECISIONS #169 in the build repo.

Deep analysis costs several times a normal ask. Set the provider spend limit.

## Roles in short

| Role | Can |
|---|---|
| Assistant User | Use the panel; read all team findings; edit and delete their own findings; read their own conversations and messages. |
| Assistant Reviewer | Confirm, edit and delete any finding (also needs Assistant User for the panel). |
| System Manager | Edit Assistant Settings; read and delete all conversations and messages; read findings. |

## Maintainers only: changing the knowledge

A fresh install never needs this.

- Cards are compiled and approved in a **separate build repo** (it has no remote). Its tool is `python3 tools/kb_compile.py` with `brd-text`, `extract`, `check`, `drift`, `index`, `approve-status`, `fmt` or `all`; approvals are in `knowledge/approvals.yaml`. The build repo's `sources/` folder is not shipped.
- Copy the approved cards into the app:

  ```bash
  bench --site <site> execute lending_assistant.kb.ingest.run \
      --kwargs "{'source': '<BUILD_DIR>/knowledge', 'commit': '<git rev-parse HEAD of the build repo>'}"
  ```

  It copies only approved cards, writes only `lending_assistant/kb/knowledge/` and `lending_assistant/public/kb_img/`, and stops without writing anything if the source is not fit. A second identical run reports new 0, changed 0, removed 0.
- Then restart (`bench restart`, or stop and start `bench start`) so the workers load the new cards.
- Then commit the app and run `kb.validate.run`.
- A changed or removed card makes team findings that used it show "check again".

## Tests and the scan

The tests write to the site, so run them on a dev site only:

```bash
bench --site <site> set-config allow_tests true
bench --site <site> run-tests --app lending_assistant
```

The widget source tests and the guardrail scan do not need a site (run them from `frappe-bench/`):

```bash
env/bin/python -m unittest lending_assistant.tests.test_chat_widget_source
env/bin/python apps/lending_assistant/scripts/guard_scan.py --check-allowlist
```

The scan fails on any use of a banned API (writes, `ignore_permissions`, raw SQL and so on) that is not marked `# AST-ALLOWED`.

## More

- `docs/user_guide.md`: how to ask good questions.
- `docs/admin_runbook.md`: daily checks, switches, keys, audit, troubleshooting.
