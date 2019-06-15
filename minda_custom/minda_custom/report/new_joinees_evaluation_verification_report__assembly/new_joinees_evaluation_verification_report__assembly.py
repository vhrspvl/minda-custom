# Copyright (c) 2013, Minda Sai Pvt LTd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
import math
from calendar import monthrange
from datetime import datetime,timedelta,date
from dateutil.rrule import * 

def execute(filters=None):
    if not filters:
        filters = {}

    columns = get_columns()

    data = []
    row = []
    employee = employee_details()
    for e in employee:
        crimping = crimping_Details(e.biometric_id,filters)
        if crimping:
            row = [e.biometric_id,e.employee_name,e.line,e.shift]
            for c in crimping:
                row += [c.date_of_joining]
                row += [c.month_of_evaluation]
                
        # else:
        #     row += [""]
            data.append(row)
    return columns, data




def get_columns():
    columns = [
        _("Employee") + ":Link/Employee:150",
        _("Employee Name") + ":Data:150",
        _("Line") + ":Link/Line:150",
        _("Shift") + ":Link/Shift:150",
        _("Date of Joining") + ":Date:150",
        _("Month of Skill Evaluation") + ":Data:150"
    ]
    return columns


# def get_conditions(filters):
#     conditions = ""
#     # if filters.get("employee"):conditions += "AND att.employee = '%s'" % filters["employee"]
#     if filters.get("from_date"): conditions += "and c.date_of_skill_evaluatation >= %(from_date)s"
#     if filters.get("to_date"): conditions += " and c.date_of_skill_evaluatation <= %(to_date)s"    
#     return conditions, filters


def employee_details():
    employee = frappe.db.sql(
        """select biometric_id,employee_name,shift,department,designation,line from `tabEmployee` where status = "Active" and line like "%%ass%%" """, as_dict = 1)
    return employee


def crimping_Details(emp,filters):
    crimp = frappe.db.sql(
        """select employee_code,associate,line_name,date_of_joining,date_of_skill_evaluatation,month_of_evaluation from `tabAssembly Evaluation` where employee_code = %s and is_evaluate=0 and date_of_skill_evaluatation between %s and %s """,(emp,filters.from_date,filters.to_date) , as_dict=1)
    return crimp


# Copyright (c) 2013, Minda Sai Pvt LTd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
import math
from calendar import monthrange
from datetime import datetime,timedelta,date
from dateutil.rrule import * 

def execute(filters=None):
    if not filters:
        filters = {}

    columns = get_columns()

    data = []
    row = []
    employee = employee_details()
    for e in employee:
        crimping = crimping_Details(e.biometric_id,filters)
        if crimping:
            row = [e.biometric_id,e.employee_name,e.line,e.shift]
            for c in crimping:
                row += [c.date_of_joining]
                row += [c.month_of_evaluation]
                
        # else:
        #     row += [""]
            data.append(row)
    return columns, data




def get_columns():
    columns = [
        _("Employee") + ":Link/Employee:150",
        _("Employee Name") + ":Data:150",
        _("Line") + ":Link/Line:150",
        _("Shift") + ":Link/Shift:150",
        _("Date of Joining") + ":Date:150",
        _("Month of Skill Evaluation") + ":Data:150"
    ]
    return columns


# def get_conditions(filters):
#     conditions = ""
#     # if filters.get("employee"):conditions += "AND att.employee = '%s'" % filters["employee"]
#     if filters.get("from_date"): conditions += "and c.date_of_skill_evaluatation >= %(from_date)s"
#     if filters.get("to_date"): conditions += " and c.date_of_skill_evaluatation <= %(to_date)s"    
#     return conditions, filters


def employee_details():
    employee = frappe.db.sql(
        """select biometric_id,employee_name,shift,department,designation,line from `tabEmployee` where status = "Active" and line like "%%ass%%" """, as_dict = 1)
    return employee


def crimping_Details(emp,filters):
    crimp = frappe.db.sql(
        """select employee_code,associate,line_name,date_of_joining,date_of_skill_evaluatation,month_of_evaluation from `tabAssembly Evaluation` where employee_code = %s and is_evaluate=0 and date_of_skill_evaluatation between %s and %s """,(emp,filters.from_date,filters.to_date) , as_dict=1)
    return crimp


# Copyright (c) 2013, Minda Sai Pvt LTd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
import math
from calendar import monthrange
from datetime import datetime,timedelta,date
from dateutil.rrule import * 

def execute(filters=None):
    if not filters:
        filters = {}

    columns = get_columns()

    data = []
    row = []
    employee = employee_details()
    for e in employee:
        crimping = crimping_Details(e.biometric_id,filters)
        if crimping:
            row = [e.biometric_id,e.employee_name,e.line,e.shift]
            for c in crimping:
                row += [c.date_of_joining]
                row += [c.month_of_evaluation]
                
        # else:
        #     row += [""]
            data.append(row)
    return columns, data




def get_columns():
    columns = [
        _("Employee") + ":Link/Employee:150",
        _("Employee Name") + ":Data:150",
        _("Line") + ":Link/Line:150",
        _("Shift") + ":Link/Shift:150",
        _("Date of Joining") + ":Date:150",
        _("Month of Skill Evaluation") + ":Data:150"
    ]
    return columns


# def get_conditions(filters):
#     conditions = ""
#     # if filters.get("employee"):conditions += "AND att.employee = '%s'" % filters["employee"]
#     if filters.get("from_date"): conditions += "and c.date_of_skill_evaluatation >= %(from_date)s"
#     if filters.get("to_date"): conditions += " and c.date_of_skill_evaluatation <= %(to_date)s"    
#     return conditions, filters


def employee_details():
    employee = frappe.db.sql(
        """select biometric_id,employee_name,shift,department,designation,line from `tabEmployee` where status = "Active" and line like "%%ass%%" """, as_dict = 1)
    return employee


def crimping_Details(emp,filters):
    crimp = frappe.db.sql(
        """select employee_code,associate,line_name,date_of_joining,date_of_skill_evaluatation,month_of_evaluation from `tabAssembly Evaluation` where employee_code = %s and is_evaluate=0 and date_of_skill_evaluatation between %s and %s """,(emp,filters.from_date,filters.to_date) , as_dict=1)
    return crimp


# Copyright (c) 2013, Minda Sai Pvt LTd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
import math
from calendar import monthrange
from datetime import datetime,timedelta,date
from dateutil.rrule import * 

def execute(filters=None):
    if not filters:
        filters = {}

    columns = get_columns()

    data = []
    row = []
    employee = employee_details()
    for e in employee:
        crimping = crimping_Details(e.biometric_id,filters)
        if crimping:
            row = [e.biometric_id,e.employee_name,e.line,e.shift]
            for c in crimping:
                row += [c.date_of_joining]
                row += [c.month_of_evaluation]
                
        # else:
        #     row += [""]
            data.append(row)
    return columns, data




def get_columns():
    columns = [
        _("Employee") + ":Link/Employee:150",
        _("Employee Name") + ":Data:150",
        _("Line") + ":Link/Line:150",
        _("Shift") + ":Link/Shift:150",
        _("Date of Joining") + ":Date:150",
        _("Month of Skill Evaluation") + ":Data:150"
    ]
    return columns


# def get_conditions(filters):
#     conditions = ""
#     # if filters.get("employee"):conditions += "AND att.employee = '%s'" % filters["employee"]
#     if filters.get("from_date"): conditions += "and c.date_of_skill_evaluatation >= %(from_date)s"
#     if filters.get("to_date"): conditions += " and c.date_of_skill_evaluatation <= %(to_date)s"    
#     return conditions, filters


def employee_details():
    employee = frappe.db.sql(
        """select biometric_id,employee_name,shift,department,designation,line from `tabEmployee` where status = "Active" and line like "%%ass%%" """, as_dict = 1)
    return employee


def crimping_Details(emp,filters):
    crimp = frappe.db.sql(
        """select employee_code,associate,line_name,date_of_joining,date_of_skill_evaluatation,month_of_evaluation from `tabAssembly Evaluation` where employee_code = %s and is_evaluate=0 and date_of_skill_evaluatation between %s and %s """,(emp,filters.from_date,filters.to_date) , as_dict=1)
    return crimp


# Copyright (c) 2013, Minda Sai Pvt LTd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
import math
from calendar import monthrange
from datetime import datetime,timedelta,date
from dateutil.rrule import * 

def execute(filters=None):
    if not filters:
        filters = {}

    columns = get_columns()

    data = []
    row = []
    employee = employee_details()
    for e in employee:
        crimping = crimping_Details(e.biometric_id,filters)
        if crimping:
            row = [e.biometric_id,e.employee_name,e.line,e.shift]
            for c in crimping:
                row += [c.date_of_joining]
                row += [c.month_of_evaluation]
                
        # else:
        #     row += [""]
            data.append(row)
    return columns, data




def get_columns():
    columns = [
        _("Employee") + ":Link/Employee:150",
        _("Employee Name") + ":Data:150",
        _("Line") + ":Link/Line:150",
        _("Shift") + ":Link/Shift:150",
        _("Date of Joining") + ":Date:150",
        _("Month of Skill Evaluation") + ":Data:150"
    ]
    return columns


# def get_conditions(filters):
#     conditions = ""
#     # if filters.get("employee"):conditions += "AND att.employee = '%s'" % filters["employee"]
#     if filters.get("from_date"): conditions += "and c.date_of_skill_evaluatation >= %(from_date)s"
#     if filters.get("to_date"): conditions += " and c.date_of_skill_evaluatation <= %(to_date)s"    
#     return conditions, filters


def employee_details():
    employee = frappe.db.sql(
        """select biometric_id,employee_name,shift,department,designation,line from `tabEmployee` where status = "Active" and line like "%%ass%%" """, as_dict = 1)
    return employee


def crimping_Details(emp,filters):
    crimp = frappe.db.sql(
        """select employee_code,associate,line_name,date_of_joining,date_of_skill_evaluatation,month_of_evaluation from `tabAssembly Evaluation` where employee_code = %s and is_evaluate=0 and date_of_skill_evaluatation between %s and %s """,(emp,filters.from_date,filters.to_date) , as_dict=1)
    return crimp


# Copyright (c) 2013, Minda Sai Pvt LTd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
import math
from calendar import monthrange
from datetime import datetime,timedelta,date
from dateutil.rrule import * 

def execute(filters=None):
    if not filters:
        filters = {}

    columns = get_columns()

    data = []
    row = []
    employee = employee_details()
    for e in employee:
        crimping = crimping_Details(e.biometric_id,filters)
        if crimping:
            row = [e.biometric_id,e.employee_name,e.line,e.shift]
            for c in crimping:
                row += [c.date_of_joining]
                row += [c.month_of_evaluation]
                
        # else:
        #     row += [""]
            data.append(row)
    return columns, data




def get_columns():
    columns = [
        _("Employee") + ":Link/Employee:150",
        _("Employee Name") + ":Data:150",
        _("Line") + ":Link/Line:150",
        _("Shift") + ":Link/Shift:150",
        _("Date of Joining") + ":Date:150",
        _("Month of Skill Evaluation") + ":Data:150"
    ]
    return columns


# def get_conditions(filters):
#     conditions = ""
#     # if filters.get("employee"):conditions += "AND att.employee = '%s'" % filters["employee"]
#     if filters.get("from_date"): conditions += "and c.date_of_skill_evaluatation >= %(from_date)s"
#     if filters.get("to_date"): conditions += " and c.date_of_skill_evaluatation <= %(to_date)s"    
#     return conditions, filters


def employee_details():
    employee = frappe.db.sql(
        """select biometric_id,employee_name,shift,department,designation,line from `tabEmployee` where status = "Active" and line like "%%ass%%" """, as_dict = 1)
    return employee


def crimping_Details(emp,filters):
    crimp = frappe.db.sql(
        """select employee_code,associate,line_name,date_of_joining,date_of_skill_evaluatation,month_of_evaluation from `tabAssembly Evaluation` where employee_code = %s and is_evaluate=0 and date_of_skill_evaluatation between %s and %s """,(emp,filters.from_date,filters.to_date) , as_dict=1)
    return crimp


# Copyright (c) 2013, Minda Sai Pvt LTd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
import math
from calendar import monthrange
from datetime import datetime,timedelta,date
from dateutil.rrule import * 

def execute(filters=None):
    if not filters:
        filters = {}

    columns = get_columns()

    data = []
    row = []
    employee = employee_details()
    for e in employee:
        crimping = crimping_Details(e.biometric_id,filters)
        if crimping:
            row = [e.biometric_id,e.employee_name,e.line,e.shift]
            for c in crimping:
                row += [c.date_of_joining]
                row += [c.month_of_evaluation]
                
        # else:
        #     row += [""]
            data.append(row)
    return columns, data




def get_columns():
    columns = [
        _("Employee") + ":Link/Employee:150",
        _("Employee Name") + ":Data:150",
        _("Line") + ":Link/Line:150",
        _("Shift") + ":Link/Shift:150",
        _("Date of Joining") + ":Date:150",
        _("Month of Skill Evaluation") + ":Data:150"
    ]
    return columns


# def get_conditions(filters):
#     conditions = ""
#     # if filters.get("employee"):conditions += "AND att.employee = '%s'" % filters["employee"]
#     if filters.get("from_date"): conditions += "and c.date_of_skill_evaluatation >= %(from_date)s"
#     if filters.get("to_date"): conditions += " and c.date_of_skill_evaluatation <= %(to_date)s"    
#     return conditions, filters


def employee_details():
    employee = frappe.db.sql(
        """select biometric_id,employee_name,shift,department,designation,line from `tabEmployee` where status = "Active" and line like "%%ass%%" """, as_dict = 1)
    return employee


def crimping_Details(emp,filters):
    crimp = frappe.db.sql(
        """select employee_code,associate,line_name,date_of_joining,date_of_skill_evaluatation,month_of_evaluation from `tabAssembly Evaluation` where employee_code = %s and is_evaluate=0 and date_of_skill_evaluatation between %s and %s """,(emp,filters.from_date,filters.to_date) , as_dict=1)
    return crimp


# Copyright (c) 2013, Minda Sai Pvt LTd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
import math
from calendar import monthrange
from datetime import datetime,timedelta,date
from dateutil.rrule import * 

def execute(filters=None):
    if not filters:
        filters = {}

    columns = get_columns()

    data = []
    row = []
    employee = employee_details()
    for e in employee:
        crimping = crimping_Details(e.biometric_id,filters)
        if crimping:
            row = [e.biometric_id,e.employee_name,e.line,e.shift]
            for c in crimping:
                row += [c.date_of_joining]
                row += [c.month_of_evaluation]
                
        # else:
        #     row += [""]
            data.append(row)
    return columns, data




def get_columns():
    columns = [
        _("Employee") + ":Link/Employee:150",
        _("Employee Name") + ":Data:150",
        _("Line") + ":Link/Line:150",
        _("Shift") + ":Link/Shift:150",
        _("Date of Joining") + ":Date:150",
        _("Month of Skill Evaluation") + ":Data:150"
    ]
    return columns


# def get_conditions(filters):
#     conditions = ""
#     # if filters.get("employee"):conditions += "AND att.employee = '%s'" % filters["employee"]
#     if filters.get("from_date"): conditions += "and c.date_of_skill_evaluatation >= %(from_date)s"
#     if filters.get("to_date"): conditions += " and c.date_of_skill_evaluatation <= %(to_date)s"    
#     return conditions, filters


def employee_details():
    employee = frappe.db.sql(
        """select biometric_id,employee_name,shift,department,designation,line from `tabEmployee` where status = "Active" and line like "%%ass%%" """, as_dict = 1)
    return employee


def crimping_Details(emp,filters):
    crimp = frappe.db.sql(
        """select employee_code,associate,line_name,date_of_joining,date_of_skill_evaluatation,month_of_evaluation from `tabAssembly Evaluation` where employee_code = %s and is_evaluate=0 and date_of_skill_evaluatation between %s and %s """,(emp,filters.from_date,filters.to_date) , as_dict=1)
    return crimp


# Copyright (c) 2013, Minda Sai Pvt LTd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
import math
from calendar import monthrange
from datetime import datetime,timedelta,date
from dateutil.rrule import * 

def execute(filters=None):
    if not filters:
        filters = {}

    columns = get_columns()

    data = []
    row = []
    employee = employee_details()
    for e in employee:
        crimping = crimping_Details(e.biometric_id,filters)
        if crimping:
            row = [e.biometric_id,e.employee_name,e.line,e.shift]
            for c in crimping:
                row += [c.date_of_joining]
                row += [c.month_of_evaluation]
                
        # else:
        #     row += [""]
            data.append(row)
    return columns, data




def get_columns():
    columns = [
        _("Employee") + ":Link/Employee:150",
        _("Employee Name") + ":Data:150",
        _("Line") + ":Link/Line:150",
        _("Shift") + ":Link/Shift:150",
        _("Date of Joining") + ":Date:150",
        _("Month of Skill Evaluation") + ":Data:150"
    ]
    return columns


# def get_conditions(filters):
#     conditions = ""
#     # if filters.get("employee"):conditions += "AND att.employee = '%s'" % filters["employee"]
#     if filters.get("from_date"): conditions += "and c.date_of_skill_evaluatation >= %(from_date)s"
#     if filters.get("to_date"): conditions += " and c.date_of_skill_evaluatation <= %(to_date)s"    
#     return conditions, filters


def employee_details():
    employee = frappe.db.sql(
        """select biometric_id,employee_name,shift,department,designation,line from `tabEmployee` where status = "Active" and line like "%%ass%%" """, as_dict = 1)
    return employee


def crimping_Details(emp,filters):
    crimp = frappe.db.sql(
        """select employee_code,associate,line_name,date_of_joining,date_of_skill_evaluatation,month_of_evaluation from `tabAssembly Evaluation` where employee_code = %s and is_evaluate=0 and date_of_skill_evaluatation between %s and %s """,(emp,filters.from_date,filters.to_date) , as_dict=1)
    return crimp


# Copyright (c) 2013, Minda Sai Pvt LTd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
import math
from calendar import monthrange
from datetime import datetime,timedelta,date
from dateutil.rrule import * 

def execute(filters=None):
    if not filters:
        filters = {}

    columns = get_columns()

    data = []
    row = []
    employee = employee_details()
    for e in employee:
        crimping = crimping_Details(e.biometric_id,filters)
        if crimping:
            row = [e.biometric_id,e.employee_name,e.line,e.shift]
            for c in crimping:
                row += [c.date_of_joining]
                row += [c.month_of_evaluation]
                
        # else:
        #     row += [""]
            data.append(row)
    return columns, data




def get_columns():
    columns = [
        _("Employee") + ":Link/Employee:150",
        _("Employee Name") + ":Data:150",
        _("Line") + ":Link/Line:150",
        _("Shift") + ":Link/Shift:150",
        _("Date of Joining") + ":Date:150",
        _("Month of Skill Evaluation") + ":Data:150"
    ]
    return columns


# def get_conditions(filters):
#     conditions = ""
#     # if filters.get("employee"):conditions += "AND att.employee = '%s'" % filters["employee"]
#     if filters.get("from_date"): conditions += "and c.date_of_skill_evaluatation >= %(from_date)s"
#     if filters.get("to_date"): conditions += " and c.date_of_skill_evaluatation <= %(to_date)s"    
#     return conditions, filters


def employee_details():
    employee = frappe.db.sql(
        """select biometric_id,employee_name,shift,department,designation,line from `tabEmployee` where status = "Active" and line like "%%ass%%" """, as_dict = 1)
    return employee


def crimping_Details(emp,filters):
    crimp = frappe.db.sql(
        """select employee_code,associate,line_name,date_of_joining,date_of_skill_evaluatation,month_of_evaluation from `tabAssembly Evaluation` where employee_code = %s and is_evaluate=0 and date_of_skill_evaluatation between %s and %s """,(emp,filters.from_date,filters.to_date) , as_dict=1)
    return crimp


# Copyright (c) 2013, Minda Sai Pvt LTd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
import math
from calendar import monthrange
from datetime import datetime,timedelta,date
from dateutil.rrule import * 

def execute(filters=None):
    if not filters:
        filters = {}

    columns = get_columns()

    data = []
    row = []
    employee = employee_details()
    for e in employee:
        crimping = crimping_Details(e.biometric_id,filters)
        if crimping:
            row = [e.biometric_id,e.employee_name,e.line,e.shift]
            for c in crimping:
                row += [c.date_of_joining]
                row += [c.month_of_evaluation]
                
        # else:
        #     row += [""]
            data.append(row)
    return columns, data




def get_columns():
    columns = [
        _("Employee") + ":Link/Employee:150",
        _("Employee Name") + ":Data:150",
        _("Line") + ":Link/Line:150",
        _("Shift") + ":Link/Shift:150",
        _("Date of Joining") + ":Date:150",
        _("Month of Skill Evaluation") + ":Data:150"
    ]
    return columns


# def get_conditions(filters):
#     conditions = ""
#     # if filters.get("employee"):conditions += "AND att.employee = '%s'" % filters["employee"]
#     if filters.get("from_date"): conditions += "and c.date_of_skill_evaluatation >= %(from_date)s"
#     if filters.get("to_date"): conditions += " and c.date_of_skill_evaluatation <= %(to_date)s"    
#     return conditions, filters


def employee_details():
    employee = frappe.db.sql(
        """select biometric_id,employee_name,shift,department,designation,line from `tabEmployee` where status = "Active" and line like "%%ass%%" """, as_dict = 1)
    return employee


def crimping_Details(emp,filters):
    crimp = frappe.db.sql(
        """select employee_code,associate,line_name,date_of_joining,date_of_skill_evaluatation,month_of_evaluation from `tabAssembly Evaluation` where employee_code = %s and is_evaluate=0 and date_of_skill_evaluatation between %s and %s """,(emp,filters.from_date,filters.to_date) , as_dict=1)
    return crimp


# Copyright (c) 2013, Minda Sai Pvt LTd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
import math
from calendar import monthrange
from datetime import datetime,timedelta,date
from dateutil.rrule import * 

def execute(filters=None):
    if not filters:
        filters = {}

    columns = get_columns()

    data = []
    row = []
    employee = employee_details()
    for e in employee:
        crimping = crimping_Details(e.biometric_id,filters)
        if crimping:
            row = [e.biometric_id,e.employee_name,e.line,e.shift]
            for c in crimping:
                row += [c.date_of_joining]
                row += [c.month_of_evaluation]
                
        # else:
        #     row += [""]
            data.append(row)
    return columns, data




def get_columns():
    columns = [
        _("Employee") + ":Link/Employee:150",
        _("Employee Name") + ":Data:150",
        _("Line") + ":Link/Line:150",
        _("Shift") + ":Link/Shift:150",
        _("Date of Joining") + ":Date:150",
        _("Month of Skill Evaluation") + ":Data:150"
    ]
    return columns


# def get_conditions(filters):
#     conditions = ""
#     # if filters.get("employee"):conditions += "AND att.employee = '%s'" % filters["employee"]
#     if filters.get("from_date"): conditions += "and c.date_of_skill_evaluatation >= %(from_date)s"
#     if filters.get("to_date"): conditions += " and c.date_of_skill_evaluatation <= %(to_date)s"    
#     return conditions, filters


def employee_details():
    employee = frappe.db.sql(
        """select biometric_id,employee_name,shift,department,designation,line from `tabEmployee` where status = "Active" and line like "%%ass%%" """, as_dict = 1)
    return employee


def crimping_Details(emp,filters):
    crimp = frappe.db.sql(
        """select employee_code,associate,line_name,date_of_joining,date_of_skill_evaluatation,month_of_evaluation from `tabAssembly Evaluation` where employee_code = %s and is_evaluate=0 and date_of_skill_evaluatation between %s and %s """,(emp,filters.from_date,filters.to_date) , as_dict=1)
    return crimp


# Copyright (c) 2013, Minda Sai Pvt LTd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
import math
from calendar import monthrange
from datetime import datetime,timedelta,date
from dateutil.rrule import * 

def execute(filters=None):
    if not filters:
        filters = {}

    columns = get_columns()

    data = []
    row = []
    employee = employee_details()
    for e in employee:
        crimping = crimping_Details(e.biometric_id,filters)
        if crimping:
            row = [e.biometric_id,e.employee_name,e.line,e.shift]
            for c in crimping:
                row += [c.date_of_joining]
                row += [c.month_of_evaluation]
                
        # else:
        #     row += [""]
            data.append(row)
    return columns, data




def get_columns():
    columns = [
        _("Employee") + ":Link/Employee:150",
        _("Employee Name") + ":Data:150",
        _("Line") + ":Link/Line:150",
        _("Shift") + ":Link/Shift:150",
        _("Date of Joining") + ":Date:150",
        _("Month of Skill Evaluation") + ":Data:150"
    ]
    return columns


# def get_conditions(filters):
#     conditions = ""
#     # if filters.get("employee"):conditions += "AND att.employee = '%s'" % filters["employee"]
#     if filters.get("from_date"): conditions += "and c.date_of_skill_evaluatation >= %(from_date)s"
#     if filters.get("to_date"): conditions += " and c.date_of_skill_evaluatation <= %(to_date)s"    
#     return conditions, filters


def employee_details():
    employee = frappe.db.sql(
        """select biometric_id,employee_name,shift,department,designation,line from `tabEmployee` where status = "Active" and line like "%%ass%%" """, as_dict = 1)
    return employee


def crimping_Details(emp,filters):
    crimp = frappe.db.sql(
        """select employee_code,associate,line_name,date_of_joining,date_of_skill_evaluatation,month_of_evaluation from `tabAssembly Evaluation` where employee_code = %s and is_evaluate=0 and date_of_skill_evaluatation between %s and %s """,(emp,filters.from_date,filters.to_date) , as_dict=1)
    return crimp


# Copyright (c) 2013, Minda Sai Pvt LTd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
import math
from calendar import monthrange
from datetime import datetime,timedelta,date
from dateutil.rrule import * 

def execute(filters=None):
    if not filters:
        filters = {}

    columns = get_columns()

    data = []
    row = []
    employee = employee_details()
    for e in employee:
        crimping = crimping_Details(e.biometric_id,filters)
        if crimping:
            row = [e.biometric_id,e.employee_name,e.line,e.shift]
            for c in crimping:
                row += [c.date_of_joining]
                row += [c.month_of_evaluation]
                
        # else:
        #     row += [""]
            data.append(row)
    return columns, data




def get_columns():
    columns = [
        _("Employee") + ":Link/Employee:150",
        _("Employee Name") + ":Data:150",
        _("Line") + ":Link/Line:150",
        _("Shift") + ":Link/Shift:150",
        _("Date of Joining") + ":Date:150",
        _("Month of Skill Evaluation") + ":Data:150"
    ]
    return columns


# def get_conditions(filters):
#     conditions = ""
#     # if filters.get("employee"):conditions += "AND att.employee = '%s'" % filters["employee"]
#     if filters.get("from_date"): conditions += "and c.date_of_skill_evaluatation >= %(from_date)s"
#     if filters.get("to_date"): conditions += " and c.date_of_skill_evaluatation <= %(to_date)s"    
#     return conditions, filters


def employee_details():
    employee = frappe.db.sql(
        """select biometric_id,employee_name,shift,department,designation,line from `tabEmployee` where status = "Active" and line like "%%ass%%" """, as_dict = 1)
    return employee


def crimping_Details(emp,filters):
    crimp = frappe.db.sql(
        """select employee_code,associate,line_name,date_of_joining,date_of_skill_evaluatation,month_of_evaluation from `tabAssembly Evaluation` where employee_code = %s and is_evaluate=0 and date_of_skill_evaluatation between %s and %s """,(emp,filters.from_date,filters.to_date) , as_dict=1)
    return crimp


# Copyright (c) 2013, Minda Sai Pvt LTd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
import math
from calendar import monthrange
from datetime import datetime,timedelta,date
from dateutil.rrule import * 

def execute(filters=None):
    if not filters:
        filters = {}

    columns = get_columns()

    data = []
    row = []
    employee = employee_details()
    for e in employee:
        crimping = crimping_Details(e.biometric_id,filters)
        if crimping:
            row = [e.biometric_id,e.employee_name,e.line,e.shift]
            for c in crimping:
                row += [c.date_of_joining]
                row += [c.month_of_evaluation]
                
        # else:
        #     row += [""]
            data.append(row)
    return columns, data




def get_columns():
    columns = [
        _("Employee") + ":Link/Employee:150",
        _("Employee Name") + ":Data:150",
        _("Line") + ":Link/Line:150",
        _("Shift") + ":Link/Shift:150",
        _("Date of Joining") + ":Date:150",
        _("Month of Skill Evaluation") + ":Data:150"
    ]
    return columns


# def get_conditions(filters):
#     conditions = ""
#     # if filters.get("employee"):conditions += "AND att.employee = '%s'" % filters["employee"]
#     if filters.get("from_date"): conditions += "and c.date_of_skill_evaluatation >= %(from_date)s"
#     if filters.get("to_date"): conditions += " and c.date_of_skill_evaluatation <= %(to_date)s"    
#     return conditions, filters


def employee_details():
    employee = frappe.db.sql(
        """select biometric_id,employee_name,shift,department,designation,line from `tabEmployee` where status = "Active" and line like "%%ass%%" """, as_dict = 1)
    return employee


def crimping_Details(emp,filters):
    crimp = frappe.db.sql(
        """select employee_code,associate,line_name,date_of_joining,date_of_skill_evaluatation,month_of_evaluation from `tabAssembly Evaluation` where employee_code = %s and is_evaluate=0 and date_of_skill_evaluatation between %s and %s """,(emp,filters.from_date,filters.to_date) , as_dict=1)
    return crimp


