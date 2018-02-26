// Copyright (c) 2016, Minda Sai Pvt LTd and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Daily Attendance Report"] = {
	"filters": [
		{
			"fieldname": "date",
			"label": __("Date"),
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
			"fieldname": "shift",
			"label": __("Employee Shift"),
			"fieldtype": "Link",
			"options": "Shift"
		},
	],
	"formatter": function (row, cell, value, columnDef, dataContext, default_formatter) {
		value = default_formatter(row, cell, value, columnDef, dataContext);
		if (dataContext["Status"] === 'Absent' || dataContext["Status"] === 'Late') {
			value = "<span style='color:red!important;font-weight:bold'>" + value + "</span>";
		}
		return value;
	}
}
