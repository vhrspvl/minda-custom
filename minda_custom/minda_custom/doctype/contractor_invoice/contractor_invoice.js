// Copyright (c) 2018, Minda Sai Pvt LTd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Contractor Invoice', {
	contractor: function(frm) {
			frappe.call({
				method:"minda_custom.minda_custom.doctype.contractor_invoice.contractor_invoice.get_mandays",
				args:{
					"start_date":frm.doc.start_date,
					"contractor":frm.doc.contractor
				},
				freeze: true,
				freeze_message: __("Fetching"),
				callback:function(r) {
						frm.set_value("basic",r.message[1][0])
						frm.set_value("total_mandays",r.message[0])
						frm.set_value("da",r.message[1][1])
						frm.set_value("basic_da",r.message[1][3])
						frm.set_value("other_allowance",r.message[1][2])
						frm.set_value("total",r.message[1][4])
				}
				
			})

	}
});
