# Copyright (c) 2013, Starboxes India and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import frappe
from datetime import datetime
from calendar import monthrange
from frappe import _, msgprint


def execute(filters=None):
    if not filters:
        filters = {}

    columns = get_columns()

    data = []
    row = []
    conditions, filters = get_conditions(filters)
    # employees = get_employees(conditions, filters)
    # for employee in employees:
    
    salary_slips = get_salary_slips(conditions,filters)
    # basic,da,oa,ot,wg,pf,esic,canteen,pt,otesic,sc,otsc,eesic,eotesic,epf =  get_ss(filters)
    for ss in salary_slips:
        # frappe.errprint(ss)
        if ss.employee_name:row = [ss.employee_name]
        else:row = [""]    

        if ss.md:row += [ss.md]
        else:row += [""]

        if ss.twh:row += [ss.twh]
        else:row += [""]

        basic = frappe.db.get_value("Salary Detail", {'salary_component':'Basic ','parent':ss.name},['amount'])
        if basic:row += [basic]
        else:row += [""]
        
        da = frappe.db.get_value("Salary Detail", {'salary_component':'Dearness Allowance ','parent':ss.name},['amount'])
        if da:row += [da]
        else:row += [""]

        # if oa:
        #     row = [oa]
        # else:
        #     row = [""] 
        # if ot:
        #     row = [ot]
        # else:
        #     row = [""]    
        # if wg:
        #     row = [wg]
        # else:
        #     row = [""]
        # if ss.gp:
        #     row = [ss.gp]
        # else:
        #     row = [""]
        # if pf:
        #     row = [pf]
        # else:
        #     row = [""]
        # if esic:
        #     row = [esic]
        # else:
        #     row = [""]   
        # if canteen:
        #     row = [canteen]
        # else:
        #     row = [""] 
        # if pt:
        #     row = [pt]
        # else:
        #     row = [""]    
        # if otesic:
        #     row = [otesic]
        # else:
        #     row = [""]
        # if ss.td:
        #     row = [ss.td]
        # else:
        #     row = [""]
        # if sc:
        #     row = [sc]
        # else:
        #     row = [""]   
        # if otsc:
        #     row = [otsc]
        # else:
        #     row = [""] 
        # if eesic:
        #     row = [eesic]
        # else:
        #     row = [""]    
        # if eotesic:
        #     row = [eotesic]
        # else:
        #     row = [""]
        # if epf:
        #     row = [epf]
        # else:
        #     row = [""]

        # if ss.transport:
        #     row = [ss.transport]
        # else:
        #     row = [""]
                        
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
        _("Employee") + ":Data:180",
        _("Man Days") + ":Int:100",
        _("OT Hours") + ":Float:100",
        _("Basic") + ":Currency:120",
        _("DA") + ":Currency:120",
        _("Other Allowance") + ":Currency:120",
        _("Overtime") + ":Currency:100",
        _("Stipend") + ":Currency:100",
        _("Gross Pay") + ":Currency:100",
        _("Provident Fund") + ":Currency:100",
        _("ESIC") + ":Currency:100",
        _("Canteen") + ":Currency:100",
        _("Professional Tax") + ":Currency:100",
        _("OT ESIC") + ":Currency:100",
        _("Total Deduction") + ":Currency:100",
        _("Service Charge") + ":Currency:100",
        _("OT Service Charge") + ":Currency:100",
        _("Employer ESIC") + ":Currency:100",
        _("Employer OT ESIC") + ":Currency:100",
        _("Employer PF") + ":Currency:100",
        _("Transport") + ":Currency:100",
        
    ]
    return columns

def get_salary_slips(conditions,filters):
    salary_slips = frappe.db.sql("""select ss.employee as employee,ss.employee_name as employee_name,ss.name as name,ss.payment_days as md,ss.total_working_hours as twh,ss.gross_pay as gp,ss.total_deduction as td from `tabSalary Slip` ss 
    where ss.docstatus = 0 %s order by employee""" % conditions, filters, as_dict=1)
    return salary_slips


def get_conditions(filters):
    conditions = ""
    if filters.get("from_date"): conditions += " and start_date >= %(from_date)s"
    if filters.get("to_date"): conditions += " and end_date >= %(to_date)s"   
    if filters.get("employee"): conditions += " and employee = %(employee)s"
    return conditions, filters
    