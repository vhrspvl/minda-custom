// Copyright (c) 2019, Minda Sai Pvt LTd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Assembly Evaluation', {
	after_save: function(frm) {
        if(frm.doc.employee_code){
            frm.add_custom_button(__('Update Employee MIS'), function () {
                frappe.call({
                    method: "minda_custom.minda_custom.doctype.assembly_evaluation.assembly_evaluation.update_mis",
                    args: { 
                        "employee": frm.doc.employee_code,
                        "line": frm.doc.line_name
                    },
                    freeze: true,
                    freeze_message: __("Updating"),
                    callback: function(r){
                        frappe.msgprint("Updated Successfully")
                    }
                })
            });
        }
	}
});
