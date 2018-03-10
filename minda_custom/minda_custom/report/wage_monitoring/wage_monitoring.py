# Copyright (c) 2013, Minda Sai Pvt LTd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import cstr, cint, getdate


def execute(filters=None):
    columns, data = [], []
    row = []

    wage_monitor = get_wm(filters)
    for wm in wage_monitor:
        row = [wm.date]
        data.append(row)
    columns, row = get_columns(filters)
    return columns, data


def get_columns(filters):
    row = []
    columns = [_("Date") + "::120"]
    for wm in frappe.get_list("Wage Monitor", fields=["date", "line", "present"]):
        columns.append(_(wm["line"]) + ":Data:90")
        wm1 = frappe.db.sql(
            "select date,present from `tabWage Monitor` where line=%s", _(wm["line"]), as_dict=1)
        frappe.errprint(wm)
        row.append(wm["present"])
        row.append(wm["date"])
    return columns, row


def get_wm(filters):
    wm = frappe.db.sql(
        "select date,present,absent,calculated_wages from `tabWage Monitor`", as_dict=1)
    return wm
