"""The only reader of Assistant Settings (DECISIONS #17).

Assistant Settings is app config, not business data. Assistant Users must not be able to read it
(it holds the API key), so there is no permission check here: every other module goes through
these two functions and never touches the doctype itself.

`get_settings()` hands out a plain copy, never the Settings Document (M2b-R12): a Document gives its caller
`type(doc)` and so the Document class, and `api_key` is not in the copy at all.
"""

import frappe

SETTINGS_DOCTYPE = "Assistant Settings"


def _cached():
	return frappe.get_cached_doc(  # AST-ALLOWED: app config, the one settings reader (DECISIONS #17)
		SETTINGS_DOCTYPE
	)


def get_settings():
	"""A fresh read-only-by-copy `frappe._dict` of the settings (child rows are `_dict`s too). No Password field."""
	doc = _cached()
	passwords = {df.fieldname for df in doc.meta.fields if df.fieldtype == "Password"}
	data = doc.as_dict()
	for fieldname in passwords:
		data.pop(fieldname, None)
	return data


def get_api_key() -> str | None:
	"""The Claude API key. Server-side only: never return it from an endpoint or write it to a log.

	Not called anywhere in M1.
	"""
	return _cached().get_password(  # AST-ALLOWED: the one reader of the API key (G8), server-side only
		"api_key", raise_exception=False
	)
