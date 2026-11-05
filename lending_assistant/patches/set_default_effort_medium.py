from lending_assistant.install import lower_default_effort


def execute():
	"""M4b (#145): default_effort high -> medium, only if it still holds the seeded `high`."""
	print(f"default_effort lowered from high to medium: {lower_default_effort()}")
