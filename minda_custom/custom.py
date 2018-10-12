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
    html = frappe.render_template(
        'frappe/templates/include/print_table.html', {'columns': columns, 'data': data})    
    spreadsheet_data = get_spreadsheet_data(columns, data)
    xlsx_file = make_xlsx(spreadsheet_data, "Minda Custom")
    data = xlsx_file.getvalue()
    attachments = [{
        'fname': add_days(today(), -1) + '.xlsx',
        'fcontent': data
    }]
    frappe.sendmail(
        recipients=['loganathan.k@mindasai.com',
                    'ajay.agrawal@mindasai.com', 'kennedy.j@mindasai.com','abdulla.pi@voltechgroup.com'],
        subject='Wage Monitor Report - ' +
        formatdate(add_days(today(), -1)),
        message='Kindly find the attached Excel Sheet of Wage Monitor Report of ' + formatdate(
            add_days(today(), -1)) + html,
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
        recipients=['loganathan.k@mindasai.com',
                    'ajay.agrawal@mindasai.com', 'kennedy.j@mindasai.com', 'abdulla.pi@voltechgroup.com'],
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
        recipients=['loganathan.k@mindasai.com', 
                    'ajay.agrawal@mindasai.com', 'kennedy.j@mindasai.com', 'abdulla.pi@voltechgroup.com'],
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
        "Employee", fields=["biometric_id","name"], filters={"status": "Left","is_deleted":0})
    # print len(left_employees)    
    for l in left_employees:
        stgids = frappe.db.get_all("Service Tag")
        for stgid in stgids:
            uid = l.biometric_id
            url = "http://robot.camsunit.com/external/1.0/user/delete?uid=%s&stgid=%s" % (
                uid, stgid.name)
            r = requests.post(url)
            if r.content == "OK":
                emp = frappe.get_doc("Employee", l.name)
                emp.is_deleted = 1
                emp.db_update()
                frappe.db.commit()
                return r.content
           


@frappe.whitelist()
def delete_from_biometric_machine(uid, uname):
    stgids = frappe.db.get_all("Service Tag")
    for stgid in stgids:
        url = "http://robot.camsunit.com/external/1.0/user/delete?uid=%s&stgid=%s" % (
            uid, stgid.name)
        r = requests.post(url)
    return r.content



@frappe.whitelist()
def calculate_wages():
    day = add_days(today(), -1)
    # day = '2018-03-04'
    for line in frappe.get_list("Line",fields=['name','roll','roll_b','roll_c','roll_g']):
        a_att = frappe.db.sql(
            """select count(*) as count from `tabAttendance` where
                        docstatus=1 and status='Present' and shift='A' and line=%s and attendance_date= %s""", (line["name"], day), as_dict=1)
        for a in a_att:
            shift_a = a.count

        b_att = frappe.db.sql(
            """select count(*) as count from `tabAttendance` where
                        docstatus=1 and status='Present' and shift='B' and line=%s and attendance_date= %s""", (line["name"], day), as_dict=1)
        for b in b_att:
            shift_b = b.count

        g_att = frappe.db.sql("""select count(*) as count from `tabAttendance` where
                        docstatus=1 and status='Present' and shift='G' and line=%s and attendance_date= %s""", (line["name"], day), as_dict=1)
        for g in g_att:
            shift_g = g.count

        c_att = frappe.db.sql(
            """select count(*) as count from `tabAttendance` where
                        docstatus=1 and status='Present' and shift='C' and line=%s and attendance_date= %s""", (line["name"], day), as_dict=1)
        for c in c_att:
            shift_c = c.count

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
        wm.roll_a = line["roll"]
        wm.roll_b = line["roll_b"]
        wm.roll_g = line["roll_g"]
        wm.roll_c = line["roll_c"]
        wm.shift_a = shift_a
        wm.shift_b = shift_b
        wm.shift_c = shift_c
        wm.shift_g = shift_g
        wm.a_absent = line["roll"] - shift_a
        wm.b_absent = line["roll_b"] - shift_b
        wm.c_absent = line["roll_c"] - shift_c
        wm.g_absent = line["roll_g"] - shift_g
        wm.present = present_days
        wm.absent = wm.a_absent + wm.b_absent + wm.c_absent + wm.g_absent
        wm.wage = '464'
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

# @frappe.whitelist()
# def markatt():
#     att_list = frappe.get_all("Temp Att", fields=['att_date','emp','status'])
#     for att in att_list:
#         att_det = frappe.db.get_value("Attendance", {'attendance_date': att.att_date, 'employee': att.emp}, ['name','employee', 'status'], as_dict=True)
#         if att_det:
#             at1 = frappe.get_doc("Attendance",att_det.name)
#             at1.db_set("status","Half Day")
#             # frappe.delete_doc("Attendance",at1.name)
#             frappe.db.commit()                   


@frappe.whitelist()
def removeduplicateatt():
    get_att = frappe.db.sql("""SELECT name FROM `tabAttendance` WHERE attendance_date = %s GROUP BY employee
                    HAVING COUNT(employee) >1""",(today()),as_dict=1)
    if get_att:                 
        for att in get_att:                 
            obj = frappe.get_doc("Attendance",att["name"])
            obj.db_set("docstatus", 2)
            frappe.delete_doc("Attendance", obj.name)
            frappe.db.commit()

@frappe.whitelist()
def emp_sunday_attendance():
    
    days = ['2018-06-03','2018-06-10','2018-06-17','2018-06-24']
    for day in days:
        attendance_list = frappe.get_list("Attendance",filters={"attendance_date":day,"status":"Present"})
        for attendance in attendance_list:
            att = frappe.get_doc("Attendance",attendance)
            sunday_attendance = frappe.new_doc("Sunday Attendance")
            sunday_attendance.update({
                "employee": att.employee,
                "employee_name": att.employee_name,
                "attendance_date": att.attendance_date,
                "in_time": att.in_time,
                "out_time": att.out_time,
                "status": att.status,
                "line":att.line,
                "company": att.company
            })
            sunday_attendance.save(ignore_permissions=True)
            sunday_attendance.submit()
            frappe.db.commit()

def van_rate_calculator():
    from_date = '2018-06-01'
    to_date = '2018-06-30'
    for contractor in frappe.get_list("Contractor"):
        salary_slips = frappe.get_all("Salary Slip",fields=['employee','payment_days','contractor'],filters={'start_date':from_date,'end_date':to_date,'contractor':contractor['name']})
        for slip in salary_slips:
            for employee in frappe.get_list("Employee",fields=['name','van_route','van_rate'],filters={'name':slip['employee']}):
                vrc_id = frappe.get_list("Van Rate Calculation",filters={'from_date':from_date,'to_date':to_date,'employee':employee})
                if vrc_id:
                    pass
                else:    
                    vrc = frappe.new_doc("Van Rate Calculation")
                    if employee['van_route'] == 'APT':
                        total = flt(slip['payment_days']) * flt('12') + flt('1000')
                    else:
                        total = flt(slip['payment_days']) * flt(employee['van_rate'])    
                    vrc.update({
                        'from_date':from_date,
                        'to_date':to_date,
                        'van_route':employee['van_route'],
                        'van_rate':employee['van_rate'],
                        'employee':employee['name'],
                        'present_days':slip['payment_days'],
                        'contractor':slip['contractor'],
                        'total':total
                    })
                    vrc.save(ignore_permissions=True)

@frappe.whitelist()
def check_duplicate_employee():
    from frappeclient import FrappeClient
    client = FrappeClient("http://59.144.18.187", "Administrator", "mindaadmin@1234")
    emp = client.get_doc('Employee',fields=["employee_name", "biometric_id"])
    print emp


@ frappe.whitelist()
def holiday_att():
    employees = frappe.get_list('Employee', filters={"status": "Active"})
    for employee in employees:
        pre_day = frappe.db.get_value("Attendance", {
                        "employee": employee.name, "attendance_date": '2018-09-12'})
        next_day = frappe.db.get_value("Attendance", {
                        "employee": employee.name, "attendance_date": '2018-09-14'})
        if pre_day and next_day:
            emp = frappe.get_doc("Employee", employee['name'])                      
            att_id = frappe.db.get_value("Attendance", {
                        "employee": employee.name, "attendance_date": '2018-09-13'})
            if att_id:
                pass
            else:
                att = frappe.new_doc("Attendance")
                att.update({
                    "employee":emp.employee,
                    "employee_name":emp.employee_name,
                    "biometric_id":emp.biometric_id,
                    "attendance_date":'2018-09-13',
                    "status": "Present",
                    "company":emp.company,
                    "department":emp.department,
                    "contractor":emp.contractor
                })
                att.save(ignore_permissions=True)
                att.submit()
                frappe.db.commit()



                        





