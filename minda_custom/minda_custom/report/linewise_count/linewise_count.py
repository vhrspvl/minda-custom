# Copyright (c) 2013, Minda Sai Pvt LTd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _


def execute(filters=None):
    if not filters:
        filters = {}
    data, row = [], []
    total = 0
    columns = [_("Contractor") + ":Link/Contractor:120"]
    columns += get_columns(filters)
    # columns += [_("Total") + ":Int:120"]
    contractors = frappe.db.sql(
        """select name from `tabContractor` order by name""", as_dict=1)
    # line_list = ["HONDA - A1", "HONDA - A2", "HONDA - A3", "EXPORT - A"]

    for contractor in contractors:
        row = [contractor.name]
        cont = frappe.db.sql(
                """select count(employee) as count from `tabAttendance` where
                    docstatus=1 and status='Present' and contractor=%s and attendance_date= %s""", (contractor.name,filters.get("date")), as_dict=hrs123how to gethoh1)
        for present in cont:
            total_present_days = present.count
        for line in frappe.get_list("Line"):
            att = frappe.db.sql(
                """select count(employee) as count from `tabAttendance` where
                    docstatus=1 and status='Present' and contractor=%s and lisne=%s and attendance_date= %s""", (contractor.name, line["name"], filters.get("date")), as_dict=1)
            for present in att:
                present_days = present.count
                total += present.count
            row += [present_days]
        row += [total_present_days]
        data.append(row)

    return columns, data


def get_columns(filters):
    columns, data = [], []
    # for contractor in frappe.get_list("Contractor"):
    for line in frappe.get_list("Line"):
            # att = frappe.db.sql(
            #     """select count(*) as count from `tabAttendance` where
            #         docstatus=1 and status='Present' and contractor=%s and line=%s and attendance_date= %s""", (contractor.name, line["name"], filters.get("date")), as_dict=1)
            # for present in att:
            #     present_days = present.count
            # if present_days > 0:
        columns.append(_(line["name"]) + ":Int:90")
    columns.append(_("Total") + ":Int:120")

    return columns