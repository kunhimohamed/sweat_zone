from . import __version__ as app_version

app_name = "sweat_zone"
app_title = "Sweat Zone"
app_publisher = "kunhimohamed6@gmail.com"
app_description = "Gym App"
app_email = "kunhimohamed6@gmail.com"
app_license = "MIT"

# fixtures
fixtures = [
    # {
    #     "dt":
    #     "Custom Field",
    #     "filters": [[
    #         "name", "in", [
    #             # Customer
    #             'Customer-to_date',
    #             'Customer-from_date',
    #             'Customer-section_break_76',
    #             'Customer-subscription_plan',
    #             'Customer-trainer',
    #             'Customer-subscriptions'
    #         ]
    #     ]]
    # }
] 

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sweat_zone/css/sweat_zone.css"
# app_include_js = "/assets/sweat_zone/js/sweat_zone.js"

# include js, css files in header of web template
# web_include_css = "/assets/sweat_zone/css/sweat_zone.css"
# web_include_js = "/assets/sweat_zone/js/sweat_zone.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "sweat_zone/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_js = {
        "Customer" : "public/js/customer.js"
    }
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# website_generators = ["Gym Subscription Plan"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "sweat_zone.utils.jinja_methods",
#	"filters": "sweat_zone.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "sweat_zone.install.before_install"
# after_install = "sweat_zone.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "sweat_zone.uninstall.before_uninstall"
# after_uninstall = "sweat_zone.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sweat_zone.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }
doc_events = {
	"Customer": {
		"on_update": "sweat_zone.events.customer.check_and_book_locker"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"sweat_zone.tasks.all"
#	],
#	"daily": [
#		"sweat_zone.tasks.daily"
#	],
#	"hourly": [
#		"sweat_zone.tasks.hourly"
#	],
#	"weekly": [
#		"sweat_zone.tasks.weekly"
#	],
#	"monthly": [
#		"sweat_zone.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "sweat_zone.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "sweat_zone.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "sweat_zone.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"sweat_zone.auth.validate"
# ]
