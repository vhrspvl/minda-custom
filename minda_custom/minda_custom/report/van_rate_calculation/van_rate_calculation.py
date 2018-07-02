# Copyright (c) 2013, Starboxes India and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import frappe
import math
from frappe import _, msgprint
from frappe.utils import (cint, cstr, date_diff, flt, getdate, money_in_words,
                          nowdate, rounded, today)
from datetime import datetime
from calendar import monthrange
from erpnext.hr.doctype.employee.employee import get_holiday_list_for_employee


def execute(filters=None):
    if not filters:
        filters = {}

    columns = get_columns(filters)

    data = []
    row = []
    conditions, filters = get_conditions(filters)
    active_employees = get_active_employees(conditions, filters)
    # active_employees = get_active_employees()
    grand_total = 0
    grand_rate = 0
    from_date = datetime.strptime(filters.get("from_date"), '%Y-%m-%d')
    present_days = 0
    working_days = monthrange(
        cint(from_date.year), from_date.month)[1]
    frappe.errprint(active_employees)    
    for emp in active_employees:
        row = [emp.employee, emp.employee_name, emp.line,
               emp.contractor, emp.van_route]
        emp_present_days = get_employee_attendance(emp.employee, filters)

        for present in emp_present_days:
            present_days = present.count
        joining_date = frappe.db.get_value(
            "Employee", emp.employee, ["date_of_joining"])
        if emp_present_days:
            row += [present_days]
        else:
            row += [""]
        # if emp_present_days and no_of_holidays:
        #     payable_days = present_days + no_of_holidays
        #     row += [payable_days]
        # else:
        #     row += [""]

        sse = frappe.db.get_value("Employee", {'employee': emp.employee}, ['van_route',
            'van_rate'], as_dict=True)
        if sse:
            
            act_van_rate = flt(sse.van_rate)
            total_actuals = 0
            if act_van_rate:
                row += [round(act_van_rate)]
                total_actuals += act_van_rate
            else:
                row += [""]
            if present_days > 0:
                if sse.van_route == "APT":
                    earned_van_rate = flt('1000') +flt(present_days)*flt('12')
                else:
                    earned_van_rate = flt(act_van_rate) * flt(present_days)
                total = 0
                if earned_van_rate:
                    row += [round(earned_van_rate)]
                    grand_rate += earned_van_rate
                    total += earned_van_rate
                else:
                    row += [""]
                if total:
                    grand_total += total
                    row += [round(total)]
                else:
                    row += [""]
            else:
                row += ["", "", "", "", "", "", ""]
        else:
            row += ["", "", "", "", ""]
        data.append(row)

    return columns, data


def get_columns(attendance):
    columns = [
        _("Employee") + ":Link/Employee:90",
        _("Employee Name") + ":Data:150",
        _("Line") + ":Data:180",
        _("Contractor") + ":Data:180",
        _("Van Route") + ":Data:180",
        _("Present Days") + ":Int:100",
        _("Van Rate") + ":Currency:100",
        _("Total") + ":Currency:100"

    ]
    return columns


def get_active_employees(conditions, filters):
    
    from_date = filters.get("from_date")
    to_date = filters.get("to_date")
    active_employees = frappe.db.sql("""select distinct `tabAttendance`.employee,`tabAttendance`.employee_name,`tabAttendance`.contractor, `tabEmployee`.van_route from `tabAttendance` 
          Join `tabEmployee` ON `tabEmployee`.name =`tabAttendance`.employee where  
        `tabAttendance`.docstatus = 1 and `tabAttendance`.status = 'Present' and `tabAttendance`.attendance_date between %s and %s order by `tabAttendance`.contractor""", (filters.get("from_date"), filters.get("to_date")), as_dict=1)
    # active_employees = frappe.db.sql(
    #     """select emp.name,emp.employee_name,emp.line,emp.contractor,emp.van_route from `tabEmployee` emp where %s emp.status = "Active" order by emp.name""" % conditions, filters, as_dict=1)
    return active_employees


def get_employee_attendance(employee, filters):
    employee_attendance = frappe.db.sql("""select count(*) as count from `tabAttendance` where \
        docstatus = 1 and status = 'Present' and employee= %s and attendance_date between %s and %s""", (employee, filters.get("from_date"), filters.get("to_date")), as_dict=1)
    return employee_attendance


def get_conditions(filters):
    conditions = ""
    if filters.get("line"):
        conditions += "line = %(line)s and"
    if filters.get("contractor"):
        conditions += "contractor = %(contractor)s and"
    return conditions, filters
