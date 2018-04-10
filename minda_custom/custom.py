# -*- coding: utf-8 -*-
# Copyright (c) 2017, VHRS and contributors
# For license information, please see license.txt

import frappe
from frappe.utils.data import today
from frappe import _
from frappe.utils import formatdate, getdate, cint, add_months, date_diff, add_days, flt, cstr
from frappe.utils.xlsxutils import make_xlsx
import requests
from erpnext.hr.doctype.employee.employee import get_holiday_list_for_employee


@frappe.whitelist()
def send_wage_report():
    custom_filter = {'date': add_days(today(), -1)}
    report = frappe.get_doc('Report', "Wage Monitor Report")
    columns, data = report.get_data(
        limit=100, filters=custom_filter, as_dict=True)
    spreadsheet_data = get_spreadsheet_data(columns, data)
    xlsx_file = make_xlsx(spreadsheet_data, "Minda Custom")
    data = xlsx_file.getvalue()
    attachments = [{
        'fname': add_days(today(), -1) + '.xlsx',
        'fcontent': data
    }]
    frappe.sendmail(
        recipients=['loganathan.k@mindasai.com', 'jayapradha@mindasai.com',
                    'ajay.agrawal@mindasai.com', 'kennedy.j@mindasai.com', 'sqlmurugan@mindasai.com', 'abdulla.pi@voltechgroup.com'],
        subject='Wage Monitor Report - ' +
        formatdate(add_days(today(), -1)),
        message='Kindly find the attached Excel Sheet of Daily Attendance Report of' + formatdate(
            add_days(today(), -1)),
        attachments=attachments
    )


def send_daily_att_report():
    custom_filter = {'date': add_days(today(), -1)}
    report = frappe.get_doc('Report', "Daily Attendance Report")
    columns, data = report.get_data(
        limit=100, filters=custom_filter, as_dict=True)
    spreadsheet_data = get_spreadsheet_data(columns, data)
    xlsx_file = make_xlsx(spreadsheet_data, "Attendance")
    data = xlsx_file.getvalue()
    attachments = [{
        'fname': add_days(today(), -1) + '.xlsx',
        'fcontent': data
    }]
    frappe.sendmail(
        recipients=['loganathan.k@mindasai.com', 'jayapradha@mindasai.com',
                    'ajay.agrawal@mindasai.com', 'kennedy.j@mindasai.com', 'sqlmurugan@mindasai.com', 'abdulla.pi@voltechgroup.com'],
        subject='Employee Attendance Report - ' +
        formatdate(add_days(today(), -1)),
        message='Kindly find the attached Excel Sheet of Daily Attendance Report of' + formatdate(
            add_days(today(), -1)),
        attachments=attachments
    )


def send_daily_linewise_report():
    custom_filter = {'date': add_days(today(), -1)}
    report = frappe.get_doc('Report', "Linewise Count")
    columns, data = report.get_data(
        limit=100, filters=custom_filter, as_dict=True)
    spreadsheet_data = get_spreadsheet_data(columns, data)
    xlsx_file = make_xlsx(spreadsheet_data, "Attendance")
    data = xlsx_file.getvalue()
    attachments = [{
        'fname': add_days(today(), -1) + '.xlsx',
        'fcontent': data
    }]
    frappe.sendmail(
        recipients=['loganathan.k@mindasai.com', 'jayapradha@mindasai.com',
                    'ajay.agrawal@mindasai.com', 'kennedy.j@mindasai.com', 'sqlmurugan@mindasai.com', 'abdulla.pi@voltechgroup.com'],
        subject='Employee Attendance Report - ' +
        formatdate(add_days(today(), -1)),
        message='Kindly find the attached Excel Sheet of Linewise Count Report of' + formatdate(
            add_days(today(), -1)),
        attachments=attachments
    )


def get_spreadsheet_data(columns, data):
    out = [[_(df.label) for df in columns], ]
    for row in data:
        new_row = []
        out.append(new_row)
        for df in columns:
            new_row.append(frappe.format(row[df.fieldname], df, row))

    return out


# @frappe.whitelist()
# def send_count_report():
#     custom_filter = {'date': add_days(today(), -1)}
#     report = frappe.get_doc('Report', "Linewise Count")
#     columns, data = report.get_data(
#         limit=500 or 500, filters=custom_filter, as_dict=True)
# # html = _("Kindly Find the attached Linewise Count Report for your reference")
#     html = frappe.render_template(
#         'frappe/templates/includes/print_table.html', {'columns': columns, 'data': data})
#     frappe.sendmail(
#         recipients=['abdulla.pi@voltechgroup.com'],
#         subject='Employee Linewise Present COunt Report - ' +
#         formatdate(add_days(today(), -1)),
#         message=html
#     )


@frappe.whitelist()
def update_in_biometric_machine(uid, uname):
    stgids = frappe.db.get_all("Service Tag")
    for stgid in stgids:
        url = "http://robot.camsunit.com/external/1.0/user/update?uid=%s&uname=%s&stgid=%s" % (
            uid, uname, stgid.name)
        r = requests.post(url)
    return r.content


@frappe.whitelist()
def delete_bulk():
    left_employees = frappe.get_list(
        "Employee", fields=["biometric_id"], filters={"status": "Left"})
    for l in left_employees:
        stgids = frappe.db.get_all("Service Tag")
        for stgid in stgids:
            uid = l.biometric_id
            url = "http://robot.camsunit.com/external/1.0/user/delete?uid=%s&stgid=%s" % (
                uid, stgid.name)
            frappe.errprint(url)
            r = requests.post(url)
            print r.content


@frappe.whitelist()
def delete_from_biometric_machine(uid, uname):
    stgids = frappe.db.get_all("Service Tag")
    for stgid in stgids:
        url = "http://robot.camsunit.com/external/1.0/user/delete?uid=%s&stgid=%s" % (
            uid, stgid.name)
        r = requests.post(url)
    return r.content


@frappe.whitelist()
def emp_absent_today():
    day = add_days(today(), -1)
    holiday = frappe.get_list("Holiday List", filters={
                              'holiday_date': day})
    if holiday:
        pass
    else:
        query = """SELECT emp.name FROM `tabAttendance` att, `tabEmployee` emp
		WHERE att.employee = emp.name AND att.attendance_date = '%s' AND att.status = 'Present' """ % (day)
        present_emp = frappe.db.sql(query, as_dict=True)
        for emp in frappe.get_list('Employee', filters={'status': 'Active'}):
            if emp in present_emp:
                pass
            else:
                doc = frappe.get_doc('Employee', emp)
                leave = frappe.db.sql("""select name from `tabLeave Application`
				where employee = %s and %s between from_date and to_date and status = 'Approved'
				and docstatus = 1""", (doc.name, day))
                if leave:
                    status = 'On Leave'
                else:
                    status = 'Absent'
                attendance = frappe.new_doc("Attendance")
                attendance.update({
                    "employee": doc.name,
                    "employee_name": doc.employee_name,
                    "attendance_date": day,
                    "in_time": '00:00',
                    "out_time": '00:00',
                    "status": status,
                    "line": doc.line,
                    "company": doc.company
                })
                attendance.save(ignore_permissions=True)
                attendance.submit()
                frappe.db.commit()


@frappe.whitelist()
def calculate_wages():
    day = add_days(today(), -1)
    # day = '2018-03-04'
    for line in frappe.get_list("Line"):
        att = frappe.db.sql(
            """select count(*) as count from `tabAttendance` where
                        docstatus=1 and status='Present' and line=%s and attendance_date= %s""", (line["name"], day), as_dict=1)
        for present in att:
            present_days = present.count

        att = frappe.db.sql(
            """select count(*) as count from `tabAttendance` where
                        docstatus=1 and status='Absent' and line=%s and attendance_date= %s""", (line["name"], day), as_dict=1)
        for absent in att:
            absent_days = absent.count

        wm = frappe.new_doc("Wage Monitor")
        wm.date = day
        wm.line = line["name"]
        wm.present = present_days
        wm.absent = absent_days
        wm.wage = '452'
        wm.calculated_wages = flt(wm.wage) * flt(wm.present)
        wm.save(ignore_permissions=True)

        # print absent_days


@frappe.whitelist()
def update_leave_application():
    day = add_days(today(), -1)
    employees = frappe.get_all('Employee', filters={"status": "Active"})
    for employee in employees:
        lwp = get_leave(employee.name, day)
        if lwp:
            pass
        else:
            query = """SELECT emp.name FROM `tabAttendance` att, `tabEmployee` emp
		               WHERE att.employee = emp.name AND att.status = 'Absent' AND att.attendance_date = '%s'""" % (day)
            absent_emp = frappe.db.sql(query, as_dict=True)
            if employee in absent_emp:
                leave_approvers = [l.leave_approver for l in frappe.db.sql("""select leave_approver from `tabEmployee Leave Approver` where parent = %s""",
                                                                           (employee.name), as_dict=True)]
                lap = frappe.new_doc("Leave Application")
                lap.leave_type = "Leave Without Pay"
                lap.status = "Approved"
                lap.follow_via_email = 0
                lap.description = "Absent Auto Marked"
                lap.from_date = day
                lap.to_date = day
                lap.employee = employee.name
                if leave_approvers:
                    lap.leave_approver = leave_approvers[0]
                else:
                    lap.leave_approver = "Administrator"
                lap.posting_date = day
                lap.company = frappe.db.get_value(
                    "Employee", employee.name, "company")
                lap.save(ignore_permissions=True)
                lap.submit()
                frappe.db.commit()


def get_leave(emp, day):
    leave = frappe.db.sql("""select name from `tabLeave Application`
				where employee = %s and %s between from_date and to_date
				""", (emp, day))
    return leave


@frappe.whitelist()
def get_employee_attendance(doc,method):
    holidays = get_holidays_for_employee(doc.employee, doc.start_date, doc.end_date)
    employee_attendance = frappe.db.sql("""select name,attendance_date from `tabAttendance` where \
            docstatus = 1 and status = 'Present' and employee= %s and attendance_date between %s and %s""", (doc.employee, doc.start_date, doc.end_date), as_dict=1)
    present_days = len(employee_attendance)
    for present in employee_attendance:
        if (present["attendance_date"].strftime('%Y-%m-%d')) in holidays:
            present_days -= 1

    doc.present_days = present_days


def get_holidays_for_employee(employee, start_date, end_date):
    holiday_list = get_holiday_list_for_employee(employee)
    holidays = frappe.db.sql_list('''select holiday_date from `tabHoliday`
        where
            parent=%(holiday_list)s
            and holiday_date >= %(start_date)s
            and holiday_date <= %(end_date)s''', {
        "holiday_list": holiday_list,
        "start_date": start_date,
        "end_date": end_date
    })

    holidays = [cstr(i) for i in holidays]

    return holidays
