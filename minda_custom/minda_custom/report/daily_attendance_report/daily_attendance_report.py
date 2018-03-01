# Copyright (c) 2013, Minda Sai Pvt LTd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import cstr, cint, getdate, today, nowdate
from frappe import msgprint, _


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
    emp_list = get_employees(conditions, filters)
    for emp in emp_list:
        row = [emp.name, emp.biometric_id, emp.employee_name,
               emp.contractor, emp.department, emp.line, emp.grade, emp.shift]
        att_details = frappe.db.get_value("Attendance", {'attendance_date': date, 'employee': emp.name}, [
                                          'name', 'shift', 'attendance_date', 'status', 'in_time', 'out_time'], as_dict=True)
        if att_details:
            if att_details.shift:
                if att_details.shift == 'A':
                    shift = 'Shift - I'
                elif att_details.shift == 'B':
                    shift = 'Shift - II'
                elif att_details.shift == 'C':
                    shift = 'Shift - III'
                elif att_details.shift == 'G':
                    shift = 'General Shift'

                row += [shift]
            else:
                row += [""]

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

            if att_details.status:
                row += [att_details.status]
            else:
                row += [""]

            # if att_details.in_time > 0 and att_details.status == 'Absent':
            #     row += ['Late']
            # elif att_details.in_time and not att_details.out_time:
            #     row += ['Failed Out Punch']
            # else:
            #     row += [""]

        else:
            row += ["", "", "", "", "Absent"]

        data.append(row)
    return columns, data


def get_columns(filters):
    columns = [
        _("Employee") + ":Link/Employee:90",
        _("Employee ID") + "::150",
        _("Employee Name") + "::150",
        _("Contractor") + "::180",
        _("Department") + "::180",
        _("Line") + "::180",
        _("Grade") + "::180",
        _("Shift") + "::180",
        _("Emp.Shift") + "::180",
        _("Attendance Date") + ":Date:90",
        _("In Time") + "::120",
        _("Out Time") + "::120",
        _("Status") + "::120",
        # _("Remarks") + "::120",
    ]
    return columns


def get_employees(conditions, filters):
    frappe.errprint(conditions)
    employees = frappe.db.sql(
        """select * from tabEmployee where %s status = 'Active'""" % conditions, filters, as_dict=1)
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
    if filters.get("contractor"):
        conditions += " contractor = %(contractor)s and"
    if filters.get("line"):
        conditions += " line = %(line)s and"
    if filters.get("shift"):
        conditions += " shift = %(shift)s and"
    return conditions, filters
