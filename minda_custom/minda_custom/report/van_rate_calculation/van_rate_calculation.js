// Copyright (c) 2016, Minda Sai Pvt LTd and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Van Rate Calculation"] = {
	"filters": [
		{
			"fieldname": "from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": [frappe.datetime.add_months(frappe.datetime.get_today())],
			"reqd": 1
		},
		{
			"fieldname": "to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": [frappe.datetime.add_months(frappe.datetime.get_today())],
			"reqd": 1
        },
        // {
		// 	"fieldname":"date_range",
		// 	"label": __("Date Range"),
		// 	"fieldtype": "DateRange",
		// 	"default": [frappe.datetime.add_months(frappe.datetime.get_today(),-1), frappe.datetime.get_today()],
		// 	"reqd": 1
		// },
        {
			"fieldname": "line",
			"label": __("Line"),
            "fieldtype": "Link",
            "options":"Line"
        },
        {
			"fieldname": "contractor",
			"label": __("Contractor"),
            "fieldtype": "Link",
            "options":"Contractor"
		},
	]
}
