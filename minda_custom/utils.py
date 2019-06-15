# -*- coding: utf-8 -*-
# Copyright (c) 2017, VHRS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import time
from frappe.utils.data import today, get_timestamp
from frappe.utils import getdate, cint, add_months, date_diff, add_days, nowdate, \
    get_datetime_str, cstr, get_datetime, time_diff, time_diff_in_seconds
from datetime import datetime, timedelta


@frappe.whitelist(allow_guest=True)
def attendance():
    global attendance_date, att_time
    min_time = time.strptime('05:30', '%H:%M')
    a_min_time = datetime.strptime('05:30', '%H:%M')
    a_max_time = datetime.strptime('07:30', '%H:%M')
    b_min_time = datetime.strptime('13:30', '%H:%M')
    b_max_time = datetime.strptime('15:30', '%H:%M')
    g_min_time = datetime.strptime('07:30', '%H:%M')
    g_max_time = datetime.strptime('09:30', '%H:%M')
    userid = frappe.form_dict.get("userid")
    stgid = frappe.form_dict.get("stgid")
    time_with_date = time.strftime("%Y-%m-%d %X", time.gmtime(
            int(frappe.form_dict.get("att_time"))))
    # create_attlog(userid,time_with_date)
    employee = frappe.db.get_value("Employee", {
        "biometric_id": userid, "status": "Active"})
    if employee:
        date = time.strftime("%Y-%m-%d", time.gmtime(
            int(frappe.form_dict.get("att_time"))))

        time_m = time.strftime("%H:%M:%S", time.gmtime(
            int(frappe.form_dict.get("att_time"))))

        time_with_date_f = datetime.strptime(
            time_with_date, "%Y-%m-%d %H:%M:%S")

        doc = frappe.get_doc("Employee", employee)
        
        if doc.employment_type != 'Contract':
            userid = frappe.form_dict.get("userid")
            biotime = frappe.form_dict.get("att_time")
            stgid = frappe.form_dict.get("stgid")
            create_pr(userid,biotime,stgid)

        prev_day = False
        if time.strptime(time_m, '%H:%M:%S') < min_time:
            date = add_days(date, -1)
            attendance_id = frappe.db.get_value("Attendance", {
                "employee": employee, "attendance_date": date})
            prev_day = True
        else:
            attendance_id = frappe.db.get_value("Attendance", {
                "employee": employee, "attendance_date": date})
        if attendance_id:
            attendance = frappe.get_doc(
                "Attendance", attendance_id)
            out_time = time_m
            in_time = attendance.in_time
            # return in_time.seconds
            times = [out_time, str(in_time)]
            if not prev_day:
                attendance.out_date = date
                attendance.out_time = max(times)
                attendance.in_time = min(times)
                attendance.db_update()
                frappe.db.commit()
                frappe.response.type = "text"
                return "ok"
            else:
                attendance.out_date = date
                attendance.out_time = out_time
                attendance.db_update()
                frappe.db.commit()
                frappe.response.type = "text"
                return "ok"
        else:
            attendance = frappe.new_doc("Attendance")
            in_time = time_m
            intime = datetime.strptime(
                in_time, '%H:%M:%S')
            # return type(a_min_time)
            if intime >= a_min_time and intime <= a_max_time:
                shift = "A"
            elif intime >= b_min_time and intime <= b_max_time:
                shift = "B"
            elif intime >= g_min_time and intime <= g_max_time:
                shift = "G"
            else:
                shift = "C"
            attendance.update({
                "employee": employee,
                "employee_name": doc.employee_name,
                "contractor": doc.contractor,
                "employment_type": doc.employment_type,
                "line": doc.line,
                "attendance_date": date,
                "status": "Present",
                "shift": shift,
                "service_tag_id": stgid,
                "in_time": in_time,
                "out_time": "00:00:00",
                "company": doc.company
            })
            attendance.save(ignore_permissions=True)
            attendance.submit()
            frappe.db.commit()
            frappe.response.type = "text"
            return "ok"
    else:
        employee = frappe.form_dict.get("userid")
        date = time.strftime("%Y-%m-%d", time.gmtime(
            int(frappe.form_dict.get("att_time"))))
        ure_id = frappe.db.get_value("Unregistered Employee", {
            "employee": employee, "attendance_date": date})
        if ure_id:
            attendance = frappe.get_doc(
                "Unregistered Employee", ure_id)
            out_time = time.strftime("%H:%M:%S", time.gmtime(
                int(frappe.form_dict.get("att_time"))))
            times = [out_time, str(attendance.in_time)]
            attendance.out_time = max(times)
            attendance.in_time = min(times)
            attendance.db_update()
            frappe.db.commit()
        else:
            attendance = frappe.new_doc("Unregistered Employee")
            in_time = time.strftime("%H:%M:%S", time.gmtime(
                int(frappe.form_dict.get("att_time"))))
            attendance.update({
                "employee": employee,
                "attendance_date": date,
                "stgid": frappe.form_dict.get("stgid"),
                "in_time": in_time,
            })
            attendance.save(ignore_permissions=True)
            frappe.db.commit()
        frappe.response.type = "text"
        return "ok"
        # query = """SELECT ro.name, ro.shift FROM `tabRoster` ro, `tabRoster Details` rod
        # WHERE rod.parent = ro.name AND ro.from_date <= '%s' AND ro.to_date >= '%s'
        # AND rod.employee = '%s' """ % (attendance_date, attendance_date, doc.employee)
        # roster = frappe.db.sql(query, as_list=1)

        # if len(roster) < 1:

        # else:
        #     doc.shift = roster[0][1]

        #     shft = frappe.get_doc("Shift Details", doc.shift)
        #     att_date = datetime.strptime(
        #         attendance_date, '%Y-%m-%d %H:%M:%S')

        #     if shft.in_out_required:
        #         shft_hrs = shft.hours_required_per_day.seconds

        #         shft_indate = datetime.combine(att_date, datetime.min.time())
        #         shft_intime = shft_indate + timedelta(0, shft.in_time.seconds)
        #         shft_intime_max = shft_intime + \
        #             timedelta(0, shft.delayed_entry_allowed_time.seconds)
        #         shft_intime_min = shft_intime - \
        #             timedelta(0, shft.early_entry_allowed_time.seconds)

        #         attendance_id = frappe.db.get_value("Attendance", {
        #             "employee": employee, "attendance_date": date})
        #         if attendance_id:
        #             attendance = frappe.get_doc(
        #                 "Attendance", attendance_id)
        #             out_time = time.strftime("%H:%M:%S", time.gmtime(
        #                 int(frappe.form_dict.get("att_time"))))
        #             times = [out_time, attendance.in_time]
        #             attendance.out_time = max(times)
        #             attendance.in_time = min(times)
        #             total_hrs = time_diff_in_seconds(
        #             attendance.out_time, attendance.in_time)
        #             attendance.overtime = (total_hrs - shft_hrs) / 3600
        #             attendance.db_update()
        #             frappe.db.commit()
        #             frappe.response.type = "text"
        #             return "ok"
        #         else:
        #             if att_date >= shft_intime_min and att_date <= shft_intime_max:
        #                 attendance = frappe.new_doc(
        #                     "Attendance")
        #                 intime = time.strftime("%H:%M:%S", time.gmtime(
        #                     int(frappe.form_dict.get("att_time"))))
        #                 attendance.update({
        #                     "employee": employee,
        #                     "employee_name": doc.employee_name,
        #                     "attendance_date": shft_indate,
        #                     "status": "Present",
        #                     "service_tag_id":stgid,
        #                     "in_time": intime,
        #                     "company": doc.company
        #                 })
        #                 attendance.save(
        #                     ignore_permissions=True)
        #                 attendance.submit()
        #                 frappe.db.commit()
        #                 frappe.response.type = "text"
        #                 return "ok"
        #             else:
        #                 attendance = frappe.new_doc(
        #                     "Attendance")
        #                 intime = time.strftime("%H:%M:%S", time.gmtime(
        #                         int(frappe.form_dict.get("att_time"))))
        #                 attendance.update({
        #                     "employee": employee,
        #                     "employee_name": doc.employee_name,
        #                     "attendance_date": shft_indate,
        #                     "status": "Absent",
        #                     "in_time": intime,
        #                     "company": doc.company
        #                 })
        #                 attendance.save(
        #                         ignore_permissions=True)
        #                 frappe.db.commit()
        #                 frappe.response.type = "text"
        #                 return "ok"
        #             frappe.response.type = "text"
        #             return "ok"
@frappe.whitelist()        
def create_pr(user,ptime,stgid):
    date = time.strftime("%Y-%m-%d", time.gmtime(
            int(ptime)))

    attendance_date = time.strftime("%Y-%m-%d %X", time.gmtime(
        int(ptime)))

    time_m = time.strftime("%H:%M:%S", time.gmtime(
        int(ptime)))
    employee = frappe.db.get_value("Employee", {
        "biometric_id": user, "status": "Active"})
    if employee:
        doc = frappe.get_doc("Employee", employee)
        pr_id = frappe.db.get_value("Punch Record", {
            "employee": employee, "attendance_date": date})
        if pr_id:
            pr = frappe.get_doc("Punch Record", pr_id)
            already_exist = False
            for t in pr.timetable:
                if str(t.punch_time) == time_m:
                    already_exist = True
            if not already_exist:
                pr.append("timetable", {
                    "punch_time": time_m
                })
                pr.save(ignore_permissions=True)
        else:
            pr = frappe.new_doc("Punch Record")
            pr.biotime = ptime
            pr.stgid = stgid
            pr.employee = employee
            pr.employee_name = doc.employee_name
            pr.attendance_date = date
            pr.append("timetable", {
                "punch_time": time_m
            })
            pr.insert()
            pr.save(ignore_permissions=True)
            frappe.db.commit()
    else:
        pr = frappe.new_doc("Punch Record")
        pr.biotime = ptime
        pr.stgid = stgid
        pr.unregistered_employee = user
        pr.attendance_date = date
        pr.append("timetable", {
            "punch_time": time_m
        })
        # pr.insert()
        pr.save(ignore_permissions=True)
        frappe.db.commit()





@frappe.whitelist()
def create_attlog(day):
    import requests
    from xml.etree import ElementTree
    from lxml import etree
    from StringIO import StringIO

    employees = frappe.get_all(
        "Employee", {"status": "Active", "employment_type":"Staff"})
    for emp in employees:
        emp = emp.name
        punch_record = frappe.db.exists(
            "Punch Record", {"attendance_date": day, "employee": emp})
        if punch_record:
            days = []
            pr = frappe.get_doc("Punch Record", punch_record)
            for t in pr.timetable:
                time_f = datetime.strptime(str(t.punch_time),'%H:%M:%S').time()
                day_f = datetime.combine(pr.attendance_date,time_f)
                day_f= datetime.strftime(day_f,'%d-%b-%Y %H:%M:%S')
                url = "http://115.124.107.68:9753/TPI/ThirdPartyIntegrationService.asmx/InsertEmployeeThumbLogFromBiometricDevice"
                headers = {'Content-Type': 'application/x-www-form-urlencoded'}
                data = {'CompanyID': '122', 'MachineEnrollNo': emp, 'MachineThumbTime': day_f, 'MachineName': '192.168.137.211'}
                r = requests.post(url,headers=headers,data=data)
                tree = etree.parse(StringIO((r.content)))
                res = tree.xpath('//text()')[0]
        
                if res == '@Thumb Log Already Saved':
                    frappe.errprint(res)
                    frappe.msgprint("""Attendance is Already fetched for %s and for time %s"""%(emp,day_f))
                elif res == '@Repeated Thumb Log Within 10 Minute Discarded':
                    frappe.errprint(res)
                    frappe.msgprint("""Repeated Thumb Log Within 10 Minute for %s and for time %s"""%(emp,day_f))
                elif res == '@Salary Process Completed For This Month, Cannot Add Attendance': 
                    frappe.errprint(res)
                    frappe.msgprint("""Salary Process Completed For This Month, Cannot Add Attendance""")   
                elif res == 'Successfull':
                    frappe.errprint(res)
                    frappe.msgprint("""Attendance is updated for %s and for time %s"""%(emp,day_f))
                else:
                    frappe.errprint(r.url)
                    frappe.errprint(data)
                    frappe.msgprint(res)


    

@frappe.whitelist()
def fetch_from_ui(from_date,to_date):
    from_date = (datetime.strptime(str(from_date), '%Y-%m-%d')).date()
    to_date = (datetime.strptime(str(to_date), '%Y-%m-%d')).date()
    for preday in daterange(from_date, to_date):
        create_attlog(preday)

def daterange(date1, date2):
    for n in range(int((date2 - date1).days)+1):
        yield date1 + timedelta(n)