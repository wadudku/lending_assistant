"""The Claude tool loop (PLAN §2 G1-G11, §6; DECISIONS #31, #32, #48, #144-#152; M4b).

The ONLY module that imports `anthropic`, calls `settings.get_api_key()` and calls `registry.dispatch` /
`registry.tool_definitions`. `run()` takes the question and the page context and returns a plain dict for the audit row;
it never takes a user, role or company (identity is `frappe.session.user` inside the request), writes nothing, and never
puts the key, a header, a request body, the system prompt or thinking text into a log, a reply or the result.

Per answer:
  1. one client (explicit `base_url`, so an environment variable cannot redirect the key), the key read once;
  2. a request with adaptive thinking, explicit effort, the strict tools (cache breakpoint on the last client tool), the
     optional web search tool after them, a stable cached system block and a volatile block after it;
  3. a loop on `stop_reason` (checked before the content is read): `end_turn`, `tool_use`, `pause_turn`, `max_tokens`,
     `refusal`; anything else fails closed. All tool results of one turn go back in ONE user message; a refusal envelope
     goes back as `is_error`; a RAISE from `dispatch` ends the turn (status `error`, fail closed, #146);
  4. G9 limits (rounds, wall clock); a limit ends in one wrap-up call that cannot use tools (status `limited`);
  5. a label check (G11): one repair call, then a visible notice.

SDK objects are read only through `trace.plain` (one place), so there is no dynamic attribute access in this file.
"""

import time

import anthropic
import frappe
from frappe.utils import now_datetime

from lending_assistant.assistant import prompts, settings, trace
from lending_assistant.assistant.tools import registry

API_BASE = "https://api.anthropic.com"
BETA_FALLBACK = "server-side-fallback-2026-07-01"
WEB_TOOL = {"type": "web_search_20260209", "name": "web_search", "max_uses": 3}

MAX_ROUNDS = 8  # tool rounds (G9)
MAX_ROUNDS_DEEP = 12
BUDGET = 90.0  # seconds of wall clock per answer, measured from the start of run()
BUDGET_DEEP = 100.0
RESERVE = 25.0  # always kept for the wrap-up call
MIN_ROUND = 10.0  # a round needs at least this much more than the reserve
ROUND_TIMEOUT_MAX = 40.0
WRAP_TIMEOUT_MAX = 25.0
DEFAULT_MAX_TOKENS = 16000
STUB_MODEL = "stub"


def _clock() -> float:
	return time.monotonic()


def _api_key():
	return settings.get_api_key()


def _make_client(key: str):
	return anthropic.Anthropic(api_key=key, base_url=API_BASE, max_retries=1)


class _Stop(Exception):
	"""Ends the turn with a status and a fixed reply (no exception text is ever carried)."""

	def __init__(self, status: str, message: str):
		super().__init__(status)
		self.status = status
		self.message = message


def _log(event: str, **fields) -> None:
	"""One warning line: user, kind and a few safe tokens (tool name, error kind, status). Never an exception text, header or body."""
	try:
		safe = {
			k: str(v)[:60] for k, v in fields.items() if str(v).replace("_", "").replace("-", "").isalnum()
		}
		logger = frappe.logger("lending_assistant_chat")
		if logger.level > 30:
			logger.setLevel(30)
		logger.warning(f"user={frappe.session.user} {event} " + " ".join(f"{k}={v}" for k, v in safe.items()))
	except Exception:
		pass


class _Turn:
	"""Everything one answer collects for the audit row."""

	def __init__(self, model: str, deep: bool):
		self.model = model
		self.served = None
		self.deep = deep
		self.usage = trace.UsageTotals()
		self.tool_calls, self.records_read, self.code_files_read, self.cards_used = [], [], [], []
		self.web_sources = []
		self.sources = []  # source labels of tool results that returned data
		self.web_used = False
		self.tool_rounds = 0
		self.started = _clock()
		self.deadline = self.started + (BUDGET_DEEP if deep else BUDGET)

	def remaining(self) -> float:
		return self.deadline - _clock()

	def label_sources(self) -> list:
		return [*self.sources, *(["web"] if self.web_used else [])]

	def result(self, answer: str, status: str, key: str | None = None) -> dict:
		if key:
			answer = answer.replace(key, "[redacted]")
		return {
			"answer": answer,
			"status": status,
			"model": self.served or self.model,
			"tokens_in": self.usage.tokens_in,
			"tokens_out": self.usage.tokens_out,
			"latency_ms": int((_clock() - self.started) * 1000),
			"tool_calls": self.tool_calls or None,
			"records_read": self.records_read or None,
			"code_files_read": self.code_files_read or None,
			"cards_used": self.cards_used or None,
			"web_sources": self.web_sources or None,
			"usage": self.usage.as_dict(),
		}


# --- helpers -------------------------------------------------------------------------------------------------------


def _text(content) -> str:
	parts = []
	for block in content or []:
		data = trace.plain(block)
		if data.get("type") == "text":
			parts.append(data.get("text") or "")
	return "".join(parts).strip()


def _replay(content):
	"""The content to send back as the assistant turn. Unchanged (the same list) unless a server-side fallback ran in the
	middle of the output; then, as the skill says, the `thinking`, `redacted_thinking` and `tool_use` blocks and any
	`server_tool_use` without its result that come BEFORE the last `fallback` block are left out, and the marker itself."""
	blocks = list(content or [])
	views = [trace.plain(b) for b in blocks]
	marks = [i for i, v in enumerate(views) if v.get("type") == "fallback"]
	if not marks:
		return content
	boundary = marks[-1]
	answered = {v.get("tool_use_id") for v in views[:boundary]}
	kept = []
	for i, block in enumerate(blocks):
		kind = views[i].get("type")
		if kind == "fallback":
			continue
		if i < boundary and (
			kind in ("thinking", "redacted_thinking", "tool_use")
			or (kind == "server_tool_use" and views[i].get("id") not in answered)
		):
			continue
		kept.append(block)
	return kept


def _request(client, turn, settings_, tools, system, messages, timeout, retries, tool_choice=None):
	kwargs = {
		"model": settings_["model"],
		"max_tokens": settings_["max_tokens"],
		"thinking": {"type": "adaptive"},
		"output_config": {"effort": settings_["effort"]},
		"tools": tools,
		"system": system,
		"messages": messages,
		"betas": [BETA_FALLBACK],
		"fallbacks": "default",
		"timeout": timeout,
	}
	if tool_choice:
		kwargs["tool_choice"] = tool_choice
	response = client.with_options(max_retries=retries).beta.messages.create(**kwargs)
	turn.usage.add(response.usage)
	served = response.model
	turn.served = served if isinstance(served, str) and served and served != settings_["model"] else None
	return response


def _clamp(value: float, low: float, high: float) -> float:
	return max(low, min(high, value))


def _run_tool(turn: _Turn, block) -> dict:
	"""Run one `tool_use` block through the dispatcher. A refusal comes back as an error result; a RAISE ends the turn."""
	view = trace.plain(block)
	name = view.get("name")
	args = view.get("input")
	label = name if isinstance(name, str) and name.replace("_", "").isalnum() else "(a name)"
	t0 = _clock()
	try:
		result = registry.dispatch(name, args)
	except Exception:  # identity, trap/rollback or internal failure: fail closed (#146)
		_log("dispatch_raised", tool=label)
		turn.tool_calls.append(
			{
				"round": turn.tool_rounds + 1,
				"name": label,
				"arguments": trace.cap_arguments(args),
				"refused": True,
				"ms": int((_clock() - t0) * 1000),
				"aborted": True,
			}
		)
		raise _Stop("error", prompts.MESSAGES["aborted"]) from None
	turn.tool_calls.append(
		{
			"round": turn.tool_rounds + 1,
			"name": label,
			"arguments": trace.cap_arguments(args),
			"refused": bool(result.is_error),
			"ms": int((_clock() - t0) * 1000),
		}
	)
	out = {"type": "tool_result", "tool_use_id": view.get("id"), "content": result.content}
	if result.is_error:
		out["is_error"] = True
	else:
		if result.source and result.source not in turn.sources:
			turn.sources.append(result.source)
		trace.merge_unique(turn.records_read, trace.records_from(label, result.content))
		trace.merge_unique(turn.code_files_read, trace.code_files_from(label, result.content))
		trace.merge_unique(turn.cards_used, trace.cards_from(label, result.content))
	return out


def _note_web(turn: _Turn, content) -> None:
	for block in content or []:
		view = trace.plain(block)
		kind = view.get("type")
		if kind == "server_tool_use" and view.get("name") == "web_search":
			turn.tool_calls.append(
				{
					"round": turn.tool_rounds + 1,
					"name": "web_search",
					"arguments": trace.cap_arguments(view.get("input")),
					"refused": False,
					"ms": None,
				}
			)
		if kind == "web_search_tool_result":
			turn.web_used = True
	trace.merge_unique(turn.web_sources, trace.web_sources_from(content))


# --- the loop --------------------------------------------------------------------------------------------------------


def _refusal(response) -> dict:
	category = trace.plain(response.stop_details).get("category")
	_log("model_refusal", category=category if isinstance(category, str) else "none")
	return {"text": prompts.MESSAGES["refused"], "status": "error"}


def _wrap_up(turn, call, messages, pending=None) -> dict:
	"""One last call that cannot use tools. `pending` = the `tool_use` blocks of the response that we did not run."""
	content = [
		{
			"type": "tool_result",
			"tool_use_id": trace.plain(b).get("id"),
			"content": '{"error": "Not run: the tool limit was reached."}',
			"is_error": True,
		}
		for b in pending or []
	]
	content.append({"type": "text", "text": prompts.WRAP_UP_REQUEST})
	messages.append({"role": "user", "content": content})
	response = call(
		timeout=_clamp(turn.remaining(), MIN_ROUND, WRAP_TIMEOUT_MAX), retries=0, tool_choice={"type": "none"}
	)
	_note_web(turn, response.content)
	stop = response.stop_reason
	if stop == "refusal":
		return _refusal(response)
	text = _text(response.content)
	if stop == "max_tokens":
		text += prompts.CUT_NOTICE
	return {"text": text + prompts.MESSAGES["limited"], "status": "limited"}


def _labels(turn, call, messages, response, answer: str) -> str:
	"""G11: one repair call if labels are missing, then a visible notice."""
	if not prompts.check_labels(answer, turn.label_sources()):
		return answer
	if turn.remaining() >= RESERVE:
		messages.append({"role": "assistant", "content": _replay(response.content)})
		messages.append({"role": "user", "content": prompts.REPAIR_REQUEST})
		turn.tool_calls.append({"repair": "labels"})
		repaired = call(
			timeout=_clamp(turn.remaining(), MIN_ROUND, WRAP_TIMEOUT_MAX),
			retries=0,
			tool_choice={"type": "none"},
		)
		if repaired.stop_reason == "end_turn" and _text(repaired.content):
			answer = _text(repaired.content)
	if prompts.check_labels(answer, turn.label_sources()):
		answer += "\n\n" + prompts.LABELS_MISSING_NOTICE
	return answer


def _loop(turn, call, messages, max_rounds) -> dict:
	while True:
		if turn.remaining() < RESERVE + MIN_ROUND:
			return _wrap_up(turn, call, messages)
		response = call(
			timeout=_clamp((turn.remaining() - RESERVE) / 2, MIN_ROUND, ROUND_TIMEOUT_MAX), retries=1
		)
		_note_web(turn, response.content)
		stop = response.stop_reason  # always before the content is read
		if stop == "end_turn":
			return {"text": _labels(turn, call, messages, response, _text(response.content)), "status": "ok"}
		if stop == "max_tokens":
			return {"text": _text(response.content) + prompts.CUT_NOTICE, "status": "limited"}
		if stop == "refusal":
			return _refusal(response)
		if stop == "pause_turn":
			turn.tool_rounds += 1
			if turn.tool_rounds > max_rounds:
				return {"text": _text(response.content) + prompts.MESSAGES["limited"], "status": "limited"}
			messages.append({"role": "assistant", "content": _replay(response.content)})
			continue
		if stop != "tool_use":
			_log("unknown_stop", reason=stop if isinstance(stop, str) else "none")
			raise _Stop("error", prompts.MESSAGES["error"])
		replay = _replay(response.content)
		uses = [b for b in replay if trace.plain(b).get("type") == "tool_use"]
		messages.append({"role": "assistant", "content": replay})
		if not uses:
			raise _Stop("error", prompts.MESSAGES["error"])
		if turn.tool_rounds >= max_rounds or turn.remaining() < RESERVE:
			return _wrap_up(turn, call, messages, pending=uses)
		results = [_run_tool(turn, block) for block in uses]
		turn.tool_rounds += 1
		messages.append({"role": "user", "content": results})  # all results of this turn in ONE user message


def _api_error(exc) -> _Stop:
	"""A generic reply per error class. Nothing from the exception (text, headers, body, class name) is kept."""
	if isinstance(exc, anthropic.AuthenticationError | anthropic.PermissionDeniedError):
		kind = "auth"
	elif isinstance(exc, anthropic.RateLimitError):
		kind = "rate_limit"
	elif isinstance(exc, anthropic.APITimeoutError):
		kind = "timeout"
	elif isinstance(exc, anthropic.APIConnectionError):
		kind = "connection"
	elif isinstance(exc, anthropic.APIStatusError):
		kind = "server"
	else:
		kind = "other"
	_log("api_error", kind=kind)
	return _Stop("error", prompts.MESSAGES["auth" if kind == "auth" else "error"])


def run(question, *, route_doctype="", route_docname="", depth="Both", deep=0, history=None) -> dict:
	"""Answer one question. Returns the audit fields plus `answer`, `status` and `usage`; see `_Turn.result`."""
	cfg = settings.get_settings()
	deep = bool(deep)
	model = (cfg.deep_model if deep else cfg.default_model) or ""
	effort = (cfg.deep_effort if deep else cfg.default_effort) or "medium"
	turn = _Turn(model, deep)
	key = _api_key()
	if not key:
		turn.model = STUB_MODEL
		return turn.result(prompts.MESSAGES["no_key"], "error")
	try:
		client = _make_client(key)
		tools = registry.tool_definitions()
		names = [t["name"] for t in tools]
		if tools:
			tools[-1]["cache_control"] = {"type": "ephemeral"}
		if cfg.web_search:
			tools.append(dict(WEB_TOOL))
			names.append("web_search")
		system = [
			prompts.stable_block(),
			prompts.volatile_block(
				today=now_datetime().date().isoformat(),
				roles=frappe.get_roles(),
				route_doctype=route_doctype,
				route_docname=route_docname,
				depth=depth,
				deep=deep,
				tools=names,
				live_data=bool(cfg.live_data),
				code_reader=bool(cfg.code_reader),
				web_search=bool(cfg.web_search),
			),
		]
		messages = [*prompts.history_messages(history), {"role": "user", "content": question}]
		fixed = {
			"model": model,
			"effort": effort,
			"max_tokens": int(cfg.max_tokens or 0) or DEFAULT_MAX_TOKENS,
		}

		def call(*, timeout, retries, tool_choice=None):
			return _request(client, turn, fixed, tools, system, messages, timeout, retries, tool_choice)

		outcome = _loop(turn, call, messages, MAX_ROUNDS_DEEP if deep else MAX_ROUNDS)
		return turn.result(outcome["text"], outcome["status"], key)
	except _Stop as stop:
		return turn.result(stop.message, stop.status, key)
	except anthropic.AnthropicError as exc:
		stop = _api_error(exc)
		return turn.result(stop.message, stop.status, key)
	except Exception:  # fail closed: a generic reply, never the exception text
		_log("internal_error")
		return turn.result(prompts.MESSAGES["error"], "error", key)
