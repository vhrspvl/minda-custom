// Copyright (c) 2016, VHRS and contributors
// For license information, please see license.txt

frappe.query_reports["Attendance Performance Analysis"] = {
	"filters": [
		{
			"fieldname": "from_date",
			"label": "From Date",
			"fieldtype": "Date",
			"default": frappe.datetime.add_days(frappe.datetime.get_today(), -365),
			"reqd": 1
		},
		{
			"fieldname": "to_date",
			"label": "To Date",
			"fieldtype": "Date",
			"default": frappe.datetime.get_today(),
			"reqd": 1
		},
		{
			"fieldname": "employee",
			"label": __("Employee"),
			"fieldtype": "Link",
			"options": "Employee"
		},
		{
			"fieldname": "contractor",
			"label": __("Contractor"),
			"fieldtype": "Link",
			"options": "Contractor"
		},
		{
			"fieldname": "line",
			"label": __("Line"),
			"fieldtype": "Link",
			"options": "Line"
		},
		{
			"fieldname": "department",
			"label": __("Department"),
			"fieldtype": "Link",
			"options": "Department"
		}
	]
}
