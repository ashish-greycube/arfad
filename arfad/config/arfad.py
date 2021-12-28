from __future__ import unicode_literals
from frappe import _
import frappe


def get_data():
	return [
			{
			"label": _("Quick Accounts"),
			"icon": "fa fa-print",
			"items": [
				{
					"type": "doctype",
					"name": "Expense Entry",
					"label": _("Expense Entry"),
					"description": _("Expense Entry"),
					"hide_count": False
				},
				{
					"type": "doctype",
					"name": "Expense Entry Settings",
					"label": _("Expense Entry Settings"),
					"description": _("Expense Entry Settings"),
					"hide_count": True
				}				
			]
		},
		{
			"label": _("Reports"),
			"items": [
				{
					"type": "report",
					"name": "General Ledger Middle East",
					"is_query_report": True,
					"doctype": "GL Entry"
				}
			]
		}		
    ]
