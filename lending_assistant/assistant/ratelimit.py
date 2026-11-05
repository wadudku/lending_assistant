"""Atomic fixed-window counters for the endpoint gates (G7, DECISIONS #25, #27, #28).

`hit()` increments first, then makes sure the key has an expiry. INCR and TTL run in one pipeline, and
EXPIRE is set when the result is 1 or when the key has no expiry at all. So a key can never stay without
a TTL: even if a process dies between INCR and EXPIRE, the next call heals it. (The old read -> setex ->
incrby order could recreate a key without a TTL, which locked the user out for good.)

Used for four buckets: per-user `ask`, `feedback` and finding `save`, and the IP layer of `ask`.
"""

import frappe

USER_PREFIX = "ast:rl"
FEEDBACK_PREFIX = "ast:rl:fb"
FINDING_PREFIX = "ast:rl:af"
IP_PREFIX = "ast:rl:ip"


def key_for(prefix: str, identity: str, window: int) -> str:
	return frappe.cache.make_key(f"{prefix}:{identity}:{window}")


def hit(key: str, window: int) -> int:
	"""Count one call in the window that `key` belongs to and return the new count."""
	pipe = frappe.cache.pipeline()
	pipe.incr(key)
	pipe.ttl(key)
	count, ttl = pipe.execute()
	if count == 1 or ttl is None or ttl < 0:  # -1: no expiry, -2: gone
		frappe.cache.expire(key, window)
	return int(count)


def exceeded(prefix: str, identity: str, limit: int, window: int) -> bool:
	"""Count one call and say whether `identity` is now above `limit` for this window."""
	return hit(key_for(prefix, identity, window), window) > limit
