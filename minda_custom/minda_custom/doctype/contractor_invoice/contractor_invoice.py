# -*- coding: utf-8 -*-
# Copyright (c) 2018, Minda Sai Pvt LTd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import flt, add_days
from frappe.utils.data import today

class ContractorInvoice(Document):
    def validate(self):
        frappe.errprint("Contract Invoicing")

@frappe.whitelist()
def get_mandays(start_date,contractor):
    manheads = frappe.db.sql("""select distinct employee from `tabSalary Slip` where start_date = %s and contractor = %s""", (start_date,contractor), as_dict=1)
    bda = get_ss(start_date,contractor)
    return len(manheads),bda

def get_ss(start_date,contractor):
    la_total = b_total = da_total = basic_da = oa_total =eesic_total = epf_total = gross = sc_total= ot_total = eotesic_total = otsc_total = amount = c_total = 0
    ssp = frappe.get_all("Salary Slip",filters={'start_date':start_date,'contractor':contractor})
    for ss in ssp:
        # frappe.errprint(ss['name'])
        mandays = frappe.db.sql("""select sum(payment_days) as manday from `tabSalary Slip` where start_date = %s and contractor = %s""", (start_date,contractor), as_dict=1)
        for m in mandays:
            manday = m['manday']

        basic = frappe.db.sql("""select td.amount as basic from `tabSalary Detail` td where 
                td.salary_component='Basic' and td.parent = %s""",(ss['name']),as_dict=1)
        for b in basic:
            b_total += b['basic']
            # print b_total

        da = frappe.db.sql("""select td.amount as da from `tabSalary Detail` td where 
            td.salary_component='Dearness Allowance' and td.parent=%s""",(ss['name']),as_dict=1)
        for d in da:
            da_total += d['da']

        oa = frappe.db.sql("""select td.amount as oa from `tabSalary Detail` td where 
            td.salary_component='Other Allowances' and td.parent=%s""",(ss['name']),as_dict=1)
        for o in oa:
            oa_total += o['oa']    

        eesic = frappe.db.sql("""select td.amount as eesic from `tabSalary Detail` td where 
            td.salary_component='Employer ESIC' and td.parent=%s""",(ss['name']),as_dict=1)
        for esic in eesic:
            eesic_total += esic['eesic'] 

        epf = frappe.db.sql("""select td.amount as epf from `tabSalary Detail` td where 
            td.salary_component='Employer PF' and td.parent=%s""",(ss['name']),as_dict=1)
        for pf in epf:
            epf_total += pf['epf'] 

        sc = frappe.db.sql("""select td.amount as sc from `tabSalary Detail` td where 
            td.salary_component='Service Charge' and td.parent=%s""",(ss['name']),as_dict=1)
        for s in sc:
            sc_total += s['sc'] 

        ot = frappe.db.sql("""select td.amount as ot from `tabSalary Detail` td where 
            td.salary_component='Overtime' and td.parent=%s""",(ss['name']),as_dict=1)
        for t in ot:
            ot_total += t['ot']  

        eotesic = frappe.db.sql("""select td.amount as eotesic from `tabSalary Detail` td where 
            td.salary_component='Employer OT ESIC' and td.parent=%s""",(ss['name']),as_dict=1)
        for ote in eotesic:
            eotesic_total += ote['eotesic']

        otsc = frappe.db.sql("""select td.amount as otsc from `tabSalary Detail` td where 
            td.salary_component='OT Service Charge' and td.parent=%s""",(ss['name']),as_dict=1)
        for os in otsc:
            otsc_total += os['otsc']

        basic_da = b_total + da_total
        gross = basic_da + oa_total + eesic_total + epf_total + la_total
        amount = gross + sc_total + ot_total + eotesic_total + otsc_total
        sgst = flt(amount) * 0.09
        cgst = flt(amount) * 0.09
        sub_total = flt(amount) + sgst + cgst

        canteen = frappe.db.sql("""select td.amount as canteen from `tabSalary Detail` td where 
            td.salary_component='Canteen' and td.parent=%s""",(ss['name']),as_dict=1)
        for c in canteen:
            c_total += c['canteen']

        lla = frappe.db.sql("""select td.amount as lla from `tabSalary Detail` td where 
            td.salary_component='Line Leader Allowance' and td.parent=%s""",(ss['name']),as_dict=1)
        for la in lla:
            la_total += la['lla']

        gross_pay = sub_total - c_total
    return b_total,da_total,oa_total,basic_da,eesic_total,epf_total,gross,sc_total,ot_total,eotesic_total,otsc_total,amount,sgst,cgst,sub_total,manday,c_total,gross_pay,la_total