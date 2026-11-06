# Lending Assistant

An AI advisor inside the Frappe Lending desk. It helps a small team understand two things together: the NRB Bank BRD (the business) and Frappe Lending (the system). It explains what the bank needs, how Frappe does it, where the two match, where they differ, and why.

It is built for a **dev site** with test data. Not for the bank's staff, and not for production.

## What it is, and what it is not

It is:

- A chat panel on every Desk page. Open it with the **Ask** button. It knows which page or record you are on.
- A reader. It answers six kinds of question: business, system, bridge (a BR requirement against Frappe), how-to, "this record", and "beyond the analysis".
- Honest about its sources. Every part of an answer carries a label: `[Analysis]`, `[Team finding]`, `[Live site]`, `[Code]`, `[General knowledge]` or `[Web]`.
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
| frappe | 16.34.0 (branch `version-16`) |
| erpnext | 16.35.0 (branch `version-16`) |
| lending | 16.5.1 (branch `version-16`) |
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

`bench get-app` does not fetch `required_apps` by itself, so get ERPNext and Lending first, then this app:

```bash
bench get-app erpnext --branch version-16
bench get-app lending --branch version-16
bench get-app https://github.com/wadudku/lending_assistant.git --branch main
```

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

A new ERPNext site opens the Setup Wizard on first login. Complete it: language, country, currency and time zone; your name, email and password; a company name and abbreviation; a chart of accounts; the financial year dates. A test company is enough. It is not confirmed whether the Ask button works before the wizard is finished (Desk starts the panel on its normal start-up event whether or not the wizard is done), so finish the wizard first.

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

A clean result ends with `validate: 0 finding(s), 5 note(s), 941 cards checked`. The 5 notes are menu paths outside the Lending sidebar, which are not checked. The card count changes when the knowledge changes. What matters is `0 finding(s)`.

A `FINDING` line means a card names a doctype, field label, Select option, Lending menu path or code file that this site does not have. This usually happens on a different Lending version. The check reads only the cards' front matter, not their text. Nothing is written.

### 9. Ask a first question

Log in as a user with Assistant User and click **Ask**. Leave Depth on Both and ask:

> What is DPD (days past due) and why does the bank care?

You should see an answer with an `[Analysis]` badge, BR ids such as BR-LMS-190 and BR-LMS-191, thumbs up and thumbs down buttons, and no red error line. If you see "The assistant is turned off.", Enabled is off. "The advisor has no API key yet." means the key is empty. See `docs/admin_runbook.md`.

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
- Then commit the app and run `kb.validate.run`.
- A changed or removed card makes team findings that used it show "check again".

## Tests and the scan

The tests write to the site, so run them on a dev site only:

```bash
bench --site <site> set-config allow_tests true
bench --site <site> run-tests --app lending_assistant
```

The widget source tests and the guardrail scan do not need a site:

```bash
cd apps/lending_assistant
../../env/bin/python -m unittest lending_assistant.tests.test_chat_widget_source
../../env/bin/python scripts/guard_scan.py --check-allowlist
```

The scan fails on any use of a banned API (writes, `ignore_permissions`, raw SQL and so on) that is not marked `# AST-ALLOWED`.

## More

- `docs/user_guide.md`: how to ask good questions.
- `docs/admin_runbook.md`: daily checks, switches, keys, audit, troubleshooting.
