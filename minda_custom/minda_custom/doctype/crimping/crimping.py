# -*- coding: utf-8 -*-
# Copyright (c) 2018, Minda Sai Pvt LTd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Crimping(Document):
    pass
    # def validate(self):
    #         self.validate_levels()

    # def validate_levels(self):
    #     if self.total_practical_mark_obtained >= 50 and self.total_practical_mark_obtained == 60 :
    #         self.legend = 'L1 - Trainee'
    #     else:
    #         self.legend = ''
