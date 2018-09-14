// Copyright (c) 2018, Minda Sai Pvt LTd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Bulk Delete from Machine', {
    bulk_delete: function (frm) {
        frappe.call({
            method: "minda_custom.custom.delete_bulk",
            freeze: true,
            callback: function (r) {
                console.log(r.message)
                if (r.message === 'OK') {
                    frappe.msgprint(__("Deleted from Machine"))
                }
            }
        })
    }
});
