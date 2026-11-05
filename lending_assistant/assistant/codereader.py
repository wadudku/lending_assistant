"""Code reader sandbox (PLAN G12). The only module that opens a file from a caller-supplied path.

Paths look like `<app>/<path inside the app repo>`, for example `lending/lending/hooks.py` (DECISIONS #38.1).
The root of each app is `<bench>/apps/<app>` and only apps in Settings -> `code_app_allowlist` are readable.
Every path is checked twice: as written, and after symlinks are resolved. A refusal never returns content and
never says whether the file exists.
"""

import fnmatch
import os
import time

import frappe

from lending_assistant.assistant import guard, settings

EXTENSIONS = (".py", ".js", ".json", ".md", ".html", ".txt", ".toml", ".cfg")
DENY_SEGMENTS = frozenset({"sites", "node_modules", "__pycache__", ".git", "dist"})
DENY_FILES = frozenset({"site_config.json", "common_site_config.json"})
MAX_FILE_BYTES = 1024 * 1024
MAX_LINES = 200  # lines per read (G9)
MAX_MATCHES = 30  # matches per search
MAX_QUERY = 200
LINE_CHARS = 240
BINARY_PROBE = 8192
SEARCH_SECONDS = 10

REFUSED = "That path is not available to the code reader."
OFF = "The code reader is turned off in Assistant Settings."


class CodeReaderRefused(guard.AssistantRefused):
	pass


def _apps_dir() -> str:
	return os.path.join(frappe.utils.get_bench_path(), "apps")


def _allowed_apps() -> list[str]:
	return [row.app_name for row in settings.get_settings().code_app_allowlist if row.app_name]


def _roots(only: str | None = None) -> dict[str, str]:
	"""{app: real path of its root}, for allowlisted apps whose folder exists."""
	apps_dir = _apps_dir()
	roots = {}
	for app in _allowed_apps():
		if not app.isidentifier() or (only and app != only):
			continue
		root = os.path.realpath(os.path.join(apps_dir, app))
		if os.path.isdir(root):
			roots[app] = root
	return roots


def _require_on():
	if not settings.get_settings().code_reader:
		raise CodeReaderRefused(OFF)


def _bad_segment(segment: str) -> bool:
	return not segment or segment.startswith(".") or segment in DENY_SEGMENTS or segment in DENY_FILES


def _is_inside(real: str, root: str) -> bool:
	return os.path.commonpath([real, root]) == root


def _check_relative(rel_parts: list[str]) -> bool:
	"""Deny list + extension on a relative path (used on the written path and on the resolved one)."""
	if not rel_parts or any(_bad_segment(p) for p in rel_parts):
		return False
	return rel_parts[-1].lower().endswith(EXTENSIONS)


def _is_binary(real: str) -> bool:
	with open(real, "rb") as handle:  # AST-ALLOWED: G12: the one place that opens a caller-supplied path, after _resolve()
		return b"\0" in handle.read(BINARY_PROBE)


def _resolve(path) -> tuple[str, str, str, str]:
	"""Validate `path`; return (app, root, real_path, display_path). Raises CodeReaderRefused on any problem."""
	if not isinstance(path, str) or not path or len(path) > 300 or "\0" in path or "\\" in path:
		raise CodeReaderRefused(REFUSED)
	if ".." in path or path.startswith(("/", "~")) or ":" in path:
		raise CodeReaderRefused(REFUSED)
	parts = path.split("/")
	app, rel_parts = parts[0], parts[1:]
	roots = _roots(only=app)
	if app not in roots or not _check_relative(rel_parts):
		raise CodeReaderRefused(REFUSED)
	root = roots[app]

	real = os.path.realpath(os.path.join(root, *rel_parts))
	if not _is_inside(real, root):
		raise CodeReaderRefused(REFUSED)
	real_rel = os.path.relpath(real, root).split(os.sep)
	if not _check_relative(real_rel):  # a symlink inside the app that points at .git, sites/, .env ...
		raise CodeReaderRefused(REFUSED)
	if not os.path.isfile(real) or os.path.getsize(real) > MAX_FILE_BYTES or _is_binary(real):
		raise CodeReaderRefused(REFUSED)
	return app, root, real, f"{app}/{'/'.join(real_rel)}"


def controller_path(module, doctype) -> str | None:
	"""`<app>/<app>/<module>/doctype/<name>/<name>.py` for a doctype's controller, when the code reader is on and the
	file is readable under the same sandbox as `read()`; else None. Never says whether any other path exists."""
	if not settings.get_settings().code_reader or not isinstance(module, str) or not isinstance(doctype, str):
		return None
	folder, name = module.lower().replace(" ", "_"), doctype.lower().replace(" ", "_").replace("-", "_")
	for app in _roots():
		try:
			return _resolve(f"{app}/{app}/{folder}/doctype/{name}/{name}.py")[3]
		except CodeReaderRefused:
			continue
	return None


def _line(text: str) -> str:
	text = text.rstrip("\r\n")
	return text if len(text) <= LINE_CHARS else text[:LINE_CHARS] + "…"


def read(path, start_line=1, end_line=None) -> str:
	"""Lines `start_line`..`end_line` (at most 200) of one file, as a `<data source="code">` envelope."""
	_require_on()
	app, root, real, display = _resolve(path)
	if isinstance(start_line, bool) or not isinstance(start_line, int) or start_line < 1:
		raise frappe.ValidationError("start_line must be a whole number of 1 or more.")
	if end_line is None:
		end_line = start_line + MAX_LINES - 1
	if isinstance(end_line, bool) or not isinstance(end_line, int) or end_line < start_line:
		raise frappe.ValidationError("end_line must be a whole number at or after start_line.")
	asked_end = end_line
	end_line = min(end_line, start_line + MAX_LINES - 1)

	lines = []
	more = False
	with open(real, encoding="utf-8", errors="replace") as handle:  # AST-ALLOWED: G12: path already validated by _resolve()
		for number, text in enumerate(handle, start=1):
			if number < start_line:
				continue
			if number > end_line:
				more = True
				break
			lines.append((number, _line(text)))

	result = {
		"path": display,
		"start_line": start_line,
		"end_line": lines[-1][0] if lines else start_line,
		"truncated": asked_end > end_line,
		"more_lines_exist": more,
		"lines": [f"{n}: {t}" for n, t in lines],
	}
	guard.fit(result, row_lists=lambda: [result["lines"]], field_dicts=lambda: [], source="code")
	if result["lines"]:
		result["end_line"] = start_line + len(result["lines"]) - 1
	return guard.as_data(result, source="code")


def search(query, app=None, path_glob=None) -> str:
	"""Literal text search (no regex), at most 30 `file:line: text` matches."""
	_require_on()
	if not isinstance(query, str) or not query.strip() or len(query) > MAX_QUERY or "\0" in query:
		raise frappe.ValidationError(f"The query must be 1 to {MAX_QUERY} characters of plain text.")
	if app is not None and (not isinstance(app, str) or app not in _roots()):
		raise CodeReaderRefused(REFUSED)
	if path_glob is not None and (
		not isinstance(path_glob, str) or len(path_glob) > 100 or ".." in path_glob or path_glob.startswith("/")
	):
		raise frappe.ValidationError("path_glob must be a short relative pattern.")

	deadline = time.monotonic() + SEARCH_SECONDS
	matches, files_scanned, timed_out, capped = [], 0, False, False

	for root_app, root in _roots(only=app).items():
		for folder, dirs, files in os.walk(root, topdown=True, followlinks=False):  # AST-ALLOWED: G12: search walks allowlisted roots only
			dirs[:] = sorted(d for d in dirs if not _bad_segment(d))
			rel_folder = os.path.relpath(folder, root)
			for filename in sorted(files):
				rel_parts = [] if rel_folder == "." else rel_folder.split(os.sep)
				rel_parts.append(filename)
				if not _check_relative(rel_parts):
					continue
				rel = "/".join(rel_parts)
				if path_glob and not fnmatch.fnmatch(rel, path_glob):
					continue
				full = os.path.join(folder, filename)
				if os.path.islink(full):
					continue  # search lists real files only; read() still follows an inside-the-root link
				try:
					real = os.path.realpath(full)
					if (
						not _is_inside(real, root)
						or not _check_relative(os.path.relpath(real, root).split(os.sep))
						or not os.path.isfile(real)
						or os.path.getsize(real) > MAX_FILE_BYTES
						or _is_binary(real)
					):
						continue
					files_scanned += 1
					with open(real, encoding="utf-8", errors="replace") as handle:  # AST-ALLOWED: G12: file already validated in this loop
						for number, text in enumerate(handle, start=1):
							if query in text:
								matches.append(f"{root_app}/{rel}:{number}: {_line(text).strip()}")
								if len(matches) >= MAX_MATCHES:
									capped = True
									break
				except OSError:
					continue
				if capped:
					break
				if time.monotonic() > deadline:
					timed_out = True
					break
			if capped or timed_out:
				break
		if capped or timed_out:
			break

	result = {
		"query": query,
		"count_returned": len(matches),
		"truncated": capped or timed_out,
		"timed_out": timed_out,
		"files_scanned": files_scanned,
		"matches": matches,
	}
	guard.fit(result, row_lists=lambda: [result["matches"]], field_dicts=lambda: [], source="code")
	result["count_returned"] = len(result["matches"])
	return guard.as_data(result, source="code")
