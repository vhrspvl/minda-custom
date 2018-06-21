# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Minda Custom",
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("Minda Custom")
		},
		{
			"color": "#589494",
			"icon": "octicon octicon-graph",
			"type": "page",
			"link": "dashboard",
			"label": _("Dashboard")
		},
	]
