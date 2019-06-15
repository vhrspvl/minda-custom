# Copyright (c) 2013, Minda Sai Pvt LTd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import msgprint, _
from frappe.utils.data import today, get_timestamp
from frappe.utils import getdate, cint, add_months, date_diff, add_days, nowdate, \
    get_datetime_str, cstr, get_datetime, time_diff, time_diff_in_seconds
from datetime import datetime, timedelta


def execute(filters=None):
    if not filters:
        filters = {}

    if not filters.get("date"):
        msgprint(_("Please select date"), raise_exception=1)

    conditions, filters = get_conditions(filters)
    columns = get_columns(filters)
    date = filters.get("date")
    if date and getdate(date) > getdate(nowdate()):
        frappe.throw(_("Date cannot be in the Future"))
    data = []
    row = []
    total_working_hours = 0
    emp_list = get_employees(conditions, filters)
    for emp in emp_list:
        row = [emp.name,emp.employee_name]
        att_details = frappe.db.get_value("Attendance", {'attendance_date': date, 'employee': emp.name}, [
                                          'name', 'shift', 'attendance_date', 'status', 'in_time', 'out_time'], as_dict=True)
        if att_details:
            if att_details.in_time == '00:00:00':
                att_details.in_time = False
            if att_details.out_time == '00:00:00': 
                att_details.out_time = False   
            
            if att_details.attendance_date:
                row += [att_details.attendance_date]
            else:
                row += [""]

            if att_details.in_time:
                row += [att_details.in_time]
            else:
                row += ["00:00"]

            if att_details.out_time:
                row += [att_details.out_time]
            else:
                row += ["00:00"]
            if att_details.in_time and att_details.out_time:
                in_time_f = datetime.strptime(
                        att_details.in_time, '%H:%M:%S')
                out_time_f = datetime.strptime(
                    att_details.out_time, '%H:%M:%S')
                if out_time_f and in_time_f:
                    worked_hrs = out_time_f - in_time_f
                    row += [worked_hrs]
                else:
                    row += ["00:00:00"]
            else:
                row += [""]

            # if att_details.status:
            #     row += [att_details.status]
            # else:
            #     row += [""]
            
            if not (att_details.in_time and att_details.out_time):
                row += ['Absent']
            elif att_details.in_time and not att_details.out_time and attendance_date == today():
                row += ['IN']    
            elif att_details.in_time and not att_details.out_time:
                row += ['Failed Out Punch']
            else:
                row += [att_details.status]

        else:
            row += ["", "", "", "","Absent"]

        data.append(row)
    return columns, data


def get_columns(filters):
    columns = [
        _("Employee") + ":Link/Employee:90",
        _("Employee Name") + "::150",
        _("Attendance Date") + ":Date:120",
        _("In Time") + "::100",
        _("Out Time") + "::100",
        _("Working Hours") + "::120",
        _("Status") + "::120",
        # _("Remarks") + "::120",
    ]
    return columns


def get_employees(conditions, filters):
    frappe.errprint(conditions)
    employees = frappe.db.sql(
        """select * from tabEmployee where %s status = 'Active' and employment_type !='Contract'""" % conditions, filters, as_dict=1)
    return employees


def check_leave_record(employee, date):
    leave_record = frappe.db.sql("""select leave_type, half_day from `tabLeave Application`
    where employee = %s and %s between from_date and to_date and status = 'Approved'
    and docstatus = 1""", (employee, date), as_dict=True)
    if leave_record:
        if leave_record[0].half_day:
            status = 'Half Day'
        else:
            status = 'On Leave'
            leave_type = leave_record[0].leave_type

        return status, leave_type


def get_conditions(filters):
    conditions = ""
    if filters.get("employee"):
        conditions += " name = %(employee)s and"

    return conditions, filters
