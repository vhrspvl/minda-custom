# -*- coding: utf-8 -*-
# Copyright (c) 2018, Minda Sai Pvt LTd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Crimping(Document):
    pass
    # def validate(self):
    #     self.validate_levels()

    # def validate_levels(self):
    #     if self.ok:
    #         self.iws = '1'
    #         if self.partially_ok:
    #             self.iws = '0.5'
    #             if self.not_ok:
    #                 self.iws = '0'
    #             else:
    #                 self.iws = ''
    #         else:
    #             self.iws = ''
    #     else:
    #         self.iws = ''
