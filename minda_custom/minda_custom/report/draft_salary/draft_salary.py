# Copyright (c) 2013, Starboxes India and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import frappe
from datetime import datetime
from calendar import monthrange
from frappe import _, msgprint
from frappe.utils import flt


def execute(filters=None):
    if not filters:
        filters = {}

    columns = get_columns()

    data = []
    row = []
    conditions, filters = get_conditions(filters)
    total = 0
    salary_slips = get_salary_slips(conditions,filters)
    
    for ss in salary_slips:
        if ss.name:row = [ss.name]
        else:row = [""]

        if ss.employee:row += [ss.employee]
        else:row += [""] 

        if ss.employee_name:row += [ss.employee_name]
        else:row += [""]

        doj = frappe.db.get_value("Employee", {'employee':ss.employee},['date_of_joining'])
        if doj:row += [doj]
        else:row += [""]

        if ss.contractor:row += [ss.contractor]
        else:row += [""]

        if ss.grade:row += [ss.grade]
        else:row += [""]

        if ss.lwp:row += [ss.lwp]
        else:row += [""]  

        if ss.twd:row += [ss.twd]
        else:row += [""]  

        if ss.md:row += [ss.md]
        else:row += [""]

        if ss.twh:row += [ss.twh]
        else:row += [""]

        basic = frappe.db.get_value("Salary Detail", {'salary_component':'Basic ','parent':ss.name},['amount'])
        wg = frappe.db.get_value("Salary Detail", {'salary_component':'Wages','parent':ss.name},['amount'])
        lla = frappe.db.get_value("Salary Detail", {'salary_component':'Line Leader Allowance','parent':ss.name},['amount'])
        
        if ss.md:
            per_day_basic = flt(basic)/flt(ss.md)
            if per_day_basic:row += [per_day_basic]
            else:row += [""]
        else:
            row += ["",""]

        if ss.md:
            per_day_wages = flt(wg)/flt(ss.md)
            if per_day_wages:row += [per_day_wages]
            else:row += [""]
        else:
            row += ["",""]

        da = frappe.db.get_value("Salary Detail", {'salary_component':'Dearness Allowance ','parent':ss.name},['amount'])
        
        if ss.md:
            per_day_da = flt(da)/flt(ss.md)
            if per_day_da:row += [per_day_da]
            else:row += [""]
        else:
            row += ["",""]

        oa = frappe.db.get_value("Salary Detail", {'salary_component':'Other Allowances','parent':ss.name},['amount'])
        
        if ss.md:
            per_day_oa = flt(oa)/flt(ss.md)
            if per_day_oa:row += [per_day_oa]
            else:row += [""]
        else:
            row += ["",""]
        
        if ss.md:
            per_day_lla = flt(lla)/flt(ss.md)
            if per_day_lla:row += [per_day_lla]
            else:row += [""]
        else:
            row += ["",""]

           
        # per_day_oa = frappe.db.get_value("Salary Structure Employee", {'employee':ss.employee},['variable'])
        # if per_day_oa:row += [per_day_oa]
        # else:row += [""]
        
        per_day_total = flt(per_day_basic) + flt(per_day_da) + flt(per_day_oa) + flt(per_day_lla)
        if per_day_total:row += [ per_day_total ]
        else:row += [""]

        if basic:row += [basic]
        else:row += [""]
        
        if da:row += [da]
        else:row += [""]

        if oa:row += [oa]
        else:row += [""] 
        
        if ss.md:
            if lla:row += [lla]
            else:row += [""]
        else:
            row += ["",""] 

        if wg:row += [wg]
        else:row += [""]

        arrear= frappe.db.get_value("Salary Detail", {'salary_component':'Arrear','parent':ss.name},['amount'])
        if arrear:row += [arrear]
        else:row += [""]

        total = flt(basic) + flt(da) + flt(oa) + flt(wg) + flt(lla) + flt(arrear)    
        if total:row += [ total ]
        else:row += [""]
        
        epf = frappe.db.get_value("Salary Detail", {'salary_component':'Employer PF','parent':ss.name},['amount'])
        if epf:row += [epf]
        else:row += [""] 

        eesic = frappe.db.get_value("Salary Detail", {'salary_component':'Employer ESIC','parent':ss.name},['amount'])
        if eesic:row += [eesic]
        else:row += [""]     
        
        ot = frappe.db.get_value("Salary Detail", {'salary_component':'Overtime','parent':ss.name},['amount'])
        if ot:row += [ot]
        else:row += [""]
        
        eotesic = frappe.db.get_value("Salary Detail", {'salary_component':'Employer OT ESIC','parent':ss.name},['amount'])
        if eotesic:row += [eotesic]
        else:row += [""]
        
        otsc = frappe.db.get_value("Salary Detail", {'salary_component':'OT Service Charge','parent':ss.name},['amount'])
        if otsc:row += [otsc]
        else:row += [""]
        
        sc = frappe.db.get_value("Salary Detail", {'salary_component':'Service Charge','parent':ss.name},['amount'])
        if sc:row += [sc]
        else:row += [""] 

        if ss.gp:row += [ss.gp]
        else:row += [""]  
        
        canteen = frappe.db.get_value("Salary Detail", {'salary_component':'Canteen','parent':ss.name},['amount'])
        if canteen:row += [canteen]
        else:row += [""] 
        
        esic = frappe.db.get_value("Salary Detail", {'salary_component':'ESIC','parent':ss.name},['amount'])
        if esic:row += [esic]
        else:row += [""] 

        otesic = frappe.db.get_value("Salary Detail", {'salary_component':'OT ESIC','parent':ss.name},['amount'])
        if otesic:row += [otesic]
        else:row += [""] 

        ptax = frappe.db.get_value("Salary Detail", {'salary_component':'Professional Tax','parent':ss.name},['amount'])
        if ptax:row += [ptax]
        else:row += [""]

        pf = frappe.db.get_value("Salary Detail", {'salary_component':'Provident Fund','parent':ss.name},['amount'])
        if pf:row += [pf]
        else:row += [""]

        lwf = frappe.db.get_value("Salary Detail", {'salary_component':'Labour Welfare Fund','parent':ss.name},['amount'])
        if lwf:row += [lwf]
        else:row += [""]
       
        if ss.td:row += [ss.td]
        else:row += [""]

        if ss.rt:row += [ss.rt]
        else:row += [""]
                        
        data.append(row)

    return columns, data


def get_columns():
    columns = [
        _("Salary Slip Id") + ":Link/Salary Slip:150",
        _("Employee") + ":Data:100",
        _("Employee Name") + ":Data:120",
        _("Date of Joining") + ":Date:120",
        _("Contractor") + ":Data:100",
        _("Grade") + ":Data:100",
        _("Leave Without Pay") + ":Data:100",
        _("Working Days") + ":Data:100",
        _("Payment Days") + ":Float:100",
        _("OT Hours") + ":Float:100",
        _("Per Day Basic") + ":Currency:100",
        _("Per Day Wages") + ":Currency:100",
        _("Per Day DA") + ":Currency:100",
        _("Per Day OA") + ":Currency:100",
        _("Per Day Line Leader") + ":Currency:100",
        _("Per Day Total") + ":Currency:100",
        _("Basic") + ":Currency:120",
        _("DA") + ":Currency:120",
        _("Other Allowance") + ":Currency:120",
        _("Line Leader") + ":Currency:120",
        _("Wages") + ":Currency:120",
        _("Arrear") + ":Currency:100",
        _("Total") + ":Currency:120",
        _("Employer PF") + ":Currency:120",
        _("Employer ESIC") + ":Currency:100",
        _("Overtime") + ":Currency:100",
        _("Employer OT ESIC") + ":Currency:100",
        _("OT Service Charge") + ":Currency:100",
        _("Service Charge") + ":Currency:100",
        _("Gross Pay") + ":Currency:100",
        _("Canteen") + ":Currency:100",
        _("ESIC") + ":Currency:100",
        _("OT ESIC") + ":Currency:100",
        _("Professional Tax") + ":Currency:100",
        _("Provident Fund") + ":Currency:100",
        _("Labour Welfare Fund") + ":Currency:100",
        _("Total Deduction") + ":Currency:100",
        _("Net Pay") + ":Currency:100",
        
    ]
    return columns

def get_salary_slips(conditions,filters):
    salary_slips = frappe.db.sql("""select ss.contractor as contractor,ss.employee as employee,ss.employee_name as employee_name,ss.name as name, ss.grade as grade,ss.leave_without_pay as lwp, ss.total_working_days as twd,ss.payment_days as md,ss.total_working_hours as twh,ss.gross_pay as gp,ss.total_deduction as td,ss.gross_pay as gp,ss.rounded_total as rt from `tabSalary Slip` ss 
    where  %s order by employee""" % conditions, filters, as_dict=1)
    return salary_slips


def get_conditions(filters):
    conditions = ""
    if filters.get("from_date"): conditions += " start_date >= %(from_date)s"
    if filters.get("to_date"): conditions += " and end_date >= %(to_date)s"   
    if filters.get("employee"): conditions += " and employee = %(employee)s"
    return conditions, filters
    