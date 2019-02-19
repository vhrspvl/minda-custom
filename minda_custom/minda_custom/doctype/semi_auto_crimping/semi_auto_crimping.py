# -*- coding: utf-8 -*-
# Copyright (c) 2019, Minda Sai Pvt LTd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class SemiAutoCrimping(Document):
	def autoname(self):
		if self.employee_code and self.month_of_evaluation:
			self.name = self.employee_code+"-"+self.month_of_evaluation



@frappe.whitelist()
def update_choose_question(choose_question):
    if choose_question:
        frappe.errprint(choose_question)
        cq = frappe.db.get_value("Choose Question", {"name": choose_question})
        if cq:
            exist_cq = frappe.get_doc("Choose Question", cq)
        else:
            exist_cq = frappe.new_doc("Choose Question")
        exist_cq.update({
		"choose_question":choose_question
        })
        exist_cq.save(ignore_permissions=True)
        frappe.db.commit()
        return "OK"