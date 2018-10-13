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
        self.total = self.amount + self.sgst + self.cgst

@frappe.whitelist()
def get_mandays(start_date,contractor):
    mandays = frappe.db.sql("""select distinct employee from `tabSalary Slip` where start_date = %s and contractor = %s""", (start_date,contractor), as_dict=1)
    bda = get_ss(start_date,contractor)
    return len(mandays),bda

def get_ss(start_date,contractor):
    b_total = da_total = basic_da = oa_total =esic_total = pf_total = gross = sc_total= ot_total = otesic_total = otsc_total = amount = 0
    ssp = frappe.get_all("Salary Slip",filters={'start_date':start_date,'contractor':contractor})
    for ss in ssp:
        # frappe.errprint(ss['name'])
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

        esic = frappe.db.sql("""select td.amount as esic from `tabSalary Detail` td where 
            td.salary_component='ESIC' and td.parent=%s""",(ss['name']),as_dict=1)
        for e in esic:
            esic_total += e['esic'] 

        pf = frappe.db.sql("""select td.amount as pf from `tabSalary Detail` td where 
            td.salary_component='Provident Fund' and td.parent=%s""",(ss['name']),as_dict=1)
        for p in pf:
            pf_total += p['pf'] 

        sc = frappe.db.sql("""select td.amount as sc from `tabSalary Detail` td where 
            td.salary_component='Service Charge' and td.parent=%s""",(ss['name']),as_dict=1)
        for s in sc:
            sc_total += s['sc'] 

        ot = frappe.db.sql("""select td.amount as ot from `tabSalary Detail` td where 
            td.salary_component='Overtime' and td.parent=%s""",(ss['name']),as_dict=1)
        for t in ot:
            ot_total += t['ot']  

        otesic = frappe.db.sql("""select td.amount as otesic from `tabSalary Detail` td where 
            td.salary_component='OT ESIC' and td.parent=%s""",(ss['name']),as_dict=1)
        for ote in otesic:
            otesic_total += ote['otesic']

        otsc = frappe.db.sql("""select td.amount as otsc from `tabSalary Detail` td where 
            td.salary_component='OT Service Charge' and td.parent=%s""",(ss['name']),as_dict=1)
        for os in otsc:
            otsc_total += os['otsc']

        basic_da = b_total + da_total
        gross = basic_da + oa_total + esic_total + pf_total 
        amount = gross + sc_total + ot_total + otesic_total + otsc_total
    return b_total,da_total,oa_total,basic_da,esic_total,pf_total,gross,sc_total,ot_total,otesic_total,otsc_total,amount