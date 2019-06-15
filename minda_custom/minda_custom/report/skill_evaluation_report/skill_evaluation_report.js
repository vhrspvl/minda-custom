frappe.query_reports["Skill Evaluation Report"] = {
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
    