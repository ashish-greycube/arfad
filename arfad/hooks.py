# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "arfad"
app_title = "Arfad"
app_publisher = "GreyCube Technologies"
app_description = "Customization for Arfad"
app_icon = "octicon octicon-file-directory"
app_color = "green"
app_email = "admin@greycube.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/arfad/css/arfad.css"
# app_include_js = "/assets/arfad/js/arfad.js"

# include js, css files in header of web template
# web_include_css = "/assets/arfad/css/arfad.css"
# web_include_js = "/assets/arfad/js/arfad.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_js = {"Company" : "public/js/company.js"}	
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
# get_website_user_home_page = "arfad.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "arfad.install.before_install"
# after_install = "arfad.install.after_install"
after_migrate="arfad.migrations.after_migrations"
# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "arfad.notifications.get_notification_config"

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

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"arfad.tasks.all"
# 	],
# 	"daily": [
# 		"arfad.tasks.daily"
# 	],
# 	"hourly": [
# 		"arfad.tasks.hourly"
# 	],
# 	"weekly": [
# 		"arfad.tasks.weekly"
# 	]
# 	"monthly": [
# 		"arfad.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "arfad.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "arfad.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "arfad.task.get_dashboard_data"
# }

fixtures = [

      {
        "dt": "Custom Field", 
        "filters": [["name", "in", ["Company-default_employee_petty_cash_payable_account_cf","Company-default_vat_tax_account_cf"]]]
      }  			     

]