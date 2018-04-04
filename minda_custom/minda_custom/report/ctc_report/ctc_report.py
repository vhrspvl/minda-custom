# Copyright (c) 2013, Starboxes India and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import frappe
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
    # conditions_emp = get_conditions(filters)
    # active_employees = get_active_employees(filters, conditions_emp)
    active_employees = get_active_employees()
    grand_earnings = 0
    grand_basic = 0
    grand_allowance = 0
    grand_dearness_allowance = 0
    grand_van_rate = 0
    grand_accomodation = 0
    grand_line_leader = 0
    from_date = datetime.strptime(filters.get("from_date"), '%Y-%m-%d')
    present_days = 0
    working_days = monthrange(
        cint(from_date.year), from_date.month)[1]
    payable_days = 0
    for emp in active_employees:
        row = [emp.name, emp.employee_name, emp.designation,
               emp.department]

        emp_present_days = get_employee_attendance(emp.name, filters)

        for present in emp_present_days:
            present_days = present.count
        holidays = get_holidays_for_employee(emp.name, filters)
        joining_date = frappe.db.get_value(
            "Employee", emp.name, ["date_of_joining"])
        no_of_holidays = 0
        for holiday in holidays:
            if datetime.strptime(holiday, '%Y-%m-%d').date() > joining_date:
                no_of_holidays += 1

        if emp_present_days:
            row += [present_days]
        else:
            row += [""]

        if no_of_holidays:
            row += [no_of_holidays]
        else:
            row += [""]

        payable_days = present_days

        if emp_present_days > 0:
            payable_days = present_days + no_of_holidays

        if payable_days:
            row += [payable_days]
        else:
            row += [""]

        # if emp_present_days and no_of_holidays:
        #     payable_days = present_days + no_of_holidays
        #     row += [payable_days]
        # else:
        #     row += [""]

        sse = frappe.db.get_value("Employee", {'employee': emp.name}, [
            'basic', 'allowance', 'dearness_allowance', 'van_rate', 'accomodation', 'line_leader'], as_dict=True)

        if sse:
            act_basic = flt(sse.basic)
            act_allowance = flt(sse.allowance)
            act_dearness_allowance = flt(sse.dearness_allowance)
            act_van_rate = flt(sse.van_rate)
            act_accomodation = flt(sse.accomodation)
            act_line_leader = flt(sse.line_leader)
            total_actuals = 0
            if act_basic:
                row += [round(act_basic)]
                total_actuals += act_basic
            else:
                row += ["0"]
            if act_allowance:
                row += [round(act_allowance)]
                total_actuals += act_allowance
            else:
                row += ["0"]
            if act_dearness_allowance:
                row += [round(act_dearness_allowance)]
                total_actuals += act_dearness_allowance
            else:
                row += [""]
            if act_van_rate:
                row += [round(act_van_rate)]
                total_actuals += act_van_rate
            else:
                row += [""]

            if act_accomodation:
                row += [round(act_accomodation)]
                total_actuals += act_accomodation
            else:
                row += [""]
            if act_line_leader:
                row += [round(act_line_leader)]
                total_actuals += act_line_leader
            else:
                row += ["0"]

            if present_days > 0:
                earned_basic = flt(act_basic) * flt(payable_days)
                earned_allowance = flt(act_allowance) * flt(payable_days)
                earned_dearness_allowance = flt(
                    act_dearness_allowance) * flt(payable_days)
                earned_van_rate = flt(act_van_rate) * flt(payable_days)
                earned_accomodation = flt(
                    act_accomodation) * flt(payable_days)
                earned_line_leader = flt(
                    act_line_leader) * flt(payable_days)
                total_earnings = 0
                if earned_basic:
                    row += [round(earned_basic)]
                    grand_basic += earned_basic
                    total_earnings += earned_basic
                else:
                    row += ["0"]
                if earned_allowance:
                    row += [round(earned_allowance)]
                    grand_allowance += earned_allowance
                    total_earnings += earned_allowance
                else:
                    row += ["0"]
                if earned_dearness_allowance:
                    row += [round(earned_dearness_allowance)]
                    grand_dearness_allowance += earned_dearness_allowance
                    total_earnings += earned_dearness_allowance
                else:
                    row += ["0"]
                if earned_van_rate:
                    row += [round(earned_van_rate)]
                    grand_van_rate += earned_van_rate
                    total_earnings += earned_van_rate
                else:
                    row += ["0"]
                if earned_accomodation:
                    row += [round(earned_accomodation)]
                    grand_accomodation += earned_accomodation
                    total_earnings += earned_accomodation
                else:
                    row += ["0"]
                if earned_line_leader:
                    row += [round(earned_line_leader)]
                    grand_line_leader += earned_line_leader
                    total_earnings += earned_line_leader
                else:
                    row += ["0"]
                if total_earnings:
                    grand_earnings += total_earnings
                    row += [round(total_earnings)]
                else:
                    row += ["0"]
            else:
                row += [""]
        else:
            row += ["0"]
        totals = ["Totals", "", "", "", "", "", "", "", "", "",
                  "", "", "", "", "", "", "", grand_basic, grand_allowance, grand_dearness_allowance, grand_van_rate, grand_accomodation, grand_line_leader, grand_earnings]
        data.append(row)

    data.append(totals)

    return columns, data


def get_columns(attendance):
    columns = [
        _("Employee") + ":Link/Employee:90",
        _("Employee Name") + ":Data:150",
        _("Designation") + ":Data:180",
        _("Department") + ":Data:180",
        _("PD") + ":Int:50",
        _("Holidays") + ":Int:50",
        _("Payable Days") + ":Int:50",
        _("Actual Basic") + ":Currency:100",
        _("Actual Allowance") + ":Currency:100",
        _("Actual Dearness Allowance") + ":Currency:100",
        _("Actual Van Rate") + ":Currency:100",
        _("Actual Accomodation") + ":Currency:100",
        _("Actual Line Leader") + ":Currency:100",
        _("Earned Basic") + ":Currency:100",
        _("Earned Allowance") + ":Currency:100",
        _("Earned Dearness Allowance") + ":Currency:100",
        _("Earned Van Rate") + ":Currency:100",
        _("Earned Accomodation") + ":Currency:100",
        _("Earned Line Leader") + ":Currency:100",
        _("Total Earnings") + ":Currency:100"

    ]
    return columns


def get_active_employees():
    active_employees = frappe.db.sql(
        """select emp.name,emp.employee_name,emp.department,emp.designation from `tabEmployee` emp where emp.status = "Active" order by emp.name""", as_dict=1)
    return active_employees


def get_holidays_for_employee(employee, filters):
    holiday_list = get_holiday_list_for_employee(employee)
    holidays = frappe.db.sql_list('''select holiday_date from `tabHoliday`
			where
				parent=%(holiday_list)s
				and holiday_date >= %(start_date)s
				and holiday_date <= %(end_date)s''', {
        "holiday_list": holiday_list,
        "start_date": filters.get("from_date"),
        "end_date": filters.get("to_date")
    })

    holidays = [cstr(i) for i in holidays]

    return holidays


def get_employee_attendance(employee, filters):
    employee_attendance = frappe.db.sql("""select count(*) as count from `tabAttendance` where \
        docstatus = 1 and status = 'Present' and employee= %s and attendance_date between %s and %s""", (employee, filters.get("from_date"), filters.get("to_date")), as_dict=1)
    return employee_attendance


def get_conditions(filters):
    conditions_emp = ""

    if filters.get("department"):
        conditions_emp += " AND emp.department = '%s'" % filters["department"]

    if filters.get("designation"):
        conditions_emp += " AND emp.designation = '%s'" % filters["designation"]

    return filters, conditions_emp
