# Copyright (c) 2013, VHRS and contributors
# For license information, please see license.txt
from __future__ import division
from __future__ import unicode_literals
import frappe
from frappe.utils import getdate


def execute(filters=None):
    if not filters:
        filters = {}

    columns = get_columns(filters)
    data = get_entries(filters)

    return columns, data


def get_columns(filters):
    return [
        "Employee#:Link/Employee:100", "Employee Name::150", "DoJ:Date:80", "TD:Int:50",
        "T-Hol:Int:50", "T-PR:Int:50", "Total Absent:Int:50", "Att%:Float:100"]


def get_entries(filters):
    conditions_emp = get_conditions(filters)[0]
    frappe.errprint(conditions_emp)
    conditions_att = get_conditions(filters)[1]

    from_date = getdate(filters.get("from_date"))
    to_date = getdate(filters.get("to_date"))
    total_days = getdate(filters.get("to_date")) - \
        getdate(filters.get("from_date"))

    query = """SELECT emp.name, emp.employee_name, emp.date_of_joining,
		(DATEDIFF('%s', '%s')+1) as t_days, 
		
		(SELECT count(hol.name) FROM `tabHoliday` hol , `tabHoliday List` hdl
			WHERE  hol.parent = hdl.name AND
			hol.holiday_date <= '%s' AND hol.holiday_date >= '%s'), 
		
		(SELECT count(name) FROM `tabAttendance` 
			WHERE employee = emp.name AND docstatus = 1 AND status= 'Present' AND attendance_date <= '%s' AND attendance_date >= '%s') 
		
		FROM 
			`tabEmployee` emp
		
		WHERE 
			IFNULL(emp.relieving_date,'2099-12-31') >= '%s' %s""" \
            % (to_date, from_date, to_date, from_date, to_date,
               from_date, to_date, conditions_emp)

    data = frappe.db.sql(query, as_list=1)
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] is None:
                data[i][j] = 0
        pre = data[i][5]
        hol = data[i][4]
        t_days = data[i][3]
        # al = data[i][7]
        # ual = t_days - hol - pre

        # deserved holidays = (holidays/total_working_days )*(presents)
        des_hol = (hol / (t_days - hol)) * pre
        p_att = ((pre + des_hol) / t_days) * 100
        d_att = ((pre + des_hol) / t_days) * 100

        # data[i].insert(6, ual)

        # data[i].insert(7, d_att)
        data[i].insert(6, (t_days - hol - pre))
        data[i].insert(7, p_att)

    return data


def get_conditions(filters):
    conditions_emp = ""
    conditions_att = ""

    if filters.get("branch"):
        conditions_emp += " AND emp.branch = '%s'" % filters["branch"]

    if filters.get("department"):
        conditions_emp += " AND emp.department = '%s'" % filters["department"]

    if filters.get("employee"):
        conditions_emp += " AND emp.name = '%s'" % filters["employee"]

    if filters.get("from_date"):
        conditions_att += " AND att.attendance_date >='%s'" % filters["from_date"]

    if filters.get("to_date"):
        conditions_att += " AND att.attendance_date <='%s'" % filters["to_date"]

    return conditions_emp, conditions_att
