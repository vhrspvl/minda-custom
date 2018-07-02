//Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt


frappe.query_reports["Active and Left Employee Report"] = {
	"filters": [
		{
			"fieldname":"month",
			"label": __("Month"),
			"fieldtype": "Select",
			"options": "January\nFebruary\nMarchr\nApril\nMay\nJune\nJuly\nAugust\nSeptember\nOctober\nNovember\nDecember",
			"default": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
            "December"][frappe.datetime.str_to_obj(frappe.datetime.get_today()).getMonth()],
        },
    ],   
}

