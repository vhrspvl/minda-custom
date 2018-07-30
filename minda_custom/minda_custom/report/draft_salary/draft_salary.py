# Copyright (c) 2013, Starboxes India and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import frappe
from frappe import _, msgprint


def execute(filters=None):
    if not filters:
        filters = {}

    columns = get_columns()

    data = []
    row = []
    conditions, filters = get_conditions(filters)
    employees = get_employees(conditions, filters)
    for employee in employees:
        salary_slips = get_salary_slips(employee.name,filters)
        basic,da,oa,eesic,epf,ot,otesic,otsc,sc,canteen,esic,otesic,pf,pt =  get_ss(employee.name,filters)
        for ss in salary_slips:
            if ss.name:
                row += [ss.name]
            if ss.employee:
                row += [ss.employee]
            if ss.employee_name:
                row += [ss.employee_name]
            if ss.contractor:
                row += [ss.contractor]
            if ss.grade:
                row += [ss.grade]
            if ss.grade:
                row += [ss.leave_without_pay]
            if ss.grade:
                row += [ss.total_working_days]
            if ss.payment_days:
                row += [ss.payment_days]
            else:
                row += [""]
            if ss.total_working_hours:
                row += [ss.total_working_hours]
            else:
                row += [""]
            if basic:
                row += [basic]
            else:
                row += [""]
            if da:
                row += [da]
            else:
                row += [""]
            if oa:
                row += [oa]
            else:
                row += [""] 
            if epf:
                row += [epf]
            else:
                row += [""]
            if eesic:
                row += [eesic]
            else:
                row += [""]
            if ot:
                row += [ot]
            else:
                row += [""] 
            if otesic:
                row += [otesic]
            else:
                row += [""]
            if otsc:
                row += [otsc]
            else:
                row += [""] 
            if sc:
                row += [sc]
            else:
                row += [""]
            if ss.gross_pay:
                row += [ss.gross_pay]
            if canteen:
                row += [canteen]
            else:
                row += [""]
            if esic:
                row += [esic]
            else:
                row += [""]
            if otesic :
                row += [otesic]
            else:
                row += [""]
            if pt :
                row += [pt]
            else:
                row += [""]
            if pf:
                row += [pf]
            else:
                row += [""]
            if ss.total_deduction:
                row += [ss.total_deduction]
            if ss.rounded_total:
                row += [ss.rounded_total]
            data.append(row)

    return columns, data
def get_ss(employee,filters):
    from_date = filters.get("from_date")
    to_date = filters.get("to_date")
    b_total=da_total=oa_total=epf_total=eesic_total=ot_total=eotesic_total=otsc_total=sc_total=canteen_total=esic_total=otesic_total=pt_total=pf_total = 0
    ssp = frappe.get_all("Salary Slip",filters={'start_date':from_date,'end_date':to_date,'employee':employee})
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
        epf = frappe.db.sql("""select td.amount as epf from `tabSalary Detail` td where 
            td.salary_component='Employer PF' and td.parent=%s""",(ss['name']),as_dict=1)
        for ep in epf:
            epf_total = ep['epf']
        eesic = frappe.db.sql("""select td.amount as eesic from `tabSalary Detail` td where 
            td.salary_component='Employer ESIC' and td.parent=%s""",(ss['name']),as_dict=1)
        for ee in eesic:
            eesic_total = ee['eesic']
        ot = frappe.db.sql("""select td.amount as ot from `tabSalary Detail` td where 
            td.salary_component='Overtime' and td.parent=%s""",(ss['name']),as_dict=1)
        for t in ot:
            ot_total = t['ot'] 
        eotesic = frappe.db.sql("""select td.amount as eotesic from `tabSalary Detail` td where 
            td.salary_component='Employer OT ESIC' and td.parent=%s""",(ss['name']),as_dict=1)
        for eote in eotesic:
            eotesic_total = eote['eotesic']
        otsc = frappe.db.sql("""select td.amount as otsc from `tabSalary Detail` td where 
            td.salary_component='OT Service Charge' and td.parent=%s""",(ss['name']),as_dict=1)
        for os in otsc:
            otsc_total = os['otsc']
        sc = frappe.db.sql("""select td.amount as sc from `tabSalary Detail` td where 
            td.salary_component='Service Charge' and td.parent=%s""",(ss['name']),as_dict=1)
        for s in sc:
            sc_total = s['sc']
        canteen = frappe.db.sql("""select td.amount as canteen from `tabSalary Detail` td where 
            td.salary_component='Canteen' and td.parent=%s""",(ss['name']),as_dict=1)
        for c in canteen:
            canteen_total = c['canteen']     
        esic = frappe.db.sql("""select td.amount as esic from `tabSalary Detail` td where 
            td.salary_component='ESIC' and td.parent=%s""",(ss['name']),as_dict=1)
        for e in esic:
            esic_total = e['esic']
        otesic = frappe.db.sql("""select td.amount as otesic from `tabSalary Detail` td where 
            td.salary_component='OT ESIC' and td.parent=%s""",(ss['name']),as_dict=1)
        for ote in otesic:
            otesic_total = ote['otesic']
        ptax = frappe.db.sql("""select td.amount as pt from `tabSalary Detail` td where 
            td.salary_component='Professional Tax' and td.parent=%s""",(ss['name']),as_dict=1)
        for pt in ptax:
            pt_total = pt['pt'] 
        pf = frappe.db.sql("""select td.amount as pf from `tabSalary Detail` td where 
            td.salary_component='Provident Fund' and td.parent=%s""",(ss['name']),as_dict=1)
        for p in pf:
            pf_total = p['pf'] 
    return b_total,da_total,oa_total,epf_total,eesic_total,ot_total,eotesic_total,otsc_total,sc_total,canteen_total,esic_total,otesic_total,pt_total,pf_total 
def get_salary_slips(employee,filters):
    from_date = filters.get("from_date")
    to_date = filters.get("to_date")
    salary_slips = frappe.db.sql("""select ss.name,ss.employee,ss.employee_name,ss.contractor,ss.grade,ss.leave_without_pay,ss.total_working_days,ss.payment_days,ss.total_working_hours,ss.gross_pay,ss.total_deduction,ss.rounded_total from `tabSalary Slip` ss 
    left join `tabVan Rate Calculation` vrc on vrc.employee = ss.employee 
    where 
    ss.start_date=%s and ss.end_date=%s group by ss.employee having ss.employee=%s """,(from_date,to_date,employee),as_dict=1)
    return salary_slips
def get_columns():
    columns = [
        _("Salary Slip Id") + ":Data:120",
        _("Employee") + ":Link/Employee:100",
        _("Employee Name") + ":Data:100",
        _("Contractor") + ":Data:120",
        _("Grade") + ":Link/Grade:100",
        _("Leave Without Pay") + ":Int:90",
        _("Working Days") + ":Float:90",
        _("Payment Days") + ":Int:90",
        _("OT Hours") + ":Float:90",
        _("Basic") + ":Currency:120",
        _("DA") + ":Currency:120",
        _("Other Allowance") + ":Currency:120",
        _("Employer PF") + ":Currency:100",
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
def get_employees(conditions, filters):
    from_date = filters.get("from_date")
    to_date = filters.get("to_date")
    active_employees = frappe.db.sql(
        """select name from `tabEmployee` %s order by name""" % conditions, filters, as_dict=1)
    return active_employees
def get_conditions(filters):
    conditions = ""
    if filters.get("employee"):
        conditions += "where name = %(employee)s"
    return conditions, filters
        