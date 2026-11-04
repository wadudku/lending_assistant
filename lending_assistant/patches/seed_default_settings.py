from lending_assistant.install import seed_defaults


def execute():
	result = seed_defaults()
	print(
		"Assistant Settings seeded: "
		f"{len(result['added_doctypes'])} doctypes, {len(result['added_code_apps'])} code apps"
	)
	if result["skipped_missing_doctypes"]:
		print("Skipped (doctype not on this site): " + ", ".join(result["skipped_missing_doctypes"]))
