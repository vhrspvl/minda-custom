// Copyright (c) 2016, Minda Sai Pvt LTd and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Draft Salary-NEEM"] = {
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
        {
			"fieldname":"employee",
			"label": __("Employee"),
			"fieldtype": "Link",
			"options": "Employee"
        },
        {
			"fieldname":"company",
			"label": __("Company"),
			"fieldtype": "Link",
			"options": "Company",
			"default": frappe.defaults.get_user_default("Company")
		}
	]
}
