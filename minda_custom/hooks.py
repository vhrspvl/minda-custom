# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "minda_custom"
app_title = "Minda Custom"
app_publisher = "Minda Sai Pvt LTd"
app_description = "All Customizations for Minda Sai"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "kennedy.j@mindasai.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/minda_custom/css/minda_custom.css"
# app_include_js = "/assets/minda_custom/js/minda_custom.js"

# include js, css files in header of web template
# web_include_css = "/assets/minda_custom/css/minda_custom.css"
# web_include_js = "/assets/minda_custom/js/minda_custom.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
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

# Website user home page (by function)
# get_website_user_home_page = "minda_custom.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "minda_custom.install.before_install"
# after_install = "minda_custom.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "minda_custom.notifications.get_notification_config"

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

doc_events = {
    # "Employee": {
    #     "on_update": "minda_custom.custom.update_status"
    # },
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
}

# Scheduled Tasks
# ---------------

scheduler_events = {
    "all": [
        "minda_custom.custom.removeduplicateatt"
    ],

    "daily_long": [
        "minda_custom.custom.emp_absent_today",
        "minda_custom.custom.send_daily_att_report",
        "minda_custom.custom.send_daily_linewise_report",
        "minda_custom.custom.removeduplicateatt",
        # "minda_custom.custom.update_leave_application",
        "minda_custom.custom.calculate_wages",
        "minda_custom.custom.send_wage_report",
    ],
    # "daily": [
    #     "minda_custom.custom.send_daily_att_report",
    #     "minda_custom.custom.send_daily_linewise_report",
    #     "minda_custom.custom.send_wage_report",
    # ],
    # "cron": {
    #     "30 16 * * *": [
    #         "minda_custom.custom.send_xlsx_report"
    #     ]
    # }
    # "hourly": [
    #     "minda_custom.custom.removeduplicateatt"
    # ],
    # 	"weekly": [
    # 		"minda_custom.tasks.weekly"
    # 	]
    # 	"monthly": [
    # 		"minda_custom.tasks.monthly"
    # 	]
}

# Testing
# -------

# before_tests = "minda_custom.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "minda_custom.event.get_events"
# }
