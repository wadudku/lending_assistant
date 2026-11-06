# Admin runbook

For the person who runs the Lending Assistant on the dev site. Commands run from `frappe-bench/`. Use bench commands only; no raw database commands.

Status: end-to-end evaluation (labelling score, red-team set, measured cost per user) has **not been run yet** (M7 postponed). Costs below are **estimates**.

## 1. Setup rules to remember

- Give a reviewer **both** roles, Assistant User and Assistant Reviewer. Assistant Reviewer alone gives no panel and the endpoints refuse the user.
- The API key goes into the **API key** field of **Assistant Settings** in the UI. Never in a file, `site_config.json` or an environment variable of the app.
- Set a monthly spend limit on the workspace or key in the Anthropic Console before turning **Enabled** on.
- Assistant Settings, Assistant Conversation, Assistant Message and Assistant Finding have no Desk shortcut. Open them from the search bar.

## 2. Daily checks

1. Open the **Assistant Message** list. Filter `Status` = `error` or `limited`. `ok` is a normal answer; `error` is a failed answer; `limited` is a partial answer (a limit was reached).
2. Read the logs. Each line has the user, an event and a few safe tokens, never a question, answer, key or request body:
   - `frappe-bench/sites/<site>/logs/lending_assistant_chat.log` (API errors, refusals, aborted answers)
   - `frappe-bench/sites/<site>/logs/lending_assistant_tools.log` (tool refusals and internal errors)
   - the same names also appear under `frappe-bench/logs/`.
3. Check usage against the spend limit in the Anthropic Console.
4. Check **Error Log** for new entries.
5. After any Frappe or Lending change, run the knowledge check (section 10).

## 3. Switches

Open **Assistant Settings**.

| Switch | Off means |
|---|---|
| Enabled | Every user gets "The assistant is turned off." (permission error, HTTP 403). |
| Live data | The tools that read records (`find_records`, `get_record`, `get_loan_dues`) refuse: "Live data is turned off in Assistant Settings." |
| Code reader | `search_code` and `read_code` refuse: "The code reader is turned off in Assistant Settings." |
| Web search | The model is not offered the web search tool. (Not tried live.) |

**Real data warning.** The dev site holds test data. If the advisor is ever used on a site with the bank's data, the question, the conversation, the cards, the filtered tool results and code excerpts go to the Claude API (and web search goes further). Get the bank's approval first, and turn **Live data** and **Web search** off until then.

## 4. Rotate the API key

1. In the Anthropic Console create the new key (with a spend limit).
2. In **Assistant Settings**, replace **API key** (it shows masked), save. No restart is needed.
3. Ask one test question as a user with Assistant User.
4. Revoke the old key in the Console.

If you test with scripts, use the environment variables `AST_ANTHROPIC_API_KEY` and `AST_TEST_PASSWORD`. Never set `ANTHROPIC_API_KEY`. Never print or commit a key.

## 5. Spend limits and rate limits

Provider side: the Console spend limit is your hard stop.

App side, counted per fixed window (the window is in Settings, default 3600 seconds):

| Bucket | Limit | Where set |
|---|---|---|
| Questions per user | 30 | Settings: Requests per user per window |
| Questions per client IP | 120 per hour | fixed in `api/chat.py` |
| Feedback clicks per user | 60 | fixed in `api/chat.py` |
| Finding saves per user | 20 | fixed in `api/findings.py` |

A user over a limit sees "You have asked too many questions for now. Please try again later." (HTTP 429). The counters expire when the window ends. To let a user continue sooner, raise the limit in Settings. Clearing a counter by hand is not documented here.

Estimates of cost, from the live checks (not a measured cost per user):

- About USD 0.31 for 8 asks, M4b smoke run 5 (normal asks USD 0.003 to 0.028; one Deep analysis ask USD 0.178).
- About USD 0.42 for 5 asks, M5 live check (upper bound).
- USD 0.19 for 3 asks, M6 live check (DECISIONS #169).

Long technical questions and Deep analysis cost the most. The request asks the provider's default fallback, so if the first model declines, a second model may be billed.

## 6. Reading the audit

**Assistant Conversation:** `user`, `title` (the first 100 characters of the first question, tags removed), `first_route`, `last_activity`, `message_count`.

**Assistant Message** (one per exchange, written on every path including errors): `conversation`, `user`, `status`, `depth`, `deep`, `model`, `route`, `route_doctype`, `route_docname`, `question`, `answer`, `roles` (the roles at that moment), `tokens_in`, `tokens_out`, `latency_ms`, `tool_calls`, `records_read`, `code_files_read`, `cards_used`, `web_sources`, `feedback`, `feedback_comment`, `finding_suggestion`, `finding`. All fields are read-only. `cards_used` lists every card the lookups returned (each tagged with how it was reached), not only the cards the model opened.

Who can see what: an Assistant User sees only their own conversations and messages. A System Manager can read and delete all. Findings are shared: every Assistant User can read all findings.

## 7. Retention

`Log retention (days)` (default 180) is **stored only**. Nothing deletes old conversations yet. Delete them from the list view as System Manager if you need to. Keep the test records listed in `build/cleanup.md` of the build repo in mind.

## 8. Confirming findings

Only a user with **Assistant Reviewer** can confirm. Open the finding (search bar: Assistant Finding), set **Status** to Confirmed and save. The server records who confirmed and when. Anyone else who tries gets "Only an Assistant Reviewer can confirm a finding." If a non-reviewer edits a confirmed finding, it returns to Draft.

Provenance fields (question, sources, cards used, Lending version, author, source message) cannot be changed after saving.

## 9. Re-ingesting knowledge after cards change

This is a maintainer task; see the README ("Maintainers only"). In short: approve cards in the build repo, run `lending_assistant.kb.ingest.run` with the build repo's `knowledge` folder and its commit, commit the app, then run the knowledge check.

What happens to findings: nothing is rewritten. When a finding is opened (or found by `search_findings`) the app compares the card versions it recorded with the shipped cards. A changed or removed card, or a different installed Lending version, shows the orange **check again** banner (and the advisor says "check again").

## 10. After a Frappe or Lending upgrade

1. `bench --site <site> backup --with-files`
2. Upgrade, then `bench --site <site> migrate` and `bench build --app lending_assistant`, restart.
3. `bench --site <site> execute lending_assistant.kb.validate.run`. Any `FINDING` line is drift: a card names a doctype, field label, option, Lending menu path or code file the site no longer has. Report it to the knowledge maintainers.
4. Compare the Lending version in `bench version` with the cards' Lending version (16.5.1 at hand-over). If they differ, findings show "check again".
5. Prove `get_loan_dues` still respects permissions: as a limited user, ask about a loan the user may not read and expect exactly "I can't find a record with that ID that you have access to."; as a user who may read it, ask what is due. The tool reads Loan Demand rows through the permission guard; it does not call Lending's own dues function.
6. On a dev copy, run the test suite (README, "Tests and the scan") and the scan.

## 11. Troubleshooting

| What you see | Cause and what to do |
|---|---|
| "The assistant is turned off." | **Enabled** is off in Assistant Settings. |
| 403 "You need the Assistant User role to use the assistant." | The user lacks the role. A reviewer needs both roles. |
| 429 "You have asked too many questions for now..." | A rate-limit bucket (section 5). Wait or raise the limit. |
| "The advisor has no API key yet." | The API key field is empty. |
| "The advisor is not set up correctly. Please tell the person who manages it." | The provider rejected the key (bad, revoked, no access). Replace it. |
| "The advisor couldn't answer right now. Please try again in a moment." | Provider error, rate limit, timeout or a bad request. Read `lending_assistant_chat.log` for `api_error kind=... http=... api_type=...`. |
| "The advisor stopped because a safety check failed, so it gave no answer." | A guard check (write trap, identity) tripped. Look for `dispatch_raised` in `lending_assistant_chat.log` and for lines in `lending_assistant_tools.log`; the Assistant Message `tool_calls` field shows `aborted`. Tell the developers. |
| "I can't help with that request." | The model declined (the log shows `model_refusal`). |
| Panel says "The advisor took too long..." | The browser waited 130 seconds (server budget is 90, 100 for Deep analysis). The answer may be in History. |
| Answer ends with "Source labels are missing in this reply; treat it as unverified." | The label check failed after one repair call. The audit row still has the answer. Note it for the evaluation. |
| A label like `[Analysis, BRD 7.6]` appears as plain text | Malformed labels count as missing. Detail must come after the label, outside the brackets. |
| Partial answer | A limit was reached; the user should ask a narrower question. |
| Panel does not appear | The user lacks Assistant User, or the assets are not built: run `bench build --app lending_assistant` and hard refresh. |
| A code change does not show | Python: restart `bench start` (web and worker). JS and CSS: `bench build --app lending_assistant`, then hard refresh. Hooks: `bench --site <site> clear-cache` and restart. Doctype JSON: `migrate`. |

**API 400 errors (lessons from #154 and #155).** The provider checks the tool definitions strictly. Two real failures: an enum that did not match its declared type, and "too many parameters with union types (limit: 16)". Unit tests that mock the API cannot catch these, and a free token-count call did not either. Only a real, minimal request does. After changing a tool schema, run one real preflight request (about one cent) before any live use. A new 400 shows in the log as `api_error kind=bad_request`.

## 12. Backup and restore

- Back up: `bench --site <site> backup --with-files`. Files land in `sites/<site>/private/backups/`.
- Restore is `bench --site <site> restore ...`. It overwrites the site: the owner decides, not the assistant team. Never run raw database commands.
- Dropping a throwaway site: see the README. It moves the site, with its backup and keys, to `frappe-bench/archived/sites/<site>/`; delete that folder when done.

## 13. Cleanup lists

The build repo's `build/cleanup.md` lists every test record (`AST-` prefix, users `ast-*@example.com`) and probe row, with the owner-deletes. Delete newest first, as Administrator through `bench --site <site> console`, never with raw SQL.
