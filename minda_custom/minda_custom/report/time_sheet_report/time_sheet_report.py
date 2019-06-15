# Copyright (c) 2013, VHRS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
import time
import math
from datetime import datetime,timedelta
from calendar import monthrange
from frappe.utils import getdate, cint, add_months, date_diff, add_days, nowdate, \
    get_datetime_str, cstr, get_datetime, time_diff, time_diff_in_seconds

def execute(filters=None):
    if not filters:
        filters = {}
    data = row = []
    filters["month"] = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov",
        "Dec"].index(filters.month) + 1  
    filters["total_days_in_month"] = monthrange(
        cint(filters.year), filters.month)[1]
    columns = [_("Name") + ":Link/Employee:100",_("Employee Name") + ":Data:120"]
    month = filters.month 
    if month == 0:
        month = 12
        filters.year = cint(filters.year) - 1
    tdm = monthrange(cint(filters.year), month)[1]
    for day in range(filters["total_days_in_month"]):   
        columns += [(_(day+1) + "::20") ] 
    employee = get_employees()
    for emp in employee:
        if emp:
            if emp.name:row = [emp.name]
            else: row = [""]
            if emp.employee_name:row += [emp.employee_name]
            else: row += [""]   
        data.append(row)         
       
    return columns, data

def get_employees():
    emp = frappe.db.sql("""select 
        * from `tabEmployee` where status='Active' """, as_dict=1)
    return emp

def get_conditions(filters):
    conditions = ""

    if filters.get("employee"):
        conditions += "AND employee = '%s'" % filters["employee"]
    return conditions
