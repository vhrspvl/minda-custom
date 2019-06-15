# -*- coding: utf-8 -*-
# Copyright (c) 2019, Minda Sai Pvt LTd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class KomaxOperatorProductionObservation(Document):
	def autoname(self):
		if self.employee_code:
			self.name = self.employee_code
