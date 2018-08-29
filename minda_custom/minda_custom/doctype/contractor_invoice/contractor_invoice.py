# -*- coding: utf-8 -*-
# Copyright (c) 2018, Minda Sai Pvt LTd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import flt, add_days
from frappe.utils.data import today

class ContractorInvoice(Document):
    pass

@frappe.whitelist()
def get_mandays(start_date,contractor):
    mandays = frappe.db.sql("""select distinct employee from `tabSalary Slip` where start_date = %s and contractor = %s""", (start_date,contractor), as_dict=1)
    bda = get_ss(start_date,contractor)
    return len(mandays),bda

def get_ss(start_date,contractor):
    b_total = da_total = basic_da = oa_total =total = 0 
    ssp = frappe.get_all("Salary Slip",filters={'start_date':start_date,'contractor':contractor})
    for ss in ssp:
        # frappe.errprint(ss['name'])
        basic = frappe.db.sql("""select td.amount as basic from `tabSalary Detail` td where 
                td.salary_component='Basic' and td.parent = %s""",(ss['name']),as_dict=1)
        for b in basic:
            b_total += b['basic']

        da = frappe.db.sql("""select td.amount as da from `tabSalary Detail` td where 
            td.salary_component='Dearness Allowance' and td.parent=%s""",(ss['name']),as_dict=1)
        for d in da:
            da_total += d['da']

        oa = frappe.db.sql("""select td.amount as oa from `tabSalary Detail` td where 
            td.salary_component='Other Allowances' and td.parent=%s""",(ss['name']),as_dict=1)
        for o in oa:
            oa_total += o['oa']    

        basic_da = b_total + da_total
        total = basic_da + oa_total
    return b_total,da_total,oa_total,basic_da,total