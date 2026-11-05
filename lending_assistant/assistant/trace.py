"""What the audit row records (G10), taken from tool results and API usage, never from the model's own text (M4b).

Pure functions over plain data. A tool result is the `<data source=...>` envelope that `registry.dispatch` returned; it
is parsed with `guard.unwrap`. Thinking text is never read (only block types are looked at), and nothing here sees the
key, a header, the system prompt or a request body.
"""

from lending_assistant.assistant.guard import unwrap

ARG_LIMIT = 500  # characters of any string in the recorded arguments


def plain(obj) -> dict:
	"""A block, usage or details object from the SDK (a pydantic model) or a dict, as a plain dict. The one place that
	reads SDK objects, so no dynamic attribute access is needed anywhere else."""
	if isinstance(obj, dict):
		return obj
	if obj is None:
		return {}
	try:
		return obj.model_dump()
	except AttributeError:
		return {}


def _n(data: dict, name: str) -> int:
	value = data.get(name, 0)
	return value if isinstance(value, int) and not isinstance(value, bool) else 0


class UsageTotals:
	"""Sums the `usage` of every API call of one answer. `input_tokens` is only the uncached remainder (skill), so the
	total prompt size is input + cache write + cache read. When a response carries `usage.iterations` (a server-side
	fallback ran), the per-hop figures are summed instead of the top-level ones, so the fallback model's tokens count."""

	def __init__(self):
		self.calls = 0
		self.input = 0
		self.cache_write = 0
		self.cache_read = 0
		self.output = 0
		self.web_search_requests = 0
		self.iterations_seen = False

	def add(self, usage) -> None:
		self.calls += 1
		data = plain(usage)
		iterations = data.get("iterations")
		parts = []
		if isinstance(iterations, list | tuple):
			parts = [
				d for d in (plain(i) for i in iterations) if _n(d, "input_tokens") or _n(d, "output_tokens")
			]
		if parts:
			self.iterations_seen = True
		for part in parts or [data]:
			self.input += _n(part, "input_tokens")
			self.cache_write += _n(part, "cache_creation_input_tokens")
			self.cache_read += _n(part, "cache_read_input_tokens")
			self.output += _n(part, "output_tokens")
		self.web_search_requests += _n(plain(data.get("server_tool_use")), "web_search_requests")

	@property
	def tokens_in(self) -> int:
		return self.input + self.cache_write + self.cache_read

	@property
	def tokens_out(self) -> int:
		return self.output

	def as_dict(self) -> dict:
		return {
			"calls": self.calls,
			"input": self.input,
			"cache_write": self.cache_write,
			"cache_read": self.cache_read,
			"output": self.output,
			"web_search_requests": self.web_search_requests,
		}


def cap_arguments(value):
	"""A copy of the model's tool arguments with every string cut to ARG_LIMIT characters."""
	if isinstance(value, str):
		return value if len(value) <= ARG_LIMIT else value[:ARG_LIMIT] + "…"
	if isinstance(value, dict):
		return {str(k)[:100]: cap_arguments(v) for k, v in value.items()}
	if isinstance(value, list | tuple):
		return [cap_arguments(v) for v in value]
	return value if value is None or isinstance(value, bool | int | float) else str(value)[:ARG_LIMIT]


def _payload(content):
	try:
		return unwrap(content)
	except Exception:
		return None


def records_from(tool: str, content: str) -> list[dict]:
	"""`{doctype, name}` entries for the records a successful result actually contains."""
	payload = _payload(content)
	if not isinstance(payload, dict):
		return []
	if tool == "get_record" and payload.get("doctype") and payload.get("name"):
		return [{"doctype": payload["doctype"], "name": payload["name"]}]
	if tool == "find_records":
		rows = payload.get("rows") or []
		return [
			{"doctype": payload.get("doctype"), "name": r["name"]}
			for r in rows
			if isinstance(r, dict) and r.get("name")
		]
	if tool == "get_loan_dues" and payload.get("loan"):
		return [
			{"doctype": "Loan", "name": payload["loan"]},
			{
				"doctype": "Loan Demand",
				"name": None,
				"loan": payload["loan"],
				"count": payload.get("rows_read", 0),
			},
		]
	return []


def code_files_from(tool: str, content: str) -> list[dict]:
	payload = _payload(content)
	if tool == "read_code" and isinstance(payload, dict) and payload.get("path"):
		return [
			{
				"path": payload["path"],
				"start_line": payload.get("start_line"),
				"end_line": payload.get("end_line"),
			}
		]
	return []


def cards_from(tool: str, content: str) -> list[dict]:
	"""`{id, version}` for every card a knowledge tool handed to the model (it saw at least the summary)."""
	payload = _payload(content)
	if not isinstance(payload, dict) or tool not in ("lookup_knowledge", "get_card", "search_knowledge"):
		return []
	cards = [payload] if tool == "get_card" else payload.get("results") or []
	return [
		{"id": c["id"], "version": c.get("version")} for c in cards if isinstance(c, dict) and c.get("id")
	]


def web_sources_from(content) -> list[dict]:
	"""`{url, title}` from the `web_search_tool_result` blocks of a response. An error result (an object, not a list)
	records nothing."""
	found = []
	for block in content or []:
		data = plain(block)
		if data.get("type") != "web_search_tool_result":
			continue
		items = data.get("content")
		if not isinstance(items, list | tuple):
			continue
		for item in items:
			item = plain(item)
			if item.get("url"):
				found.append({"url": item["url"], "title": item.get("title") or ""})
	return found


def merge_unique(target: list, new: list) -> None:
	for item in new:
		if item not in target:
			target.append(item)
