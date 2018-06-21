# -*- coding: utf-8 -*-
# Copyright (c) 2018, Minda Sai Pvt LTd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import flt, add_days
from frappe.utils.data import today

class CanteenMonitor(Document):
    def validate(self):
        present_count = self.present_count
        total = flt(self.guests) + flt(self.drivers) + flt(self.interviewees) + flt(self.other) + flt(self.present_count)
        self.head_count = total 
        self.total = total*self.average_wage
        # self.present_count = self.get_present_count()
@frappe.whitelist()
def get_present_count(day):
    present_count = frappe.db.sql("""select distinct employee from `tabAttendance` where
                    docstatus=1 and status='Present' and attendance_date = %s""", (day), as_dict=1)
    return len(present_count)

     
