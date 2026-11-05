"""The two code tools (PLAN §4, M4a): `search_code` and `read_code`, over the sandbox in `codereader` (G12).

No path is opened here: `codereader` resolves every path, applies the deny list and the size and line caps (at most 30
matches per search, at most 200 lines per read) and returns the `<data source="code">` envelope. Both tools need the
Code reader switch, which the registry checks. No `@frappe.whitelist`.
"""

from lending_assistant.assistant import codereader

SEARCH_CODE_SCHEMA = {
	"name": "search_code",
	"description": (
		"Search the source code for a piece of text (not a regular expression). Returns up to 30 'path:line: text' "
		"matches. Narrow it with 'app' (for example lending) or 'path_glob' (for example *loan_repayment*)."
	),
	"strict": True,
	"input_schema": {
		"type": "object",
		"properties": {
			"query": {"type": "string", "description": "The text to find, at most 200 characters."},
			"app": {
				"type": "string",
				"description": "Only search this app, or leave it out for all readable apps.",
			},
			"path_glob": {
				"type": "string",
				"description": "A short relative pattern such as *loan_repayment*; optional.",
			},
		},
		"required": ["query"],
		"additionalProperties": False,
	},
}
READ_CODE_SCHEMA = {
	"name": "read_code",
	"description": (
		"Read lines of one source file, at most 200 per call. The path is '<app>/<path inside the app>', for example "
		"lending/lending/hooks.py. Use search_code to find the file and line first."
	),
	"strict": True,
	"input_schema": {
		"type": "object",
		"properties": {
			"path": {"type": "string", "description": "<app>/<path inside the app repo>."},
			"start_line": {
				"type": "integer",
				"description": "First line, 1 or more; leave it out for 1.",
			},
			"end_line": {
				"type": "integer",
				"description": "Last line; leave it out, or more than 200 lines after start_line is cut to 200 lines.",
			},
		},
		"required": ["path"],
		"additionalProperties": False,
	},
}
SCHEMAS = (SEARCH_CODE_SCHEMA, READ_CODE_SCHEMA)


def search_code(query, app=None, path_glob=None) -> str:
	return codereader.search(query, app, path_glob)


def read_code(path, start_line=None, end_line=None) -> str:
	return codereader.read(path, 1 if start_line is None else start_line, end_line)
