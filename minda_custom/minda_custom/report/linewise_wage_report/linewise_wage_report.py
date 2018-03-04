# Copyright (c) 2013, Minda Sai Pvt LTd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
import calendar
from calendar import monthrange
from frappe.utils import cstr, cint, getdate


def execute(filters=None):
    if not filters:
        filters = {}
    data, row = [], []
    total = 0
    columns = [_("Date") + "::120"]
    columns += get_columns(filters)

    filters["month"] = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov",
                        "Dec"].index(filters.month) + 1
    cal = calendar.Calendar()
    dates = cal.itermonthdates(cint(filters.year), filters.month)
    dateformat = []
    for day in dates:
        if day.month == filters.month:
            dateformat.append(day)
    for fday in dateformat:
        row1 = [cstr(fday)]
        for line in frappe.get_list("Line"):
            # att = frappe.db.sql(
            #     """select count(*) as count from `tabAttendance` where
            #     docstatus=1 and status='Present' and line=%s and attendance_date= %s""", (line["name"], filters.get("date")), as_dict=1)
            # for present in att:
            #     present_days = present.count
            #     total += present.count
            row1 += [""]
        row1 += [""]

        row2 = ["Shift I"]
        for line in frappe.get_list("Line"):
            att = frappe.db.sql(
                """select count(*) as count from `tabAttendance` where
                docstatus=1 and status='Present' and line=%s and attendance_date= %s and shift='A'""", (line["name"], filters.get("date")), as_dict=1)
            for present in att:
                present_days = present.count
                total += present.count
            row2 += [present_days]
        row2 += [total]

        row3 = ["Shift II"]
        for line in frappe.get_list("Line"):
            att = frappe.db.sql(
                """select count(*) as count from `tabAttendance` where
                docstatus=1 and status='Present' and line=%s and attendance_date= %s and shift='B'""", (line["name"], filters.get("date")), as_dict=1)
            for present in att:
                present_days = present.count
                total += present.count
            row3 += [present_days]
        row3 += [total]

        row4 = ["Shift III"]
        for line in frappe.get_list("Line"):
            att = frappe.db.sql(
                """select count(*) as count from `tabAttendance` where
                docstatus=1 and status='Present' and line=%s and attendance_date= %s and shift='C'""", (line["name"], filters.get("date")), as_dict=1)
            for present in att:
                present_days = present.count
                total += present.count
            row4 += [present_days]
        row4 += [total]

        data.append(row1)
        data.append(row2)
        data.append(row3)
        data.append(row4)

    return columns, data


def get_columns(filters):
    columns, data = [], []
    # for contractor in frappe.get_list("Contractor"):
    for line in frappe.get_list("Line"):
        columns.append(_(line["name"]) + "::90")
    columns.append(_("Total") + ":Int:120")

    return columns
