"""A scripted stand-in for the Anthropic client (M4b tests). No network: `orchestrator._make_client` is patched to return a
`FakeClient` that serves the scripted responses in order and records every request it was sent."""

import copy
from types import SimpleNamespace

FAKE_KEY = "sk-ast-test-FAKEKEY-0123456789"


class Obj(SimpleNamespace):
	def model_dump(self):
		return {k: (v.model_dump() if isinstance(v, Obj) else v) for k, v in vars(self).items()}


def text(t, **kw):
	return Obj(type="text", text=t, **kw)


def thinking(t="", signature="sig"):
	return Obj(type="thinking", thinking=t, signature=signature)


def tool_use(id, name, input=None):
	return Obj(type="tool_use", id=id, name=name, input=input if input is not None else {})


def server_tool_use(id, query):
	return Obj(type="server_tool_use", id=id, name="web_search", input={"query": query})


def web_result(tool_use_id, items):
	"""items = [(url, title)] for a result, or a dict for an error object."""
	content = (
		items
		if isinstance(items, dict)
		else [Obj(type="web_search_result", url=u, title=t) for u, t in items]
	)
	return Obj(type="web_search_tool_result", tool_use_id=tool_use_id, content=content)


def fallback_block(frm="claude-sonnet-5-5", to="claude-sonnet-5"):
	return Obj(type="fallback", from_=Obj(model=frm), to=Obj(model=to))


def usage(i=100, o=20, cw=0, cr=0, iterations=None, web=0):
	return Obj(
		input_tokens=i, output_tokens=o, cache_creation_input_tokens=cw, cache_read_input_tokens=cr,
		iterations=iterations, server_tool_use=Obj(web_search_requests=web) if web else None,
	)  # fmt: skip


def response(stop, *content, u=None, model="claude-sonnet-5-5", details=None):
	return Obj(stop_reason=stop, content=list(content), usage=u or usage(), model=model, stop_details=details)


class FakeClient:
	def __init__(self, script):
		self.script = list(script)
		self.calls = []
		self.retries = []

	def with_options(self, max_retries=None):
		self._pending_retries = max_retries
		return self

	@property
	def beta(self):
		return self

	@property
	def messages(self):
		return self

	def create(self, **kwargs):
		snap = copy.copy(kwargs)
		snap["messages"] = list(kwargs["messages"])
		snap["messages"] = [dict(m) for m in snap["messages"]]
		self.calls.append(snap)
		self.retries.append(self._pending_retries)
		item = self.script.pop(0)
		if isinstance(item, BaseException):
			raise item
		return item(kwargs) if callable(item) else item
