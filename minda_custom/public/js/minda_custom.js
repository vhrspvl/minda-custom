frappe.ui.form.on("Salary Slip", {
    validate: function (frm) {
        frappe.call({
            method: "minda_custom.custom.get_employee_attendance",
            args: {
                "employee": frm.doc.employee,
                "start_date": frm.doc.start_date,
                "end_date": frm.doc.end_date
            },
            callback: function (r) {
                frm.set_value("present_days", r.message)
            }
        })
    }
});
