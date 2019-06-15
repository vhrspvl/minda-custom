// Copyright (c) 2016, Minda Sai Pvt LTd and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["evaluvation pending"] = {
	"filters": [
		{
			"fieldname": "from_date",
			"label": __("Date of Skill Evaluation From"),
			"fieldtype": "Date",
			"default": frappe.datetime.month_start(),
			"reqd": 1
		},
		{
			"fieldname": "to_date",
			"label": __("Date of Skill Evaluation To"),
			"fieldtype": "Date",
			"default": frappe.datetime.get_today(),
			"reqd": 1
		},
	]
}
