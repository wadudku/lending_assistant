"""The only reader of Assistant Settings (DECISIONS #17).

Assistant Settings is app config, not business data. Assistant Users must not be able to read it
(it holds the API key), so there is no permission check here: every other module goes through
these two functions and never touches the doctype itself.
"""

import frappe

SETTINGS_DOCTYPE = "Assistant Settings"


def get_settings():
	"""Cached read of the Assistant Settings single."""
	return frappe.get_cached_doc(SETTINGS_DOCTYPE)


def get_api_key() -> str | None:
	"""The Claude API key. Server-side only: never return it from an endpoint or write it to a log.

	Not called anywhere in M1.
	"""
	return get_settings().get_password("api_key", raise_exception=False)
