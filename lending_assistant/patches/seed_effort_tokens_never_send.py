from lending_assistant.install import raise_max_tokens_default, seed_defaults


def execute():
	"""M2a: effort per model (#31), max_tokens 4096 -> 16000 if untouched (#32), never-send list (#33)."""
	result = seed_defaults()
	raised = raise_max_tokens_default()
	print(
		f"Never-send fields seeded: {len(result['added_never_send'])}; effort set: {result['set_effort']}; "
		f"max_tokens raised to 16000: {raised}"
	)
	if result["skipped_never_send"]:
		print("Skipped (doctype or field not on this site): " + ", ".join(result["skipped_never_send"]))
