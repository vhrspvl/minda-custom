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
    # employees = get_employees(conditions, filters)
    # for employee in employees:
    total = 0
    salary_slips = get_salary_slips(conditions,filters)
    # basic,da,oa,ot,wg,pf,esic,canteen,pt,otesic,sc,otsc,eesic,eotesic,epf =  get_ss(filters)
    for ss in salary_slips:
        # frappe.errprint(ss)
        if ss.name:row = [ss.name]
        else:row = [""]

        if ss.employee:row += [ss.employee]
        else:row += [""] 

        if ss.employee_name:row += [ss.employee_name]
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
        per_day_basic = flt(basic)/flt(ss.md)
        
        if per_day_basic:row += [per_day_basic]
        else:row += [""]
        
        da = frappe.db.get_value("Salary Detail", {'salary_component':'Dearness Allowance ','parent':ss.name},['amount'])
        per_day_da = flt(da)/flt(ss.md)

        if per_day_da:row += [per_day_da]
        else:row += [""]

        per_day_oa = frappe.db.sql("""select variable from `tabSalary Structure Employee` where `tabSalary Structure Employee`.employee = %s""",(ss['employee']),as_dict=1)
        
        if per_day_oa:row += [per_day_oa]
        else:row += [""]
        
        if basic:row += [basic]
        else:row += [""]
        
        if da:row += [da]
        else:row += [""]

        oa = frappe.db.get_value("Salary Detail", {'salary_component':'Other Allowances','parent':ss.name},['amount'])
        if oa:row += [oa]
        else:row += [""]  

        total = flt(basic) + flt(da) + flt(oa)    
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
       
        if ss.td:row += [ss.td]
        else:row += [""]

        if ss.rt:row += [ss.rt]
        else:row += [""]
                        
        data.append(row)

    return columns, data

def get_ss(filters):
    from_date = filters.get("from_date")
    to_date = filters.get("to_date")
    b_total = da_total = oa_total = ot_total = wg_total = pf_total = esic_total = canteen_total = pt_total = otesic_total = sc_total = otsc_total = eesic_total = eotesic_total = epf_total = 0
    ssp = frappe.get_all("Salary Slip",filters={'start_date':from_date,'end_date':to_date})
    
    for ss in ssp:
        basics = frappe.db.sql("""select td.amount as basic from `tabSalary Detail` td where 
            td.salary_component='Basic' and td.parent=%s""",(ss['name']),as_dict=1)
        for b in basics:
            b_total = b['basic']
        da = frappe.db.sql("""select td.amount as da from `tabSalary Detail` td where 
            td.salary_component='Dearness Allowance' and td.parent=%s""",(ss['name']),as_dict=1)
        for d in da:
            da_total = d['da']
        oa = frappe.db.sql("""select td.amount as oa from `tabSalary Detail` td where 
            td.salary_component='Other Allowances' and td.parent=%s""",(ss['name']),as_dict=1)
        for o in oa:
            oa_total = o['oa']  
        ot = frappe.db.sql("""select td.amount as ot from `tabSalary Detail` td where 
            td.salary_component='Overtime' and td.parent=%s""",(ss['name']),as_dict=1)
        for t in ot:
            ot_total = t['ot'] 
        wg = frappe.db.sql("""select td.amount as wg from `tabSalary Detail` td where 
            td.salary_component='Wages' and td.parent=%s""",(ss['name']),as_dict=1)
        for w in wg:
            wg_total = w['wg']
        pf = frappe.db.sql("""select td.amount as pf from `tabSalary Detail` td where 
            td.salary_component='Provident Fund' and td.parent=%s""",(ss['name']),as_dict=1)
        for p in pf:
            pf_total = p['pf'] 
        esic = frappe.db.sql("""select td.amount as esic from `tabSalary Detail` td where 
            td.salary_component='ESIC' and td.parent=%s""",(ss['name']),as_dict=1)
        for e in esic:
            esic_total = e['esic'] 
        canteen = frappe.db.sql("""select td.amount as canteen from `tabSalary Detail` td where 
            td.salary_component='Canteen' and td.parent=%s""",(ss['name']),as_dict=1)
        for c in canteen:
            canteen_total = c['canteen']     
        ptax = frappe.db.sql("""select td.amount as pt from `tabSalary Detail` td where 
            td.salary_component='Professional Tax' and td.parent=%s""",(ss['name']),as_dict=1)
        for pt in ptax:
            pt_total = pt['pt'] 
        otesic = frappe.db.sql("""select td.amount as otesic from `tabSalary Detail` td where 
            td.salary_component='OT ESIC' and td.parent=%s""",(ss['name']),as_dict=1)
        for ote in otesic:
            otesic_total = ote['otesic']
        sc = frappe.db.sql("""select td.amount as sc from `tabSalary Detail` td where 
            td.salary_component='Service Charge' and td.parent=%s""",(ss['name']),as_dict=1)
        for s in sc:
            sc_total = s['sc']   
        otsc = frappe.db.sql("""select td.amount as otsc from `tabSalary Detail` td where 
            td.salary_component='OT Service Charge' and td.parent=%s""",(ss['name']),as_dict=1)
        for os in otsc:
            otsc_total = os['otsc']
        eesic = frappe.db.sql("""select td.amount as eesic from `tabSalary Detail` td where 
            td.salary_component='Employer ESIC' and td.parent=%s""",(ss['name']),as_dict=1)
        for ee in eesic:
            eesic_total = ee['eesic']
        eotesic = frappe.db.sql("""select td.amount as eotesic from `tabSalary Detail` td where 
            td.salary_component='Employer OT ESIC' and td.parent=%s""",(ss['name']),as_dict=1)
        for eote in eotesic:
            eotesic_total = eote['eotesic']    
        epf = frappe.db.sql("""select td.amount as epf from `tabSalary Detail` td where 
            td.salary_component='Employer PF' and td.parent=%s""",(ss['name']),as_dict=1)
        for ep in epf:
            epf_total = ep['epf'] 
        
    return b_total,da_total,oa_total,ot_total,wg_total,pf_total,esic_total,canteen_total,pt_total,otesic_total,sc_total,otsc_total,eesic_total,eotesic_total,epf_total


def get_columns():
    columns = [
        _("Salary Slip Id") + ":Data:150",
        _("Employee") + ":Data:100",
        _("Employee Name") + ":Data:120",
        _("Contractor") + ":Data:100",
        _("Grade") + ":Data:100",
        _("Leave Without Pay") + ":Data:100",
        _("Working Days") + ":Data:100",
        _("Payment Days") + ":Int:100",
        _("OT Hours") + ":Float:100",
        _("Per Day Basic") + ":Currency:100",
        _("Per Day DA") + ":Currency:100",
        _("Per Day OA") + ":Currency:100",
        _("Basic") + ":Currency:120",
        _("DA") + ":Currency:120",
        _("Other Allowance") + ":Currency:120",
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
        _("Total Deduction") + ":Currency:100",
        _("Net Pay") + ":Currency:100",
        
    ]
    return columns

def get_salary_slips(conditions,filters):
    salary_slips = frappe.db.sql("""select ss.contractor as contractor,ss.employee as employee,ss.employee_name as employee_name,ss.name as name, ss.grade as grade,ss.leave_without_pay as lwp, ss.total_working_days as twd,ss.payment_days as md,ss.total_working_hours as twh,ss.gross_pay as gp,ss.total_deduction as td,ss.gross_pay as gp,ss.rounded_total as rt from `tabSalary Slip` ss 
    where ss.docstatus = 0 %s order by employee""" % conditions, filters, as_dict=1)
    return salary_slips


def get_conditions(filters):
    conditions = ""
    if filters.get("from_date"): conditions += " and start_date >= %(from_date)s"
    if filters.get("to_date"): conditions += " and end_date >= %(to_date)s"   
    if filters.get("employee"): conditions += " and employee = %(employee)s"
    return conditions, filters
    