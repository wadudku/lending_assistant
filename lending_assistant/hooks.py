app_name = "lending_assistant"
app_title = "Lending Assistant"
app_publisher = "Wadud"
app_description = "Lending Assistant"
app_email = "shams.wadud@polygontech.xyz"
app_license = "mit"

# Apps
# ------------------

required_apps = ["erpnext", "lending"]

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "lending_assistant",
# 		"logo": "/assets/lending_assistant/logo.png",
# 		"title": "Lending Assistant",
# 		"route": "/lending_assistant",
# 		"has_permission": "lending_assistant.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/lending_assistant/css/chat_widget.css"
app_include_js = "/assets/lending_assistant/js/chat_widget.js"

# include js, css files in header of web template
# web_include_css = "/assets/lending_assistant/css/lending_assistant.css"
# web_include_js = "/assets/lending_assistant/js/lending_assistant.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "lending_assistant/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "lending_assistant/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "lending_assistant.utils.jinja_methods",
# 	"filters": "lending_assistant.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "lending_assistant.install.before_install"
after_install = "lending_assistant.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "lending_assistant.uninstall.before_uninstall"
# after_uninstall = "lending_assistant.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "lending_assistant.utils.before_app_install"
# after_app_install = "lending_assistant.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "lending_assistant.utils.before_app_uninstall"
# after_app_uninstall = "lending_assistant.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "lending_assistant.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "lending_assistant.notifications.get_notification_config"

# Awesome Bar
# -----------
# Extra search results: list of dicts with label, description, route, index.
# route: ["List", "ToDo"], "/desk/docs/some/page", or "https://example.com"
# awesomebar_search = ["lending_assistant.search.awesomebar_results"]

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# G1 layer 2: the write trap. Every hook below does nothing unless a tool is running inside
# guard.read_only_tool_context(); then it raises PermissionError("The assistant can only read.").
# Every `before_*` / `on_*` / `after_*` event that frappe/model/*.py fires is here or in NOT_TRAPPED in
# tests/test_guard_rework4.py, with a reason; that test fails when a Frappe upgrade adds one (M2b-R18).
# `before_mapping` and `after_mapping` stay untrapped: get_mapped_doc only builds an unsaved document in memory, and saving
# it goes through the trapped save events.
_TRAP = "lending_assistant.assistant.guard.block_if_read_only"
doc_events = {
	"*": {
		# insert, save, submit, cancel, delete, rename
		"before_insert": _TRAP,
		"after_insert": _TRAP,  # M4a: trapped as well (#147)
		"before_naming": _TRAP,  # naming takes the next number from a series (a write)
		"before_validate": _TRAP,
		"before_save": _TRAP,
		"on_update": _TRAP,
		"before_submit": _TRAP,
		"on_submit": _TRAP,
		"before_cancel": _TRAP,
		"on_cancel": _TRAP,
		"on_trash": _TRAP,
		"after_delete": _TRAP,  # fired by delete_doc(..., for_reload=True) after the row is gone, M4a-R20
		"before_rename": _TRAP,
		"after_rename": _TRAP,  # M4a: trapped as well (#147)
		"before_reload": _TRAP,  # fired just before a DocType row is deleted to be re-imported
		# saving a submitted document (action "update_after_submit"), M2b-R18
		"before_update_after_submit": _TRAP,
		"on_update_after_submit": _TRAP,
		# discarding a draft, M2b-R18
		"before_discard": _TRAP,
		"on_discard": _TRAP,
		# db_set() and the end of every save / delete, M2b-R18
		"before_change": _TRAP,
		"on_change": _TRAP,
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"lending_assistant.tasks.all"
# 	],
# 	"daily": [
# 		"lending_assistant.tasks.daily"
# 	],
# 	"hourly": [
# 		"lending_assistant.tasks.hourly"
# 	],
# 	"weekly": [
# 		"lending_assistant.tasks.weekly"
# 	],
# 	"monthly": [
# 		"lending_assistant.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "lending_assistant.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "lending_assistant.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "lending_assistant.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "lending_assistant.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["lending_assistant.utils.before_request"]
# after_request = ["lending_assistant.utils.after_request"]

# Job Events
# ----------
# before_job = ["lending_assistant.utils.before_job"]
# after_job = ["lending_assistant.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"lending_assistant.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []


# Fixtures
# --------
# Only the two Assistant roles are exported (DECISIONS #2). The filter must stay name-based so that
# `bench export-fixtures` never drags other Roles into the app.
fixtures = [
	{
		"dt": "Role",
		"filters": [["name", "in", ["Assistant User", "Assistant Reviewer"]]],
	}
]
