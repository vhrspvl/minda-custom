# -*- coding: utf-8 -*-
# Copyright (c) 2019, Minda Sai Pvt LTd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class AssemblyEvaluation(Document):
    def autoname(self):
        if self.employee_code and self.month_of_evaluation:
            self.name = self.employee_code+"-"+self.month_of_evaluation



@frappe.whitelist()
def update_mis(employee,line):
    doc = frappe.get_doc("Employee", employee)
    doc.update({
        "line": line
    })
    doc.save(ignore_permissions=True)
    frappe.db.commit()