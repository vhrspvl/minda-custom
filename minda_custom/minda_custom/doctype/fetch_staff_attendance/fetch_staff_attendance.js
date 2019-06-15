// Copyright (c) 2019, Minda Sai Pvt LTd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Fetch Staff Attendance', {
	refresh: function(frm) {

    },
    fetch: function (frm) {
        frappe.call({
            method: "minda_custom.utils.fetch_from_ui",
            args: {
                "from_date": frm.doc.from_date,
                "to_date": frm.doc.to_date
            },
            freeze: true,
            freeze_message: "Fetching",
            callback: function (r) {
                if (r) {
                    console.log(r)
                //     if r == '@Thumb Log Already Saved':
                //     return res
                //     frappe.msgprint("""Attendance is Already fetched for %s and for time %s"""%(emp,day))
                // elif res == '@Repeated Thumb Log Within 10 Minute Discarded':
                //     frappe.msgprint("""Repeated Thumb Log Within 10 Minute for %s and for time %s"""%(emp,day))
                // elif res == '@Salary Process Completed For This Month, Cannot Add Attendance': 
                //     frappe.msgprint("""Salary Process Completed For This Month, Cannot Add Attendance""")   
                // elif res == 'Successfull':
                //     frappe.msgprint("""Attendance is updated for %s and for time %s"""%(emp,day))
                // else:
                //     frappe.msgprint(res)
                //     frappe.msgprint(__("Attendance Fetched"));
                }
            }
        })

    }
});
