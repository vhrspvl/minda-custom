# Copyright (c) 2013, VHRS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import frappe
from frappe import _, msgprint


def execute(filters=None):
    if not filters:
        filters = {}

    columns = get_columns()

    data = []
    row1 = row2 = row3 = row4 = row5 = row6 = row7 =  []
    row8 = row9 = row10 = row11 = row12 = row13 = []
    row14 = row15 = []
    basics = 0
    da = 0
    b_total = 0
    da_total = 0
    oa_total = 0
    ot_total = 0
    wg_total = 0
    pf_total = 0
    esic_total = 0
    canteen_total = 0
    pt_total = 0
    otesic_total = 0
    sc_total = 0
    otsc_total = 0
    eesic_total = 0
    eotesic_total = 0
    epf_total = 0
    conditions, filters = get_conditions(filters)
    salary_components = get_salary_components(conditions,filters)
    # for ss in salary_components:
    from_date = filters.get("from_date")
    to_date = filters.get("to_date")
    ssp = frappe.get_all("Salary Slip",filters={'start_date':from_date,'end_date':to_date })
    for ss in ssp:
        basics = frappe.db.sql("""select td.amount as basic from `tabSalary Detail` td where 
            td.salary_component='Basic' and td.parent=%s""",(ss['name']),as_dict=1)
        for b in basics:
            b_total += b['basic']
        da = frappe.db.sql("""select td.amount as da from `tabSalary Detail` td where 
            td.salary_component='Dearness Allowance' and td.parent=%s""",(ss['name']),as_dict=1)
        for d in da:
            da_total += d['da']
        oa = frappe.db.sql("""select td.amount as oa from `tabSalary Detail` td where 
            td.salary_component='Other Allowances' and td.parent=%s""",(ss['name']),as_dict=1)
        for o in oa:
            oa_total += o['oa']  
        ot = frappe.db.sql("""select td.amount as ot from `tabSalary Detail` td where 
            td.salary_component='Overtime' and td.parent=%s""",(ss['name']),as_dict=1)
        for t in ot:
            ot_total += t['ot'] 
        wg = frappe.db.sql("""select td.amount as wg from `tabSalary Detail` td where 
            td.salary_component='Wages' and td.parent=%s""",(ss['name']),as_dict=1)
        for w in wg:
            wg_total += w['wg']
        pf = frappe.db.sql("""select td.amount as pf from `tabSalary Detail` td where 
            td.salary_component='Provident Fund' and td.parent=%s""",(ss['name']),as_dict=1)
        for p in pf:
            pf_total += p['pf'] 
        esic = frappe.db.sql("""select td.amount as esic from `tabSalary Detail` td where 
            td.salary_component='ESIC' and td.parent=%s""",(ss['name']),as_dict=1)
        for e in esic:
            esic_total += e['esic'] 
        canteen = frappe.db.sql("""select td.amount as canteen from `tabSalary Detail` td where 
            td.salary_component='Canteen' and td.parent=%s""",(ss['name']),as_dict=1)
        for c in canteen:
            canteen_total += c['canteen']     
        ptax = frappe.db.sql("""select td.amount as pt from `tabSalary Detail` td where 
            td.salary_component='Professional Tax' and td.parent=%s""",(ss['name']),as_dict=1)
        for pt in ptax:
            pt_total += pt['pt'] 
        otesic = frappe.db.sql("""select td.amount as otesic from `tabSalary Detail` td where 
            td.salary_component='OT ESIC' and td.parent=%s""",(ss['name']),as_dict=1)
        for ote in otesic:
            otesic_total += ote['otesic']
        sc = frappe.db.sql("""select td.amount as sc from `tabSalary Detail` td where 
            td.salary_component='Service Charge' and td.parent=%s""",(ss['name']),as_dict=1)
        for s in sc:
            sc_total += s['sc']   
        otsc = frappe.db.sql("""select td.amount as otsc from `tabSalary Detail` td where 
            td.salary_component='OT Service Charge' and td.parent=%s""",(ss['name']),as_dict=1)
        for os in otsc:
            otsc_total += os['otsc']
        eesic = frappe.db.sql("""select td.amount as eesic from `tabSalary Detail` td where 
            td.salary_component='Employer ESIC' and td.parent=%s""",(ss['name']),as_dict=1)
        for ee in eesic:
            eesic_total += ee['eesic']
        eotesic = frappe.db.sql("""select td.amount as eotesic from `tabSalary Detail` td where 
            td.salary_component='Employer OT ESIC' and td.parent=%s""",(ss['name']),as_dict=1)
        for eote in eotesic:
            eotesic_total += eote['eotesic']    
        epf = frappe.db.sql("""select td.amount as epf from `tabSalary Detail` td where 
            td.salary_component='Employer PF' and td.parent=%s""",(ss['name']),as_dict=1)
        for ep in epf:
            epf_total += ep['epf']
           
    if b_total:
        row1 = ['Basic',b_total]
    else:
        row1= ["",""]
    if da_total:
        row2 = ['Dearness Allowance',da_total]
    else:
        row2= ["",""]
    if oa_total:
        row3 = ['Other Allowances',oa_total]
    else:
        row3= ["",""]
    if ot_total:
        row4 = ['Overtime',ot_total]
    else:
        row4 = ["",""]
    if wg_total:
        row5 = ['Wages',wg_total]
    else:
        row5 = ["",""]
    if pf_total:
        row6 = ['Provident Fund',pf_total]
    else:
        row6 = ["",""]
    if esic_total:
        row7 = ['ESIC', esic_total]
    else:
        row7 = ["",""]
    if canteen_total:
        row8 = ['Canteen',canteen_total]
    else:
        row8 = ["",""]
    if pt_total :
        row9 = ['Professional Tax',pt_total ]
    else:
        row9 = ["",""]
    if otesic_total:
        row10 = ['OT ESIC',otesic_total]
    else:
        row10 = ["",""]
    if sc_total :
        row11 = ['Service Charge',sc_total ]
    else:
        row11 = ["",""]
    if otsc_total:
        row12 = ['OT Service Charge',otsc_total]
    else:
        row12 = ["",""]
    if eesic_total :
        row13 = ['Employer ESIC', eesic_total ]
    else:
        row13 = ["",""]
    if eotesic_total:
        row14 = ['Employer OT ESIC',eotesic_total]
    else:
        row14 = ["",""]
    if epf_total:
        row15 = ['Employer PF',epf_total]
    else:
        row15 = ["",""]
    data.append(row1)
    data.append(row2)
    data.append(row3)
    data.append(row4)
    data.append(row5)
    data.append(row6)
    data.append(row7)
    data.append(row8)
    data.append(row9)
    data.append(row10)
    data.append(row11)
    data.append(row12)
    data.append(row13)
    data.append(row14)
    data.append(row15)

    return columns,data


def get_columns():
    columns = [
        _("Salary Components") + ":Data:180",
        _("Amount") + ":Currency:180",
    ]
    return columns

def get_salary_components(conditions,filters):
    salary_components = frappe.db.sql("""select name from `tabSalary Component` order by name""" , as_dict=1)
    return salary_components


def get_conditions(filters):
    conditions = ""
    if filters.get("from_date"): conditions += " and start_date >= %(from_date)s"
    if filters.get("to_date"): conditions += " and end_date >= %(to_date)s"  
    return conditions, filters